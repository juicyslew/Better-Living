import pygame
import datetime as dt
from Constants import *

d = dt.datetime.today()


class Visualizer():
    def __init__(self):
        #Initialize Pygame and Display
        pygame.init()
        pygame.display.init()
        #Create Screen
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.running = True

        #Create Background
        self.screen.fill(LIGHT_BLUE)

        #Create Hour Line Surface
        self.hourlines = pygame.Surface((SCREEN_SIZE))
        self.hourlines.fill(CK)
        self.hourlines.set_colorkey(CK)

        #Get Font Ready For Calendar
        self.font = pygame.font.SysFont('Helvetica', 17)
        pygame.display.set_caption('Better Living')

        #Draw Hour Lines and Render Text
        yinterval = SCREEN_SIZE[1]/len(HOURS)
        line_y = 0 #iteratively changes this value to draw all lines
        for i in HOURS:
            #Render Text
            f = self.font.render(HOURSTEXT[i], False, BLUE)
            f.set_alpha(CAL_HOUR_FONT_ALPHA)
            #Text Is blitted to screen (Not Lines)
            self.screen.blit(f, (0 + CAL_HOUR_FONT_MARGIN_LEFT, line_y+CAL_HOUR_FONT_MARGIN_TOP))

            #Draw Line
            pygame.draw.line(self.hourlines, BLUE, (0,line_y), (SCREEN_SIZE[0], line_y), 2)
            #Increase Interval
            line_y += yinterval
        self.hourlines.set_alpha(CAL_HOUR_LINE_ALPHA)
        self.screen.blit(self.hourlines, (0,0))
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.flip()

v = Visualizer();
v.run()
