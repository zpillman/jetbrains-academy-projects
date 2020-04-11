# Write your code here


class CoffeeMachine:
    # CoffeeMachine class stores the amount of each item inside the machine
    def __init__(self, water, milk, bean, cup, money):
        self.water = water
        self.milk = milk
        self.bean = bean
        self.cup = cup
        self.money = money

    def __str__(self):
        return (
            "The coffee machine has:\n"
            "{} of water\n"
            "{} of milk\n"
            "{} of coffee beans\n"
            "{} of disposable cups\n"
            "{} of money"
        ).format(self.water, self.milk, self.bean, self.cup, self.money)

    def fill_machine(self):
        self.water += int(input("Write how many ml of water do you want to add:"))
        self.milk += int(input("Write how many ml of milk do you want to add:"))
        self.bean += int(input("Write how many grams of coffee beans do you want to add:"))
        self.cup += int(input("Write how many disposable cups do you want to add:"))

    def make_cup(self, drink):
        if self.has_enough_resources(drink):
            self.water -= drink.water
            self.milk -= drink.milk
            self.bean -= drink.bean
            self.cup -= 1
            self.money += drink.cost

    def take_money(self):
        print("I gave you " + str(self.money))
        self.money = 0

    def has_enough_resources(self, drink):
        if self.water < drink.water:
            print("Sorry, not enough water!")
            return False
        elif self.milk < drink.milk:
            print("Sorry, not enough milk!")
            return False
        elif self.bean < drink.bean:
            print("Sorry, not enough beans!")
            return False
        elif self.cup < 1:
            print("Sorry, not enough disposable cups!")
            return False
        else:
            print("I have enough resources, making you a coffee!")
            return True


class Drink:
    # drink class holds attributes of the related drink
    def __init__(self, water, milk, bean, cost):
        self.water = water
        self.milk = milk
        self.bean = bean
        self.cost = cost


# create our coffee machine with the values provided from the instructions
coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

# create our drinks
espresso = Drink(250, 0, 16, 4)
latte = Drink(350, 75, 20, 7)
cappuccino = Drink(200, 100, 12, 6)


def process_user_input():
    # get user action first
    usr_action = input("Write action (buy, fill, take, remaining, exit):")

    while usr_action != "exit":
        # process the action
        if usr_action == "buy":
            coffee_choice = input(
                "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            # process purchasing an espresso
            if coffee_choice == "back":
                print(coffee_machine)
                break
            elif int(coffee_choice) == 1:
                coffee_machine.make_cup(espresso)
            elif int(coffee_choice) == 2:
                coffee_machine.make_cup(latte)
            elif int(coffee_choice) == 3:
                coffee_machine.make_cup(cappuccino)
            else:
                print("Error, invalid coffee choice")

        elif usr_action == "fill":
            coffee_machine.fill_machine()
        elif usr_action == "take":
            coffee_machine.take_money()
        elif usr_action == "remaining":
            print(coffee_machine)
        else:
            print("Error, not a valid choice")

        usr_action = input("Write action (buy, fill, take, remaining, exit):")


process_user_input()
