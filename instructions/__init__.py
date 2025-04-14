from otree.api import *

doc = """
Matching pennies game
"""


class C(BaseConstants):
    NAME_IN_URL = 'instructions'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    IntroQ1 = models.IntegerField(label="I am supposed to stay quiet and focus on the experiment", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)  # for the instructions quiz
    IntroQ2 = models.IntegerField(label="The experiment is split into five blocks and each block consists of 15 rounds", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    IntroQ3 = models.IntegerField(label="In each round, I always interact with the same participant", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    
    Inst1Q1 = models.IntegerField(label="I can make my decision by clicking on the payoffs in the table.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    Inst1Q2 = models.IntegerField(label="What is the baseline payoff you can earn if you choose Tails and the other player chooses Heads?")  # for the instructions quiz
    Inst1Q3 = models.IntegerField(label="What is your baseline payoff if both choose Tails?")
    Inst1Q4 = models.IntegerField(label="Suppose, you learn that the other player chose Heads before you made your choice. What action choice will then maximize your payoff?", choices = [[1, 'Heads'], [0, 'Tails']], widget=widgets.RadioSelectHorizontal)

    Inst2Q1 = models.IntegerField(label="A round cannot end before the timer reaches zero.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)  # for the instructions quiz
    Inst2Q2 = models.IntegerField(label="If both players make a choice before the timer reaches zero, my actual payment is the baseline payoff times the payoff percentage shown when I made my decision", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    Inst2Q3 = models.IntegerField(label="When the timer reaches zero, the payoff percentage will also be zero.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    Inst2Q4 = models.IntegerField(label="If the other player chooses an action while your screen shows a payoff percentage of 50, you earn half of your baseline payoff by choosing an action within the next 5 seconds.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)

def IntroQ1_error_message(player, value):
    if value != 1:
        return 'The answer is not correct. Please read the information on this page carefully.'

def IntroQ2_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'
    
def IntroQ3_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'
    
def Inst1Q1_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'

def Inst1Q2_error_message(player, value):
    if value != 800:
        return 'The answer is not correct. Please read the information on this page carefully.'
    
def Inst1Q3_error_message(player, value):
    if value != 200:
        return 'The answer is not correct. Please read the information on this page carefully.'    
    
def Inst1Q4_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'   

def Inst2Q1_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'

def Inst2Q2_error_message(player, value):
    if value != 1:
        return 'The answer is not correct. Please read the information on this page carefully.'
    
def Inst2Q3_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'
    
def Inst2Q4_error_message(player, value):
    if value != 1:
        return 'The answer is not correct. Please read the information on this page carefully.'


# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['IntroQ1', 'IntroQ2', 'IntroQ3']
    
    @staticmethod
    def vars_for_template(player: Player):
        vars = dict(
            num_periods=player.session.config['periods_per_block'],
            tot_periods=4*player.session.config['periods_per_block']+3,
        )
        return(vars)
    

class Instructions1(Page):
    form_model = 'player'
    form_fields = ['Inst1Q1', 'Inst1Q2', 'Inst1Q3', 'Inst1Q4']

class Instructions2(Page):
    form_model = 'player'
    form_fields = ['Inst2Q1', 'Inst2Q2', 'Inst2Q3', 'Inst2Q4']








page_sequence = [Introduction, Instructions1, Instructions2]