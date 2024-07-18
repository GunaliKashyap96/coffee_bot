"""
The coffee_bot function is the main entry point for the coffee ordering application. It guides the user through the process of selecting a coffee size, drink type, and milk type (for lattes), and then prints a summary of the order.

The get_size, get_drink_type, and order_latte functions are helper functions that handle the user input for each step of the ordering process. The print_message function is used to display an error message if the user enters an invalid selection.
"""

def coffee_bot():
    print('Welcome to the cafe!')
    size = get_size()
    drink_type = get_drink_type()

    if drink_type == 'latte':
        milk_type = order_latte()
        print(f'Alright, that\'s a {size} {drink_type} with {milk_type}!')
    else:
        print(f'Alright, that\'s a {size} {drink_type}!')

    name = input('Can I get your name please? \n ')
    print(f'Thanks, {name}! Your drink will be ready shortly!')

def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

def get_size():
    while True:
        res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n > ')
        if res == 'a':
            return 'small'
        elif res == 'b':
            return 'medium'
        elif res == 'c':
            return 'large'
        else:
            print_message()

def get_drink_type():
    while True:
        res = input('What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n > ')
        if res == 'a':
            return 'brewed coffee'
        elif res == 'b':
            return 'mocha'
        elif res == 'c':
            return 'latte'
        else:
            print_message()

def order_latte():
    while True:
        res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n > ')
        if res == 'a':
            return '2% milk'
        elif res == 'b':
            return 'non-fat milk'
        elif res == 'c':
            return 'soy milk'
        else:
            print_message()

coffee_bot()
