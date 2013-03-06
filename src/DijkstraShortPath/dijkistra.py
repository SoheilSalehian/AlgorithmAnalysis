#!/usr/bin/python





#list of processed vertices so far
verticesProcessed = [1]

#computed shortest path distance list with index of the processed vertices
shortestPathDistance = [0]

numberOfNodes = 0

#while verticesProcessed != not yet explored vertices
#    among all edges that have their tail in verticesProcessed and head not in there:
#    choose the one that minimizes:
#        shortestPathDistance so far to the current vertex + distance from current vertex to the chosen (a.k.a Dijkstra greedy criteria)
#add this new chosen vertix to verticesProcessed
#set shortestPathDistance[new chosen]= shortestPathDistance[everything previously in verticesProcessed] + distance from the current vertex to the newly chosen vertex  


def dijkstraLoop(edgesDic):
    
    while(len(verticesProcessed) < numberOfNodes):
        length = 0
        dGreedyCriteriaDic = {}
        #our current node is the last element from the verticesProcessed list
        currentNode = verticesProcessed[-1]
        print "currentNode", currentNode
        #read the source nodes from edgesDic
        for node in edgesDic.keys():
            #find among the dictionary keys, the current node and the appropriate adjacents such that they are not processed yet
            if (node[0] == currentNode and not node[1] in verticesProcessed):
                #store the possible outgoing edge lengths
                length= edgesDic[node]
                #sort the lengths to find the minimum
                print length, node[1]
            else:
                #else skip and iterate over the next adjacent
                continue
            #Dijkstra's greedy criteria calculated as the sum of current shortest path and minimum possible outgoing edge
            dGreedyCriteriaDic[node[1]] = shortestPathDistance[currentNode-1] + length
#                print dGreedyCriteriaDic
            #extract the key with the minimum Dijkstra's greedy criteria value to be the chosen one!!
            chosenNode = min(dGreedyCriteriaDic, key=dGreedyCriteriaDic.get)
#                print "greedy",chosenNode
        verticesProcessed.append(chosenNode)
        shortestPathDistance.append(dGreedyCriteriaDic[chosenNode])
        print shortestPathDistance
        
            

# this function reads the data of a adjancey matrix text format and converts it into a hash with a tuple key of the two nodes 
# and their corresponding weight as key
def readData():
    global numberOfNodes
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
        numberOfNodes = i[0]
    print numberOfNodes
    print edgesDic
    return edgesDic    



if __name__ == '__main__':
    edges = readData()
    dijkstraLoop(edges)


