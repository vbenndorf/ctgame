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

def IntroQ1_error_message(player, value):
    if value != 1:
        return 'The answer is not correct. Please read the information on this page carefully.'

def IntroQ2_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'
    
def IntroQ3_error_message(player, value):
    if value != 0:
        return 'The answer is not correct. Please read the information on this page carefully.'


# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['IntroQ1', 'IntroQ2', 'IntroQ3']
    
    @staticmethod
    def vars_for_template(player: Player):
        vars = dict(
            num_periods = player.session.config['periods_per_block'],
            tot_periods = 4*player.session.config['periods_per_block'],
        )
        return(vars)
    



class Instructions1(Page):
    pass


class Instructions2(Page):
    pass



class Quiz(Page):
    form_model = 'player'
    form_fields = ['Q1', 'Q2', 'Q3']




page_sequence = [Introduction, Instructions1, Instructions2, Quiz]
