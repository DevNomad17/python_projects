class Asset:
    def __init__(self, asset_id, product_code, parent_asset_id=None):
        self.asset_id = asset_id
        self.product_code = product_code
        self.parent_asset_id = parent_asset_id
        self.children = []  # To store child assets

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        # String representation for debugging
        return f"Asset(id={self.asset_id}, productCode={self.product_code}, children={len(self.children)})"
