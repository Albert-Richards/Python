import pdb
"""## exercise 1
num = float(input("Burger price:"))
price = {"Burger": num}
user_funds = 10.31
item_price = price["Burger"]

if item_price < user_funds:
    print("You have enough money!")
if item_price == user_funds:
    print("You have the precise amount of money")
if item_price > user_funds:
    print("Sorry you don't have enough money")

##exercise 2
def product(n):
    total = 1
    for n in n:
        total *= n
    return total

print(product([4,4,5]))"""
##exercise 3
#pdb.set_trace()
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
        return True
print(is_prime(78))
##exercise
"""pdb.set_trace()
item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[i])

print(item_list[5])"""