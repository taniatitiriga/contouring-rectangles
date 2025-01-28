import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from rectangle import Rectangle
from drawer import add_rectangle_to_plot

class RectangleDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contouring Rectangles")
        
        buttonStyle = ttk.Style()
        buttonStyle.configure(
            "Custom.TButton", 
            font=("Arial", 22),
            padding=(10, 10)
        )

        # Create input fields for the two points
        self.create_input_fields()

        # Create a Matplotlib figure and embed it in Tkinter
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect('equal')
        self.ax.set_title("Graph")
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=2, rowspan=12, padx=30, pady=30)

    def create_input_fields(self):
        # Input labels and entry fields - point 1
        ttk.Label(self.root, text="Point 1", font=("Arial", 28)).grid(row=0, column=0, sticky="e")
        
        ttk.Label(self.root, text="X: ", font=("Arial", 23)).grid(row=1, column=0, sticky="e")
        self.x1_entry = ttk.Entry(self.root, width=12, font=("Arial", 23))
        self.x1_entry.grid(row=1, column=1, sticky="w", padx=20, pady=10)
        
        ttk.Label(self.root, text="Y: ", font=("Arial", 23)).grid(row=2, column=0, sticky="e")
        self.y1_entry = ttk.Entry(self.root, width=12, font=("Arial", 23))
        self.y1_entry.grid(row=2, column=1, sticky="w", padx=20, pady=10)

        # Input labels and entry fields - point 2 
        ttk.Label(self.root, text="Point 2", font=("Arial", 28)).grid(row=3, column=0, sticky="e")
        
        ttk.Label(self.root, text="X: ", font=("Arial", 23)).grid(row=4, column=0, sticky="e")
        self.x2_entry = ttk.Entry(self.root, width=12, font=("Arial", 23))
        self.x2_entry.grid(row=4, column=1, sticky="w", padx=20, pady=10)
        
        ttk.Label(self.root, text="Y: ", font=("Arial", 23)).grid(row=5, column=0, sticky="e")
        self.y2_entry = ttk.Entry(self.root, width=12, font=("Arial", 23))
        self.y2_entry.grid(row=5, column=1, sticky="w", padx=20, pady=10)

        # Button to add the rectangle
        self.add_button = ttk.Button(self.root, text="Add Rectangle",command=self.add_rectangle, style="Custom.TButton")
        self.add_button.grid(row=6, column=1, padx=20, pady=10)

    def add_rectangle(self):
        # Get the input values
        try:
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())
        except ValueError:
            print("Invalid input. Please enter numeric values for the coordinates.")
            return

        # Create a Rectangle object
        rectangle = Rectangle(x1, y1, x2, y2)

        # Add the rectangle to the plot
        add_rectangle_to_plot(self.ax, rectangle)

        # Refresh the canvas
        self.canvas.draw()
