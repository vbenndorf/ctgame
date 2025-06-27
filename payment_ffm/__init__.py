from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_ffm'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass




class Results(Page):
    def vars_for_template(self):
        context = {
            'payoff_plus_participation_fee': self.participant.payoff_plus_participation_fee()}
        return context



page_sequence = [Results]
