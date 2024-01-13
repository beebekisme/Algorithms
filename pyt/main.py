import dearpygui.dearpygui as dpg
from algorithms import Sorting_Algorithms
import pprint

dpg.create_context()


with dpg.theme(tag='algo_button_border_theme'):
    with dpg.theme_component():
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (255, 255, 255, 100))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))
        dpg.add_theme_color(dpg.mvThemeCol_Border, (255, 255, 255, 255))
        dpg.add_theme_color(dpg.mvThemeCol_BorderShadow, (0, 0, 0, 0))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
        dpg.add_theme_style(dpg.mvStyleVar_FrameBorderSize, 2)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 8)

def check_data(sender, app_data, user_data):
    print(f'sender - {sender} \n app_data - {app_data} \n user_data - {user_data}')
    pprint.pprint(dpg.get_item_state(f"{sender}"))
    


with dpg.window(tag="Primary Window", width=1280, height=720):
    dpg.add_text("Visualizing Algorithms Here")
    dpg.draw_line((100, 10), 
                  (100, 100), 
                  color=(255, 255, 255, 255), 
                  thickness=10)

with dpg.window(tag ="Algorithms List", label = "Algorithms List", width=250, height=250):
    algo_list = [item for item in dir(Sorting_Algorithms) if not item.startswith("__")]
    
    for algo in algo_list:
        button_title = algo.replace("_", " ").title()
        dpg.add_button(label=f"{button_title}", tag=f"{button_title}", width=200, height=50, callback=check_data, user_data=algo)
        dpg.bind_item_theme(f"{button_title}", "algo_button_border_theme")
        dpg.bind_item_handler_registry(f"{button_title}", "button handler")
        


dpg.create_viewport(title='Visualizing Algorithms', width=1280, height=720)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()