from ships import *
from utils import *
from obstacle import *
from laser import *
import math
import collision as coll


def main():
	player = Player_Ship(3, [FIELD_WIDTH-50, FIELD_HEIGHT/2], math.pi/2)
	enemy = Enemy_Ship(3, [100, 100], math.pi/2)
	field_display = pygame.display.set_mode((FIELD_WIDTH, FIELD_HEIGHT))
	response = coll.Response()

	def laser_obstacle_collision(): #TODO: move?
		"""removes lasers that collide with obstacles"""

		for laser in Laser_Manager.laser_list:
			for obstacle in Obstacle_Manager.obstacle_list:
				if coll.collide(laser.coll_laser, obstacle.coll_obstacle):
					Laser_Manager.laser_list.remove(laser)
					break

	def corner_collision_pushback(ship, corner):
		"""pushes back a given ship from a corner"""

		overlap = Ship.h_box_radius - dist(ship.pos, corner)
		push_dir = math.atan2(ship.pos[1] - corner[1], ship.pos[0] - corner[0])
		ship.update_pos(x_comp(overlap, push_dir), y_comp(overlap, push_dir))

	def player_obstacle_collision():
		"""detects collision between a ship and obstacles and moves the ship accordingly"""

		for obstacle in Obstacle_Manager.obstacle_list:
			if coll.collide(player.coll_ship, obstacle.coll_obstacle, response):
				#left side collision
				if response.overlap_n.x == 1:
					player.update_pos((obstacle.pos[0] - obstacle.width/2) - (player.pos[0] + Ship.h_box_radius), 0)
				#right side collision
				elif response.overlap_n.x == -1:
					player.update_pos((obstacle.pos[0] + obstacle.width/2) - (player.pos[0] - Ship.h_box_radius), 0)
				#top collision
				elif response.overlap_n.y == 1:
					player.update_pos(0, (obstacle.pos[1] - obstacle.height/2) - (player.pos[1] + Ship.h_box_radius))
				#bottom collision
				elif response.overlap_n.y == -1:
					player.update_pos(0, (obstacle.pos[1] + obstacle.height/2) - (player.pos[1] - Ship.h_box_radius))
				#corner collision
				else:
					#top
					if response.overlap_n.y > 0:
						#left
						if response.overlap_n.x > 0:
							corner_collision_pushback(player, obstacle.verts["t_left"])
						#right
						else:
							corner_collision_pushback(player, obstacle.verts["t_right"])

					#bottom
					else:
						#left
						if response.overlap_n.x > 0:
							corner_collision_pushback(player, obstacle.verts["b_left"])
						#right
						else:
							corner_collision_pushback(player, obstacle.verts["b_right"])

				response.reset()

	def run_game():
			"""contains actions of each frame"""
			run = True
			Obstacle_Manager.init_obstacles()
			while run: 
				pygame.time.delay(DELAY)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
				player.update_all()
				Laser_Manager.update_lasers()
				Obstacle_Manager.update_obstacles()
				laser_obstacle_collision()
				player_obstacle_collision()

				Laser_Manager.draw_all_lasers(field_display)
				Obstacle_Manager.draw_all_obstacles(field_display)
				player.draw(field_display)
				pygame.display.update()
				field_display.fill((20,20,20))

			pygame.quit()	

	run_game()
 
main()

#.       python3 main.py

