def parent_function(Name, Coins):
    def another_function():
        nonlocal Coins
        Coins -= 1
        if Coins > 1:
            print("\n" + Name + " has " + str(Coins) + " coins left.")
        elif Coins == 1:
            print("\n" + Name + " has " + str(Coins) + " coin left.")
        else:
            print("\n" + Name + " is out of coins.")
    return another_function

tommy = parent_function("Tommy", 4)
sarah = parent_function("Sarah", 5)
tommy()
tommy()
tommy()

sarah()