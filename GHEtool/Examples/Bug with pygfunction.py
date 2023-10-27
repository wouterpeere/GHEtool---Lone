import numpy as np
import pygfunction as gt
import matplotlib.pyplot as plt

list_of_boreholes = [
    gt.boreholes.Borehole(150, 0.7, 0.075, 0, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 6, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 12, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 18, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 24, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 30, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 36, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 42, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 48, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 54, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 60, 0),
    gt.boreholes.Borehole(150, 0.7, 0.075, 0, 30),
    gt.boreholes.Borehole(150, 0.7, 0.075, 6, 30),
    gt.boreholes.Borehole(150, 0.7, 0.075, 12, 30),
    gt.boreholes.Borehole(150, 0.7, 0.075, 18, 30),
    gt.boreholes.Borehole(150, 0.7, 0.075, 24, 30),
    gt.boreholes.Borehole(150, 0.7, 0.075, 0+2.5, 34),
    gt.boreholes.Borehole(150, 0.7, 0.075, 6+2.5, 34),
    gt.boreholes.Borehole(150, 0.7, 0.075, 12+2.5, 34),
    gt.boreholes.Borehole(150, 0.7, 0.075, 18+2.5, 34),
    gt.boreholes.Borehole(150, 0.7, 0.075, 24+2.5, 34),
]

gt.boreholes.visualize_field(list_of_boreholes, view3D=False)
# plt.show()
times = gt.load_aggregation.ClaessonJaved(3600, 3600*8760*100).get_times_for_simulation()
print(gt.gfunction.gFunction(list_of_boreholes, 2.4/2.4/10**6, times).gFunc)
