def histogram(data, n, b, h):
    # data is a list
    # n is an integer
    # b and h are floats
    
    # Write your code here
    if b == h:
        print('b and h are the same value')
        return []
    if n <= 0:
        return []
    if b > h:
        temp = b
        b = h
        h = temp

    hist = [0] * n
    new_data = []

    for value in data:  # new data list for the given boundary
        if b < value < h:
            new_data.append(value)

    w = (h - b) / n  # bin width

    # remove repeat numbers
    new_data = list(set(new_data))

    for i in range(0, n):  # increment -> hist
        for k in range(0, len(new_data)):  # increment -> data
            if b + i * w <= new_data[k] < b + (i + 1) * w:  # check if data value in bin
                hist[i] += 1

    # return the variable storing the histogram
    # Output should be a list
    return hist


def happybirthday(name_to_day, name_to_month, name_to_year):
    # name_to_day, name_to_month and name_to_year are dictionaries
    # Write your code here
    date_to_all = {}
    for name in name_to_day:
        day = name_to_day[name]
        month = name_to_month[name]
        year = name_to_year[name]
        age = 2022 - year
        info = (month, year, age)
        if day in date_to_all:
            old_info = date_to_all[day][1]
            old_age = old_info[2]
            if age > old_age:
                date_to_all[day] = (name, info)
        else:
            date_to_all[day] = (name, info)
    return date_to_all
    # return the variable storing date_to_all
    # Output should be a dictionary
    pass
