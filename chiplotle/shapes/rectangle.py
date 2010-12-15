from chiplotle.shapes.polygon import Polygon
from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.commands import PU, PD, PA

class Rectangle(Polygon):
   '''
      A rectangle with a width, height, and offset.
      
      offset is a CoordinatePair for moving the Rectangle around on the page.
      
      The Rectangle is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, offset):  
      self.width = width
      self.heigth = height
      
      corners = []
      corners.append(CoordinatePair(-width/2, -height/2))
      corners.append(CoordinatePair(-width/2, height/2))
      corners.append(CoordinatePair(width/2, height/2))
      corners.append(CoordinatePair(width/2, -height/2))
      Polygon.__init__(self, [corners], offset)  
      
   
'''
from shapes.rectangle import Rectangle
r1 = Rectangle(1000,2000, [0,0])
r1.points
r1.format
io.view(r1)

'''