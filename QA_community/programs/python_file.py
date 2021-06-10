file = open("teams.txt", "w")
teams = "Man Utd." + "\n" + "Chelsea" + "\n" + "Liverpool" + "\n" + "Arsenal" + "\n" + "Man City"
file.write(teams)
file.close()
file = open("teams.txt", "r")
print(file.readline())
file.readline()
file.readline()
print(file.readline())
