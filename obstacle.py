import pygame
from utils import *
import random as rnd
import collision as coll

class Obstacle():

	def __init__(self, height, width, position):
		self.height = height
		self.width = width
		self.pos = position
		self.color = (255,255,255)
		self.verts = {}
		self.verts["b_left"] = [self.pos[0] - self.width/2, self.pos[1] + self.height/2]
		self.verts["b_right"] = [self.pos[0] + self.width/2, self.pos[1] + self.height/2]
		self.verts["t_left"] = [self.pos[0] - self.width/2, self.pos[1] - self.height/2]
		self.verts["t_right"] = [self.pos[0] + self.width/2, self.pos[1] - self.height/2]
		self.coll_obstacle = coll.Poly.from_box(coll.Vector(position[0], position[1]), width, height)

	def draw(self, surface):
		pygame.draw.polygon(surface, self.color, (self.verts["b_left"], self.verts["b_right"], self.verts["t_right"], self.verts["t_left"]))

class Obstacle_Manager():

	obstacle_list = []

	def init_obstacles():
		"""instantiates all obstacles at the beginning of the game"""

		Obstacle_Manager.init_constant_obstacles()
		for x_region in range(200, FIELD_WIDTH - 100, 100):
			for y_region in range(50, FIELD_HEIGHT, 100):
				x_pos = rnd.randint(x_region - 50, x_region + 50)
				y_pos = rnd.randint(y_region - 50, y_region + 50)
				width = rnd.randint(10, 50)
				height = rnd.randint(10, 50)
				obst = Obstacle(height, width,(x_pos,y_pos))
				Obstacle_Manager.obstacle_list.append(obst)

	def init_constant_obstacles():
		"""instantiates contant obstacles on each side of the field"""

		for x_pos in [100, FIELD_WIDTH - 100]:
			for y_pos in [50, FIELD_HEIGHT - 50]:
				obst = Obstacle(250, 25,(x_pos,y_pos))
				Obstacle_Manager.obstacle_list.append(obst)

	def update_obstacles():
		"""updates all obstacles in the field"""
		pass
		
	def draw_all_obstacles(surface):
		"""draws all obstacles in the field"""

		for obstacle in Obstacle_Manager.obstacle_list:
			obstacle.draw(surface)

