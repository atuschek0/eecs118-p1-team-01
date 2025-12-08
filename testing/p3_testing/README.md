# EECS 118 Project 3 Test Results

Project 3 test results still pending. 

*E31 testing (probably) not required and E32 testing completed. -- KB*

## E31 -- Implement A\* Search Algorithm

### E31 Autograder Results

Instructions didn't include an autograder prompt.

*I ran the test anyways and it returned a lot of things we weren't prompted to implement. I wouldn't worry about it, unless we find out it's required in the Gradescope submission. -- KB*

```
$python autograder.py -q E31

Starting on 12-8 at 4:11:22

Question E31
============
*** PASS: test_cases\E31\astar_0.test
***     solution:               ['Right', 'Down', 'Down']
***     expanded_states:        ['A', 'B', 'D', 'C', 'G']
*** PASS: test_cases\E31\astar_1_graph_heuristic.test
***     solution:               ['0', '0', '2']
***     expanded_states:        ['S', 'A', 'D', 'C']
*** PASS: test_cases\E31\astar_2_manhattan.test
***     pacman layout:          mediumMaze
***     solution length: 68
***     nodes expanded:         221
*** PASS: test_cases\E31\astar_3_goalAtDequeue.test
***     solution:               ['1:A->B', '0:B->C', '0:C->G']
***     expanded_states:        ['A', 'B', 'C']
*** FAIL: test_cases\E31\astar_expand_1.test
***     graph:
***             1      1      6
***         *Q ---> A ---> B ---> [G]
***          |             ^
***          |      3      |
***          \-------------/
***
***         S is the start state, G is the goal.  Arrows mark possible state
***         transitions.  The number next to the arrow is the cost of that transition.
***
***         The heuristic value of each state is:
***             Q 1.0
***             A 6.0
***             B 0.0
***             G 0.0
***     student solution:               ['1', '0']
***     student expanded_states:        ['Q', 'B', 'A']
***
***     correct solution:               ['0', '0', '0']
***     correct expanded_states:        ['Q', 'B', 'A', 'B']
***     correct rev_solution:           ['0', '0', '0']
***     correct rev_expanded_states:    ['Q', 'B', 'A', 'B']
*** FAIL: test_cases\E31\astar_expand_2.test
***     graph:
***             B           E
***            ^  \        ^  \
***           /    V      /    V
***         *A --> C --> D --> F --> [G]
***
***         A is the start state, G is the goal.  Arrows mark
***         possible state transitions.  This graph has multiple
***         paths to the goal, but the heuristic is chosen poorly.
***         This means many nodes will be expanded before aStarSearch
***         has to backtrack to find the optimal solution.
***
***         The heuristic value of each state is:
***             A 10.0
***             B 9.0
***             C 6.0
***             D 5.0
***             E 4.0
***             F 1.0
***             G 0.0
***     student solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
***     student expanded_states:        ['A', 'C', 'D', 'F', 'E', 'B']
***
***     correct solution:               ['0:A->B', '0:B->C', '0:C->D', '0:D->E', '0:E->F', '0:F->G']
***     correct expanded_states:        ['A', 'C', 'D', 'F', 'E', 'F', 'B', 'C', 'D', 'E', 'F']
***     correct rev_solution:           ['0:A->B', '0:B->C', '0:C->D', '0:D->E', '0:E->F', '0:F->G']
***     correct rev_expanded_states:    ['A', 'C', 'D', 'F', 'E', 'F', 'B', 'C', 'D', 'E', 'F']
*** PASS: test_cases\E31\graph_backtrack.test
***     solution:               ['1:A->C', '0:C->G']
***     expanded_states:        ['A', 'B', 'C', 'D']
*** PASS: test_cases\E31\graph_manypaths.test
***     solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
***     expanded_states:        ['A', 'B1', 'C', 'B2', 'D', 'E1', 'F', 'E2']
*** Tests failed.

### Question E31: 0/15 ###


Finished at 4:11:22

Provisional grades
==================
Question E31: 0/15
------------------
Total: 0/15

Your grades are NOT yet registered.  To register your grades, make sure
to follow your instructor's guidelines to receive credit on your project.
```

### E31 Testing

The test case Far gave for E31 is a duplicate of the first E32 test case, and it can't run without E32 implemented.

---

## E32 -- Multi-Corner Navigation (CornersProblem)

### E32 Autograder Results

```
$ python autograder.py -q E32

python autograder.py -q E32
Note: due to dependencies, the following tests will be run: E15 E32
Starting on 12-8 at 4:21:25

Question E15
============
<p1_Search.node object at 0x00000210A1634B50>
*** PASS: test_cases\E15\graph_backtrack.test
***     solution:               ['1:A->C', '0:C->G']
***     expanded_states:        ['A', 'B', 'C', 'D']
<p1_Search.node object at 0x00000210A1634190>
*** PASS: test_cases\E15\graph_bfs_vs_dfs.test
***     solution:               ['1:A->G']
***     expanded_states:        ['A', 'B']
<p1_Search.node object at 0x00000210A1635650>
*** PASS: test_cases\E15\graph_infinite.test
***     solution:               ['0:A->B', '1:B->C', '1:C->G']
***     expanded_states:        ['A', 'B', 'C']
<p1_Search.node object at 0x00000210A1634990>
*** PASS: test_cases\E15\graph_manypaths.test
***     solution:               ['1:A->C', '0:C->D', '1:D->F', '0:F->G']
***     expanded_states:        ['A', 'B1', 'C', 'B2', 'D', 'E1', 'F', 'E2']
<p1_Search.node object at 0x00000210A163D9D0>
*** PASS: test_cases\E15\pacman_1.test
***     pacman layout:          mediumMaze
***     solution length: 68
***     nodes expanded:         269

### Question E15: 20/20 ###


Question E32
============
<p1_Search.node object at 0x00000210A1635AD0>
*** PASS: test_cases\E32\corner_tiny_corner.test
***     pacman layout:          tinyCorner
***     solution length:                28

### Question E32: 15/15 ###


Finished at 4:21:25

Provisional grades
==================
Question E15: 20/20
Question E32: 15/15
------------------
Total: 35/35

Your grades are NOT yet registered.  To register your grades, make sure
to follow your instructor's guidelines to receive credit on your project.
```

### E32 Testing

*Far didn't even update the title bar from UC Berkeley course for these tests!* 😂

**Tiny Corners Layout with Breadth First Search (BFS)**

![E32 BFS test](e32_bfs.png)

```
$ python catman.py -l tinyCorners -p SearchAgent -a fn=astar,prob=CornersProblem --frameTime 0.5

python catman.py -l tinyCorners -p SearchAgent -a fn=astar,prob=CornersProblem --frameTime 0.5
[SearchAgent] using function astar and heuristic nullHeuristic
[SearchAgent] using problem type CornersProblem
AGENT INDEX: 0 TYPE: True
Path found with total cost of 28 in 0.0 seconds
Search nodes expanded: 252
Pacman emerges victorious! Score: 512
Average Score: 512.0
Scores:        512.0
Win Rate:      1/1 (1.00)
Record:        Win
```

**Medium Corners Layout with Uniform Cost Search (UCS)**

![E32 UCS test](e32_ucs.png)

```
$ python catman.py -l mediumCorners -p SearchAgent -a fn=ucs,prob=CornersProblem --frameTime 0.5

[SearchAgent] using function ucs
[SearchAgent] using problem type CornersProblem
AGENT INDEX: 0 TYPE: True
<p1_Search.node object at 0x000001E956A16310>
Path found with total cost of 106 in 0.0 seconds
Search nodes expanded: 1966
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win
```

**Medium Corners Layout with A\* Search**

![E32 A-Star test](e32_astar.png) 
```
$ python catman.py -l mediumCorners -p AStarCornersAgent -z 0.5

python catman.py -l mediumCorners -p AStarCornersAgent -z 0.5
AGENT INDEX: 0 TYPE: True
Path found with total cost of 106 in 0.0 seconds
Search nodes expanded: 1966
Pacman emerges victorious! Score: 434
Average Score: 434.0
Scores:        434.0
Win Rate:      1/1 (1.00)
Record:        Win
```

---

## E33 -- Admissible Heuristic for the Corners Problem

### E33 Autograder Results

```
python autograder.py -q E33
```

### E33 Testing

**Tiny Corners with A\* Search**
```
python catman.py -l tinyCorners -p AStarCornersAgent -z 0.5
```

**Medium Corners with A\* Search**
```
python catman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

## E34 -- Food Search Heuristic (Many-Goal Search)

### E34 Autograder Results

```
python autograder.py -q E34
```

### E34 Testing

**Food Search - Test Search Layout**
```
python catman.py -l testSearch -p AStarFoodSearchAgent
```

**Food Search - Tiny Search Layout**
```
python catman.py -l tinySearch -p AStarFoodSearchAgent
```

**Food Search - Tricky Search Layout**
```
python catman.py -l trickySearch -p AStarFoodSearchAgent
```

**Food Search - Medium Search Layout**
```
python catman.py -l mediumSearch -p AStarFoodSearchAgent
```

---

## E35 -- Closest-Dot Search (Greedy Repeated BFS)

### E35 Autograder Results

```
python autograder.py -q E35
```

### E35 Testing

**Closest-Dot Search - Test Search Layout**
```
python catman.py -l testSearch -p ClosestDotSearchAgent
```

**Closest-Dot Search - Tiny Search Layout**
```
python catman.py -l tinySearch -p ClosestDotSearchAgent
```

**Closest-Dot Search - Tricky Search Layout**
```
python catman.py -l trickySearch -p ClosestDotSearchAgent
```

**Closest-Dot Search - Medium Search Layout**
```
python catman.py -l mediumSearch -p ClosestDotSearchAgent
```
