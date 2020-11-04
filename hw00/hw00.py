import snap
import numpy
import matplotlib.pyplot as plt

# Section 1 #
# Load data from file, then construct a directed graph
wiki_g = snap.LoadEdgeListStr(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
# solution to hw
print('*' * 10 + ' Section I ' + '*' * 10)
print("The wiki-vote graph has " + str(wiki_g.GetNodes()) + " nodes.")
# self_loop_nodes = 0
# for edge in wiki_g.Edges():
#    if edge.GetSrcNId() == edge.GetDstNId():
#        self_loop_nodes = self_loop_nodes + 1
# Better use built-in functions to count the self-edges...
print("The wiki-vote graph has " + str(snap.CntSelfEdges(wiki_g)) + " self-looped nodes.")
print("The wiki-vote graph has " + str(snap.CntUniqDirEdges(wiki_g)) + " unique directed edges.")
print("The wiki-vote graph has " + str(snap.CntUniqUndirEdges(wiki_g)) + " unique undirected edges.")
print("The wiki-vote graph has " + str(int(snap.CntUniqUndirEdges(wiki_g) / 2)) + " reciprocated edges.")

nodes_zero_out_degree = 0
nodes_zero_in_degree = 0
nodes_more_than_10_outgoing_edges = 0
nodes_fewer_than_10_incoming_edges = 0

min_out_degree = 1
max_out_degree = 1

for node in wiki_g.Nodes():
    if node.GetOutDeg() == 0:
        nodes_zero_out_degree = nodes_zero_out_degree + 1
    if node.GetInDeg() == 0:
        nodes_zero_in_degree = nodes_zero_in_degree + 1
    if node.GetOutDeg() > 10:
        nodes_more_than_10_outgoing_edges = nodes_more_than_10_outgoing_edges + 1
    if node.GetInDeg() < 10:
        nodes_fewer_than_10_incoming_edges = nodes_fewer_than_10_incoming_edges + 1
    if node.GetOutDeg() > max_out_degree:
        max_out_degree = node.GetOutDeg()

print("The wiki-vote graph has " + str(nodes_zero_out_degree) + " nodes of zero out-degree.")
print("The wiki-vote graph has " + str(nodes_zero_in_degree) + " nodes of zero in-degree.")
print("The wiki-vote graph has " + str(nodes_more_than_10_outgoing_edges) + " nodes with more than 10 outgoing-edges.")
print(
    "The wiki-vote graph has " + str(nodes_fewer_than_10_incoming_edges) + " nodes with fewer than 10 incoming-edges.")

# Section 2 #
print('*' * 10 + ' Section II ' + '*' * 10)
NId = snap.GetMxOutDegNId(wiki_g)
x = numpy.arange(min_out_degree, max_out_degree + 1, 1)
y = numpy.ones(max_out_degree)
for node in wiki_g.Nodes():
    if node.GetOutDeg() != 0:
        y[node.GetOutDeg() - 1] = y[node.GetOutDeg() - 1] + 1
x = numpy.log10(x)
y = numpy.log10(y)

# Assume that the least-linear-regression y=ax+b
a, b = numpy.polyfit(x, y, deg=1)
y_reg = a * x + b

plt.figure(figsize=(12.8, 7.2))
plt.title('Distribution of Out-Degree of Nodes In Wiki_Vote Network')
plt.xlabel(r'$\log{OutDegree}$')
plt.ylabel(r'$\log{Count}$')
# plt.xlim(right=numpy.amax(x), left=0.0)
# plt.ylim(top=max(numpy.amax(y), numpy.amax(y_reg)), bottom=0.0)
handle_datpnt = plt.scatter(x, y, label='datapoint')
handle_reg, = plt.plot(x, y_reg, color='red', label='least-square regression')
plt.legend([handle_datpnt, handle_reg], ['datapoint', 'least-square regression'])
plt.show()

# Section 3 #
print('*' * 10 + ' Section III ' + '*' * 10)
# sof for stackoverflow
sof_g = snap.LoadEdgeListStr(snap.PNGraph, "stackoverflow-Java.txt", 0, 1)
# connected components vector
wcc_vec = snap.TCnComV()
snap.GetWccs(sof_g, wcc_vec)
print("The stackoverflow-Java graph has " + str(len(wcc_vec)) + " weakly connected components.")
#
largest_wcc = snap.GetMxWcc(sof_g)
print(
    'The largest weekly connected component of stackoverflow graph has ' + str(largest_wcc.GetNodes()) + ' nodes and ' +
    str(snap.CntUniqDirEdges(sof_g)) + ' edges.')

rankscoremap = snap.TIntFltH()
snap.GetPageRank(sof_g, rankscoremap)
maplen = len(rankscoremap)
rankscoremap.SortByDat()
cnt = 0
print("If you use PageRank score, then")
for item in rankscoremap:
    if cnt >= maplen - 3:
        print("\tTop " + str(maplen - cnt) + " node is " + str(item) + " with score " + str(rankscoremap[item]))
    cnt = cnt + 1

hubscore = snap.TIntFltH()
authscore = snap.TIntFltH()
snap.GetHits(sof_g, hubscore, authscore)
cnt = 0
hubscore.SortByDat()
authscore.SortByDat()
print("If you use HITS score, then")
for item in authscore:
    if cnt >= maplen - 3:
        print("\tTop " + str(maplen - cnt) + " node is " + str(item) + " with authority " + str(authscore[item]))
    cnt = cnt + 1

print('\t' + '-' * 45)

cnt = 0
for item in hubscore:
    if cnt >= maplen - 3:
        print("\tTop " + str(maplen - cnt) + " node is " + str(item) + " with hub " + str(hubscore[item]))
    cnt = cnt + 1

