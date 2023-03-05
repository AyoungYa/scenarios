def get_uri_and_count(file_name):
    result = {}
    with open(file_name, "r") as f:
        for line in f.readlines():
            uri, time = line.split(' ')
            if result.get(uri):
                result[uri] = result[uri] + 1
            else:
                result[uri] = 1
    return result

