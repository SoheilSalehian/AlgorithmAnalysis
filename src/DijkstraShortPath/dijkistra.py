#!/usr/bin/python

from collections import OrderedDict


    



#Store items in the order the keys were last added
class LastUpdatedOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

#initialize the dictionary to have source vertex 1 with distance 0       
exploredPathDistanceDic = {}        
#ordered dictionary by vertices (key)
exploredPathDistanceDic = LastUpdatedOrderedDict(OrderedDict(exploredPathDistanceDic.items()))

#book keeping parameters
numberOfNodes = 0
finalNode = 0
blocked = False

#while verticesProcessed != not yet explored vertices
#    among all edges that have their tail in verticesProcessed and head not in there:
#    choose the one that minimizes:
#        shortestPathDistance so far to the current vertex + distance from current vertex to the chosen (a.k.a Dijkstra greedy criteria)
#add this new chosen vertix to verticesProcessed
#set shortestPathDistance[new chosen]= shortestPathDistance[everything previously in verticesProcessed] + distance from the current vertex to the newly chosen vertex  
exploredVertices = {}
shortestPath = [0]

exploredPathDistanceDic = {1:0}


def dijkstraLoop(edgesDic):
    
    
    
    
#    for node in edgesDic.keys():
#        if(exploredVertices[-1]==node[0] and node[1] not in exploredVertices):
#            dGreedyCriteria.append(shortestPath[-1] + edgesDic[node])
#            print dGreedyCriteria
#    shortestPath.append(min(dGreedyCriteria))
#    print exploredVertices
#    print shortestPath
        
        
            
    
#    if(1):
#        length = 0
#        dGreedyCriteriaDic = {}
#        #our current node is the last element from the ordered exploredDistanceDic
#        currentNode = next(reversed(exploredPathDistanceDic))
#        print "currentNode", currentNode
#        #read the source nodes from edgesDic
#        for node in edgesDic.keys():
#            #find among the dictionary keys, the current node and the appropriate adjacents such that they are not processed yet
#            if (node[0] == currentNode):
#                #store the possible outgoing edge lengths
#                length= edgesDic[node]
#                #sort the lengths to find the minimum
#                print length, node[1]
#            else:
#                #else skip and iterate over the next adjacent
#                continue
#            #Dijkstra's greedy criteria calculated as the sum of current shortest path (value of the latest key in exploredPathDistanceDic) and minimum possible length of outgoing edge
#            dGreedyCriteriaDic[node[1]] = next(reversed(exploredPathDistanceDic.values())) + length
#            print "greedy",dGreedyCriteriaDic
##            iterateFlag = True
#            chosenNode = min(dGreedyCriteriaDic, key=dGreedyCriteriaDic.get)
#            if (chosenNode == finalNode):
#                exploredPathDistanceDic[chosenNode] = dGreedyCriteriaDic[chosenNode]
#                continue
#            else:
#                return
#        #if we there is no way from the currentNode to go we are have scanned shortpaths as much as we could, now need to start again
#        if (iterateFlag):
#            #extract the key with the minimum Dijkstra's greedy criteria value to be the chosen one!!
#            chosenNode = min(dGreedyCriteriaDic, key=dGreedyCriteriaDic.get)
#            iterateFlag = False
#            
#            #check to see if we have traversed any edges at all
#            if(not chosenNode in exploredPathDistanceDic.keys()):
#                exploredPathDistanceDic[chosenNode] = dGreedyCriteriaDic[chosenNode]
#            #if the chosenNode already exists and its current value is larger than what the criteria have found, take the newly found value
#            elif (exploredPathDistanceDic[chosenNode] > dGreedyCriteriaDic[chosenNode]):    
#                exploredPathDistanceDic[chosenNode] = dGreedyCriteriaDic[chosenNode]
#            #otherwise no need to update the dictionary for this node, return
#            else:
#                blocked = True
#                return
#        #if we haven't then this is as far as we could go for this node    
#        else:
#            exploredPathDistanceDic[chosenNode] = 0
#            return 
#        
            

# this function reads the data of a adjancey matrix text format and converts it into a hash with a tuple key of the two nodes 
# and their corresponding weight as key
def readData():
    global numberOfNodes, nodesLeft
    #keep the edge information in the hash edges 
    edgesDic = {}
    with open('/home/soheil/workspace/AlgorithmAnalysis/src/DijkstraShortPath/exampleInput.txt',"r") as fp:
        #step through each line
        for i in fp.readlines():
            #first split the line to spaces as a preprocessing step
            nodes = i.split()
            #go through node information of each line
            for j in xrange (1,len(nodes)):
                #extract the connected node information as key
                key = (int(nodes[0]),int(nodes[j].split(",")[0]))
                #extract the weight information as value of the hash 
                edgesDic[key] = int(nodes[j].split(",")[1])
    numberOfNodes = int(i[0])
    return edgesDic    





if __name__ == '__main__':
    edges = readData()
    dijkstraLoop(edges)
#    for i in xrange(numberOfNodes):
#        dijkstraLoop(edges,i+1)
#        if (blocked):
#            exploredPathDistanceDic[0] = 1  
#        print sorted(exploredPathDistanceDic.items(), key=lambda x: x[0])
    
        



