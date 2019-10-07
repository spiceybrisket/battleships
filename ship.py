class Ship:
    def __init__(self):
        self.__ship_length = 3

    @property  # getter
    def ship_length(self):
        return self.__ship_length
