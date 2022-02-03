import pygame
from text_box import Text_Box


class Button:

    def __init__(self, screen, rect, colour, action=None):
        self.screen = screen
        self.rect = rect
        self.colour = colour
        self.action = action

        # Text aspect of button
        self.text_box = Text_Box(screen, str(), rect)
        self.text = str()

    def draw(self):  # Draw button
        pygame.draw.rect(self.screen, self.colour, self.rect)
        self.text_box.draw()

    def __in_rect(self):  # Returns true if mouse hovering button, else false
        mousex = pygame.mouse.get_pos()[0]
        mousey = pygame.mouse.get_pos()[1]
        xcheck = mousex > self.rect.left and mousex < self.rect.right
        ycheck = mousey > self.rect.top and mousey < self.rect.bottom
        return xcheck and ycheck

    def __click(self):  # Run code if button pressed
        if self.action is not None:
            self.action.run(self)

    def update(self, mouse_down):  # Update button
        if self.__in_rect() and mouse_down:
            self.__click()
        self.draw()
