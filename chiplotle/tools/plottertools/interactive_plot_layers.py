from chiplotle.geometry.core.layersvisitor import LayersVisitor

def interactive_plot_layers(shape, plotter):
   '''Sorts given `shape` by layers and interactively plots,
   requesting the use to change page every time a layer is done printing.'''
   v = LayersVisitor()
   v.visit(shape)

   for layer, shapes in v.layers.items():
      raw_input('Please set/change paper and hit ENTER to plot layer [%s].' % layer)
      print 'Plotting layer [%s]...' % layer
      plotter.write(shapes)
      plotter._sleep_while_buffer_full()
      print 'Done plotting layer [%s].' % layer



if __name__ == '__main__':
   from chiplotle import *

   r1 = rectangle(1000, 1000)
   r1.layer = 1
   r2 = rectangle(500, 500)
   r2.layer = None
   t  = isosceles(500, 200)
   t.layer = None

   rg = Group([r1, r2])
   rg.layer = 2
   g = Formation([t, rg])
   g.layer = 3

   plotter = instantiate_plotters()[0]
   interactive_plot_layers(g, plotter)