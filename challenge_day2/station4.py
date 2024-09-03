def solution_station_4(number):
    if number <= 1:
        return "false"
    if number <= 3:
        return "true"
    if number % 2 == 0 or number % 3 == 0:
        return "false"
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return "false"
        i += 6
    
    return "true"
