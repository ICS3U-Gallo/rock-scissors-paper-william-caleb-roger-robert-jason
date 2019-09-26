







"""
Name: William
Game: Rocker Paper Scissor

"""
import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "William's Paper Rock Scissor Game"

player_score = 0
computer_score = 0

player_move = ""
computer_move = ""

result = ""


def computer_decision():
   global computer_move
   number = random.randint(1, 3)

   # Assign computer's choice based on the randomized number.
   if number == 1:
       computer_move = "Rock"
   elif number == 2:
       computer_move = "Paper"
   elif number == 3:
       computer_move = "Scissor"


def compare_move():

   global player_move, computer_move, player_score, computer_score, result

   if player_move == "Rock":
       if computer_move == "Paper":
           computer_score = computer_score + 1
           result = "Computer wins!"
       elif computer_move == "Scissor":
           player_score = player_score + 1
           result = "You win!"
       else:
           result = "It is a tie!"
   elif player_move == "Paper":
       if computer_move == "Rock":
           player_score = player_score + 1
           result = "You win!"
       elif computer_move == "Scissor":
           computer_score = computer_score + 1
           result = "Computer wins!"
       else:
           result = "It is a tie!"
   elif player_move == "Scissor":
       if computer_move == "Rock":
           player_score = player_score + 1
           result = "You win!"
       elif computer_move == "Paper":
           computer_score = computer_score + 1
           result = "Computer wins!"
       else:
           result = "It is a tie!"


class TextButton:
   """ Text-based button """
   def __init__(self,
                center_x, center_y,
                width, height,
                text,
                font_size=18,
                font_face="Arial",
                face_color=arcade.color.LIGHT_GRAY,
                highlight_color=arcade.color.WHITE,
                shadow_color=arcade.color.GRAY,
                button_height=2):
       self.center_x = center_x
       self.center_y = center_y
       self.width = width
       self.height = height
       self.text = text
       self.font_size = font_size
       self.font_face = font_face
       self.pressed = False
       self.face_color = face_color
       self.highlight_color = highlight_color
       self.shadow_color = shadow_color
       self.button_height = button_height

   def draw(self):
       """ Draw the button """
       arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                    self.height, self.face_color)

       if not self.pressed:
           color = self.shadow_color
       else:
           color = self.highlight_color

       # Bottom horizontal
       arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                        self.center_x + self.width / 2, self.center_y - self.height / 2,
                        color, self.button_height)

       # Right vertical
       arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                        self.center_x + self.width / 2, self.center_y + self.height / 2,
                        color, self.button_height)

       if not self.pressed:
           color = self.highlight_color
       else:
           color = self.shadow_color

       # Top horizontal
       arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                        self.center_x + self.width / 2, self.center_y + self.height / 2,
                        color, self.button_height)

       # Left vertical
       arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                        self.center_x - self.width / 2, self.center_y + self.height / 2,
                        color, self.button_height)

       x = self.center_x
       y = self.center_y
       if not self.pressed:
           x -= self.button_height
           y += self.button_height

       arcade.draw_text(self.text, x, y,
                        arcade.color.BLACK, font_size=self.font_size,
                        width=self.width, align="center",
                        anchor_x="center", anchor_y="center")

   def on_press(self):
       self.pressed = True

   def on_release(self):
       self.pressed = False


def check_mouse_press_for_buttons(x, y, button_list):
   """ Given an x, y, see if we need to register any button clicks. """
   for button in button_list:
       if x > button.center_x + button.width / 2:
           continue
       if x < button.center_x - button.width / 2:
           continue
       if y > button.center_y + button.height / 2:
           continue
       if y < button.center_y - button.height / 2:
           continue
       button.on_press()


def check_mouse_release_for_buttons(x, y, button_list):
   """ If a mouse button has been released, see if we need to process
       any release events. """
   for button in button_list:
       if button.pressed:
           button.on_release()


class RockTextButton(TextButton):
   def __init__(self, center_x, center_y, action_function):
       super().__init__(center_x, center_y, 100, 40, "Rock", 18, "Arial")
       self.action_function = action_function

   def on_release(self):
       super().on_release()
       self.action_function()
       global player_move
       player_move = "Rock"
       computer_decision()
       compare_move()


class PaperTextButton(TextButton):
   def __init__(self, center_x, center_y, action_function):
       super().__init__(center_x, center_y, 100, 40, "Paper", 18, "Arial")
       self.action_function = action_function

   def on_release(self):
       super().on_release()
       self.action_function()
       global player_move
       player_move = "Paper"
       computer_decision()
       compare_move()


class ScissorTextButton(TextButton):
   def __init__(self, center_x, center_y, action_function):
       super().__init__(center_x, center_y, 100, 40, "Scissor", 18, "Arial")
       self.action_function = action_function

   def on_release(self):
       super().on_release()
       self.action_function()
       global player_move
       player_move = "Scissor"
       computer_decision()
       compare_move()


class MyGame(arcade.Window):
   """
   Main application class.

   NOTE: Go ahead and delete the methods you don't need.
   If you do need a method, delete the 'pass' and replace it
   with your own code. Don't leave 'pass' in this program.
   """

   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       # Set the working directory (where we expect to find files) to the same
       # directory this .py file is in. You can leave this out of your own
       # code, but it is needed to easily run the examples using "python -m"
       # as mentioned at the top of this program.
       file_path = os.path.dirname(os.path.abspath(__file__))
       os.chdir(file_path)

       arcade.set_background_color(arcade.color.LIGHT_BLUE)

       self.pause = False
       self.coin_list = None
       self.button_list = None

   def setup(self):
       # Create your sprites and sprite lists here
       self.coin_list = arcade.SpriteList()

       # Create our on-screen GUI buttons
       self.button_list = []

       rock_button = RockTextButton(160, 450, self.pause_program)
       paper_button = PaperTextButton(360, 450, self.pause_program)
       scissor_button = ScissorTextButton(560, 450, self.pause_program)

       self.button_list.append(rock_button)
       self.button_list.append(paper_button)
       self.button_list.append(scissor_button)

   def on_draw(self):
       """
       Render the screen.
       """

       arcade.start_render()

       # Draw the coins
       self.coin_list.draw()

       # Draw the buttons
       for button in self.button_list:
           button.draw()

       game_instruction = "Input R for Rock, P for Paper and S for Scissor. Input Q to quit the game."
       arcade.draw_text(game_instruction, 100, 520, arcade.color.BLACK, 16)
       arcade.draw_text("Your Move: " + player_move, 100, 340, arcade.color.PURPLE, 16)
       arcade.draw_text("Computer's Move: " + computer_move, 100, 300, arcade.color.PURPLE, 16)
       arcade.draw_text("Result: " + result, 100, 260, arcade.color.PURPLE, 16)
       arcade.draw_text("Your Score: " + str(player_score), 100, 140, arcade.color.DARK_GREEN, 16)
       arcade.draw_text("Computer Score: " + str(computer_score), 100, 100, arcade.color.DARK_GREEN, 16)

   def update(self, delta_time):
       """
       All the logic to move, and the game logic goes here.
       Normally, you'll call update() on the sprite lists that
       need it.
       """

       if self.pause:
           return

   def on_mouse_press(self, x, y, button, key_modifiers):
       """
       Called when the user presses a mouse button.
       """
       check_mouse_press_for_buttons(x, y, self.button_list)

   def on_mouse_release(self, x, y, button, key_modifiers):
       """
       Called when a user releases a mouse button.
       """
       check_mouse_release_for_buttons(x, y, self.button_list)

   def pause_program(self):
       self.pause = True

   def resume_program(self):
       self.pause = False


def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()


if __name__ == "__main__":
   main()


