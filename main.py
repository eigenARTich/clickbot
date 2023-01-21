from pyautogui import click, position


# pip install PyAutoGUI

def print_position():
    while True:
        print(position())

# print_position() # searching for coordinates of the button

x = 961
y = 533


def click_button(x, y):
    for i in range(100):
        click(x, y)
        print('click: ', i)

click_button(x, y)
