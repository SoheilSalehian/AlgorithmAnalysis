#!/usr/bin/python

import random
import numpy as np

class BaseNode(object):
    def __init__(self, nodeID=None, adjacentList=[]):
        self.nodeID = int(nodeID)
        self.adjacentList = adjacentList
    
        
class SuperNode(BaseNode):
    def __init__(self, superNodeID, sourceNodeID):
        self.superNodeID = superNodeID
        self.sourceNodeID = sourceNodeID
        
 
        
class Graph(SuperNode):
    def __init__(self, adjacentList = [], edges=[[]],  n=6):
        self.adjacentList = adjacentList
        self.edges = edges
        self.n = n
        self.contractionDic = {} 
    
    
    def addToContractionDic(self, superNodeID, sourceNodeID):
        superNode = SuperNode(superNodeID, sourceNodeID)
        self.contractionDic [superNode.superNodeID]= superNode.sourceNodeID





if __name__ == '__main__':
    with open('/home/soheil/workspace/AlgorithmAnalysis/src/RandomizedContractionMinCut/test_input.txt',"r") as fp:
        myFile = fp.readlines()
    

    myGraph = Graph(n=len(myFile)-1)
#    print myGraph
#    print myFile
    lineList = [[0]]
    for line in myFile:
        lineList.append([int(i) for i in line.split()])
#    print lineList[:-1]
    
    myGraph = Graph(adjacentList=lineList[:-1], n=len(myFile)-1)
    print myGraph.adjacentList
    #choose node and supernode candidate
    
    
    node = myGraph.adjacentList[2]
    superNodeCandidate = 3
    print node,"supernode", superNodeCandidate

    for adjacent in node:
        print adjacent
        if (adjacent == superNodeCandidate):
            print"removing self loop"
            #delete the node being fused(node) in the list of the superNode candidate (self loops removed)
            selfLoopIndex = myGraph.adjacentList[adjacent].index(node[0])
            del myGraph.adjacentList[superNodeCandidate][selfLoopIndex]
        elif(adjacent == node[0]):
            #delete the node from the graph
            print "deleting"
            myGraph.adjacentList[node[0]]=[]
        else:
            #replace the node being fused(node) in the list of all that is connected to it to the superNode Candidate
            replaceIndex = myGraph.adjacentList[adjacent].index(node[0]) 
            myGraph.adjacentList[adjacent][replaceIndex] = superNodeCandidate
    
    #after first contraction the superNodeCandidate becomes a SuperNode and keeps track of its source via sourceNodes
    myGraph.addToContractionDic(superNodeCandidate, node[0])
    
    print myGraph.contractionDic
    
    
    

