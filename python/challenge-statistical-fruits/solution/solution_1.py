apple = [1, 2.3, 4, 5]
orange = [3, 4.4, 5.5, 0.4, 0.6, 1.2, 3.2]
banana = [4, 5, 6]

fruits = {"apple": apple, "orange": orange, "banana": banana}

total_weights = {}
for basket_name, weights in fruits.items():
    total_weight = sum(weights)
    total_weights[basket_name] = total_weight

sorted_weights = sorted(total_weights.items(), key=lambda x: x[1], reverse=True)

output = ""
for basket_name, weight in sorted_weights:
    output += f"{basket_name}: {weight}, "

print(output[:-2])