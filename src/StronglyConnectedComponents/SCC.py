#!/usr/bin/python
import numpy as np
import random


    #1: read the data from the text file
    #2: convert the data into numpy matrix form (Graph G)
    #3: set global variable @var firstPassFinish+=0 and @var leaderList=[]
    
    
#DFSLoop(Graph G) & DFSLoop(Graph Gr)
    #4: Go through each node of the graph in decreasing order
    #5:   if node is not explored
    #6:     add i to the leaderList
    #7:     run the DFS(G,i) recursively
    
    #8: DFS(G,i)
    #9:   mark i as explored
    #10:  set leader(i)=node S (?)
    #11:  go through each arc (i,j) of graph G
    #12:     if j is not explored
    #13:     DFS(G,j)
    #14:  firstPassFinish +=1
    #15:  finishTime[i].append(firstPassFinish) to bookkeep the coming node i' order

#TODO: integrate global variables into class attributes
firstPassFinish = -1
finishTimeDic = {}
leadersDic={}
leader = None

class Node(object):
    def __init__(self,explored=0):
        self.explored = 0


def DFSLoop(graph, exploredList, secondPass):
    global leader
    #Go through each node of the graph in decreasing order
    for node in reversed(xrange(graph.shape[0])):
        #if node is not explored then
        if (exploredList[node] == 0):
            #add i as the leader
            if (secondPass):
                leader = node
                leadersDic[leader] = [node]
            #run the DFS(G,i) recursively
            depthFirstSearch(graph,node, secondPass)
       
      
            
def depthFirstSearch(graph, node, secondPass):
    global firstPassFinish, finishTimeList, leadersDic
#    print "node is",node+1
    #mark i as explored
    exploredList[node] = 1
    if (secondPass):
        leadersDic[leader] += [node]
    #TODO:need to fix the indexing of nextNode with more than one connection: random.randrange(0,nextNode[0].size)]
    nextNode = np.nonzero(graph[node])
#    print "nextNode", nextNode[0].size
    print node+1, '---->',nextNode[0][0]+1
    for nexts in xrange(nextNode[0].size):
        if (exploredList[nextNode[0][nexts]] == 0):
            depthFirstSearch(graph, nextNode[0][nexts], secondPass)
        #increment the firstPassFinish after we are done
    if not (secondPass):
        #increment the firstpassfinish variable as the we have finished the first pass for original node input
        firstPassFinish +=1
        #store the finishing times in a dictionary
        finishTimeDic[node]=firstPassFinish
    return

            

        
#pass 1 -> pass 2 transition
#1: grab original G and swap columns corresponding to finishTimeDic
#2: now swap rows based on finishTimeDic
def columnSwap(originalArray, array, first, second):
    
    #TODO:advanced slicing option my_array[:,[0, 1]] = my_array[:,[1, 0]]
    #swap the columns first
#    temp = np.copy(originalArray[:,first])
    array[:,first] = array[:,second]
#    print "column swap"
#    print array
#    print "original"
#    print originalArray


def rowSwap(originalArray, array, first, second):
    
    #TODO:advanced slicing option my_array[:,[0, 1]] = my_array[:,[1, 0]]
    #swap the columns first
#    print "row swap"
#    print array
    #swap the rows next
    array[first, :] = array[second,:]   
    

        




if __name__ == '__main__':

    G = np.zeros((9,9), dtype=np.int)
    connected = [7,5,9,1,8,8,9,2,6]
    j = 0
    for i in xrange(G.shape[0]):
        G[i,connected[j]-1] = 1
        
        j +=1
#    print G
    G[5,2] = 1
#    G[0,3] = 1
    G[6,3] = 1
#    a = np.array([[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,1,0]])
#    print a, '\n'
##    rowAndColumnSwap(a, 3, 2)
##    rowAndColumnSwap(a, 1, 4)
##    print a
#    myDic = {'1':4, '2':3}
#    for vertexOne,vertexTwo in myDic.items():
#        rowAndColumnSwap(a, vertexOne, vertexTwo)  
#    
#    print a
    
#    print G.T
#    for i in xrange(8):
#        nextNode = np.nonzero(G.T[i])
#        print i,": ",nextNode
#    
#    for i in xrange(8):
#        nextNode = np.nonzero(G[i])
#        print i,": ",nextNode
    
    exploredList = [0,0,0,0,0,0,0,0,0]
    DFSLoop(G, exploredList, secondPass=0)
    print exploredList
    print finishTimeDic
    print leadersDic

    print G, '\n'
    Gnew = G.copy()
    
    columnSwap(G, Gnew, 0, 6)
    
    print Gnew, '\n'
    columnSwap(G, Gnew, 2, 0)

#    for vertexOne,vertexTwo in finishTimeDic.items():
##        print vertexOne, vertexTwo
#        columnSwap(G,Gnew, vertexOne, vertexTwo)
#        rowSwap(G,Gnew, vertexOne, vertexTwo)

        

    

    
#
#    print "...Second Pass..."
#    exploredList = [0,0,0,0,0,0,0,0,0]
#    DFSLoop(G, exploredList, secondPass=1)
#    print exploredList
#    print finishTimeDic
#    print leadersDic
    
    


        
