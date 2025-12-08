# EECS 118 Project 3 Test Results

Project 3 test results still pending. 

## E31 -- Implement A\* Search Algorithm

### E31 Autograder Results

Instructions didn't include an autograder prompt.

### E31 Testing

```
python catman.py -l tinyCorners -p SearchAgent -a fn=astar,prob=CornersProblem --frameTime 0.5
```

---

## E32 -- Multi-Corner Navigation (CornersProblem)

### E32 Autograder Results

```
python autograder.py -q E32
```

### E32 Testing

**Tiny Corners Layout with Breadth First Search (BFS)**
```
python catman.py -l tinyCorners -p SearchAgent -a fn=breadthFirstSearch,prob=CornersProblem --frameTime 0.5
```

**Medium Corners Layout with Uniform Cost Search (UCS)**
```
python catman.py -l mediumCorners -p SearchAgent -a fn=ucs,prob=CornersProblem --frameTime 0.5
```

**Medium Corners Layout with A\* Search**
```
python catman.py -l mediumCorners -p AStarCornersAgent -z 0.5
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
