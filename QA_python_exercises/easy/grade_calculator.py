maths_mark = int(input("Enter your maths mark:"))
chem_mark = int(input("Enter your chemistry mark:"))
phys_mark = int(input("Enter your physics mark:"))
percent = float((maths_mark + chem_mark + phys_mark)/3)
print(f"Your percentage score is: {percent}%")

if percent >= 70:
    print("Your grade is: A")
elif 60 <= percent < 70:
    print("Your grade is: B")
elif 50 <= percent < 60:
    print(f"Your grade is: C")
elif 40 <= percent < 50:
    print(f"Your grade is: D")
else:
    print("You have failed")
 