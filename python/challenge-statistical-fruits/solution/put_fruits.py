def put_fruits():
    basket_capacity = 10
    basket_weight = 0

    result = []
    while basket_weight <= basket_capacity:
        try:
            fruit_weight = float(input("Enter the weight of the fruit: "))
        except ValueError:
            continue
        if (basket_weight + fruit_weight) > basket_capacity:
            return basket_weight, result
        else:
            basket_weight += fruit_weight
            result.append(fruit_weight)

    return basket_weight, result


if __name__ == "__main__":
    fruits = put_fruits()
    print(fruits)
