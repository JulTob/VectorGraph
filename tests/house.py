from VectorGraph import SVG, POINT, POLYGON, POLYLINE, RECTANGLE, CIRCLE, LINE, GROUP

# Create the SVG canvas
svg = SVG(width=200, height=200, view_origin=POINT(-100, -100), view_end=POINT(100, 100))

# Define the CSS styles
house_style = GROUP(classification='house')
house_style.fill('white')
house_style.perimeter('black', '2px')

roof_style = GROUP(classification='roof')
roof_style.fill('none')
roof_style.perimeter('#d1495b', '10px')
roof_style.roundify()

door_style = GROUP(classification='door')
door_style.fill('#d1495b')

stair_style = GROUP(classification='stair')
stair_style.fill('gray')

window_style = GROUP(classification='window')
window_style.fill('#fdea96')

window_sill_style = GROUP(classification='window-sill')
window_sill_style.fill('#d1495b')
window_sill_style.roundify()

# Add the CSS styles to the SVG
svg.add_style(house_style)
svg.add_style(roof_style)
svg.add_style(door_style)
svg.add_style(stair_style)
svg.add_style(window_style)
svg.add_style(window_sill_style)

# Add the house elements
# Wall
wall_points = [POINT(-65, -80), POINT(-65, 10), POINT(0, 70), POINT(65, 10), POINT(65, -80)]
wall = POLYGON(points=wall_points).classify('wall')
svg += wall

# Roof
roof_points = [POINT(-75, 8), POINT(0, 78), POINT(75, 8)]
roof = POLYLINE(points=roof_points).classify('roof')
svg += roof

# Door
door = RECTANGLE(x=-45, y=-10, width=30, height=60, rx=2).classify('door')
svg += door

# Door knob
door_knob = CIRCLE(x=-35, y=-40, r=2).classify('door-knob')
svg += door_knob

# Stairs
stair1 = RECTANGLE(x=-47, y=-70, width=34, height=5).classify('stair')
stair2 = RECTANGLE(x=-49, y=-75, width=38, height=5).classify('stair')
svg += stair1
svg += stair2

# Window
window = RECTANGLE(x=5, y=-15, width=40, height=35, rx=5).classify('window')
svg += window

# Window cross lines
window_line1 = LINE(origin=POINT(5, -32.5), end=POINT(45, -32.5))
window_line2 = LINE(origin=POINT(25, -15), end=POINT(25, -50))
svg += window_line1
svg += window_line2

# Window sill
window_sill = RECTANGLE(x=2, y=-48, width=46, height=5, rx=5).classify('window-sill')
svg += window_sill

# Round window
round_window = CIRCLE(x=0, y=25, r=15).classify('window')
svg += round_window

# Round window cross lines
round_window_line1 = LINE(origin=POINT(-15, 25), end=POINT(15, 25))
round_window_line2 = LINE(origin=POINT(0, 40), end=POINT(0, 10))
svg += round_window_line1
svg += round_window_line2

# Draw the SVG
svg.draw('house.svg')

print("House SVG created.")
