# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

class Solution:
     
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        
        # Tarjan's algorithm
        
        #track level of vertex in graph from start
        dfn = [None for i in range(n)]
        
        #track the lowest val level it can reach (highest up)
        low = [None for i in range(n)]
        
        cur = 0
        start = 0
        res = []
        self.level = 0
       
        def dfs (cur, parent):
            if dfn[cur] is None:
                dfn[cur] = self.level
                low[cur] = self.level
                self.level+=1
                
                for nb in graph[cur]:
                    
                    # not visited
                    if dfn[nb] is None:
                        dfs(nb, cur)
                
                # check if there exist a lower reachable node reached by your neighbours
                # you only need to look at the neighbour level because recursion will update the neighbours accurately before we get to updating low[cur] due to using dfs
                
                # for graph we add bidirectional edges, so to find actual cycles, we ignore the neighbour we just came from (i!=parent)
                if parent is not None:
                    lowest = min([low[i] for i in graph[cur] if i!=parent]+[low[cur]])
                else:
                    lowest = min(low[i] for i in graph[cur]+[low[cur]])
                
                low[cur] = lowest
        
        # there will always be a vertex 0 in graph
        dfs(0, None)
        
        # check every edge
        
        # if start node points back to minimum node and that node is still lower in graph (so higher level) than level that end is in OR
        
        # if end node points back to minimum node and that node is still lower in graph (so higher level) than level that start is in
        
        # then we have a critical edge
        for v in connections:
            if low[v[0]]>dfn[v[1]] or low[v[1]]>dfn[v[0]]:
                res.append(v)
        return res
    
    
    
                
                    
                
                
            
            
            
        
        