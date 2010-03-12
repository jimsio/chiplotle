import random
from chiplotle import *
plotter = instantiate_plotter()

left = plotter.margins.soft.left
right = plotter.margins.soft.right
top = plotter.margins.soft.top
bottom = plotter.margins.soft.bottom

plotter.selectPen(1)

# this draws 20 curves with 10 random control points each
n_curves = 20
n_control_points=10

for i in range(n_curves):
	bez=[]
	for p in range(n_control_points):
		x=random.randint(left,right)
		y=random.randint(bottom, top)
		bez.append((x,y))
	b = Bezier(bez)
	plotter.write(b.format)

plotter.selectPen(0)
