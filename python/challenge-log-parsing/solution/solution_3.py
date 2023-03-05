result = {}
with open("../assets/access.log", "r") as f:
    for line in f.readlines():
        uri, time = line.split(' ')
        if result.get(uri):
            result[uri].append(float(time.strip()))
        else:
            result[uri] = [float(time.strip())]

minUri, minTime = '', 99999
maxUri, maxTime = '', 0
for k, v in result.items():
    avgTime = sum(v) / len(v)
    if minTime > avgTime:
        minUri = k
        minTime = avgTime
    if maxTime < avgTime:
        maxUri = k
        maxTime = avgTime

print(minUri, minTime)
print(maxUri, maxTime)


