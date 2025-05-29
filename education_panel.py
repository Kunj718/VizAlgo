import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3

from algo_des_db import AlgorithmDescriptionDB

class EducationalPanel(tk.Toplevel):
    def __init__(self, master, algorithm_name):
        super().__init__(master)
        self.title(f"{algorithm_name} Algorithm Description")
        self.geometry(self.calculate_position())  # Position the window
        self.resizable(False, False)
        self.attributes("-topmost", True)  # Ensure it stays on top
        
        # Fetch algorithm details
        self.db = AlgorithmDescriptionDB()
        algorithm_info = self.db.get_algorithm_info(algorithm_name)

        if not algorithm_info:
            algorithm_info = {
                "definition": "No information available.",
                "working": "",
                "complexity": "",
                "pseudocode": ""
            }

        self.configure(bg="white")

        # Create a canvas with a scrollbar
        container = tk.Frame(self, bg="white")
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg="white", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="white")  # The frame inside the canvas

        # Connect the frame to the canvas
        scroll_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Enable scrolling with the mouse wheel
        self.bind("<Enter>", lambda e: self.bind_all("<MouseWheel>", self._on_mousewheel))
        self.bind("<Leave>", lambda e: self.unbind_all("<MouseWheel>"))

        # Function to add section titles
        def add_title(frame, text):
            label = tk.Label(frame, text=text, font=("Arial", 18, "bold", "underline"), bg="white")
            label.pack(anchor="w", pady=(5, 2))

        # Function to add section text
        def add_text(frame, text):
            label = tk.Label(frame, text=text, font=("Arial", 14), wraplength=350, justify="left", bg="white")
            label.pack(anchor="w", pady=(0, 5))

        # Add formatted content
        add_title(scroll_frame, "Definition:")
        add_text(scroll_frame, algorithm_info["definition"])

        add_title(scroll_frame, "Working:")
        add_text(scroll_frame, algorithm_info["working"])

        add_title(scroll_frame, "Time Complexity:")
        add_text(scroll_frame, algorithm_info["complexity"])

        add_title(scroll_frame, "Pseudocode:")
        add_text(scroll_frame, algorithm_info["pseudocode"])

        # Add relevant image
        # self.add_algorithm_image(scroll_frame, algorithm_name)

        # Save references
        self.canvas = canvas
        self.scroll_frame = scroll_frame

    def calculate_position(self):
        """Calculate the position for the window to be in the middle-right of the screen."""
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 500  # Width of the description panel
        window_height = 720  # Height of the description panel

        x_position = screen_width - window_width + 300  # 20 pixels from right
        y_position = (screen_height // 2) - (window_height // 2)  # Centered vertically

        return f"{window_width}x{window_height}+{x_position}+{y_position}"

    # def add_algorithm_image(self, frame, algorithm_name):
    #     """Load and display an image relevant to the algorithm."""
    #     image_path = f"images/{algorithm_name.lower().replace(' ', '_')}.png"

    #     try:
    #         img = Image.open(image_path)
    #         img = img.resize((350, 200), Image.LANCZOS)
    #         img_tk = ImageTk.PhotoImage(img)

    #         img_label = tk.Label(frame, image=img_tk, bg="white")
    #         img_label.image = img_tk  # Keep a reference to avoid garbage collection
    #         img_label.pack(pady=10)
    #     except Exception as e:
    #         print(f"Image not found for {algorithm_name}: {e}")

    def _on_mousewheel(self, event):
        """Enable scrolling with the mouse wheel."""
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# import sqlite3

# from algo_des_db import AlgorithmDescriptionDB  # Ensure this module is correctly implemented

# class EducationalPanel(tk.Toplevel):
#     def __init__(self, master, algorithm_name):
#         super().__init__(master)
#         self.title(f"{algorithm_name} Algorithm Description")
#         self.geometry(self.calculate_position())  # Position the window at the middle-right
#         # self.resizable(False, False)
        
#         # Ensure the window stays on top
#         self.attributes("-topmost", True)
        
#         # Fetch algorithm details
#         self.db = AlgorithmDescriptionDB()
#         algorithm_info = self.db.get_algorithm_info(algorithm_name)

#         if not algorithm_info:
#             algorithm_info = {
#                 "definition": "No information available.",
#                 "working": "",
#                 "complexity": "",
#                 "pseudocode": ""
#             }

#         # Apply styling
#         self.configure(bg="white")

#         # Create a frame for content with padding
#         content_frame = tk.Frame(self, bg="white", padx=10, pady=10)
#         content_frame.pack(fill="both", expand=True)

#         # Function to add section titles
#         def add_title(frame, text):
#             label = tk.Label(frame, text=text, font=("Arial", 18, "bold", "underline"), bg="white")
#             label.pack(anchor="w", pady=(5, 2))

#         # Function to add section text
#         def add_text(frame, text):
#             label = tk.Label(frame, text=text, font=("Arial", 16), wraplength=350, justify="left", bg="white")
#             label.pack(anchor="w", pady=(0, 5))

#         # Add formatted content
#         add_title(content_frame, "Definition:")
#         add_text(content_frame, algorithm_info["definition"])

#         add_title(content_frame, "Working:")
#         add_text(content_frame, algorithm_info["working"])

#         add_title(content_frame, "Time Complexity:")
#         add_text(content_frame, algorithm_info["complexity"])

#         add_title(content_frame, "Pseudocode:")
#         add_text(content_frame, algorithm_info["pseudocode"])

#         # Add relevant image
#         # self.add_algorithm_image(content_frame, algorithm_name)

#     def calculate_position(self):
#         """Calculate the position for the window to be in the middle-right of the screen."""
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()

#         window_width = 500  # Width of the description panel
#         window_height = 860  # Height of the description panel

#         x_position = screen_width - window_width + 300  # 20 pixels from right
#         y_position = (screen_height // 2) - (window_height // 2)  # Centered vertically

#         return f"{window_width}x{window_height}+{x_position}+{y_position}"

#     # def add_algorithm_image(self, frame, algorithm_name):
#     #     """Load and display an image relevant to the algorithm."""
#     #     image_path = f"images/{algorithm_name.lower().replace(' ', '_')}.png"

#     #     try:
#     #         img = Image.open(image_path)
#     #         img = img.resize((350, 200), Image.LANCZOS)
#     #         img_tk = ImageTk.PhotoImage(img)

#     #         img_label = tk.Label(frame, image=img_tk, bg="white")
#     #         img_label.image = img_tk  # Keep a reference to avoid garbage collection
#     #         img_label.pack(pady=10)
#     #     except Exception as e:
#     #         print(f"Image not found for {algorithm_name}: {e}")


# # import tkinter as tk
# # from algo_des_db import AlgorithmDescriptionDB

# # class EducationalPanel(tk.Toplevel):
# #     def __init__(self, master, algorithm_name):
# #         super().__init__(master)
# #         self.title(f"{algorithm_name} - Description")
# #         self.configure(bg="white")
# #         # self.resizable(False, False)  # Prevent resizing

# #         # Ensure database connection
# #         db = AlgorithmDescriptionDB()
# #         algo_info = db.get_algorithm_info(algorithm_name)

# #         if algo_info:
# #             description_text = (
# #                 f"📌 Definition:\n{algo_info['definition']}\n\n"
# #                 f"⚙️ Working:\n{algo_info['working']}\n\n"
# #                 f"⏳ Complexity:\n{algo_info['complexity']}\n\n"
# #                 f"📜 Pseudocode:\n{algo_info['pseudocode']}"
# #             )
# #         else:
# #             description_text = "Algorithm description not found."

# #         # Text widget for better formatting
# #         self.text_widget = tk.Text(self, wrap="word", font=("Arial", 12), bg="white", width=50, height=15)
# #         self.text_widget.insert("1.0", description_text)
# #         self.text_widget.config(state="disabled")  # Make it read-only
# #         self.text_widget.pack(padx=10, pady=10, fill="both", expand=True)

# #         # Position the window dynamically
# #         self.position_window(master)

# #         # Ensure it stays on top and doesn't minimize
# #         self.attributes('-topmost', True)
# #         self.grab_set()  # Keep focus on the panel

# #     def position_window(self, master):
# #         """Position the window in the middle-right side of the main application."""
# #         master.update_idletasks()

# #         main_x = master.winfo_x()
# #         main_y = master.winfo_y()
# #         main_width = master.winfo_width()
# #         main_height = master.winfo_height()

# #         panel_width = 520
# #         panel_height = 400

# #         pos_x = main_x + main_width - panel_width - 20
# #         pos_y = main_y + (main_height // 2) - (panel_height // 2)

# #         self.geometry(f"{panel_width}x{panel_height}+{pos_x}+{pos_y}")

# # #----------------------------------------------------------------------------------------------------------------------------------------------
# # # import tkinter as tk
# # # from algo_des_db import *

# # # class EducationalPanel(tk.Toplevel):
# # #     def __init__(self, master, algorithm_name):
# # #         super().__init__(master)
# # #         self.title(f"{algorithm_name} - Description")
# # #         self.configure(bg="white")
# # #         # self.resizable(False, False)  # Prevent resizing

# # #         # Get description from database
# # #         GAI = AlgorithmDescriptionDB()
# # #         description = GAI.get_algorithm_info(algorithm_name)
        
# # #         # Create a label to display the description
# # #         self.text_label = tk.Label(self, text=description, font=("Arial", 12), bg="white", wraplength=400, justify="left")
# # #         self.text_label.pack(padx=10, pady=10)

# # #         # Position the window dynamically
# # #         self.position_window(master)

# # #         # Make sure the window stays on top
# # #         self.attributes('-topmost', True)

# # #     def position_window(self, master):
# # #         """ Position the window in the middle-right side of the main application """
# # #         master.update_idletasks()  # Ensure correct dimensions

# # #         # Get main window dimensions
# # #         main_x = master.winfo_x()
# # #         main_y = master.winfo_y()
# # #         main_width = master.winfo_width()
# # #         main_height = master.winfo_height()

# # #         # Set width & height of the educational panel
# # #         panel_width = 420
# # #         panel_height = 300

# # #         # Calculate position (middle-right)
# # #         pos_x = main_x + main_width - panel_width - 20  # Right side with 20px margin
# # #         pos_y = main_y + (main_height // 2) - (panel_height // 2)  # Middle vertically
# # #         self.geometry(f"{panel_width}x{panel_height}+{pos_x}+{pos_y}")


# # # #-------------------------------------------------------------------------------------------------------------------------------------------
# # #     # def __init__(self, master, algorithm_name):
# # #     #     """ Initialize the educational panel as a Toplevel window """
# # #     #     self.algorithm_name = algorithm_name
# # #     #     self.window = tk.Toplevel(master)
# # #     #     self.window.title(f"{algorithm_name} - Algorithm Description")
# # #     #     self.window.configure(bg="#E8F5E9")  # Light green background
        
# # #     #     # Set window size and position (right-middle side)
# # #     #     window_width = 420
# # #     #     window_height = 300
# # #     #     screen_width = self.window.winfo_screenwidth()
# # #     #     screen_height = self.window.winfo_screenheight()
# # #     #     x_position = screen_width - window_width - 20  # 20px margin from right
# # #     #     y_position = (screen_height // 2) - (window_height // 2)  # Middle of screen

# # #     #     self.window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        
# # #     #     # Make the window stay on top and prevent minimization
# # #     #     self.window.attributes('-topmost', True)
# # #     #     self.window.protocol("WM_DELETE_WINDOW", self.window.withdraw)  # Hide instead of close

# # #     #     # Fetch algorithm details from the database
# # #     #     db = AlgorithmDescriptionDB()
# # #     #     description = db.get_algorithm_info(algorithm_name)

# # #     #     # Title Label
# # #     #     title_label = tk.Label(self.window, text=algorithm_name, font=("Arial", 14, "bold"), bg="#E8F5E9")
# # #     #     title_label.pack(pady=5)

# # #     #     # Description Box
# # #     #     self.text_box = tk.Text(self.window, wrap="word", font=("Arial", 12), height=15, width=50, bg="white", bd=2, relief="sunken")
# # #     #     self.text_box.insert("1.0", description if description else "No description available.")
# # #     #     self.text_box.config(state="disabled")  # Read-only mode
# # #     #     self.text_box.pack(padx=10, pady=5, fill="both", expand=True)
# # # #----------------------------------------------------------------------------------------------------------------------------------------------

# # # # import tkinter as tk
# # # # from algo_des_db import AlgorithmDescriptionDB

# # # # class EducationalPanel:
# # # #     def __init__(self, parent, algorithm_name):
# # # #         self.parent = parent
# # # #         self.algorithm_name = algorithm_name
# # # #         self.db = AlgorithmDescriptionDB()
# # # #         self.window = None

# # # #         self.show_description()

# # # #     def show_description(self):
# # # #         """Creates a Toplevel window at the bottom right corner to show algorithm details."""
# # # #         if self.window:
# # # #             self.window.destroy()  # Destroy existing window before creating a new one

# # # #         self.window = tk.Toplevel(self.parent)
# # # #         self.window.title(f"{self.algorithm_name} Description")
# # # #         self.window.geometry("400x300+1000+500")  # Bottom-right position
# # # #         self.window.configure(bg="white")

# # # #         # Fetch Algorithm Details
# # # #         details = self.db.get_algorithm_info(self.algorithm_name)

# # # #         if details:
# # # #             definition_label = tk.Label(self.window, text="Definition:", font=("Arial", 10, "bold"), bg="white")
# # # #             definition_label.pack(anchor="w", padx=10, pady=5)
# # # #             definition_text = tk.Text(self.window, wrap="word", height=3, width=50, bg="white", borderwidth=0)
# # # #             definition_text.insert("1.0", details["definition"])
# # # #             definition_text.config(state="disabled")
# # # #             definition_text.pack(padx=10, pady=2)

# # # #             working_label = tk.Label(self.window, text="Working:", font=("Arial", 10, "bold"), bg="white")
# # # #             working_label.pack(anchor="w", padx=10, pady=5)
# # # #             working_text = tk.Text(self.window, wrap="word", height=3, width=50, bg="white", borderwidth=0)
# # # #             working_text.insert("1.0", details["working"])
# # # #             working_text.config(state="disabled")
# # # #             working_text.pack(padx=10, pady=2)

# # # #             complexity_label = tk.Label(self.window, text="Time Complexity:", font=("Arial", 10, "bold"), bg="white")
# # # #             complexity_label.pack(anchor="w", padx=10, pady=5)
# # # #             complexity_text = tk.Label(self.window, text=details["complexity"], bg="white")
# # # #             complexity_text.pack(padx=10, pady=2)

# # # #             pseudocode_label = tk.Label(self.window, text="Pseudocode:", font=("Arial", 10, "bold"), bg="white")
# # # #             pseudocode_label.pack(anchor="w", padx=10, pady=5)
# # # #             pseudocode_text = tk.Text(self.window, wrap="word", height=5, width=50, bg="white", borderwidth=0)
# # # #             pseudocode_text.insert("1.0", details["pseudocode"])
# # # #             pseudocode_text.config(state="disabled")
# # # #             pseudocode_text.pack(padx=10, pady=2)

# # # #         else:
# # # #             error_label = tk.Label(self.window, text="No description available!", font=("Arial", 12), fg="red", bg="white")
# # # #             error_label.pack(pady=20)

# # # # # import tkinter as tk
# # # # # from tkinter import scrolledtext
# # # # # from algo_des_db import *

# # # # # class EducationalPanel(tk.Frame):
# # # # #     def __init__(self, parent, algorithm_name=""):
# # # # #         super().__init__(parent, bg="white", bd=2, relief=tk.RIDGE)
# # # # #         self.algorithm_name = algorithm_name

# # # # #         self.title_label = tk.Label(self, text=algorithm_name, font=("Arial", 16, "bold"), bg="white")
# # # # #         self.title_label.pack(pady=5)

# # # # #         self.text_area = tk.Text(self, wrap="word", height=15, width=60, font=("Arial", 12))
# # # # #         self.text_area.pack(padx=10, pady=5, fill="both", expand=True)

# # # # #         self.load_description(self.algorithm_name)
# # # # #         # self.load_algorithm_info()

# # # # #     def load_description(self, algorithm_name):
# # # # #         """ Fetch and display algorithm details from the database """
# # # # #         description = get_algorithm_description(algorithm_name)
# # # # #         self.text_area.config(state=tk.NORMAL)
# # # # #         self.text_area.delete("1.0", tk.END)  # Clear previous content
# # # # #         self.text_area.insert(tk.END, description if description else "Description not available.")
# # # # #         self.text_area.config(state=tk.DISABLED)  # Disable editing

# # # # #     # def load_algorithm_info(self):
# # # # #     #     """ Fetch algorithm details from the database and display them. """
# # # # #     #     conn = sqlite3.connect("algorithms.db")
# # # # #     #     cursor = conn.cursor()

# # # # #     #     cursor.execute("SELECT description, complexity, pseudocode FROM algorithms WHERE name=?", (self.algorithm_name,))
# # # # #     #     result = cursor.fetchone()
# # # # #     #     conn.close()

# # # # #     #     if result:
# # # # #     #         description, complexity, pseudocode = result
# # # # #     #         content = f"📖 Definition:\n{description}\n\n"
# # # # #     #         content += f"⏳ Complexity:\n{complexity}\n\n"
# # # # #     #         content += f"📝 Pseudocode:\n{pseudocode}\n"
# # # # #     #     else:
# # # # #     #         content = "No details available for this algorithm."

# # # # #     #     self.text_area.insert("1.0", content)
# # # # #     #     self.text_area.config(state="disabled")  # Make text read-only
