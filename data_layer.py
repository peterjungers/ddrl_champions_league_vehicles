"""
This is the data module for champions_league_vehicle_database.py. It is called
by the business module, business_layer.py, and returns a list of tuples.
"""


import sqlite3


class DatabaseQuery:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection == None:
            cls.__connection = sqlite3.connect("champions_league_vehicle_database.db")


    @classmethod
    def category_search(cls, team, season, place):
        cls.connect()

        cursor = cls.__connection.cursor()

        if team == "All" and season == "All" and place == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            ORDER BY season, CAST(place AS INTEGER)
            """)
            cursor.execute(query)
            rows = cursor.fetchall()


        elif team == "All" and season == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE place = ?
            ORDER BY season
            """)
            cursor.execute(query, [place])
            rows = cursor.fetchall()

        elif season == "All" and place == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE team = ?
            ORDER BY vehicle
            """)
            cursor.execute(query, [team])
            rows = cursor.fetchall()

        elif place == "All" and team == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE season = ?
            ORDER BY CAST(place AS INTEGER)
            """)
            cursor.execute(query, [season])
            rows = cursor.fetchall()

        elif team == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE season = ?
            AND place = ?
            """)
            cursor.execute(query, (season, place))
            rows = cursor.fetchall()

        elif season == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE team = ?
            AND place = ?
            ORDER BY season
            """)
            cursor.execute(query, (team, place))
            rows = cursor.fetchall()

        elif place == "All":
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE team = ?
            AND season = ?
            ORDER BY CAST(place AS INTEGER)
            """)
            cursor.execute(query, (team, season))
            rows = cursor.fetchall()

        else:
            query = ("""
            SELECT team, vehicle, season, place
            FROM champions_league_vehicles
            WHERE team = ?
            AND season = ?
            AND place = ?
            """)
            cursor.execute(query, (team, season, place))
            rows = cursor.fetchall()

        return rows


    @classmethod
    def vehicle_search(cls, vehicle):
        cls.connect()

        cursor = cls.__connection.cursor()

        query = ("""
        SELECT team, vehicle, season, place
        FROM champions_league_vehicles
        WHERE LOWER(vehicle) = LOWER(?)
        ORDER BY season
        """)
        cursor.execute(query, [vehicle])
        rows = cursor.fetchall()

        return rows
