MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Coin values
QUARTERS_VALUE = 0.25
DIMES_VALUE = 0.10
NICKELS_VALUE = 0.05
PENNIES_VALUE = 0.01

espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
ESPRESSO_COST = MENU["espresso"]["cost"]

latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
LATTE_COST = MENU["latte"]["cost"]

cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
CAPPUCCINO_COST = MENU["cappuccino"]["cost"]


def making_coffee(type, wat_res, cof_res, milk_res, mac_money):
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_amount = (
        (quarters * QUARTERS_VALUE)
        + (dimes * DIMES_VALUE)
        + (nickels * NICKELS_VALUE)
        + (pennies * PENNIES_VALUE)
    )
    if total_amount >= MENU[type]["cost"]:
        if type == "espresso":
            wat_res -= espresso_water
            cof_res -= espresso_coffee
            change = round((total_amount - ESPRESSO_COST), 2)
        else:
            wat_res -= MENU[type]["ingredients"]["water"]
            cof_res -= MENU[type]["ingredients"]["coffee"]
            milk_res -= MENU[type]["ingredients"]["milk"]
            change = round((total_amount - MENU[type]["cost"]), 2)
        mac_money += MENU[type]["cost"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {type} ☕😃. Enjoy!")
    else:
        print("Sorry 🙁 that's not enough money. Money refunded")

    return [wat_res, cof_res, milk_res, mac_money]


def is_resources_sufficient(order_ingredients, t_water, t_milk, t_coffee):
    t_ingredients = {"water": t_water, "milk": t_milk, "coffee": t_coffee}
    for item in order_ingredients:
        if order_ingredients[item] >= t_ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


total_water = resources["water"]
total_milk = resources["milk"]
total_coffee = resources["coffee"]
machine_money = 0

machine_is_on = True
while machine_is_on:
    choose = input(
        "What would you like? (espresso/latte/cappuccino) or (report/coffee requirements): "
    ).lower()
    if choose == "off":
        machine_is_on = False

    elif choose == "report":
        print(f"Water: {total_water}ml")
        print(f"Milk: {total_milk}ml")
        print(f"Coffee: {total_coffee}g")
        print(f"Money: ${machine_money}")
    elif choose == "coffee requirements":
        print(
            f"Espresso needs {espresso_water}ml of water, {espresso_coffee}g of Coffee, and costs ${ESPRESSO_COST}."
        )
        print(
            f"Latte requires {latte_water}ml of Water, {latte_milk}ml of Milk, {latte_coffee}g Coffee, Cost: ${LATTE_COST}."
        )
        print(
            f"Cappuccino contains {cappuccino_water}ml of Water, {cappuccino_milk}ml of Milk, {cappuccino_coffee}g Coffee and costs ${CAPPUCCINO_COST}."
        )
    else:
        drink = MENU[choose]
        if is_resources_sufficient(
            drink["ingredients"], total_water, total_milk, total_coffee
        ):
            coffee_making = making_coffee(
                choose, total_water, total_coffee, total_milk, machine_money
            )
            total_water = coffee_making[0]
            total_coffee = coffee_making[1]
            total_milk = coffee_making[2]
            machine_money = coffee_making[3]
