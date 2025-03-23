from collections import defaultdict


class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # Undirected graph with n vertices

        # Get the complete connected components

        # Idea 1 do union find and then check in each group whether they are all connected?
        # Idea 2 do bfs to check whether 

        # Parents [0, 0, 0, 3, 3, 5]
        # Then check for each group with an adjacency list + hashtable 
        # Whether they are all connected with each other

        parents = [x for x in range(n)]
        adjacencyList = [{x} for x in range(n)]

        def findParent(n1):
                if parents[n1] == n1:
                    return n1

                return findParent(parents[n1])

        for n1, n2 in edges:
            adjacencyList[n1].add(n2)
            adjacencyList[n2].add(n1)

            parent_of_n1 = findParent(n1)
            parent_of_n2 = findParent(n2)

            parents[parent_of_n2] = parent_of_n1

        index_dict = defaultdict(list)
        for i in range(n):
            index_dict[findParent(i)].append(i)
            
        output = 0
        for nodes_to_check in index_dict.values():
            if any(adjacencyList[nodes_to_check[0]] != adjacencyList[node] for node in nodes_to_check):
                continue
            
            output += 1
                
        return output
