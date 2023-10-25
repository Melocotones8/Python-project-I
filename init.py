from menus_input import main_menu, user_action
from game import main_descopt

main_menu()
user_choice = user_action()

main_descopt(user_choice)

print('-' * 30)
print("THANK YOU AND SEE YOU NEXT TIME")
print('*' * 30)
