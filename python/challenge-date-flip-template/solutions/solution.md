# Solution

In this solution, we use the `datetime.datetime.strptime()` method to parse the input string and convert it into a datetime object. The `strptime()` method takes two arguments: the string to parse and the format of the string. The format for the input string is `"%Y-%m-%d"`.

Once we have the datetime object, we can extract the day, month, and year values using the `day`, `month`, and `year` attributes.

Finally, we use string formatting to create a new string in the format `dd-mm-yyyy`. The string is formatted using the `"{}-{}-{}".format(day, month, year)` syntax.
