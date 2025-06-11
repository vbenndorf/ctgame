from otree.api import *

doc = """
Matching pennies game
"""


class C(BaseConstants):
    NAME_IN_URL = 'matching_pennies'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 53
    B = 200
    C = 800
    PLAYER1_ROLE = 'Player 1'
    PLAYER2_ROLE = 'Player 2'
    NUM_TRIALS = 5
    PERIODS_PER_BLOCK = 12
    


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    first_sender_id = models.IntegerField(initial=0)


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
    simultaneous = models.BooleanField(default=False)
    epsilon = models.FloatField()
    delta = models.FloatField()
    trial_pay = models.CurrencyField()


# FUNCTIONS
def creating_session(subsession: Subsession):
    import random
    subsession.group_randomly()  # shuffles players randomly, so they can end up in any group, and any position within the group
    treatment_list = [[0, 0.2], [40, 0.2], [200, 0.2], [40, 1/3]]
    if subsession.round_number == 1:
        random.shuffle(treatment_list)
        for player in subsession.get_players():
            participant = player.participant
            participant.treatment = treatment_list  #store randomized list of treatments in participant field which is persistent over all rounds

    if subsession.round_number <= C.NUM_TRIALS: #training rounds
        for player in subsession.get_players():
            player.epsilon = 40
            player.delta = 0.2
    if C.NUM_TRIALS  < subsession.round_number <= C.NUM_TRIALS + C.PERIODS_PER_BLOCK:
        for player in subsession.get_players():
            player.epsilon = player.participant.treatment[0][0]
            player.delta = player.participant.treatment[0][1]
    if C.NUM_TRIALS + C.PERIODS_PER_BLOCK < subsession.round_number <= C.NUM_TRIALS + 2*C.PERIODS_PER_BLOCK:
        for player in subsession.get_players():
            player.epsilon = player.participant.treatment[1][0]
            player.delta = player.participant.treatment[1][1]
    if C.NUM_TRIALS + 2*C.PERIODS_PER_BLOCK < subsession.round_number <= C.NUM_TRIALS + 3*C.PERIODS_PER_BLOCK:
        for player in subsession.get_players():
            player.epsilon = player.participant.treatment[2][0]
            player.delta = player.participant.treatment[2][1]
    if subsession.round_number > C.NUM_TRIALS + 3*C.PERIODS_PER_BLOCK:
        for player in subsession.get_players():
            player.epsilon = player.participant.treatment[3][0]
            player.delta = player.participant.treatment[3][1]


def set_payoffs(group: Group):
    #subsession = group.subsession
    #session = group.session
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)

    t1 = p1.time_of_move
    t2 = p2.time_of_move
    timeout1 = p1.time_out
    timeout2 = p2.time_out
    delta = p1.delta
    eps = p1.epsilon

    if timeout1:
        t1 = 65000
    if timeout2:
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

    factor1 = 1 - (1 - delta) * (min(t1, 60000) / 60000)
    factor2 = 1 - (1 - delta) * (min(t2, 60000) / 60000)
    if p1.time_out or p2.time_out:
        if p1.time_out and p2.time_out:
            p1.trial_pay = ((C.B + C.C) / 2) * delta
            p2.trial_pay = ((C.B + C.C) / 2) * delta
        elif p1.time_out:
            p1.trial_pay = ((C.B + C.C) / 2) * delta
            p2.trial_pay = ((C.B + C.C) / 2) * factor2
        elif p2.time_out:
            p1.trial_pay = ((C.B + C.C) / 2) * factor1
            p2.trial_pay = ((C.B + C.C) / 2) * delta
    else:
        if p1.penny_side:
            if p2.penny_side:
                p1.trial_pay = (C.B + eps) * factor1
                p2.trial_pay = C.C * factor2
            else:
                p1.trial_pay = C.C * factor1
                p2.trial_pay = C.B * factor2
        else:
            if p2.penny_side:
                p1.trial_pay = C.C * factor1
                p2.trial_pay = C.B * factor2
            else:
                p1.trial_pay = C.B * factor1
                p2.trial_pay = C.C * factor2
   
    if p1.round_number > C.NUM_TRIALS:
        p1.payoff = p1.trial_pay
        p2.payoff = p2.trial_pay

 

# PAGES
class BlockStart(Page):
    @staticmethod
    def is_displayed(player: Player):
        temp = [1,C.NUM_TRIALS+1,C.NUM_TRIALS + C.PERIODS_PER_BLOCK +1,C.NUM_TRIALS + 2*C.PERIODS_PER_BLOCK+1,C.NUM_TRIALS + 3*C.PERIODS_PER_BLOCK+1]
        return any(player.round_number == x for x in temp)
    
    @staticmethod
    def vars_for_template(player):
        if player.round_number > 1:
             
            prev_round = player.in_round(player.round_number - 1)
            return dict(
                prev_eps = prev_round.epsilon,
                prev_del = prev_round.delta
            )

class Choice3(Page):
    form_model = 'player'
    form_fields = ['penny_side', 'time_of_move', 'move_in_beginning', 'time_out', 'simultaneous']

    @staticmethod
    def vars_for_template(player):
        B_eps = int(player.epsilon + C.B)
        return dict(
            B_eps=B_eps
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(player_id=player.id_in_group,
                    delta=player.delta,
                    epsilon=player.epsilon)

    @staticmethod
    def live_method(player: Player, data):
        if data['penny_side']:
            penny_side = True
        else:
            penny_side = False

        if player.group.first_sender_id == 0:
            player.group.first_sender_id = player.id_in_group
            first = True
        else:
            first = False
        return {1: {"type": "button", "penny_side": penny_side, "player": player.id_in_group, "first": first},
                2: {"type": "button", "penny_side": penny_side, "player": player.id_in_group, "first": first}}


    #before_next_page = set_payoffs


class WaitPage1(WaitPage):
    template_name = 'matching_pennies/WaitPage1.html'
    after_all_players_arrive = set_payoffs


class RoundSummary(Page):
    @staticmethod
    def vars_for_template(player):
        if player.penny_side:
            move = 'Heads'
        else:
            move = 'Tails'
        player_id = player.id_in_group
        op_id = 2**(2-player_id)
        op = player.group.get_player_by_id(op_id)
        op_time_out = op.time_out
        op_beginning = op.move_in_beginning
        if op.penny_side:
            op_move = 'Heads'
        else:
            op_move = 'Tails'

        if player.move_in_beginning:
            time = 0.00
        else:
            p_time = player.time_of_move
            op_time = op.time_of_move
            if op_beginning:
                if p_time <= 10000:
                    time = 0.00
                else:
                    time = p_time - 10000
            elif p_time < op_time:
                time = p_time - 5000
            else:
                if p_time - op_time <= 5000:
                    time = op_time - 5000
                else:
                    time = p_time - 10000
        if time < 0:
            time = 0

        return dict(
            move=move,
            op_move=op_move,
            time=time/1000,
            op_time_out=op_time_out
        )


class ResultsWaitPage(WaitPage):
    #after_all_players_arrive = set_payoffs
    wait_for_all_groups = True


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


page_sequence = [BlockStart,ResultsWaitPage,Choice3, WaitPage1, RoundSummary, ResultsWaitPage, ResultsSummary]
