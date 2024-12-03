class Rectangle:
    def __init__(self, width=1, height=1):
      self.width = int(width)
      self.height = int(height)

    def set_width(self, width):
      self.width = width

    def set_height(self, height):
      self.height = height

    def get_area(self):
      return self.width * self.height

    def get_perimeter(self):
      return 2 * self.width + 2 * self.height

    def get_diagonal(self):
      return (self.width ** 2 + self.height ** 2) ** .5

    def __str__(self):
      return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
      
    def get_picture(self):
      if (self.width>50 or self.height>50):
        return "Too big for picture."
      onerow="*"*self.width + "\n"
      return onerow*self.height

    def get_amount_inside(self,othr):
      if not isinstance(othr, Rectangle):
        print("Error: no such shape to fit.")
        return 0
      if (othr.width>self.width or othr.height>self.height):
        return 0
      nfitwide = int(self.width / othr.width)
      nfittall = int(self.height / othr.height)
      return nfitwide*nfittall

class Square(Rectangle):
    def __init__(self, side=1):
      self.width = side
      self.height = side
      self.side = side

    def set_side(self, side):
      self.side = side
      self.set_width(side)

    def set_width(self, width):
      self.width = width
      self.height = width
      self.side = width

    def set_height(self, height):
      self.width = height
      self.height = height
      self.side = height

    def __str__(self):
      return "Square(side="+str(self.side)+")"