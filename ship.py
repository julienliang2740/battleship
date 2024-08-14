class Ship:
    def __init__(self, coordinates, id, is_sunk):
        ship_array = []
        for coords in coordinates:
            ship_array.append([coords, False])
        self.ship_array = ship_array
        self.id = id
        self.is_sunk = is_sunk

    def process_hit(self, hit_coords): # register the hit and check if ship has been sunk
        to_return = "untouched"
        for coords_hit_list in self.ship_array:
            if hit_coords == coords_hit_list[0]:
                if coords_hit_list[1] == True:
                    to_return =  "repeat hit"
                    break
                elif coords_hit_list[1] == False:
                    coords_hit_list[1] = True
                    to_return = "hit"
                    break

        has_untouched = False
        for coords_hit_list in self.ship_array:
            if coords_hit_list[1] == False:
                has_untouched = True
                break
        if not has_untouched:
            self.is_sunk = True
        
        return to_return



if __name__ == '__main__':
    myship = Ship([[0,0], [1,0], [2,0]], 1, False)
    print(myship.ship_array)
    myship.process_hit([0,0])
    myship.process_hit([1,0])
    myship.process_hit([2,0])
    print(myship.ship_array)
    print(myship.is_sunk)