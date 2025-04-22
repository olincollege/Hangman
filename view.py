"""
View module for Hangman game using Pygame.
"""

import pygame

# --- Module-level constants ---
WIDTH = 800
HEIGHT = 600
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
MSG_COLOR = (200, 0, 0)
INPUT_COLOR_ACTIVE = pygame.Color("dodgerblue2")
INPUT_COLOR_INACTIVE = pygame.Color("lightskyblue3")
FONT_NAME = "Arial"
FONT_LARGE = 48
FONT_SMALL = 32
FPS = 30
HANGMAN_BASE_Y = 350
HANGMAN_LINE_W = 8


class View:
    """
    Manages all visual elements and user text input for the Hangman game using
    Pygame.
    """

    def __init__(self):
        """
        Initialize Pygame, create the main window, set up fonts, and start the
        clock.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hangman")
        self.font = pygame.font.SysFont(FONT_NAME, FONT_LARGE)
        self.small_font = pygame.font.SysFont(FONT_NAME, FONT_SMALL)
        self.clock = pygame.time.Clock()

    def display_game_state(self, game):
        """
        Render the current state of the game by drawing the gallows and body
        parts, showing the partially guessed word, and lists the letters already
        used. Then updates the display and maintain the frame rate.

        Args:
            game: An object with attributes:
                    mistakes_made (int): number of incorrect guesses.
                    known_word (List[str]): current revealed letters.
                    used_letters (List[str]): letters guessed so far.
        """
        self.screen.fill(BG_COLOR)
        self.draw_hangman(game.mistakes_made)
        word_surf = self.font.render(
            " ".join(game.known_word), True, LINE_COLOR
        )
        self.screen.blit(word_surf, (50, 420))

        guesses = ", ".join(game.used_letters)
        guess_surf = self.small_font.render(
            f"Guessed: {guesses}", True, LINE_COLOR
        )
        self.screen.blit(guess_surf, (50, 480))

        pygame.display.flip()
        self.clock.tick(FPS)

    def draw_hangman(self, mistakes):
        """
        Draw the gallows and hangman body parts corresponding to the number of
        mistakes.

        Args:
            mistakes (int): Number of incorrect guesses made by the player.
        """
        # Draw gallows
        pygame.draw.line(
            self.screen,
            LINE_COLOR,
            (50, HANGMAN_BASE_Y),
            (50, 50),
            HANGMAN_LINE_W,
        )
        pygame.draw.line(
            self.screen, LINE_COLOR, (50, 50), (150, 50), HANGMAN_LINE_W
        )
        pygame.draw.line(
            self.screen, LINE_COLOR, (150, 50), (150, 100), HANGMAN_LINE_W
        )

        # Draw body parts in order
        if mistakes > 0:  # head
            pygame.draw.circle(self.screen, LINE_COLOR, (150, 130), 30, 5)
        if mistakes > 1:  # torso
            pygame.draw.line(self.screen, LINE_COLOR, (150, 160), (150, 230), 5)
        if mistakes > 2:  # left arm
            pygame.draw.line(self.screen, LINE_COLOR, (150, 180), (100, 220), 5)
        if mistakes > 3:  # right arm
            pygame.draw.line(self.screen, LINE_COLOR, (150, 180), (200, 220), 5)
        if mistakes > 4:  # left leg
            pygame.draw.line(self.screen, LINE_COLOR, (150, 230), (125, 275), 5)
        if mistakes > 5:  # right leg
            pygame.draw.line(self.screen, LINE_COLOR, (150, 230), (175, 275), 5)

    def display_message(self, message, duration=2000):
        """
        Display a temporary message at the bottom of the screen.

        Args:
            message (str): Text to display.
            duration (int): Time in milliseconds to show the message.
        """
        msg_surf = self.small_font.render(message, True, MSG_COLOR)
        rect = msg_surf.get_rect(center=(WIDTH // 2, 520))
        self.screen.blit(msg_surf, rect)
        pygame.display.flip()
        pygame.time.delay(duration)

    def text_input_box(self, prompt="Enter a letter:"):
        """
        Show a text input box and return a single letter entered by the user
        or None if the window is closed.

        Presents a clickable input field. Only one alphabetical character
        is accepted, and pressing Enter returns that character. If the user
        closes the window, returns None.

        Args:
            prompt (str): Prompt text shown above the input box.

        Returns:
            str or None: Lowercase letter entered, or None on quit.
        """
        input_box = pygame.Rect(50, 550, 200, 36)
        color = INPUT_COLOR_INACTIVE
        active = False
        text = ""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    active = input_box.collidepoint(event.pos)
                    color = (
                        INPUT_COLOR_ACTIVE if active else INPUT_COLOR_INACTIVE
                    )
                elif event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        if len(text) == 1:
                            return text
                        else:
                            text = ""
                            self.display_message(
                                "Please enter ONE letter", 1000
                            )
                    elif event.key == pygame.K_BACKSPACE:
                        text = ""
                    else:
                        char = event.unicode.lower()
                        if char.isalpha() and len(text) == 0:
                            text = char

            self.screen.fill(BG_COLOR, input_box)
            prompt_surf = self.small_font.render(prompt, True, LINE_COLOR)
            self.screen.blit(prompt_surf, (50, 510))

            txt_surf = self.small_font.render(text, True, LINE_COLOR)
            self.screen.blit(txt_surf, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(self.screen, color, input_box, 2)

            pygame.display.flip()
            self.clock.tick(FPS)
