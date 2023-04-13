
def read_log(file_name: str) -> int:
    line_count = 0
    
    with open(file_name, "r") as f:
        for line in f.readlines():
            print(line)
            line_count += 1
    return line_count
