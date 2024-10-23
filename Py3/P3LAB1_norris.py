# CTI 110
# P3LAB1 - Choose your own adventure
# norrisa
# 10/22/24

def main():
    print("Choose Your Own Adventure")
    go_home() 

def go_home():
    print("You decide to go home.")
    print("But should you get some food?")
    print("1. Order [pizza]")
    print("2. Get [chinese]")
    choice = input()
    if choice == "pizza":
        get_pizza()
    elif choice == "chinese":
        get_chinese()

def get_pizza():
    print("The pizza is cursed!")
    print("💀💀💀 BAD ENDING 💀💀💀")

def get_chinese():
    print("The food is delicious!")
    print("🥡🥡🥡 GOOD ENDING 🥡🥡🥡")


# start the program
main()