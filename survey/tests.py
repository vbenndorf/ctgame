from otree.api import Currency as cu, currency_range
from . import *
from otree.api import Bot


import random

class PlayerBot(Bot):

    def play_round(self):
        yield ShorterSurvey, dict(age=random.randint(1,199),female=random.randint(1,3),understanding_descriptions=random.randint(1,7),responsiveness=random.randint(1,7),problems=random.randint(1,7))


