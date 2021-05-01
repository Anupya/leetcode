# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

import collections

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # BFS
        # key = dividend, value = list (divisor, quotient)
        graph = {}
        
        # build graph
        for eqn, quo in zip(equations, values):
            var1, var2 = eqn[0], eqn[1]

            if var1 in graph:
                graph[var1].append((var2, quo))
            else:
                graph[var1] = [(var2, quo)]

            if var2 in graph:
                graph[var2].append((var1, 1/quo))
            else:
                graph[var2] = [(var1, 1/quo)]
        
        # traverse graph
        divisions = []
        for query in queries:
            var1, var2 = query[0], query[1]
            
            if var1 not in graph or var2 not in graph:
                divisions.append(-1.0)
                continue
            
            # find path from var1 to var2
            dq = collections.deque([(var1, 1.0)])
            visited = set()
            n = len(divisions)
            
            while dq:
                front, product = dq.popleft()
                if front == var2:
                    divisions.append(product)
                    break
                
                visited.add(front)
                for neighbour, value in graph[front]:
                    if neighbour not in visited:
                        dq.append((neighbour, product*value))
            
            if n == len(divisions):
                divisions.append(-1)
        
        return divisions
                
            
            
  
                