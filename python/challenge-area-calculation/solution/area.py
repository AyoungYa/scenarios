from solution.subclass import Circle, Square


def cal_area(input_str):
    """
     Implement area calculation using the two classes from the previous steps.
    :param input_str:
    :return:
    """
    # TODO: Write your code here
    # Note: Do not change the existing code
    shape_type, length = input_str.split(" ")
    shape_type = int(shape_type.trim())
    length = float(length.trim())

    shape_name = ''
    area = 0
    if shape_type == 1:
        area = Circle(length).area()
        shape_name = 'circle'

    elif shape_type == 2:
        area = Square(length).area()
        shape_name = 'square'
    return shape_name, area


def get_input():
    # TODO: Write your code here
    # Note: Do not change the existing code
    return input("Please input shape type(1: circle, 2: square) and length with space to split:")


if __name__ == '__main__':
    input_str = get_input()
    shape_name, area = cal_area(input_str)
    print(f"The area of the {shape_name} is {area}")
