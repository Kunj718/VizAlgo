import sqlite3

class AlgorithmDescriptionDB:
    def __init__(self, db_name="algo_descriptions.db"):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        """Creates the table if it doesn't exist."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS algorithms (
                    name TEXT PRIMARY KEY,
                    definition TEXT,
                    working TEXT,
                    complexity TEXT,
                    pseudocode TEXT
                )
            """)
            conn.commit()

    def insert_algorithm(self, name, definition, working, complexity, pseudocode):
        """Inserts an algorithm description into the database."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO algorithms (name, definition, working, complexity, pseudocode)
                VALUES (?, ?, ?, ?, ?)
            """, (name, definition, working, complexity, pseudocode))
            conn.commit()

    def get_algorithm_info(self, name):
        """Retrieves algorithm details based on the algorithm name."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT definition, working, complexity, pseudocode FROM algorithms WHERE name = ?", (name,))
            result = cursor.fetchone()
            if result:
                return {
                    "definition": result[0],
                    "working": result[1],
                    "complexity": result[2],
                    "pseudocode": result[3]
                }
            return None

# import sqlite3

# # Database Initialization
# def initialize_database():
#     """ Creates and populates the algorithm descriptions database if it doesn't exist. """
#     conn = sqlite3.connect("algorithm_descriptions.db")
#     cursor = conn.cursor()
    
#     # Create table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS algorithms (
#             name TEXT PRIMARY KEY,
#             definition TEXT,
#             working TEXT,
#             time_complexity TEXT,
#             pseudocode TEXT
#         )
#     ''')
    
#     # Insert data if not already present
#     algorithms_data = [
#         ("Bubble Sort", 
#          "Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
#          "1. Start at the first element.\n2. Compare it with the next element and swap if necessary.\n3. Repeat for all elements until the list is sorted.",
#          "Best: O(n), Average: O(n²), Worst: O(n²)",
#          "for i = 0 to n-1:\n    for j = 0 to n-i-1:\n        if arr[j] > arr[j+1]:\n            swap(arr[j], arr[j+1])"),
        
#         ("Insertion Sort",
#          "Insertion Sort builds the final sorted array one item at a time, picking elements and placing them in the correct position.",
#          "1. Consider the first element as sorted.\n2. Pick the next element and insert it into the correct position among the sorted elements.\n3. Repeat until the array is sorted.",
#          "Best: O(n), Average: O(n²), Worst: O(n²)",
#          "for i = 1 to n-1:\n    key = arr[i]\n    j = i - 1\n    while j >= 0 and arr[j] > key:\n        arr[j+1] = arr[j]\n        j = j - 1\n    arr[j+1] = key"),
        
#         ("Linear Search",
#          "Linear Search is a simple searching algorithm that checks each element in a list sequentially until the target value is found.",
#          "1. Start at the first element.\n2. Compare it with the target value.\n3. If found, return the index; otherwise, move to the next element.\n4. Repeat until found or the list ends.",
#          "Best: O(1), Average: O(n), Worst: O(n)",
#          "for i = 0 to n-1:\n    if arr[i] == target:\n        return i\nreturn -1"),
        
#         ("Binary Search",
#          "Binary Search is an efficient searching algorithm that works by dividing the list into halves and searching in the relevant half iteratively.",
#          "1. Find the middle element.\n2. If it matches the target, return the index.\n3. If the target is smaller, search the left half; otherwise, search the right half.\n4. Repeat until the target is found or the list is empty.",
#          "Best: O(1), Average: O(log n), Worst: O(log n)",
#          "low = 0, high = n-1\nwhile low ≤ high:\n    mid = (low + high) / 2\n    if arr[mid] == target:\n        return mid\n    elif arr[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1\nreturn -1")
#     ]
    
#     # Insert only if the data is not already present
#     for data in algorithms_data:
#         cursor.execute("INSERT OR IGNORE INTO algorithms VALUES (?, ?, ?, ?, ?)", data)
    
#     conn.commit()
#     conn.close()

# # Function to Retrieve Algorithm Description
# def get_algorithm_description(algorithm_name):
#     """ Fetch algorithm description from the database. """
#     conn = sqlite3.connect("algorithm_descriptions.db")
#     cursor = conn.cursor()
    
#     cursor.execute("SELECT definition, working, time_complexity, pseudocode FROM algorithms WHERE name = ?", (algorithm_name,))
#     result = cursor.fetchone()
    
#     conn.close()

#     if result:
#         definition, working, time_complexity, pseudocode = result
#         return f"**Definition:**\n{definition}\n\n**Working:**\n{working}\n\n**Time Complexity:**\n{time_complexity}\n\n**Pseudocode:**\n{pseudocode}"
#     else:
#         return "Algorithm description not found."

# # Initialize database when the script is run
# initialize_database()


# # import sqlite3

# # def setup_database():
# #     conn = sqlite3.connect("algorithms.db")
# #     cursor = conn.cursor()

# #     # Create table if not exists
# #     cursor.execute('''CREATE TABLE IF NOT EXISTS algorithms (
# #                         name TEXT PRIMARY KEY,
# #                         description TEXT,
# #                         complexity TEXT,
# #                         pseudocode TEXT)''')

# #     # Insert example data
# #     data = [
# #         ("Bubble Sort", 
# #          "Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.",
# #          "Best: O(n), Average: O(n²), Worst: O(n²)",
# #          "for i in range(n):\n  for j in range(0, n-i-1):\n    if arr[j] > arr[j+1]:\n      swap(arr[j], arr[j+1])"),
        
# #         ("Merge Sort",
# #          "Merge Sort is a divide-and-conquer algorithm that recursively splits the array into halves, sorts each half, and then merges them back together.",
# #          "O(n log n) in all cases",
# #          "def mergeSort(arr):\n  if len(arr) > 1:\n    mid = len(arr) // 2\n    L = arr[:mid]\n    R = arr[mid:]\n    mergeSort(L)\n    mergeSort(R)\n    merge(L, R, arr)"),
        
# #         ("Binary Search",
# #          "Binary Search is an efficient algorithm for finding an item in a sorted list by repeatedly dividing the search space in half.",
# #          "O(log n)",
# #          "def binarySearch(arr, x):\n  left, right = 0, len(arr) - 1\n  while left <= right:\n    mid = (left + right) // 2\n    if arr[mid] == x:\n      return mid\n    elif arr[mid] < x:\n      left = mid + 1\n    else:\n      right = mid - 1")
# #     ]

# #     # Insert data into table
# #     cursor.executemany("INSERT OR IGNORE INTO algorithms VALUES (?, ?, ?, ?)", data)

# #     conn.commit()
# #     conn.close()

# # # Run once to initialize DB
# # setup_database()

# # #------------------------------------------------------------------------------------------------------------
# # # import sqlite3

# # # def create_database():
# # #     conn = sqlite3.connect("algorithms.db")
# # #     cursor = conn.cursor()
    
# # #     cursor.execute('''
# # #         CREATE TABLE IF NOT EXISTS algorithms (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             name TEXT UNIQUE,
# # #             description TEXT,
# # #             complexity TEXT,
# # #             use_cases TEXT,
# # #             pseudocode TEXT
# # #         )
# # #     ''')
    
# # #     conn.commit()
# # #     conn.close()

# # # def insert_algorithm(name, description="Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.", 
# # #                      complexity="Best: O(n), Worst: O(n²), Avg: O(n²), Space: O(1)",
# # #                        use_cases="Used in small datasets, teaching sorting concepts.",
# # #                          pseudocode="1. Repeat until no swaps are needed:\n2. Iterate over elements and swap adjacent elements if needed."):
# # #     conn = sqlite3.connect("algorithms.db")
# # #     cursor = conn.cursor()

# # #     cursor.execute('''
# # #         INSERT OR IGNORE INTO algorithms (name, description, complexity, use_cases, pseudocode) 
# # #         VALUES (?, ?, ?, ?, ?)
# # #     ''', (name, description, complexity, use_cases, pseudocode))

# # #     conn.commit()
# # #     conn.close()

# # # create_database()
# # # # insert_algorithm(
# # # #     "Bubble Sort",
# # # #     "Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.",
# # # #     "Best: O(n), Worst: O(n²), Avg: O(n²), Space: O(1)",
# # # #     "Used in small datasets, teaching sorting concepts.",
# # # #     "1. Repeat until no swaps are needed:\n2. Iterate over elements and swap adjacent elements if needed."
# # # # )
