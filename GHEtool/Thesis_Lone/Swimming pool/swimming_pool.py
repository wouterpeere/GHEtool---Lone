"""
This document contains the sizing of a borefield, according to the three sizing methods in GHEtool
for a swimming pool. This swimming pool has an enormous imbalance towards heat extraction.
"""
# import all the relevant functions
from GHEtool import *
import time

if __name__ == "__main__":
    # initiate ground, fluid and pipe data
    ground_data = GroundFluxTemperature(3, 10)
    fluid_data = FluidData(0.2, 0.568, 998, 4180, 1e-3)
    pipe_data = MultipleUTube(1, 0.015, 0.02, 0.4, 0.05, 2)

    # initiate borefield
    borefield = Borefield()

    # set ground data in borefield
    borefield.set_ground_parameters(ground_data)
    borefield.set_fluid_parameters(fluid_data)
    borefield.set_pipe_parameters(pipe_data)

    borefield.create_rectangular_borefield(15, 20, 6, 6, 110, 4)

    # set temperature bounds
    borefield.set_min_ground_temperature(3)
    borefield.set_max_ground_temperature(17)

    borefield.calculation_setup(max_nb_of_iterations=100)

    # load the hourly profile
    load = HourlyGeothermalLoad()
    load.load_hourly_profile("swimming_pool.csv", header=True, separator=";", col_heating=1, col_cooling=0)
    borefield.load = load

    ### size the borefield
    # according to L2
    L2_start = time.time()
    depth_L2 = borefield.size(100, L2_sizing=True)
    L2_stop = time.time()

    # according to L3
    L3_start = time.time()
    depth_L3 = borefield.size(100, L3_sizing=True)
    L3_stop = time.time()

    # according to L4
    L4_start = time.time()
    depth_L4 = borefield.size(100, L4_sizing=True)
    L4_stop = time.time()

    ### print results
    print("The sizing according to L2 took", round((L2_stop - L2_start) * 1000, 4), "ms and was", depth_L2, "m.")
    print("The sizing according to L3 took", round((L3_stop - L3_start) * 1000, 4), "ms and was", depth_L3, "m.")
    print("The sizing according to L4 took", round((L4_stop - L4_start) * 1000, 4), "ms and was", depth_L4, "m.")

    print("The average ground temperature for L2 is", borefield._Tg(H=depth_L2))
    print("The average ground temperature for L3 is", borefield._Tg(H=depth_L3))
    print("The average ground temperature for L4 is", borefield._Tg(H=depth_L4))

    borefield.plot_load_duration()
    borefield.print_temperature_profile(plot_hourly=True)
