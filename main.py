# Functions
def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print("Alright, one {} {}, coming up!".format(size, drink_type))
    name = input("Can I get your name please? \n>")
    print("Thanks, {}! Your drink will be ready shortly.".format(name))


def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def get_size():
    res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")
    if res in drink_size.keys():
        return drink_size[res]
    else:
        print_message()
        return get_size()


def get_drink_type():
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
    if res in drink_type.keys():
        if drink_type[res] == "latte":
            return order_latte()
        else:
            return drink_type[res]
    else:
        print_message()
        return get_drink_type()


def order_latte():
    res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n >")
    if res in milk_type.keys():
        return milk_type[res]
    else:
        print_message()
        return order_latte()


# Dictionaries
drink_size = {"a": "small", "b": "medium", "c": "large"}
drink_type = {"a": "brewed coffee", "b": "mocha", "c": "latte"}
milk_type = {"a": "latte", "b": "non-fat latte", "c": "soy latte"}

# Call the program
coffee_bot()
