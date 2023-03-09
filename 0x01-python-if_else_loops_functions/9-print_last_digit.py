st_digit(number):
    if number < 0:
        last = ((number * -1) % 10)
    else:
        last = number % 10
    print('{}'.format(last), end="")
    return last
