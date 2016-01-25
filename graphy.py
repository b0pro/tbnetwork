#coding=utf-8
__author__ = 'user'

import networkx as nx
import matplotlib.pyplot as plt

def spltTB(strName=""):
    user = strName.split(".")[0]
    tbhead = strName.split(".")[1].split("_")[0]
    return user+"-"+tbhead

def drawNetworkGraph(data=[{}]):

    srcMachine = []
    srcTable = []
    dstMachine = []
    dstTable = []

    for i in range(data.__len__()):
        fielddata = data[i].getData()
        srcMachine.append(fielddata.get(u"源库"))
        srcTable.append(fielddata.get(u"源库")+"("+spltTB(fielddata.get(u"源表")) + ")")
        dstMachine.append(fielddata.get(u"目标库"))
        dstTable.append(fielddata.get(u"目标库")+"("+spltTB(fielddata.get(u"目标表"))+")")

    weights = {}
    G = nx.DiGraph()
    #pos=nx.spring_layout(G)
    labels={}
    nodenum = 0
    for i in range(srcTable.__len__()):
        if(G.has_node(srcTable[i]) == False):
            G.add_node(srcTable[i])
            labels[srcTable[i]] = srcTable[i]
            nodenum = nodenum+1
        if(G.has_node(dstTable[i]) == False):
            G.add_node(dstTable[i])
            labels[dstTable[i]] = dstTable[i]
            nodenum = nodenum+1

        key = srcTable[i] + ":" + dstTable[i]
        weights[key] = weights.get(key,0)+1



    for i in range(srcTable.__len__()):
        key = srcTable[i] + ":" + dstTable[i]
        G.add_edge(srcTable[i],dstTable[i],weight=weights.get(key))

    edgewidth = [ d['weight'] for (u,v,d) in G.edges(data=True)]
    pos = nx.spring_layout(G)
    #nx.draw(G,color=edgewidth)
    nx.draw_networkx_nodes(G,pos)
    nx.draw_networkx_edges(G,pos,color=edgewidth)
    nx.draw_networkx_labels(G,pos,labels,font_size=9)

    plt.show()

