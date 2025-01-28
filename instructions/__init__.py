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
    IntroQ2 = models.IntegerField(label="The experiment is split into five blocks and each block consists of 15 periods", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    IntroQ3 = models.IntegerField(label="I always interact with the same participant in each period", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    
    Inst1Q1 = models.IntegerField(label="I can make my decision by clicking on the payoffs in the matrix.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    Inst1Q2 = models.IntegerField(label="Consider the game in the screenshot. What is the maximum payoff you can earn if you choose Tails and the other player chooses Heads?")  # for the instructions quiz
    Inst1Q3 = models.IntegerField(label="And what are your maximum payoffs if both of you choose Tails?")

    Inst2Q1 = models.IntegerField(label="A period cannot end before the timer reaches zero.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)  # for the instructions quiz
    Inst2Q2 = models.IntegerField(label="My actual payment is the maximum payment times the payoff percentage shown when I made my decision", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)
    Inst2Q3 = models.IntegerField(label="When the timer reaches zero, the payoff percentage will also be zero.", choices = [[1, 'True'], [0, 'False']], widget=widgets.RadioSelectHorizontal)

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
    if value != 240:
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
    form_fields = ['Inst1Q1', 'Inst1Q2', 'Inst1Q3']

class Instructions2(Page):
    form_model = 'player'
    form_fields = ['Inst2Q1', 'Inst2Q2', 'Inst2Q3']








page_sequence = [Introduction, Instructions1, Instructions2]