from VectorGraph import SVG, POINT, CIRCLE, RECTANGLE, LINE, GROUP

# Create the SVG canvas
svg = SVG(width=200, height=200, view_origin=POINT(-100, -100), view_end=POINT(100, 100))

# Define the CSS styles
gingerbread_style = GROUP(classification='gingerbread')
gingerbread_style.fill('#cd803d')

head_style = GROUP(classification='head')
head_style.fill('#cd803d')

eye_style = GROUP(classification='eye')
eye_style.fill('white')

mouth_style = GROUP(classification='mouth')
mouth_style.fill('none')
mouth_style.perimeter('white', '2px')

limb_style = GROUP(classification='limb')
limb_style.perimeter('#cd803d', '35px')
limb_style.roundify()

button_style = GROUP(classification='button')
button_style.fill('white')

# Add the CSS styles to the SVG
svg.add_style(gingerbread_style)
svg.add_style(head_style)
svg.add_style(eye_style)
svg.add_style(mouth_style)
svg.add_style(limb_style)
svg.add_style(button_style)

# Add the head
head = CIRCLE(x=0, y=50, r=30).classify('head')
svg += head

# Add the eyes
left_eye = CIRCLE(x=-12, y=55, r=3).classify('eye')
right_eye = CIRCLE(x=12, y=55, r=3).classify('eye')
svg += left_eye
svg += right_eye

# Add the mouth
mouth = RECTANGLE(x=-10, y=40, width=20, height=5, rx=2).classify('mouth')
svg += mouth

# Add the limbs
left_arm = LINE(origin=POINT(-40, 10), end=POINT(40, 10)).classify('limb')
left_leg = LINE(origin=POINT(-25, -50), end=POINT(0, 15)).classify('limb')
right_leg = LINE(origin=POINT(25, -50), end=POINT(0, 15)).classify('limb')
svg += left_arm
svg += left_leg
svg += right_leg

# Add the buttons
button1 = CIRCLE(x=0, y=10, r=5).classify('button')
button2 = CIRCLE(x=0, y=-10, r=5).classify('button')
svg += button1
svg += button2

# Draw the SVG
svg.draw('gingerbread_man.svg')

print("Gingerbread man SVG created.")
