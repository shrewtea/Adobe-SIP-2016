"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]
building_list=[]
def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point=x_point
        self.y_point=y_point
        self.width=width
        self.height=height
        self.color=color
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def draw(self): 
        pygame.draw.rect(screen, BLUE, (self.x_point,self.y_point,self.height,self.width))
    def move(self,speed):
        self.x_point += speed



class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width=width
        self.height=height
        self.base=base
        self.color=color
        self.speed=speed
        self.build_list=[]
        self.combined_width=0
        #building_list=[]

    def add_building(self, x_location):
        width=30
        height=600
        self.combined_width += width
        building1=Building(x_location,random.randint(0,600), height, width, BLUE)
        #building_list.append(Building(x_location,100,60,-80,BLUE))
        self.build_list.append(building1)
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """

    def add_buildings(self):
        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """
        while self.combined_width<self.width:
            self.add_building(self.combined_width)


        # for i in range (10):
        #     counter=0
        #     self.add_building(counter)
        #     counter+=1
        #     #counter+=1 

    def draw_buildings(self):
        for i in self.build_list:
            i.draw()

        """
        This calls the draw method on each building.
        """

    def move_buildings(self):
        for i in self.build_list:
            i.move(1)
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """


FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = BLACK

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
building=Scroller(80,25,15,5,BLUE)
# -------- Main Program Loop -----------
#building1 = Building(100, 100, 60, -80, BLUE)

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
   #building1 = Building(20, 20, 50, 100, BLUE)
    #building1.draw()

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here
    
   
    #building1.draw()
    #building1.move(5)
     # building_var=Scroller(0,0,0,BLUE,0)
     # building_var.add_buildings()
# varBuilding=Scroller(200,20,40,100,BLUE)
# varBuilding.add_building(10)
# varBuilding.add_buildings()
# varBuilding.draw_buildings()
# varBuilding.move_buildings()
    back_scroller.add_building(0)
    back_scroller.add_buildings()

    middle_scroller.add_building(0)
    middle_scroller.add_buildings()

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()

# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
