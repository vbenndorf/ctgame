from otree.api import *

doc = """
Matching pennies game
"""


class C(BaseConstants):
    NAME_IN_URL = 'matching_pennies'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    eps = 2
    B = 2
    C = 8
    B_eps = B + eps
    DELTA = 0.2
    PLAYER1_ROLE = 'Player 1'
    PLAYER2_ROLE = 'Player 2'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    ready_check = models.IntegerField(
        choices=[1, 2, 3],
    )
    penny_side = models.BooleanField(
        label='Please choose Heads or Tails',
        choices=[
            [True, "Heads"],
            [False, "Tails"],
        ]
    )
    move_in_beginning = models.BooleanField(intial=False)
    time_of_move = models.FloatField()
    time_out = models.BooleanField(initial=False)
    stop = models.BooleanField()
    stop_time = models.FloatField(min=0, max=60000, default=0)
    simultaneous = models.BooleanField(default=False)
    #stop_move_simultaneous = models.BooleanField(default=False)
    Q1 = models.IntegerField()  # for the instructions quiz
    Q2 = models.IntegerField()
    Q3 = models.IntegerField()


# FUNCTIONS
def creating_session(subsession: Subsession):
    #session = subsession.session
    subsession.group_randomly()  # shuffles players randomly, so they can end up in any group, and any position within the group


def set_payoffs(group: Group):
    #subsession = group.subsession
    #session = group.session
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    t1 = p1.time_of_move
    t2 = p2.time_of_move

    if t1 == -1:
        t1 = 65000
    if t2 == -1:
        t2 = 65000
    if p1.move_in_beginning:
        t1 = 0
    else:
        t1 = max(t1 - 5000, 0)
    if p2.move_in_beginning:
        t2 = 0
    else:
        t2 = max(t2 - 5000, 0)
    if t1 >= t2:
        if (t1 - t2) < 5000:
            t1 = t2
        else:
            t1 = t1 - 5000
    if t2 > t1:
        if (t2 - t1) < 5000:
            t2 = t1
        else:
            t2 = t2 - 5000

    factor1 = 1 - (1 - C.DELTA) * (t1 / 60000)
    factor2 = 1 - (1 - C.DELTA) * (t2 / 60000)
    # TODO: add correct payoffs when one ore more players time out
    if p1.time_out or p2.time_out:
        if p1.time_out and p2.time_out:
            p1.payoff = ((C.C-C.B)**2 + 2*C.B*(C.C-C.B) - C.B*C.eps)/(2*(C.C-C.B) - C.eps) * C.DELTA
            p2.payoff = ((C.B + C.C)/2) * C.DELTA
        elif p1.time_out:
            if p2.penny_side:
                p1.payoff = ((C.B + C.C + C.eps)/2) * C.DELTA
            else:
                p1.payoff = ((C.B + C.C)/2) * C.DELTA
            p2.payoff = ((C.B + C.C)/2) * factor2
        elif p2.time_out:
            p1.payoff = (C.C ** 2 - C.B ** 2 - C.B * C.eps) / (2 * (C.C - C.B) - C.eps) * factor1
            if p1.penny_side:
                p2.payoff = (C.C**2 - C.B**2 - C.B*C.eps)/(2*(C.C-C.B)-C.eps) * C.DELTA
            else:
                p2.payoff = (C.C**2 - C.B**2 - C.C*C.eps)/(2*(C.C-C.B)-C.eps) * C.DELTA
    else:
        if p1.penny_side:
            if p2.penny_side:
                p1.payoff = C.B_eps * factor1
                p2.payoff = C.C * factor2
            else:
                p1.payoff = C.C * factor1
                p2.payoff = C.B * factor2
        else:
            if p2.penny_side:
                p1.payoff = C.C * factor1
                p2.payoff = C.B * factor2
            else:
                p1.payoff = C.B * factor1
                p2.payoff = C.C * factor2



# PAGES
class WaitPage1(WaitPage):
    template_name = 'matching_pennies/WaitPage1.html'




class Choice3(Page):
    form_model = 'player'
    form_fields = ['penny_side', 'time_of_move', 'move_in_beginning', 'time_out', 'stop', 'stop_time', 'simultaneous']

    @staticmethod
    def js_vars(player: Player):
        return dict(player_id=player.id_in_group)

    @staticmethod
    def live_method(player: Player, data):
        if data['type'] == 'checkbox':
            num = data['num']
            penny_side = data['penny_side']
            check = data['check']
            return {1: {"type": "checkbox", "player": player.id_in_group, "check": check, "num": num, "penny_side": penny_side},
                    2: {"type": "checkbox", "player": player.id_in_group, "check": check, "num": num, "penny_side": penny_side}}
        if data['type'] == 'button':
            if data['first']:
                if data['penny_side']:
                    if player.id_in_group == 1:
                        return {1: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": True},
                                2: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": True}}
                    else:
                        return {1: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": True},
                                2: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": True}}
                else:
                    if player.id_in_group == 1:
                        return {1: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": True},
                                2: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": True}}
                    else:
                        return {1: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": True},
                                2: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": True}}
            else:  #not first
                if data['penny_side']:
                    if player.id_in_group == 1:
                        return {1: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": False},
                                2: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": False}}
                    else:
                        return {1: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": False},
                                2: {"type": "button", "penny_side": True, "player": player.id_in_group, "first": False}}
                else:
                    if player.id_in_group == 1:
                        return {1: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": False},
                                2: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": False}}
                    else:
                        return {1: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": False},
                                2: {"type": "button", "penny_side": False, "player": player.id_in_group, "first": False}}


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    #wait_for_all_groups = True


class ResultsSummary(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS

    @staticmethod
    def vars_for_template(player: Player):
        session = player.session

        player_in_all_rounds = player.in_all_rounds()
        return dict(
            total_payoff=sum([p.payoff for p in player_in_all_rounds]),
            player_in_all_rounds=player_in_all_rounds,
        )


page_sequence = [WaitPage1, Choice3,
                 ResultsWaitPage, ResultsSummary]
