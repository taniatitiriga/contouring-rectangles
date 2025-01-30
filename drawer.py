import matplotlib.patches as patches

def add_rectangle_to_plot(ax, rectangle):
    """Draw a rectangle on graph. Returns the rectangle to be stored for hide/unhide functionality."""
    lower_left_x, lower_left_y, width, height = rectangle.calculate_geometry()
    
    rect_patch = patches.Rectangle(
        (lower_left_x, lower_left_y), width, height, linewidth=2, edgecolor='blue', facecolor='blue', alpha=0.3
    )
    
    ax.add_patch(rect_patch)
    return rect_patch

def add_contour_to_plot(ax, contour):
    """Draw the contour on graph."""
    
    cont_patch = patches.Polygon(contour, closed=True, edgecolor='red', facecolor='none', linewidth=2)
    ax.add_patch(cont_patch)
