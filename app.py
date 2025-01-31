import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from rectangle import Rectangle
from drawer import add_rectangle_to_plot
from drawer import add_contour_to_plot
from contour import find_contour

class RectangleDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contouring Rectangles")

        # UI
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=3) 
        self.root.grid_rowconfigure(0, weight=3)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_rowconfigure(8, weight=3)
        
        # Custom button
        buttonStyle = ttk.Style()
        buttonStyle.configure(
            "Custom.TButton", 
            font=("Arial", 16),
            padding=(8, 8)
        )

        self.create_input_fields()

        # Create and enbed graph
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.ax.grid(visible=True, linestyle="--", linewidth=1)
        self.ax.set_aspect('equal')
        self.ax.set_title("Graph")
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1, column=2, rowspan=12, padx=30, pady=30)

        self.patches = []
        self.contour = []
        self.rectangles = []
        self.rect_visible = True

    def create_input_fields(self):
        # Create the left pannel for GUI

        # Point 1
        ttk.Label(self.root, text="Point 1", font=("Arial", 23)).grid(row=1, column=0, sticky="e")
        
        ttk.Label(self.root, text="X: ", font=("Arial", 18)).grid(row=2, column=0, sticky="e")
        self.x1_entry = ttk.Entry(self.root, width=12, font=("Arial", 18))
        self.x1_entry.grid(row=2, column=1, sticky="w", padx=20, pady=10)
        
        ttk.Label(self.root, text="Y: ", font=("Arial", 18)).grid(row=3, column=0, sticky="e")
        self.y1_entry = ttk.Entry(self.root, width=12, font=("Arial", 18))
        self.y1_entry.grid(row=3, column=1, sticky="w", padx=20, pady=10)

        # Point 2 
        ttk.Label(self.root, text="Point 2", font=("Arial", 23)).grid(row=4, column=0, sticky="e")
        
        ttk.Label(self.root, text="X: ", font=("Arial", 18)).grid(row=5, column=0, sticky="e")
        self.x2_entry = ttk.Entry(self.root, width=12, font=("Arial", 18))
        self.x2_entry.grid(row=5, column=1, sticky="w", padx=20, pady=10)
        
        ttk.Label(self.root, text="Y: ", font=("Arial", 18)).grid(row=6, column=0, sticky="e")
        self.y2_entry = ttk.Entry(self.root, width=12, font=("Arial", 18))
        self.y2_entry.grid(row=6, column=1, sticky="w", padx=20, pady=10)

        # "Add rectangle" button
        self.add_button = ttk.Button(self.root, text="Add",command=self.add_rectangle, style="Custom.TButton")
        self.add_button.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # "Add random" button
        self.random_button = ttk.Button(self.root, text="Random", command=self.random_rectangle, style="Custom.TButton")
        self.random_button.grid(row=7, column=0, padx=20, pady=10, sticky="e")

        # "Hide rectangles" button
        self.toggle_button = ttk.Button(self.root, text="Hide", command=self.toggle_rectangles, style="Custom.TButton")
        self.toggle_button.grid(row=8, column=1, padx=20, pady=10, sticky="w")
        
        # "Clear" button
        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear_rectangles, style="Custom.TButton")
        self.clear_button.grid(row=8, column=0, padx=20, pady=10, sticky="e")

    def add_rectangle(self):
        """Adds a rectangle from user input to the plot and stores it to memory.\n - input: any 2 points (can have any slope);\n - output: corresponding rectangle (edges parallel to the xOy axis).\n - adds to memory and to embedded graph."""
        try:
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())
        except ValueError:
            print("Invalid input. Please enter numeric values for the coordinates.")
            return

        # Create a rectangle
        rectangle = Rectangle(x1, y1, x2, y2)
        patch = add_rectangle_to_plot(self.ax, rectangle)
        self.rectangles.append((x1, y1, x2, y2))

        # Store rectangles
        if patch:
            self.patches.append(patch)

        contour = find_contour(self.rectangles)
        add_contour_to_plot(self.ax, contour)

        # Refresh
        self.canvas.draw()
    
    def toggle_rectangles(self):
        """Toggles the visibility of all the rectangles."""
        self.rect_visible = not self.rect_visible  # Toggle state

        for rect in self.patches:
            rect.set_visible(self.rect_visible)
        
        self.toggle_button.config(text="Unhide" if not self.rect_visible else "Hide")

        self.canvas.draw()
        
    def clear_rectangles(self):
        """Clear the graph."""
        # Clear the variables
        for patch in self.ax.patches:
            patch.remove()
        
        for line in self.ax.get_lines():
            line.remove()
        
        self.patches = []
        self.contour = []
        self.rectangles = []
        self.rect_visible = True
        # Refresh
        self.canvas.draw()
    
    def random_rectangle(self):
        """Insert a random rectangle."""
        point_set=[]
        