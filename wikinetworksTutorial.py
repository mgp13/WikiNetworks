# WikiNetworks tutorial
# This tutorial demonstrates the use of the WikiNetworks package to download and process pathway representations from WikiPathways database into machine-readable networks that can be used with visualization software or in downstream programming applications
# Author: Mukta Palshikar, mukta_palshikar@Urmc.rochester.edu

# Import all functions from wikinetworks
from wikinetworks import *

# Create an instance of the WikiPathways database
__all__ = ["WikiPathways"]
s=WikiPathways()

#Specify the test pathways using the WikiPathways IDs. Here we select two pathways:
# WP2727:
# WP2456:

testPathways = ["WP2727","WP2456"]
for pathID in testPathways:
    graph = runParsePathway(s, pathID) #download and process pathways, generate a NetworkX digraph object
    print("Nodes:", len(graph.nodes())) #print number of nodes in the pathway
    print("Edges:", len(graph.edges())) #print number of edges in the pathway
    print("SIF graph:", '_'.join([pathID, "edgeList.csv"])) #location of the edgelist file. SIF = simple interaction format
    print("Graphml: ", ''.join([pathID, "_graph.graphml"])) #location of the graphml file
    print("***")
