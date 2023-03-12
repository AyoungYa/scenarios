def put_fruits():
    basket_capacity = 10
    basket_weight = 0

    result = []
    while basket_weight <= basket_capacity:
        fruit_weight = float(input("Enter the weight of the fruit: "))
        basket_weight += fruit_weight
        if basket_weight > basket_capacity:
            return result
        else:
            result.append(fruit_weight)

    return result


if __name__ == "__main__":
    fruits = put_fruits()
    print(fruits)
