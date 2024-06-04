from pyautogui import press, hold, keyDown, keyUp
from time import sleep
from random import randint

def generate_character():
    char_list = ['w', 'a', 's', 'd', 'space']
    random_int = randint(0,4)
    random_char = char_list[random_int]
    return random_char

def press_button():
    while True:
        generated_character = generate_character()
        if generated_character == 'space':
            seep(10)
            keyDown(generated_character)
            sleep(0.1)
            keyUp(generated_character)
        else:
            sleep(10)
            keyDown(generated_character)
            sleep(2)
            keyUp(generated_character)

def main():
    print("Grodans Anti-AFK script")
    print("-----------------------")
    print("Main menu")
    print("---------")
    print("1: Start script")
    print("2: Exit")
    user_input = input("Enter value (1-2): ")
    while user_input != "1" and user_input != "2":
        user_input = input("Please enter a value between (1-2): ")
    else:
        if user_input == "2":
            print("Exiting script")
            exit()
        elif user_input == "1":
            press_button()


if __name__ == "__main__":
    main()


