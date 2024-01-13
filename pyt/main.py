import dearpygui.dearpygui as dpg
from algorithms import Sorting_Algorithms

dpg.create_context()



with dpg.window(tag="Primary Window", width=1280, height=720):
    dpg.add_text("Visualizing Algorithms Here")

with dpg.window(label = "Algorithms List", width=500, height=300):
    algo_list = [item for item in dir(Sorting_Algorithms) if not item.startswith("__")]
    for algo in algo_list:

        dpg.add_button(label = algo.replace("_", " ").title())
dpg.create_viewport(title='Visualizing Algorithms', width=1280, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()