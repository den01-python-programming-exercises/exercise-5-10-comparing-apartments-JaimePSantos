class Apartment:

    def __init__(self, rooms, squares, price_per_square):
        self.rooms = rooms
        self.square = squares
        self.price_per_square = price_per_square
    
    def larger_than(self,other):
      if(self.square>other.square):
        return True
      else:
        return False
    
    def price_difference(self, other):
      thisPrice = self.price_per_square * self.square
      otherPrice = other.price_per_square * other.square
      return abs(thisPrice - otherPrice)

    def more_expensive_than(self,other):
      thisPrice = self.price_per_square * self.square 
      otherPrice = other.price_per_square * other.square
      if thisPrice - otherPrice > 0:
        return True
      else:
        return False