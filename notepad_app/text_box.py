import pygame, pygame.font, time


class Text_Box:

    def __init__(self, screen, text, rect):
        self.screen = screen
        self.text = text
        self.rect = rect

        self.font = pygame.font.Font("./resources/Roboto.ttf", 24)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))

    def draw(self):  # Draw text box
        def get_text_rect():  # Get rectangle values to dynamically center text

            text_width = self.text_surface.get_width()
            text_height = self.text_surface.get_height()
            rect_x = self.rect.left
            rect_y = self.rect.top
            rect_width = self.rect.right - rect_x
            rect_height = self.rect.bottom - rect_y

            x = rect_x + (rect_width // 2) - (text_width // 2)
            y = rect_y + (rect_height // 2) - (text_height // 2)

            return pygame.Rect(x, y, text_width, text_height)

        rect = get_text_rect()
        self.screen.blit(self.text_surface, rect)

    def update_text(self, text):  # Update text
        self.text = text
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))


class Input_Box:

    def __init__(self, screen, x, y, size):
        self.screen = screen
        self.x, self.y = x, y
        self.size = size
        self.font = pygame.font.Font("./resources/Roboto.ttf", 24)

    def draw(self, text):
        split_text = text.split('\n')

        cursor_height = 0
        line_width = 0

        for i, line in enumerate(split_text):
            line_surface = self.font.render(line, True, (0, 0, 0))
            line_height = line_surface.get_height()
            pos = (self.x, self.y + (i * line_height))

            rect = pygame.Rect(pos, self.size)
            self.screen.blit(line_surface, rect)

        # Settings for cursor
        cursor_height = line_height
        line_width = line_surface.get_width()

        # Make and draw the cursor
        cursor_y = cursor_height*(len(split_text)-1)
        cursor_rect = pygame.Rect(line_width, cursor_y, 3, cursor_height)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.screen, (0, 0, 0), cursor_rect)

    def update(self, input_string=str()):  # Update string
        self.draw(input_string)
