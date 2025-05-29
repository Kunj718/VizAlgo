from algo_des_db import AlgorithmDescriptionDB

db = AlgorithmDescriptionDB()

# Sample Data
db.insert_algorithm(
    "Bubble Sort",
    "Bubble Sort is a simple sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.",
    "It repeatedly steps through the list, compares adjacent elements, and swaps them if necessary.",
    "Best: O(n)\nWorst: O(n²)\nAvg: O(n²)",
    "for i in range(n):\n    for j in range(n - i - 1):\n        if arr[j] > arr[j + 1]:\n            swap(arr[j], arr[j + 1])"
)

db.insert_algorithm(
    "Selection Sort",
         "Selection Sort works by repeatedly finding the minimum element from the unsorted part "
         "and moving it to the sorted part.",
         "1. Find the minimum element in the unsorted array.\n"
         "2. Swap it with the leftmost unsorted element.\n"
         "3. Move the boundary of the sorted section one step right.\n"
         "4. Repeat until fully sorted.",
         "Best: O(n²)\nAverage: O(n²)\nWorst: O(n²)",
         "for i in range(n):\n"
         "    min_idx = i\n"
         "    for j in range(i+1, n):\n"
         "        if arr[j] < arr[min_idx]:\n"
         "            min_idx = j\n"
         "    swap(arr[i], arr[min_idx])"
)

db.insert_algorithm(
    "Insertion Sort",
         "Insertion Sort builds the sorted array one element at a time, picking elements and "
         "placing them at the correct position.",
         "1. Take an element from the unsorted section.\n"
         "2. Compare it with elements in the sorted section.\n"
         "3. Insert it at the correct position.\n"
         "4. Repeat until all elements are sorted.",
         "Best: O(n)\nAverage: O(n²)\nWorst: O(n²)",
         "for i in range(1, n):\n"
         "    key = arr[i]\n"
         "    j = i - 1\n"
         "    while j >= 0 and arr[j] > key:\n"
         "        arr[j + 1] = arr[j]\n"
         "        j -= 1\n"
         "    arr[j + 1] = key"
)

db.insert_algorithm(
    "Merge Sort",
         "Merge Sort is a divide-and-conquer algorithm that recursively splits the array into halves, "
         "sorts them, and then merges them back together.",
         "1. Divide the array into two halves.\n"
         "2. Recursively sort both halves.\n"
         "3. Merge the sorted halves back together.",
         "Best: O(n log n)\nAverage: O(n log n)\nWorst: O(n log n)",
         "def merge_sort(arr):\n"
         "    if len(arr) > 1:\n"
         "        mid = len(arr) // 2\n"
         "        left_half = arr[:mid]\n"
         "        right_half = arr[mid:]\n"
         "        merge_sort(left_half)\n"
         "        merge_sort(right_half)\n"
         "        merge(arr, left_half, right_half)"
)

db.insert_algorithm(
    "Binary Search",
    "Binary Search is a searching algorithm that finds the position of a target value within a sorted array.",
    "It works by repeatedly dividing the search interval in half.",
    "Best: O(1)\nWorst: O(log n)\nAvg: O(log n)",
    "low = 0, high = n-1\nwhile low <= high:\n    mid = (low + high) // 2\n    if arr[mid] == target:\n        return mid\n    elif arr[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1"
)

db.insert_algorithm(
    "Linear Search",
         "Linear Search is a simple searching algorithm that checks each element in the array "
         "one by one until the target element is found.",
         "1. Start from the leftmost element.\n"
         "2. Compare with the target.\n"
         "3. If found, return index.\n"
         "4. If not, move to the next element.",
         "Best: O(1)\nAverage: O(n)\nWorst: O(n)",
         "for i in range(n):\n"
         "    if arr[i] == target:\n"
         "        return i"
)

db.insert_algorithm(
    "Jump Search",
         "Jump Search is an improvement over Linear Search that divides the array into blocks and searches "
         "only relevant blocks before performing a linear search.",
         "1. Jump ahead by √n steps.\n"
         "2. If the target is greater, jump again.\n"
         "3. If the target is smaller, perform linear search in that block.",
         "Best: O(1)\nAverage:O(√n)\nWorst: O(√n)",
         "def jump_search(arr, target):\n"
         "    step = int(math.sqrt(len(arr)))\n"
         "    prev = 0\n"
         "    while arr[min(step, len(arr)) - 1] < target:\n"
         "        prev = step\n"
         "        step += int(math.sqrt(len(arr)))\n"
         "        if prev >= len(arr):\n"
         "            return -1\n"
         "    for i in range(prev, min(step, len(arr))):\n"
         "        if arr[i] == target:\n"
         "            return i"
)

db.insert_algorithm(
    "BFS",
    "Breadth-First Search (BFS) is a graph traversal algorithm that explores all neighbors "
    "before moving to the next level.",
    "1. Start from the root node.\n"
    "2. Explore all neighbors before moving deeper.\n"
    "3. Use a queue to track nodes to visit.",
    "Best: O(1)\nAverage: O(V+E)\nWorst: O(V+E)",
    "def bfs(graph, start):\n"
    "    queue = [start]\n"
    "    visited = set()\n"
    "    while queue:\n"
    "        node = queue.pop(0)\n"
    "        if node not in visited:\n"
    "            visited.add(node)\n"
    "            queue.extend(graph[node])"
)

db.insert_algorithm(
    "DFS",
    "Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible "
    "along each branch before backtracking.",
    "1. Start from the root node.\n"
    "2. Explore deeper before moving to the next branch.\n"
    "3. Use a stack (recursion) to track nodes.",
    "Best: O(1)\nAverage: O(V+E)\nWorst: O(V+E)",
    "def dfs(graph, start, visited=set()):\n"
    "    if start not in visited:\n"
    "        visited.add(start)\n"
    "        for neighbor in graph[start]:\n"
    "            dfs(graph, neighbor, visited)"
)
print("Database initialized with sample data.")
