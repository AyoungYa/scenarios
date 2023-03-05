
def read_log(file_name):
    count = 0
    with open(file_name, "r") as f:
        for line in f.readlines():
            print(line)
            count += 1
