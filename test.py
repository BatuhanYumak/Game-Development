import unittest
from unittest.mock import patch, MagicMock
import pygame
from win import show_win_screen


class TestWinFunction(unittest.TestCase):
    @patch("show_win_screen.pygame.display.update")
    @patch("show_win_screen.pygame.event.get")
    @patch("show_win_screen.pygame.quit")
    @patch("show_win_screen.exit")
    def test_show_win_screen(
        self, mock_exit, mock_quit, mock_event_get, mock_display_update
    ):
        # Mock the Pygame window and image
        window = MagicMock()
        win_image = MagicMock()
        win_width = 551
        win_height = 720

        # Simulate the event loop to quit the game
        mock_event_get.side_effect = [[pygame.event.Event(pygame.QUIT)], []]

        # Call the show_win_screen function
        show_win_screen(window, win_image, win_width, win_height)

        # Assert that the window fill and blit methods were called
        window.fill.assert_called_once_with((0, 0, 0))
        window.blit.assert_called_once_with(
            win_image,
            (
                win_width // 2 - win_image.get_width() // 2,
                win_height // 2 - win_image.get_height() // 2,
            ),
        )

        # Assert that the Pygame display was updated
        mock_display_update.assert_called()

        # Assert that Pygame quit and exit were called
        mock_quit.assert_called()
        mock_exit.assert_called()


if __name__ == "__main__":
    unittest.main()
