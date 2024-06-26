'''
VectorGraph
SVG Library for mathematical graphs

'''



class SHAPE:
	def cartesian(shape,svg):
		shape.y = svg.view_origin.y + ( svg.view_end.y - shape.y)
		return shape

	def set_color(shape, color='', perimeter_color=''):
		if color:
			shape.color = color
		if perimeter_color:
			shape.stroke = perimeter_color
		return shape

	def colorize(shape, color='', perimeter_color=''):
		shape.set_color(color=color, perimeter_color=perimeter_color)
		return shape

	def transparent(shape, perimeter_color=''):
		shape.set_color(color='none', perimeter_color=perimeter_color)
		return shape

	def set_perimeter(shape, color='', size=3):
		if color:
			shape.stroke = color
		if size > 0:
			shape.stroke_width = size
		return shape

	def no_perimeter(shape):
		shape.set_perimeter('',0)
		return shape

	def classify(shape, classification):
		shape.classification = classification
		return shape

	def group_to(shape, classification):
		classify(shape, classification)
		return shape


class GROUP:
	counter = 1

	def __init__(group, classification=None, properties=''):
		if classification is None:
			classification = f'group{GROUP.counter}'
			GROUP.counter += 1
		group.classification = classification
		group.properties = properties + '\n'

	def add(group, shape):
		shape.classification = group.classification

	def fill(group,color):
		if color:
			group.properties += f"\t fill: {color} ;\n"

	def perimeter(group,color,width):
		if color:
			group.properties += f"\t stroke: {color} ;\n"
		if width:
			group.properties += f"\t stroke-width: {width} ;\n"

	def roundify(group):
		group.properties += f"\t stroke-linecap: round ;\n"

	def string(group):
		string = f"\n .{group.classification}  "
		string += '{'
		if group.properties.strip:
			string += f"{group.properties}"
		string += '\t}\n'
		return string

	def cartesian(a,b):
		pass



class POINT(SHAPE):
	def __init__(point,x=0,y=0, r = 3, color = 'red', stroke = 'black', stroke_width = '1px', classification = ''):
		point.x = x
		point.y = y
		point.r = r
		point.color = color
		point.stroke = stroke
		point.stroke_width = stroke_width
		point.classification = classification

	def string(point):
		string = f"<circle "
		string += f"cx = '{point.x}' cy = '{point.y}' r = '{point.r}' "
		if point.classification: string += f"class = '{point.classification}' "
		if point.color: string += f"fill = '{point.color}' "
		if point.stroke: string += f"stroke = '{point.stroke}' "
		if point.stroke_width: string += f"stroke-width = '{point.stroke_width}' "
		string += " />"
		return string



class LINE(SHAPE):
	def __init__(line, origin = POINT(0,0), end = POINT(1,1), color = 'black', stroke_width=1, classification = ''):
		line.origin = origin
		line.end = end
		line.color = color
		line.stroke_width = stroke_width
		line.classification = classification

	def string(line):
		string = f"<line "
		if line.classification: string += f"class = '{line.classification}' "
		string += f"x1 = '{line.origin.x}' y1 = '{line.origin.y}' "
		string += f"x2 = '{line.end.x}' y2 = '{line.end.y}' "
		string += f"stroke = '{line.color}' "
		string += f"stroke-width = '{line.stroke_width}' "
		string += " />"
		return string

	def cartesian(line,svg):
		line.origin.cartesian(svg)
		line.end.cartesian(svg)

class POLYLINE(SHAPE):
	def __init__(line, points = None, color = 'black', width=3, classification = ''):
		if points is None:
			points = [POINT(0,0), POINT(1,1), POINT(0,1)] # default shape
		line.points = points
		line.color = color
		line.stroke_width = width
		line.classification = classification

	def string(line):
		points_str = " ".join(f"{point.x},{point.y}" for point in line.points)
		string = f"<polyline "
		if line.classification: string += f"class = '{line.classification}' "
		string += f"points = '{points_str}' "
		string += f"stroke ='{line.color}' stroke-width='{line.stroke_width}' "
		string += f"fill='none' "
		string += " />"
		return string

	def cartesian(line,svg):
		for point in line.points:
			point.cartesian(svg)


class RECTANGLE(SHAPE):
	def __init__(rectangle,x=0,y=0, height = 10, width = 10, color = 'white', stroke = 'black', stroke_width = 3, rx = 0, ry = 0,  classification = '' ):
		rectangle.x = x
		rectangle.y = y
		rectangle.height = height
		rectangle.width = width
		rectangle.color = color
		rectangle.stroke = stroke
		rectangle.stroke_width = stroke_width
		rectangle.classification = classification
		rectangle.rx = rx
		rectangle.ry = ry


	def string(rectangle):
		string = f"<rect "
		if rectangle.classification:
			string += f"class = '{rectangle.classification}'"
		string += f"x = '{rectangle.x}' y = '{rectangle.y}' "
		string += f"height = '{rectangle.height}' width = '{rectangle.width}' "
		if rectangle.color:
			string += f"fill = '{rectangle.color}' "
		if rectangle.stroke:
			string += f"stroke = '{rectangle.stroke}' "
		if rectangle.stroke_width:
			string += f"stroke-width = '{rectangle.stroke_width}' "
		if rectangle.rx:
			string += f"rx = '{rectangle.rx}' "
		if rectangle.ry:
			string += f"ry = '{rectangle.ry}' "
		string += " />"
		return string

class SQUARE(RECTANGLE):
	def __init__(square,x=0,y=0, length = 10, color = 'white', stroke = 'black', stroke_width = 3, classification = '' ):
		super().__init__(x, y, length, length, color, stroke, stroke_width, classification)


class ELLIPSE(SHAPE):
	def __init__(ellipse,x=0,y=0, rx= 10, ry= 5, color = 'white', stroke = 'black', stroke_width = 3, classification = '' ):
		ellipse.x = x
		ellipse.y = y
		ellipse.rx = rx
		ellipse.ry = ry
		ellipse.color = color
		ellipse.stroke = stroke
		ellipse.stroke_width = stroke_width
		ellipse.classification = classification

	def string(ellipse):
		string = f"<ellipse "
		if ellipse.classification:
			string += f"class = '{ellipse.classification}' "
		string += f"cx = '{ellipse.x}' cy = '{ellipse.y}' rx = '{ellipse.rx}' ry = '{ellipse.ry}' "
		if ellipse.color:
			string += f"fill = '{ellipse.color}' "
		if ellipse.stroke:
			string += f"stroke = '{ellipse.stroke}' "
		if ellipse.stroke_width:
			string += f"stroke-width = '{ellipse.stroke_width}' "
		string += " />"
		return string

class CIRCLE(SHAPE):
	def __init__(circle,x=0,y=0, r = 10, color = 'white', stroke = 'black', stroke_width = 3, classification = '' ):
		circle.x = x
		circle.y = y
		circle.r = r
		circle.color = color
		circle.stroke = stroke
		circle.stroke_width = stroke_width
		circle.classification = classification

	def string(circle):
		string = f"<circle "
		if circle.classification:
			string += f"class = '{circle.classification}' "
		string += f"cx = '{circle.x}' cy = '{circle.y}' r = '{circle.r}' "
		if circle.color:
			string += f"fill = '{circle.color}' "
		if circle.stroke:
			string += f"stroke = '{circle.stroke}' "
		if circle.stroke_width:
			string += f"stroke-width = '{circle.stroke_width}' "
		string += " />"
		return string

class POLYGON(SHAPE):
	def __init__(polygon, points = [POINT(1,0), POINT(1,1), POINT(0,1), POINT(0,0)], color = 'white', stroke = 'black', stroke_width=3, classification = ''):
		polygon.points = points
		polygon.color = color
		polygon.stroke = stroke
		polygon.stroke_width = stroke_width
		polygon.classification = classification

	def string(polygon):
		string = f"<polygon "
		if polygon.classification: string += f"class = '{polygon.classification}' "
		points_str = " ".join(f"{point.x},{point.y}" for point in polygon.points)
		string += f"points = '{points_str}' "
		if polygon.color:
			string += f"fill = '{polygon.color}' "
		if polygon.stroke:
			string += f"stroke = '{polygon.stroke}' "
		if polygon.stroke_width:
			string += f"stroke-width = '{polygon.stroke_width}' "

		string += " />"
		return string

	def cartesian(polygon,svg):
		for point in polygon.points:
			point.cartesian(svg)

class TRIANGLE(POLYGON):
	def __init__(triangle, p1 = POINT(0,0), p2 = POINT(0,4), p3 = POINT(3,0), color = 'black', stroke_width=3, classification = ''):
		super().__init__( [p1,p2,p3], color, stroke, stroke_width, classification)


class EDGE(POINT):
	def __init__(point,x=0,y=0, mode = 'l', color = 'red', stroke = 'black', stroke_width = 1):
		point.x = x
		point.y = y
		point.mode = mode
		point.color = color
		point.stroke = stroke
		point.stroke_width = stroke_width


class PATH(SHAPE):
	def __init__(path, edges = [], color = 'black', stroke_width=3, close=True, classification = ''):
		path.edges = edges
		path.color = color
		path.stroke_width = stroke_width
		path.close = True
		path.classification = classification

	def string(path):
		string = f"<path "
		if path.classification: string += f"class = '{path.classification}' "
		if path.close: z = f"Z "
		edges_str = " ".join(f"\n\t\t\t{edge.mode} {edge.x},{edge.y}" for edge in path.edges)
		string += f"d = '{edges_str} {z}' "
		string += " />"
		return string

	def cartesian(path,svg):
		new_edges = []
		for edge in path.edges:
			edge.cartesian(svg)
			new_edges.append(edge)
		path.points = new_edges
		return path

class SVG:
	def __init__(svg, width=100, height=100, view_origin = POINT(0,0), view_end = POINT(100,100), classification = ''):
		svg.width = width
		svg.height = height
		svg.view_origin = view_origin
		svg.view_end = view_end
		svg.classification = classification

		svg.elements = []
		svg.styles = []

	def add_element(svg,element):
		if element:
			# Invert the y-coordinate relative to view_origin and view_end
			element.cartesian(svg)
			svg.elements.append(element.string())

	def __iadd__(svg, element):
		valid = isinstance(element,SHAPE)
		if valid:
			svg.add_element(element)
		return svg

	def __add__(svg, element):
		valid = isinstance(element,SHAPE)
		if valid:
			new_svg = SVG(svg.width, svg.height, svg.view_origin, svg.view_end)
			new_svg.add_element(element)
			return new_svg
		return svg

	def add_style(svg, group):
		if isinstance(group, GROUP):
			style_string = group.string()
			if style_string:
				svg.styles.append(style_string)

	def add_group(svg, group):
		svg.add_style(group)

	def stylize(svg, group):
		svg.add_style(group)

	def string(svg):
		string = "<svg "

		elements_str = "\n\t".join(svg.elements)
		styles_str = "\n".join(style for style in svg.styles if style is not None)

		if svg.classification: string  += f"class = '{svg.classification}'  "


		string  += f"width = '{svg.width}' "
		string += f"height = '{svg.height}' "

		vb_x = svg.view_origin.x
		vb_y = svg.view_origin.y
		vb_width  = svg.view_end.x  - svg.view_origin.x
		vb_height = svg.view_end.y - svg.view_origin.y

		string += f"viewBox = '{vb_x} {vb_y} {vb_width} {vb_height}'"
		string += f' xmlns="http://www.w3.org/2000/svg"'


		string  += f" > \n"

			# Interpreter
		string += "\n\t"

		string += f"{elements_str}"
		string += f"\n<style> {styles_str} </style>\n\t"


		string += "\n</svg>"

		return string

	def draw(svg, FileName="Graph.svg"):
		content = '\n' + svg.string()
		with open(FileName, 'w') as file:
			file.write(content)
		print(f"File {FileName} Created")




class PLANE:
	def __init__(plane, x_from = 0, x_to = 100, y_from = 0, y_to = 100):
		plane.x_from= x_from
		plane.x_to = x_to
		plane.y_from = y_from
		plane.y_to = y_to
