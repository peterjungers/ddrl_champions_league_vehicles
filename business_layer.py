"""
This is the business module for champions_league_vehicle_database.py. It, in
turn, connects to the data module, data_layer.py, and returns class list
objects to the main module.
"""


from data_layer import DatabaseQuery


class ListCreator:
    def __init__(self, team, vehicle, season, place):
        self.__team = team
        self.__vehicle = vehicle
        self.__season = season
        self.__place = place


    @property
    def team(self):
        return self.__team

    @property
    def vehicle(self):
        return self.__vehicle

    @property
    def season(self):
        return self.__season

    @property
    def place(self):
        return self.__place


    @staticmethod
    def get_category_list(team, season, place):
        list_of_entities = []

        list_of_rows = DatabaseQuery.category_search(team, season, place)
        for row in list_of_rows:
            single_entity = ListCreator(row[0], row[1], row[2], row[3])
            list_of_entities.append(single_entity)

        return list_of_entities


    @staticmethod
    def get_vehicle_list(vehicle):
        list_of_entities = []

        list_of_rows = DatabaseQuery.vehicle_search(vehicle)
        for row in list_of_rows:
            single_entity = ListCreator(row[0], row[1], row[2], row[3])
            list_of_entities.append(single_entity)

        return list_of_entities
