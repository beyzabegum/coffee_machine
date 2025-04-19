"""
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""

import pdb
resources={
   "water": 400,
   "milk": 300,
   "coffee": 200,
   "money": 0.0 
}

coffee_requirements = {
   "espresso": {"water": 50, "coffee": 18, "price":2.5},
   "latte": {"water": 100, "milk": 150, "coffee": 21, "price":3.0},
   "cappuccino": {"water":150, "milk":100, "coffee": 25, "price":3.5}
}

def process_coins():
   print("Please insert coins.")
   quarters = float(input("How many quarters? (0.25 each) "))
   dimes = float(input("How many dimes? (0.10 each) "))
   nickels = float(input("How many nickels? (0.05 each)"))
   pennies = float(input("How many pennies? (0.01 each)"))

   monetary_value = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
   print(f"Total money inserted: ${monetary_value: }")
   return monetary_value



def coffee_machine():
    while True:
     coffee_choice = input("What would you like? (espresso/latte/cappuccino) ")

     if coffee_choice == "report":
        print("Resource report:")
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Money: ${resources['money']}")

     elif coffee_choice in coffee_requirements:
        enough_resources = True
        items = list(coffee_requirements[coffee_choice].items())
        for ingredient, amount in items[:-1]:
           #pdb.set_trace()
           if resources[ingredient] < amount:
              print(f"Sorry, there is not enough {ingredient}.")
              enough_resources =  False
              break
        if enough_resources:
          monetary_value = process_coins()   # money that person gave 
          required_value = coffee_requirements[coffee_choice]["price"]   # money that we need for that coffee

          if required_value > monetary_value:
             print("Sorry that's not enough money. Money refunded.")
             break
          if required_value < monetary_value:
             change = monetary_value - required_value
             print(f"Here is ${change} dollars in change.")

          resources["money"] = required_value + resources["money"]
             

          print(f"Preparing your {coffee_choice}...")
          items = list(coffee_requirements[coffee_choice].items())
          for ingredient, amount in items[:-1]:
               resources[ingredient] -= amount
          print(f"Your {coffee_choice} is ready. Enjoy!")

     elif coffee_choice == "exit":
        print("Thank you for your coming. Goodbye!")
        break
    
     elif coffee_choice == "off":
        print("Turning off the coffee machine.")
        break
    
     else:
        print("Invalid choice. Please select espresso,latte,cappuccino or type exit to quit. ")
 
coffee_machine()