class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        return iter([
            {'length': self.length},
            {'width': self.width}
        ])
if __name__ == "__main__":
    rect = Rectangle(10, 5)

    for item in rect:
        print(item)
