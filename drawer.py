import matplotlib.patches as patches

def add_rectangle_to_plot(ax, rectangle):
    """Draw a rectangle on the Matplotlib axis."""
    lower_left_x, lower_left_y, width, height = rectangle.calculate_geometry()
    rect_patch = patches.Rectangle(
        (lower_left_x, lower_left_y), width, height, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.3
    )
    ax.add_patch(rect_patch)
