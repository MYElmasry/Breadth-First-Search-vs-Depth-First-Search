# Breadth-First-Search-vs-Depth-First-Search
## Code from course form universitat autònoma de barcelona
### BREADTH-FIRST SEARCH algorithm
1. Set initial state as the first path of the list
2. While first path does not reach the goal and list is not empty:
    - Get the first path of the list
    - Expand the path obtained in previous step
    - Remove cycles from paths obtained in previous step
    - Insert remaining paths at the **end** of the list
3. If the list is not empty, return the first path of the list
else (list is empty), there is not any solution
### DEPTH-FIRST SEARCH algorithm
1. Set initial state as the first path of the list
2. While first path does not reach the goal and list is not empty:
    - Get the first path of the list
    - Expand the path obtained in previous step
    - Remove cycles from paths obtained in previous step
    - Insert remaining paths at the **beginning** of the list
3. If the list is not empty, return the first path of the list
else (list is empty), there is not any solution
