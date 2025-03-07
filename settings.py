from os import environ


SESSION_CONFIGS = [
    dict(
        name='info_only',
        display_name="Only Instructions",
        app_sequence=['nopay','informed_consent', 'instructions'],
        num_demo_participants=1,
        periods_per_block=10,
    ),
    dict(
        name='matching_pennies',
        display_name="Matching Pennies game only",
        app_sequence=['matching_pennies'],
        num_demo_participants=2,
        periods_per_block=10,
        real_world_currency_per_point=0.0005,
    ),
    dict(
            name='matching_pennies_static',
            display_name="Matching Pennies (static) game only",
            app_sequence=['matching_pennies_static'],
            num_demo_participants=2,
            periods_per_block=10,
            real_world_currency_per_point=0.0005,
        ),
    dict(
        name='survey',
        display_name='Survey',
        app_sequence=['survey'],
        num_demo_participants=1,
    ),
    dict(
        name='experiment',
        display_name="Complete experiment",
        app_sequence=['nopay','informed_consent', 'instructions','matching_pennies','survey'],
        num_demo_participants=2,
        periods_per_block=10,
        real_world_currency_per_point=0.0005,
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['treatments']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '8237229297659'

INSTALLED_APPS = ['otree']
