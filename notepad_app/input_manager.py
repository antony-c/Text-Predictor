import pygame


class Input_Manager:

    def __init__(self):
        self.mouse_pressed = False  # Is the mouse currently held down
        self.previous = False  # Was the mouse held down the previous frame
        self.mouse_clicked = False  # Should the mouse be clicked this frame
        self.string = ""

    def key_update(self, text):  # Recieve user keyboard input
        if text.key == pygame.K_BACKSPACE:
            self.string = self.string[0:-1]
        elif text.key == pygame.K_RETURN:
            self.string += "\n"
        else:
            self.string += text.unicode

    # When the mouse is clicked only have it clicked for 1 frame
    def mouse_update(self):
        self.mouse_pressed = pygame.mouse.get_pressed()[0]
        if self.mouse_pressed:  # Is the mouse button held down
            self.mouse_clicked = not self.previous
            self.previous = True
        else:  # The mouse button isnt held down
            self.mouse_clicked = False
            self.previous = False
