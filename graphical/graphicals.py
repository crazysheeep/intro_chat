import pygame
import random
import math

background_colour = (65,188,156)
(width, height) = (400, 400)
drag = 0.999
elasticity =1
gravity = (math.pi, 0.1)

def addVectors((angle1, length1), (angle2, length2)):
    x  = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y  = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)

def findParticle(particles, x, y):
    for p in particles:
        if math.hypot(p.x-x, p.y-y) <= p.size:
            return p
    return None

class Particle():
    def __init__(self, (x, y), size, colour):
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.thickness = 0
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
            self.colour =  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity
	    self.colour =  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
            self.colour =  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity
            self.colour =  (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fun with pygame!")

def changeColour():
	number_of_particles = 3
	my_particles = []

	for n in range(number_of_particles):
	    size = random.randint(10, 20)
	    x = random.randint(size, width-size)
	    y = random.randint(size, height-size)

	    if n == 0:
		colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	    elif n == 1:
		colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	    elif n == 2:
		colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

	    particle = Particle((x, y), size, colour)
	    particle.speed = random.random()
	    particle.angle = random.uniform(0, math.pi*2)

	    my_particles.append(particle)


	selected_particle = None
	running = True
	while running:
	    for event in pygame.event.get():
		if event.type == pygame.QUIT:
		    running = False
		    pygame.quit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
		    (mouseX, mouseY) = pygame.mouse.get_pos()
		    selected_particle = findParticle(my_particles, mouseX, mouseY)
		elif event.type == pygame.MOUSEBUTTONUP:
		    selected_particle = None
		elif event.type == pygame.KEYDOWN:
		    if event.key == pygame.K_UP:
		        my_particles[0].angle, my_particles[0].speed = addVectors((my_particles[0].angle, my_particles[0].speed), (0, 2))
		    elif event.key == pygame.K_RIGHT:
		        my_particles[0].angle, my_particles[0].speed = addVectors((my_particles[0].angle, my_particles[0].speed), (math.pi/2, 2))
		    elif event.key == pygame.K_LEFT:
		        my_particles[0].angle, my_particles[0].speed = addVectors((my_particles[0].angle, my_particles[0].speed), (-math.pi/2, 2))
		        

	    if selected_particle:
		(mouseX, mouseY) = pygame.mouse.get_pos()
		dx = mouseX - selected_particle.x
		dy = mouseY - selected_particle.y
		selected_particle.angle = 0.5*math.pi + math.atan2(dy, dx)
		selected_particle.speed = math.hypot(dx, dy) * 0.1

	    screen.fill(background_colour)

	    for particle in my_particles:
		particle.move()
		particle.bounce()
		particle.display()

	    pygame.display.flip()
	    pygame.time.delay(10)
changeColour()
