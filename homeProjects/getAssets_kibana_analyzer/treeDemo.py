import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt

# Parse the XML and build the graph
def build_graph(xml_data):
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()
    G = nx.DiGraph()

    for asset in root.findall("asset"):
        asset_id = asset.find("id").text
        integration_id = asset.find("integrationId").text
        parent = asset.find("parentAsset/id")
        G.add_node(asset_id, label=f"{integration_id}")

        if parent is not None and parent.text:
            parent_id = parent.text
            G.add_edge(parent_id, asset_id)
    return G

# Draw using a hierarchical layout
def draw_hierarchical(graph, title):
    plt.figure(figsize=(12, 8))
    pos = nx.nx_agraph.graphviz_layout(graph, prog="dot")  # Requires pygraphviz or pydot
    labels = nx.get_node_attributes(graph, "label")
    nx.draw(graph, pos, with_labels=False, node_size=2000, node_color="lightblue", arrows=True)
    nx.draw_networkx_labels(graph, pos, labels, font_size=8)
    plt.title(title)
    plt.show()

# XML data example (replace with your XML input)
xml_data = """
<getAssetsResponseParameters>
    <asset>
        <id>SIEBEL-PRD-ASSET-1-A7727SZN</id>
        <integrationId>1-A771W2AB</integrationId>
        <status>Active</status>
        <serviceType>SERVICE</serviceType>
        <parentAsset>
            <id>SIEBEL-PRD-ASSET-3-A7727SZN</id>
        </parentAsset>
    </asset>
    <asset>
        <id>SIEBEL-PRD-ASSET-2-A7727SZN</id>
        <integrationId>2-A771W2AB</integrationId>
        <status>Active</status>
        <serviceType>SERVICE</serviceType>
        <parentAsset>
            <id>SIEBEL-PRD-ASSET-3-A7727SZN</id>
        </parentAsset>
    </asset>
    <asset>
        <id>SIEBEL-PRD-ASSET-3-A7727SZN</id>
        <integrationId>3-A771W2AB</integrationId>
        <status>Active</status>
        <serviceType>SERVICE</serviceType>
        <parentAsset>
        </parentAsset>
    </asset>
    <asset>
        <id>SIEBEL-PRD-ASSET-4-A7727SZN</id>
        <integrationId>4-A771W2AB</integrationId>
        <status>Active</status>
        <serviceType>SERVICE</serviceType>
        <parentAsset>
            <id>SIEBEL-PRD-ASSET-3-A7727SZN</id>
        </parentAsset>
    </asset>
</getAssetsResponseParameters>
"""
G = build_graph(xml_data)
draw_hierarchical(G, "Hierarchical Visualization")
