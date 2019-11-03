from ui import *
from tests import *

"""
    TODO: Add the functions <add>, <list> and <filter>
    TODO: Add data validation
    TODO: Add <undo> function
"""

def run_tests():
    Tests.test_add_student_to_list()

def main():
    list_of_students = []
    menu_option = [UI.add, UI.list_students]
    UI.clear_screen()

    while True:
        UI.print_options()
        option = input("Enter an option: ")
        UI.clear_screen()

        try:
            option = int(option)

            if option < 0:
                print("You have entered a negative value!\n")
                continue

            if option == 0:
                return

            menu_option[option - 1](list_of_students)
        except (ValueError, IndexError):
            print("Enter an integer between 0 and 4!\n")
        except Exception as e:
            print(e)


run_tests()
main()
