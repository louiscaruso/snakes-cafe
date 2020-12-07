import sys
#code from class demo
def snakes():
    orders = {
    'wings':0,
    }

    print(orders)

    print('Welcome to Snakes Cafe')
    print('Please see our menu below.')
    print(menu)

    
    print("If you wanna quit input 'QUIT' at anytime.")

# if userInput == "QUIT":
        
    user_input = input('What would you like to order?:  ')

    while (user_input != 'QUIT'):
        user_input = input('What would you like to order??: ')

    if user_input.upper() == 'QUIT':
        print('Goodbye')    
        sys.exit()
        

    print(user_input)

    print(orders['wings'])

    orders['wings'] += 1
    
    print(orders)


menu = """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""

if __name__ == "__main__":
    snakes()

