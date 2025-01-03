import hashlib
import json


class AggregatedResponseWithFilter:
    def __init__(self, output_file):
        self.fingerprint_map = {}  # Maps fingerprints to normalized trees
        self.aggregated_responses = {}  # Aggregated groups
        self.output_file = output_file

    def normalize_tree(self, asset):
        """Normalize the tree by representing the hierarchy as product codes."""
        normalized = {"productCode": asset.product_code, "children": []}
        for child in asset.children:
            normalized["children"].append(self.normalize_tree(child))
        return normalized

    def calculate_fingerprint(self, normalized_tree):
        """Calculate a hash for the normalized tree."""
        tree_json = json.dumps(normalized_tree, sort_keys=True)
        return hashlib.md5(tree_json.encode()).hexdigest()

    def add_response(self, response):
        """Process and add a response for aggregation."""
        for root_asset in response.root_assets:
            # Normalize the tree
            normalized_tree = self.normalize_tree(root_asset)

            # Generate a unique fingerprint
            fingerprint = self.calculate_fingerprint(normalized_tree)

            # Aggregate based on the fingerprint
            if fingerprint not in self.fingerprint_map:
                self.fingerprint_map[fingerprint] = normalized_tree
                self.aggregated_responses[fingerprint] = []
            self.aggregated_responses[fingerprint].append(response)

    def tree_contains_product_code(self, tree, product_codes):
        """Check if the tree contains any of the specified product codes."""
        if tree["productCode"] in product_codes:
            return True
        for child in tree["children"]:
            if self.tree_contains_product_code(child, product_codes):
                return True
        return False

    def write_filtered_responses(self, product_codes):
        """Write filtered aggregated responses to the output file, sorted by number_of_responses."""
        filtered_data = []

        # Check if product codes are provided; if empty, include all groups
        if not product_codes:
            for fingerprint, normalized_tree in self.fingerprint_map.items():
                filtered_data.append({
                    "tree": normalized_tree,
                    "number_of_responses": len(self.aggregated_responses[fingerprint]),
                })
        else:
            # Collect and filter data
            for fingerprint, normalized_tree in self.fingerprint_map.items():
                if self.tree_contains_product_code(normalized_tree, product_codes):
                    filtered_data.append({
                        "tree": normalized_tree,
                        "number_of_responses": len(self.aggregated_responses[fingerprint]),
                    })

        # Sort by number_of_responses in descending order
        filtered_data.sort(key=lambda x: x["number_of_responses"], reverse=True)

        # Convert sorted data into dictionary format for output
        sorted_output = {f"Group {idx + 1}": group for idx, group in enumerate(filtered_data)}

        # Write the sorted data to the output file
        with open(self.output_file, "w", encoding="utf-8") as file:
            json.dump(sorted_output, file, indent=2)
        print(f"Filtered and sorted responses written to {self.output_file}")
