# test_olympic_rings.py
from VectorGraph import SVG, POINT, CIRCLE, GROUP

# Create the SVG canvas
svg = SVG(width=310, height=210, view_origin=POINT(-5, -5), view_end=POINT(305, 205))

# Define the group for the rings with shared properties
rings_group = GROUP()

# Add styles for the group
rings_group.perimeter(color='', width=5)

# Define the colors and positions of the rings
colors_positions = [
    ('blue', (50, 150)),
    ('black', (150, 150)),
    ('red', (250, 150)),
    ('yellow', (100, 100)),
    ('green', (200, 100))
]

# Add the rings to the SVG
for color, (x, y) in colors_positions:
    ring = CIRCLE(x=x, y=y, r=50).transparent(perimeter_color=color)
    rings_group.add(ring)
    svg += ring

# Add the group to the SVG
svg.add_style(rings_group)

# Draw the SVG
svg.draw('olympic_rings.svg')

print("Olympic rings SVG created.")
