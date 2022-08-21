import tzlocal

import data
from data.game import Game


class Pregame:
    def __init__(self, game: Game, time_format):
        self.home_team = game.home_abbr()
        self.away_team = game.away_abbr()
        self.time_format = time_format

        self.date = self.__convert_date(game.datetime())

        try:
            self.start_time = self.__convert_time(game.datetime())
        except:
            self.start_time = "TBD"

        # self.status = game.status()

    def __convert_time(self, game_time_utc):
        """Converts pregame UTC times into the local time zone"""
        time_str = "{}:%M".format(self.time_format)
        if self.time_format == "%-I":
            time_str += "%p"
        return game_time_utc.astimezone(tzlocal.get_localzone()).strftime(time_str)

    def __convert_date(self, game_time_utc):
        date_text = game_time_utc.astimezone(tzlocal.get_localzone()).strftime('%a')
        if date_text == data.today.astimezone(tzlocal.get_localzone()).strftime('%a'):
            date_text = 'TODAY'
        return date_text

    def __str__(self):
        s = "<{} {}> {} @ {}; {};".format(
            self.__class__.__name__,
            hex(id(self)),
            self.away_team,
            self.home_team,
            self.start_time,
        )
        return s