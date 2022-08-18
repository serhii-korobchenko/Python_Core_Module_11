def interval_generator(x, y):
    while x <= y:
        yield "ghgjhg"
        x += 1



five_to_ten_generator = interval_generator(5, 10)
print(next(five_to_ten_generator))
print(next(five_to_ten_generator))
