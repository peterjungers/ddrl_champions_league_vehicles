# ****************************************************************************
# Author:           Peter Jungers
# Program name:     Champions League vehicle database
# Version:	        1.0
# Date:             06/10/2022
# Description:      A searchable database of all Damon Die-Cast Racing League
#                   (DDRL) Champions League vehicles
# Inputs:           vehicle
# Outputs:          entity.team, entity.vehicle, entity.season, entity.place
#                   in list_of_entities
# Main module:      champions_league_vehicle_database.py
# Other modules:    business_layer.py, data_layer.py
# Related files:    champions_league_vehicle_database.ui,
#                   champions_league_vehicle_database.db, checkered_flag.png
# ****************************************************************************


import pathlib
import pygubu
import tkinter as tk
import tkinter.messagebox as mb

from business_layer import ListCreator


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "champions_league_vehicle_database.ui"


class ChampionsLeagueVehicleDatabaseApp:
    def __init__(self, master=None):
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.__mainwindow = builder.get_object("main_window", master)
        builder.connect_callbacks(self)

        self.__mainwindow.iconphoto(True, tk.PhotoImage(file='checkered_flag.png'))

        self.__team_combobox = builder.get_object("team_combobox")
        self.__season_combobox = builder.get_object("season_combobox")
        self.__place_combobox = builder.get_object("place_combobox")

        self.__vehicle_name_entry = builder.get_object("vehicle_name_entry")

        self.__category_search_button = builder.get_object("category_search_button")
        self.__vehicle_search_button = builder.get_object("vehicle_search_button")

        self.__data_tree = builder.get_object("data_tree")

        self.set_up_data_tree()


    def set_up_data_tree(self):
        """
        Initializes GUI treeview attributes
        """

        # Sets amount of columns
        self.__data_tree.configure(columns=(0, 1, 2, 3))

        # Labels column headings
        self.__data_tree.heading(0, text="Team")
        self.__data_tree.heading(1, text="Vehicle")
        self.__data_tree.heading(2, text="Season")
        self.__data_tree.heading(3, text="Place")

        # Sets column attributes
        self.__data_tree.column(0, width=10, anchor="w")
        self.__data_tree.column(1, width=100, anchor="w")
        self.__data_tree.column(2, width=5, anchor="center")
        self.__data_tree.column(3, width=5, anchor="center")

        # Sets text and background colors when called
        self.__data_tree.tag_configure(
            "team_damon",foreground="black", background="#6fa8dc")
        self.__data_tree.tag_configure(
            "team_ian", foreground="black", background="#e06666")
        self.__data_tree.tag_configure(
            "team_benny", foreground="black", background="#ffd966")
        self.__data_tree.tag_configure(
            "team_peter", foreground="black", background="#93c47d")

        # Initializes comboboxes to "All" and shows results upon opening program
        self.__team_combobox.current(0)
        self.__season_combobox.current(0)
        self.__place_combobox.current(0)
        self.get_category_search()


    def clear_table(self):
        for data in self.__data_tree.get_children():
            self.__data_tree.delete(data)


    def get_category_search(self):
        self.clear_table()

        team = self.__team_combobox.get()
        season = self.__season_combobox.get()
        place = self.__place_combobox.get()

        list_of_entities = ListCreator.get_category_list(team, season, place)
        self.get_list_objects(list_of_entities)


    def get_vehicle_search_on_button_click(self):
        self.get_vehicle_search()

    def get_vehicle_search_on_keypress(self, event=None):
        self.get_vehicle_search()

    def get_vehicle_search(self):
        vehicle = self.__vehicle_name_entry.get()

        if vehicle == "":
            mb.showerror(title="Whoops!", message="Please enter a vehicle name.")
        else:
            list_of_entities = ListCreator.get_vehicle_list(vehicle)
            self.get_list_objects(list_of_entities)


    def get_list_objects(self, list_of_entities):
        # Gets ListCreator class objects, populates tree
        if list_of_entities:
            self.clear_table()
            for entity in list_of_entities:
                if entity.team == "Damon":
                    self.__data_tree.insert("", "end",
                                            values=(
                    entity.team, entity.vehicle, entity.season, entity.place),
                                            tags=("team_damon")
                                            )
                elif entity.team == "Ian":
                    self.__data_tree.insert("", "end",
                                            values=(
                    entity.team, entity.vehicle, entity.season, entity.place),
                                            tags=("team_ian")
                                            )
                elif entity.team == "Benny":
                    self.__data_tree.insert("", "end",
                                            values=(
                    entity.team, entity.vehicle, entity.season, entity.place),
                                            tags=("team_benny")
                                            )
                elif entity.team == "Peter":
                    self.__data_tree.insert("", "end",
                                            values=(
                    entity.team, entity.vehicle, entity.season, entity.place),
                                            tags=("team_peter"))
        else:
            mb.showerror(title="Whoops!", message="Sorry, no results. The spelling has to be exact.")


    def run(self):
        self.__mainwindow.mainloop()


if __name__ == "__main__":
    app = ChampionsLeagueVehicleDatabaseApp()
    app.run()
