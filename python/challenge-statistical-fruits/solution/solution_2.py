basket_capacity = 10
basket_weight = 0

while basket_weight <= basket_capacity:
    fruit_weight = float(input("Enter the weight of the fruit: "))
    basket_weight += fruit_weight
    if basket_weight > basket_capacity:
        print("The basket is full. Total weight: {:.2f}kg".format(basket_weight))
        break