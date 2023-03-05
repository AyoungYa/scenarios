result = {}
with open("../assets/access.log", "r") as f:
    for line in f.readlines():
        uri, time = line.split(' ')
        if result.get(uri):
            result[uri] = result[uri] + 1
        else:
            result[uri] = 1
for k, v in result.items():
    print(k, v)

