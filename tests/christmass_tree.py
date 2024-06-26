from VectorGraph import SVG, POINT, POLYGON, RECTANGLE

# Create the SVG canvas
svg = SVG(width=200, height=400, view_origin=POINT(-100, -200), view_end=POINT(200, 400))

# Define the triangles for the tree
tree_sections = [
    ([(0, 0), (-80, -120), (80, -120)], "#234236"),
    ([(0, 40), (-60, -60), (60, -60)], "#0C5C4C"),
    ([(0, 80), (-40, 0), (40, 0)], "#38755B")
]

# Add the triangles to the SVG
for points, color in tree_sections:
    polygon_points = [POINT(x, y) for x, y in points]
    tree_section = POLYGON(points=polygon_points).colorize(color=color)
    svg += tree_section

# Define the rectangle for the trunk
trunk = RECTANGLE(x=-20, y=-120, width=40, height=30).colorize(color='brown')
svg += trunk

# Draw the SVG
svg.draw('christmas_tree.svg')

print("Christmas tree SVG created.")
