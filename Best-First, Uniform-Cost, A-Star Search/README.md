# Search Algorithms

| **Algorithm**         | **Uses Cost (g(n))** | **Uses Heuristic (h(n))** | **Optimal** | **Complete** | **Eval Function**   | **Assumption**                  |
|-----------------------|----------------------|---------------------------|-------------|--------------|---------------------|---------------------------------|
| **Uniform-Cost Search** | ✅                   | ❌                        | ✅          | ✅           | ```f(n) = g(n)```         | ```h(n) = 0``` for every state        |
| **Best-First Search**   | ❌                   | ✅                        | ❌          | ❌           | ```f(n) = h(n)```         | ```g(n) = 0``` for every state        |
| **A* Search**           | ✅                   | ✅                        | ✅          | ✅           | ```f(n) = g(n) + h(n)```  | ```None```                            |


## Uniform-Cost Search (UCS):
This algorithm finds the <i>least-cost path</i> in a <i>weighted</i> graph. It iteratively expands nodes in the order of their cumulative path cost, <code>g(n)</code>, from the start node. It uses a priority queue where nodes with lower costs are dequeued first.
<br><br>Additionally, it is optimal and complete if costs are non-negative. It has the ability to explore a large number of nodes if the solution is far from the start.

## Best-First Search:
It is a <i>greedy approach</i> to search for a goal state efficiently. It uses a heuristic function <code>h(n)</code> to estimate the cost from the current node to the goal. It expands the node with the smallest heuristic value first.
<br><br>However, it is not always optimal or complete. It mostly focuses only on perceived shortest paths, potentially missing optimal solutions.

## A Search*:
This algorithm combines the both the advantages of UCS and Best-First Search. It implements both the path cost <code>g(n)</code> and heuristic estimate <code>h(n)</code> to prioritize nodes, minimizing ```f(n) = g(n) + h(n)```. 
<br><br>It expands nodes with the smallest f(n) value first.
<br>
Additionally, it is optimal and complete if the heuristic is admissible (never overestimates) and consistent.
It balances exploration of cost and guidance toward the goal.
