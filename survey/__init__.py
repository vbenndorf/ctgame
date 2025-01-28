from otree.api import *


author = 'Volker Benndorf'
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pay_survey = models.CurrencyField()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=1, max=199, label="What is your age?")
    gender = models.StringField(
        choices=['Female', 'Male', 'Non-binary/Other'],
        widget=widgets.RadioSelect,
        label="What is your gender?",
    )
    problems = models.LongStringField(blank=True)
    responsiveness = models.IntegerField(
        blank=True, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal
    )
    understanding_descriptions = models.IntegerField(
        blank=True, choices=[1, 2, 3, 4, 5, 6, 7], widget=widgets.RadioSelectHorizontal
    )


# FUNCTIONS
# PAGES
class ShorterSurvey(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'gender',
        'understanding_descriptions',
        'responsiveness',
        'problems',
    ]



page_sequence = [ShorterSurvey]
