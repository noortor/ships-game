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

	def player_obstacle_collision():
		"""changes the horizonal or vertical velocity of the ship to 0 """
		#print("hi")
		for obstacle in Obstacle_Manager.obstacle_list:
			if coll.collide(player.coll_ship, obstacle.coll_obstacle, response):
				if abs(response.overlap_n.x) == 1:
					player.update_pos(- player.vel[0], 0)
				elif abs(response.overlap_n.y) == 1:
					player.update_pos(0, - player.vel[1])
				else:
					"""#top
					if response.overlap_n.y > 0:
						#left
						if response.overlap_n.x > 0:
							pass
						#right
						else:
							pass"""

						if player.vel[0] > 0:
							player.update_pos(player.vel[1], - player.vel[0])
						else:
							player.update_pos(- player.vel[1], player.vel[0])
					#bottom
					else:
						"""#left
						if response.overlap_n.x > 0:
							pass
						#right
						else:
							if player.dir <= math.pi/4 or player.dir >= math.pi * 3/2:
								player.update_pos(player.vel[1], - player.vel[0])
							elif player.dir > math.pi/4 and player.dir < math.pi:
								player.update_pos(- player.vel[1], player.vel[0])
							"""

						if player.vel[0] > 0:
							player.update_pos(- player.vel[1], player.vel[0])
						else:
							player.update_pos(player.vel[1], - player.vel[0])
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

