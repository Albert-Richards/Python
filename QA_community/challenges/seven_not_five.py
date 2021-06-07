seven_not_five = []
for i in range(2000, 3200):
    if i % 7 ==0 :
        seven_not_five.append(i)
        if i % 5 ==0 :
            seven_not_five.remove(i)
print(seven_not_five)
    