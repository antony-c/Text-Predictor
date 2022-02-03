import pygame, sys, util, json
from button import Button
from input_manager import Input_Manager
from text_box import Input_Box
from add_word import Add_Word


def main():
    def update_screen():
        # Find up to 3 predictions based on most recent word typed
        words = util.Word_Data.predict(current_word, json_data)

        # Update buttons
        for i, button in enumerate(buttons):
            button.update(input_manager.mouse_clicked)
            button.text_box.update_text(words[i])

        # Update input box
        input_box.update(input_manager.string)

    def generate_buttons():
        buttons = list()

        LIGHT = (160, 160, 160)
        DARK = (110, 110, 110)

        rect = pygame.Rect(0, HEIGHT-(HEIGHT/16), WIDTH/3, HEIGHT/16)
        buttons.append(Button(screen, rect, LIGHT, Add_Word(input_manager)))

        rect = pygame.Rect(WIDTH/3, HEIGHT-(HEIGHT/16), WIDTH/3, HEIGHT/16)
        buttons.append(Button(screen, rect, DARK, Add_Word(input_manager)))

        rect = pygame.Rect((WIDTH*2/3), HEIGHT-(HEIGHT/16), WIDTH/3, HEIGHT/16)
        buttons.append(Button(screen, rect, LIGHT, Add_Word(input_manager)))

        return buttons

    pygame.init()

    input_manager = Input_Manager()

    BG_COLOUR = (255, 255, 255)
    SIZE = (WIDTH, HEIGHT) = (900, 800)

    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Notepad--')

    input_box = Input_Box(screen, 0, 0, SIZE)
    current_word = str()

    # Make buttons
    buttons = generate_buttons()

    with open("data.json") as file:
        json_data = json.load(file)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                input_manager.key_update(event)
                text_split = input_manager.string.split()
                if len(text_split) > 1:
                    current_word = text_split[len(text_split) - 1].lower()

        # Update the input manager: check if mouse is pressed
        input_manager.mouse_update()

        screen.fill(BG_COLOUR)  # Draw background
        update_screen()  # Run all updating code
        pygame.display.flip()  # Push to screen


main()
