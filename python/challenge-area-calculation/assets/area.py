def cal_area(input_str):
    """
     Implement area calculation using the two classes from the previous steps.
    :param input: user input str
    :return: shape_name: the shape of input, one of: square, circle or none
             area: the area of the shape, if not square or circle, return 0
    """
    # TODO: Write your code here
    # Note: Do not change the existing code
    shape_name = None
    area = None
    return shape_name, area

def get_input():
    """
    Get the input from keyboard and return the str
    :return:
    """
    # TODO: Write your code here
    # Note: Do not change the existing code
    input_str = None
    return input_str


if __name__ == "__main__":
    input_str = get_input()
    shape_name, area = cal_area(input_str)
    print(f"The area of the {shape_name} is {area}")
