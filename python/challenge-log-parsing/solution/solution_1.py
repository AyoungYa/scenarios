with open("../assets/access.log", "r") as f:
    for line in f.readlines():
        print(line)