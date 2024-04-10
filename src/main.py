# imports
import pygame
import sys

import Util.colors as COLORS
import GUI.show_game as show_game
import GUI.show_menu as show_menu

def main():
    # Check command line arguments
    filename = check_args(sys.argv)
    # Initialize the game
    pygame.init()

    # Define constants

    # Screen size
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 640

    # Frames per second
    FPS = 60

    # Current state of the game
    current_state = "menu"

    # Initialize the game objects
    game = show_game.Game(SCREEN_WIDTH, SCREEN_HEIGHT, filename)
    menu = show_menu.Menu(SCREEN_WIDTH, SCREEN_HEIGHT)
    colors = COLORS.colors()

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Masyu")

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                # Cambiar entre menú y juego
                if current_state == "menu":
                    current_state = "game"
                elif current_state == "game":
                    current_state = "menu"

        screen.fill(colors.BLACK)

        # Draw the current state
        if current_state == "menu":
            menu.draw(screen, events, current_state)
            current_state = menu.current_state
        elif current_state == "game":
            game.draw(screen, events)

        # Update the screen
        pygame.display.flip()

        # Control the frame rate
        clock.tick(FPS)

    # Quit the game
    pygame.quit()
    sys.exit()

def check_args(args: str) -> str:
    """get the filename from the command line arguments

    Args:
        args (str): command line arguments

    Returns:
        str: filename
    """
    if len(args) != 2:
        print("Usage: python main.py <file_name>")
        exit(1)

    return args[1]

if __name__ == "__main__":
    main()