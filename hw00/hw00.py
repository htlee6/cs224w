import snap

# Section 1 #

# Load data from file, then construct a directed graph
wiki_g = snap.LoadEdgeListStr(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
# solution to hw
print("The graph has " + str(wiki_g.GetNodes()) + " nodes.")
# self_loop_nodes = 0
# for edge in wiki_g.Edges():
#    if edge.GetSrcNId() == edge.GetDstNId():
#        self_loop_nodes = self_loop_nodes + 1
# Better use built-in functions to count the self-edges...
print("The graph has " + str(snap.CntSelfEdges(wiki_g)) + " self-looped nodes.")
print("The graph has " + str(snap.CntUniqDirEdges(wiki_g)) + " unique directed edges.")
print("The graph has " + str(snap.CntUniqUndirEdges(wiki_g)) + " unique undirected edges.")
print("The graph has " + str(int(snap.CntUniqUndirEdges(wiki_g)/2)) + " reciprocated edges.")

nodes_zero_out_degree = 0
nodes_zero_in_degree = 0
nodes_more_than_10_outgoing_edges = 0
nodes_fewer_than_10_incoming_edges = 0
for node in wiki_g.Nodes():
    if node.GetOutDeg() == 0:
        nodes_zero_out_degree = nodes_zero_out_degree + 1
    if node.GetInDeg() == 0:
        nodes_zero_in_degree = nodes_zero_in_degree + 1
    if node.GetOutDeg() > 10:
        nodes_more_than_10_outgoing_edges = nodes_more_than_10_outgoing_edges + 1
    if node.GetInDeg() < 10:
        nodes_fewer_than_10_incoming_edges = nodes_fewer_than_10_incoming_edges + 1
print("The graph has " + str(nodes_zero_out_degree) + " nodes of zero out-degree.")
print("The graph has " + str(nodes_zero_in_degree) + " nodes of zero in-degree.")
print("The graph has " + str(nodes_more_than_10_outgoing_edges) + " nodes with more than 10 outgoing-edges.")
print("The graph has " + str(nodes_fewer_than_10_incoming_edges) + " nodes with fewer than 10 incoming-edges.")

# Section 2 #


# Section 3 #
