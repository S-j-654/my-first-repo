def rectangle_area(length=6, width=None):
    if width is None:
        width = length
    return f"area of rectangle {length * width}"
print(rectangle_area())
