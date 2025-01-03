class GetAssetsResponse:
    def __init__(self):
        self.assets = {}  # Dictionary to store all assets by their ID
        self.root_assets = []  # List to store root assets (no parent)

    def add_asset(self, asset):
        self.assets[asset.asset_id] = asset

    def build_tree(self):
        # Link child assets to their respective parents
        for asset in self.assets.values():
            if asset.parent_asset_id:
                parent = self.assets.get(asset.parent_asset_id)
                if parent:
                    parent.add_child(asset)
                else:
                    print(f"Warning: Parent asset with ID {asset.parent_asset_id} not found!")
            else:
                # If no parent, it's a root asset
                self.root_assets.append(asset)

    def __repr__(self):
        # String representation for debugging
        return f"GetAssetsResponse(rootAssets={self.root_assets})"
