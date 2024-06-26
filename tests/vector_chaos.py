from VectorGraph import SVG, POINT, VECTOR

# Create the SVG canvas
svg = SVG(width=200, height=200, view_origin=POINT(-100, -100), view_end=POINT(100, 100))

# Define a vector
vector = VECTOR(start=POINT(0, 0), end=POINT(50,  50), length=10, separation=10, color='red', stroke_width=2)
svg += vector
vector = VECTOR(start=POINT(0, 0), end=POINT(50, -50), length=15, separation=20, color='green', stroke_width=2)
svg += vector
vector = VECTOR(start=POINT(0, 0), end=POINT(-50,  50), length=15, separation=10, color='blue', stroke_width=2)
svg += vector
vector = VECTOR(start=POINT(0, 0), end=POINT(-50, -50), length=10, separation=20, color='orange', stroke_width=2)
svg += vector

vector = VECTOR(start=POINT(0, 0), end=POINT(70,  0), length=25, separation=10, color='gold', stroke_width=2)
svg += vector
vector = VECTOR(start=POINT(0, 0), end=POINT(0, -70), length=15, separation=30, color='silver', stroke_width=2)
svg += vector
vector = VECTOR(start=POINT(0, 0), end=POINT(-70,  0), length=25, separation=15, color='black', stroke_width=2)
svg += vector
vector = VECTOR(start=POINT(0, 0), end=POINT(0, 70), length=15, separation=15, color='yellow', stroke_width=2)
svg += vector

# Draw the SVG
svg.draw('vector.svg')

print("Vector SVG created.")

