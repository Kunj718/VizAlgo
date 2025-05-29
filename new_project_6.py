import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import threading
import networkx as nx
from sorting import *
from searching import *
from graph_traversal import *
from code_display import CodeDisplay
from algo import *
from Step_control import *
from algo_des_db import *
from education_panel import *
# import time
# from login import login_user

class AlgorithmVisualizer:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Algorithm Visualizer")
        # self.root.geometry("1000x700")
        self.root.configure(bg="#E8F5E9")
        self.root.state('zoomed')  # Allow maximized window

        # Control Variables
        self.running = False
        self.target_value = None
        self.speed = 1
        self.graph = None
        # self.dark_mode = False
        self.graph_positions = None
        self.data = []
                                
        # Step by step execution.
        self.step_mode = False  # Tracks if step-by-step mode is active
        self.current_step = 0   # Keeps track of the current step
        self.step_event = threading.Event()  # Synchronizes step execution
        self.step_event.set()  # Allows steps to proceed initially
        self.step_history = []  # Initialize history to track steps
        
        # UI Elements
        self.create_widgets()
        self.update_ui()
        # self.create_ui()

    def create_widgets(self):
        # Header Frame
        # header_frame = tk.Frame(self.root)
        # header_frame.pack(fill=tk.X, pady=10)
        # style = ttk.Style()
        # style.configure("B.TButton" , font=("Arial",12,"underline"))
        header_frame = tk.Label(self.root, text="Algorithm Visualizer", font=("Helvetica", 20, "bold"), bg="#E8F5E9", fg="black").pack(pady=10)


        # Control Frame
        control_frame = tk.Frame(self.root, bg="#A5D6A7", bd=2, relief=tk.RIDGE)
        control_frame.pack(fill="x",padx=10, pady=5)

        self.type_label = tk.Label(control_frame, text="Select Type:", font=("Arial",12,"underline","bold"), bg="#A5D6A7")
        self.type_label.grid(row=0, column=0)
        self.type_combo = ttk.Combobox(control_frame, values=["Sorting", "Searching", "Graph Traversal"], state="readonly" , font=("Arial",12,"bold"))
        self.type_combo.grid(padx=7, pady=10)
        self.type_combo.grid(row=0, column=1)
        self.type_combo.current(None)

        self.algorithm_label = tk.Label(control_frame, text="Select Algorithm:" , font=("Arial",12,"underline","bold"), bg="#A5D6A7")
        self.algorithm_label.grid(row=0, column=2)
        self.algorithm_combo = ttk.Combobox(control_frame, values=[], state="readonly" , font=("Arial",12,"bold"))
        self.algorithm_combo.grid(padx=7, pady=10)
        self.algorithm_combo.grid(row=0, column=3)

        self.run_button = ttk.Button(control_frame, text="Run", command=self.start_algorithm)
        self.run_button.grid(padx=7, pady=10)
        self.run_button.grid(row=0, column=4)

        self.stop_button = ttk.Button(control_frame, text="Stop", command=self.stop_algorithm)
        self.stop_button.grid(padx=7, pady=10)
        self.stop_button.grid(row=0, column=5)

        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset)
        self.reset_button.grid(padx=7, pady=10)
        self.reset_button.grid(row=0, column=6)

        self.generate_button = ttk.Button(control_frame, text="Generate", command=self.generate_data)
        self.generate_button.grid(padx=7, pady=10)
        self.generate_button.grid(row=0, column=11)

        self.data_label = tk.Label(control_frame, text="Input Size:" , font=("Arial",12,"underline","bold"), bg="#A5D6A7")
        self.data_label.grid(pady=10)
        self.data_label.grid(row=0, column=7)
        self.data_size_spinbox = ttk.Spinbox(control_frame, from_=5, to=50, increment=1)
        self.data_size_spinbox.grid(row=0, column=8)

        self.target_label = tk.Label(control_frame, text="Target Value:" , font=("Arial",12,"underline","bold"), bg="#A5D6A7")
        self.target_label.grid(padx=7, pady=10)
        self.target_label.grid(row=0, column=9)
        self.target_entry = tk.Entry(control_frame)
        self.target_entry.grid(row=0, column=10)

        self.speed_label = tk.Label(control_frame, text="Speed:" , font=("Arial",12,"underline","bold"), bg="#A5D6A7")
        self.speed_label.grid( pady=10)
        self.speed_label.grid(row=0, column=12)
        self.speed_scale = tk.Scale(control_frame, from_=1, to=5, orient="horizontal", bg="#A5D6A7" ,command=self.update_speed)
        self.speed_scale.set(1)
        self.speed_scale.grid(row=0, column=13)

        #Step by step execution.
        self.step_checkbox_var = tk.BooleanVar()
        self.step_checkbox = ttk.Checkbutton(control_frame, text="Step Mode", variable=self.step_checkbox_var, command=self.toggle_step_mode)
        self.step_checkbox.grid(row=1, column=4)
        self.next_button = ttk.Button(control_frame, text="Next Step", command=lambda: next_step(self))
        self.next_button.grid(row=1, column=5, pady=5)
        self.prev_button = ttk.Button(control_frame, text="Previous Step", command=lambda: prev_step(self))
        self.prev_button.grid(row=1, column=6)

        # Visualization Frame
        # main_frame = tk.Frame(self.root)
        # main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        # Plot Canvas
        # self.canvas_frame = ttk.Frame(main_frame)
        # self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # self.canvas = FigureCanvasTkAgg(self.figure, self.canvas_frame)
        # self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.figure, self.ax = plt.subplots(figsize=(9,5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(pady=20)

        # Code Display
        code_display_frame = tk.Frame(self.root, bg="white", bd=2, relief=tk.RIDGE).pack(fill="x",padx=10,pady=5)
        self.code_display = CodeDisplay(code_display_frame)
        self.type_combo.bind("<<ComboboxSelected>>", self.update_ui)

        # Educational panel
        # self.educational_panel = EducationalPanel(self.root)
        # self.educational_panel.pack(side="right",fill="both",expand=True)

    def update_ui(self, event=None):
        type_selected = self.type_combo.get()
        if type_selected == "Sorting":
            self.algorithm_combo["values"] = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"]
            self.code_display.load_code(self.algorithm_combo.get().upper().replace(" ","_"))
        elif type_selected == "Searching":
            self.algorithm_combo["values"] = ["Linear Search", "Binary Search", "Jump Search"]
            self.code_display.load_code(self.algorithm_combo.get().upper().replace(" ","_"))
        elif type_selected == "Graph Traversal":
            self.algorithm_combo["values"] = ["BFS", "DFS"]
            self.code_display.load_code(self.algorithm_combo.get().upper().replace(" ","_"))
        self.algorithm_combo.current(None)
        self.algorithm_combo.bind("<<ComboboxSelected>>",self.display_algorithm_code)
        self.algorithm_combo.bind("<<ComboboxSelected>>",self.show_educational_panel)

    def display_algorithm_code(self, event=None):
        algorithm = self.algorithm_combo.get()
        if algorithm == "Bubble Sort":
            self.code_display.load_code(BUBBLE_SORT)
        elif algorithm == "Insertion Sort":
            self.code_display.load_code(INSERTION_SORT)
        elif algorithm == "Merge Sort":
            self.code_display.load_code(MERGE_SORT)
        elif algorithm == "Selection Sort":
            self.code_display.load_code(SELECTION_SORT)
        elif algorithm == "Linear Search":
            self.code_display.load_code(LINEAR_SEARCH)
        elif algorithm == "Binary Search":
            self.code_display.load_code(BINARY_SEARCH)
        elif algorithm == "Jump Search":
            self.code_display.load_code(JUMP_SEARCH)
        # elif algorithm == "BFS":
        #     self.code_display.load_code(BFS_ALGORITHM)
        # elif algorithm == "DFS":
        #     self.code_display.load_code(DFS_ALGORITHM)

    def show_educational_panel(self, event=None):
        algorithm = self.algorithm_combo.get()
        if hasattr(self, 'educational_panel') and self.educational_panel.winfo_exists():
            self.educational_panel.destroy()
        if algorithm:
            self.educational_panel = EducationalPanel(self.root,algorithm)

    def generate_data(self):
        if self.type_combo.get() == "Graph Traversal":
            try:
                num_nodes = int(self.data_size_spinbox.get())
                if num_nodes <= 0:
                    raise ValueError("Size must be greater than 0.")
                self.generate_graph(num_nodes)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer.")
        else:
            try:
                size = int(self.data_size_spinbox.get())
                if size <= 0:
                    raise ValueError("Size must be greater than 0.")
                self.data = [random.randint(30, 100) for _ in range(size)]
                self.update_plot(self.data, ["blue"] * len(self.data))
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer for the array size.")

    def generate_graph(self, num_nodes):
        # self.graph = nx.erdos_renyi_graph(n=num_nodes, p=0.3)
        self.graph = nx.balanced_tree(r=2,h=int(num_nodes**0.5))
        for node in self.graph.nodes:
            self.graph.nodes[node]['value'] = random.randint(1, 100)
        self.graph_positions = nx.spring_layout(self.graph)  # Save fixed positions
        self.update_graph_plot()

    def update_graph_plot(self, highlight_node=None, target_value=None, found=None):
        self.ax.clear()
        pos = self.graph_positions  # Use fixed positions
        node_colors = []

        for node in self.graph.nodes:
            if node == highlight_node:
                node_colors.append('green' if found else 'yellow')
            else:
                node_colors.append('red' if found is False else 'blue')

        nx.draw(self.graph, pos, ax=self.ax, node_color=node_colors, with_labels=True, 
                labels={n: self.graph.nodes[n]['value'] for n in self.graph.nodes})
        self.canvas.draw()

    def update_plot(self, data, colors):
        self.ax.clear()
        bars = self.ax.bar(range(len(data)), data, color=colors)
        for bar, val in zip(bars, data):
            bar_height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width() / 2, bar_height - bar_height * 0.1, str(val), 
                         ha='center', va='bottom', fontsize=10 if bar_height > 15 else 8, color="white")
        self.ax.set_title("Algorithm Visualization")
        self.ax.set_xlim(-1, len(data))
        self.ax.set_ylim(0, max(data) + 10)
        self.canvas.draw()

    def start_algorithm(self):
        if not self.running:
            self.running = True
            algorithm = self.algorithm_combo.get()

            if self.type_combo.get() == "Sorting":
                if self.step_mode:
                    if algorithm == "Merge Sort":
                        threading.Thread(target=merge_sort, args=(self, 0, len(self.data) - 1, self.code_display,self.root)).start()
                    else:
                        step_sorting(self , eval(algorithm.lower().replace(" ","_")),self.data , self.root , self.code_display)
                else:
                    thread = threading.Thread(target=self.run_sorting, args=(algorithm,))
                    thread.start()

            elif self.type_combo.get() == "Searching":
                try:
                    self.target_value = int(self.target_entry.get())
                except ValueError:
                    self.target_value = None
                    messagebox.showerror("Error", "Please enter a valid integer for the target value.")
                    return
                if self.step_mode:
                    step_searching(self , eval(algorithm.lower().replace(" ","_")),self.data ,self.target_value ,self.root , self.code_display)
                else:
                    thread = threading.Thread(target=self.run_searching, args=(algorithm,))
                    thread.start()

            elif self.type_combo.get() == "Graph Traversal":
                try:
                    self.target_value = int(self.target_entry.get())
                except ValueError:
                    self.target_value = None
                    messagebox.showerror("Error", "Please enter a valid integer for the target value.")
                    return
                if self.step_mode:
                    step_traversal(self, eval(algorithm.lower().replace(" ","_")),self.target_value,self.code_display,self.root,self.data,start_node=0)
                else:
                    thread = threading.Thread(target=self.run_graph_traversal, args=(algorithm,))
                    thread.start()

    def run_graph_traversal(self , algorithm):
        start_node = 0
        # self.educational_panel.load_description(algorithm)
        if algorithm == "BFS":
            self.code_display.load_code(BFS)
            bfs(self , start_node , self.target_value , self.code_display, self.root, step_by_step = False)
            # self.stop_algorithm()
        elif algorithm == "DFS":
            self.code_display.load_code(DFS)
            dfs(self , start_node , self.target_value , self.code_display, self.root, step_by_step = False)
            # self.stop_algorithm()
        self.running = False

    def run_sorting(self, algorithm):
        # self.educational_panel.load_description(algorithm)
        # self.code_display(algorithm.upper().replace(" ","_"))
        if algorithm == "Bubble Sort":  
            self.code_display.load_code(BUBBLE_SORT)
            bubble_sort(self, self.data, self.root , self.code_display, step_by_step = False)
            # self.stop_algorithm()
        elif algorithm == "Insertion Sort":          
            self.code_display.load_code(INSERTION_SORT)
            insertion_sort(self, self.data, self.root , self.code_display, step_by_step=False)
            # self.stop_algorithm()
        elif algorithm == "Merge Sort":
            self.code_display.load_code(MERGE_SORT)
            merge_sort(self, 0, len(self.data) - 1, self.code_display, self.root)
            # self.stop_algorithm()
        elif algorithm == "Selection Sort":
            self.code_display.load_code(SELECTION_SORT)
            selection_sort(self, self.data, self.root, self.code_display, step_by_step=False)
            # self.stop_algorithm()
        self.running = False

    def run_searching(self, algorithm):
        # self.educational_panel.load_description(algorithm)
        if algorithm == "Linear Search":
            self.code_display.load_code(LINEAR_SEARCH)
            linear_search(self, self.data, self.root , self.code_display, step_by_step=False)
            # self.stop_algorithm()
        elif algorithm == "Binary Search":
            self.code_display.load_code(BINARY_SEARCH)
            binary_search(self, self.data, self.root , self.code_display, step_by_step=False)
            # self.stop_algorithm()
        elif algorithm == "Jump Search":
            self.code_display.load_code(JUMP_SEARCH)
            jump_search(self, self.data, self.root, self.code_display, step_by_step=False)
            # self.stop_algorithm()
        self.running = False

    def stop_algorithm(self):
        self.running = False
        self.lock = threading.Lock()
        with self.lock:
            if self.data:
                self.update_plot(self.data, ["yellow"] * len(self.data))  # Turn array yellow
        # self.run_button.config(text="Resume", command=self.resume_algorithm)  # Change Run button to Resume

    def resume_algorithm(self):
        if not self.running:
            self.running = True
            algorithm = self.algorithm_combo.get()

            if self.type_combo.get() == "Sorting":
                if self.step_mode:
                    step_sorting(self, eval(algorithm.lower().replace(" ", "_")), self.data, self.root, self.code_display)
                else:
                    thread = threading.Thread(target=self.run_sorting, args=(algorithm,))
                    thread.start()
            
            elif self.type_combo.get() == "Searching":
                thread = threading.Thread(target=self.run_searching, args=(algorithm,))
                thread.start()

            elif self.type_combo.get() == "Graph Traversal":
                thread = threading.Thread(target=self.run_graph_traversal, args=(algorithm,))
                thread.start()

            self.run_button.config(text="Run", command=self.start_algorithm)  # Change back to Run when resumed

    def reset(self):
        self.running = False
        self.data = []
        self.graph = None
        self.graph_positions = None
        self.ax.clear()
        self.canvas.draw()

    def update_speed(self, event=None):
        self.speed = int(self.speed_scale.get())

    def toggle_step_mode(self):
        self.step_mode = self.step_checkbox_var.get()    
    
    # def update_educational_panel(self, event):
    #     """ Update the educational panel based on algorithm selection """
    #     self.educational_panel.destroy()
    #     self.educational_panel = EducationalPanel(self.main_frame, self.algorithm_var.get())
    #     self.educational_panel.pack(side="right", fill="both", expand=True)



if __name__ == "__main__":
    root = tk.Tk()
    app = AlgorithmVisualizer(root)
    root.mainloop()
