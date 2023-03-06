def time_statistics(file_name):
    max_uri, max_avg_time = None, None
    min_uri, min_avg_time = None, None
    # TODO: implement this function
    # Note: Do not change the existing code

    return (max_uri, max_avg_time), (min_uri, min_avg_time)


if __name__ == '__main__':
    file_name = 'access.log'
    (max_uri, max_avg_time), (min_uri, min_avg_time) = time_statistics(file_name)
    print("Maximum average uri: ", max_uri, ", average value: ", max_avg_time)
    print("Minimum average uri: ", min_uri, ", average value: ", min_avg_time)