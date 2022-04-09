class Destination:
    def __init__(self, dir) -> None:
        self.dir = dir
    def write(self):
        print(self.dir)