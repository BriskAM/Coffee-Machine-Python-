class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def remaining_resources(self):
        print(f'''The coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.coffee_beans} g of coffee beans
        {self.disposable_cups} disposable cups
        ${self.money} of money
        ''')

    def buy_coffee(self, coffee):
        if coffee == 'back':
            return
        elif int(coffee) == 1:
            espresso = {"water": 250, "coffee_beans": 16, "cost": 4}
            if (self.water >= espresso["water"] and self.coffee_beans >= espresso["coffee_beans"]
                    and self.disposable_cups >= 1):
                print('I have enough resources, making you a coffee!')
                self.water -= espresso["water"]
                self.coffee_beans -= espresso["coffee_beans"]
                self.disposable_cups -= 1
                self.money += espresso["cost"]
            else:
                print(f"Sorry, not enough {'water' if self.water < espresso["water"] else
                'coffee beans' if self.coffee_beans < espresso["coffee_beans"] else 'cups'}!")
        elif int(coffee) == 2:
            latte = {"water": 350, "milk": 75, "coffee_beans": 20, "cost": 7}
            if (self.water >= latte["water"] and self.coffee_beans >= latte["coffee_beans"]
                    and self.milk >= latte["milk"] and self.disposable_cups >= 1):
                print('I have enough resources, making you a coffee!')
                self.water -= latte["water"]
                self.coffee_beans -= latte["coffee_beans"]
                self.milk -= latte["milk"]
                self.disposable_cups -= 1
                self.money += latte["cost"]
            else:
                print(f"Sorry, not enough {'water' if self.water < latte["water"] else
                'coffee beans' if self.coffee_beans < latte["coffee_beans"] else 'cups'
                if self.disposable_cups < 1 else 'milk'}!")
        elif int(coffee) == 3:
            cappuccino = {"water": 200, "milk": 100, "coffee_beans": 12, "cost": 6}
            if (self.water >= cappuccino["water"] and self.coffee_beans >= cappuccino["coffee_beans"]
                    and self.milk >= cappuccino["milk"] and self.disposable_cups >= 1):
                print('I have enough resources, making you a coffee!')
                self.water -= cappuccino["water"]
                self.coffee_beans -= cappuccino["coffee_beans"]
                self.milk -= cappuccino["milk"]
                self.disposable_cups -= 1
                self.money += cappuccino["cost"]
            else:
                print(f"Sorry, not enough {'water' if self.water < cappuccino["water"] else
                'coffee beans' if self.coffee_beans < cappuccino["coffee_beans"] else 'cups'
                if self.disposable_cups < 1 else 'milk'}!")

    def fill_resources(self):
        self.water += int(input("Write how many ml of water you want to add:"))
        self.milk += int(input("Write how many ml of milk you want to add:"))
        self.coffee_beans += int(input("Write how many grams of coffee beans you want to add:"))
        self.disposable_cups += int(input("Write how many disposable cups you want to add:"))

    def take_money(self):
        print(f"I gave you ${self.money}")
        self.money = 0


def main():
    coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
    while True:
        action = input("Write action (buy, fill, take, remaining, exit):")
        if action == 'buy':
            coffee_machine.buy_coffee(
                input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
        elif action == 'fill':
            coffee_machine.fill_resources()
        elif action == 'take':
            coffee_machine.take_money()
        elif action == 'remaining':
            coffee_machine.remaining_resources()
        elif action == 'exit':
            break
    return


if __name__ == "__main__":
    main()
