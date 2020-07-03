class Coffee:
    def __init__(self, water, milk, beans, cost, name):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost
        self.name = name


espresso = Coffee(250, 0, 16, 4, 'espresso')
latte = Coffee(350, 75, 20, 7, 'latte')
cappuccino = Coffee(200, 100, 12, 6, 'cappuccino')


class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.coffee_types = {1: espresso, 2: latte, 3: cappuccino}

    def report_status(self):
        print('The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')

    def select_action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit)')
            action = input()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.report_status()
            else:
                break
            print()

    def buy(self):
        options = ''
        for key, value in self.coffee_types.items():
            options = options + str(key) + ' - ' + value.name + ', '
        options = options + 'back - to main menu:'

        print('What do you want to buy? ' + options)
        choice = input()
        if choice == 'back':
            print()
            return
        selected_coffee = self.coffee_types.get(int(choice))
        self.remove_stock(selected_coffee)

    def check_stock(self, selected_coffee):
        if self.water - selected_coffee.water < 0:
            print('Sorry, not enough water!')
            return False
        if self.milk - selected_coffee.milk < 0:
            print('Sorry, not enough milk!')
            return False
        if self.beans - selected_coffee.beans < 0:
            print('Sorry, not enough coffee beans!')
            return False
        if self.cups - 1 < 0:
            print('Sorry, not enough disposable cups!')
            return False
        return True

    def remove_stock(self, selected_coffee):
        if self.check_stock(selected_coffee):
            self.water = self.water - selected_coffee.water
            self.milk = self.milk - selected_coffee.milk
            self.beans = self.beans - selected_coffee.beans
            self.cups = self.cups - 1
            self.money = self.money + selected_coffee.cost

    def fill(self):
        print('Write how many ml of water do you want to add:')
        fill_water = int(input())
        self.water = self.water + fill_water
        print('Write how many ml of milk do you want to add:')
        fill_milk = int(input())
        self.milk = self.milk + fill_milk
        print('Write how many grams of coffee beans do you want to add:')
        fill_beans = int(input())
        self.beans = self.beans + fill_beans
        print('Write how many disposable cups of coffee do you want to add:')
        fill_cups = int(input())
        self.cups = self.cups + fill_cups

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0


coffeeMachine = CoffeeMachine(water=400, milk=540, beans=120, cups=9, money=550)
coffeeMachine.select_action()
