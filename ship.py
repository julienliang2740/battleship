class Ship:
    def __init__(self, size, bow, stern): # bow, stern -> (int, int, bool)
        # True -> alive, False -> shot
        ship_array = []

        if bow[0] == stern[0]:
            for n in range(bow[1], stern[1]+1):
                ship_array.append((bow[0], n, True))
        elif bow[1] == stern[1]:
            for n in range(bow[0], stern[0]+1):
                ship_array.append((n, bow[1], True))

        self.ship_array = ship_array
        self.size = size
    
    def is_sunk(self):
        for point in self.ship_array:
            if point[2]:
                return False
        return True

    def process_hit(self, coords): # coords -> (int, int)
        for point in self.ship_array:
            if point[0] == coords[0] and point[1] == coords[1]:
                if point[2] == False:
                    return "repeat_hit"
                elif point[2] == True:
                    return "hit"
        return