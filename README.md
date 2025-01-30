# contouring-rectangles

## Project overview
This project presents a Python implementation of the _**Lipski-Preparata**_ algorithm for finding the _**contour of a union of iso-oriented rectangles**_. The algorithm operates in $O(n \log{n} +p \log{(\frac{2n^2}{p})})$ complexity, with a $O(n \log{n})$ best case, when there are no inner holes in the figure.
Potential use cases include:
- object detection and bounding boxes,
- collision detection in robotics and game development,
- shape and pattern recognition in LLM training and
- image processing.

Visualization and user interface are implemented with the use of `matplotlib` and `tkinter` libraries from `python3`.

## Repository structure
This repository contains the following Python scripts:
1. `main.py`:
  - Main function of the program, runs the methods and routines described in `app.py`
2.  `app.py`:
  - Routines run for user interface, collecting input, calling the functions associated to `rectangle.py` and `contour.py`.
  - Initializes the UI window and buttons.
  - Calls functions for computing and drawing the shapes.
3.  `contour.py`:
  - Implementation of the Lipski-Preparata algorithm [1].
  - Adapts the algorithm to fit Python framework and UX/UI standards.
4.  `rectangle.py`
5.  `drawer.py`

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or later
- pip (Python package manager)

You can check your Python version using:
```
python --version
```

## Installation
1. Clone the repository:
```
git clone https://github.com/taniatitiriga/contouring-rectangles.git
cd contouring-rectangles
```
2. Set up a virtual environment (Optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```
3. Install required libraries:
- Install `matplotlib` for visualization:
```
pip install matplotlib
```

## Usage
### Run

  - **Run the script** (or use your prefered IDE - I recommend VSCode):
```
python main.py
```
### Interacting with the interface

The interface is straight-forward and easy to use. Input any 2 points with floating point coordinates $\in [0, 10]$. Then, hit the Add button. This will display a new rectangle (blue) and the contour (red). If you want to see the contour better, click Hide.
Continue adding rectangles and see how the contour gets dynamically re-computed.

![interface](https://github.com/user-attachments/assets/08fdede1-c1af-4065-bb97-b0248624dc8c)

## Credits
A project by [Tania Titirigă](https://www.linkedin.com/in/tania-titiriga/) and [Mark Dragotă](https://www.linkedin.com/in/markdragota/). 

## Bibliography
[1] W. Lipski and F. P. Preparata, _["Finding the contour of a union of isooriented rectangles"](https://doi.org/10.1016/0196-6774(80)90011-5)_, Coordinated Science Lab., Univ. of Illinois at UrbanaChampaign, 1979.




