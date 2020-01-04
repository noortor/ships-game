from ships import *
import pygame
import math

WIDTH = 300
HEIGHT = 300
DELAY = 50

def x_comp(vector_len, angle):
	return math.cos(angle) * vector_len

def y_comp(vector_len, angle):
	return math.sin(angle) * vector_len