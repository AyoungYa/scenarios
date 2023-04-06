def count_characters(input_string):
    """
    This function takes a string as input and returns a dictionary with the count of each character in the string.

    Parameters:
    input_string (str): A string to count the characters in.

    Returns:
    dict: A dictionary with the count of each character in the input string.
    """
    # Create an empty dictionary to store the character counts
    character_count = {}

    # Iterate over each character in the input string
    for char in input_string:
        # If the character is not a whitespace character, add it to the dictionary or increase its count
        if char != " ":
            character_count[char] = character_count.get(char, 0) + 1

    # Return the character count dictionary
    return character_count
