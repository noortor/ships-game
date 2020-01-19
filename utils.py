import math

FIELD_WIDTH = 800
FIELD_HEIGHT = 500
DELAY = 20

def x_comp(vector_len, angle):
	"""returns the x component of a vector given its magnitude and direction"""

	return math.cos(angle) * vector_len

def y_comp(vector_len, angle):
	"""returns the y component of a vector given its magnitude and direction"""

	return math.sin(angle) * vector_len

def rotate_point(center, point, angle):
	"""rotates a point around a center by a certain angle"""

	diff_x = point[0] - center[0]
	diff_y = point[1] - center[1]
	point[0] = center[0] + diff_x * math.cos(angle) - diff_y * math.sin(angle)
	point[1] = center[1] + diff_x * math.sin(angle) + diff_y * math.cos(angle)

def rotate_vertices(vertices, center, angle):
	"""rotates all vertices in a list of vertices"""

	for point in vertices:
		rotate_point(center, point, angle)

def dist(point1, point2):
	"""returns the distance between 2 points"""

	return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)