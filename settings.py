from os import environ


SESSION_CONFIGS = [
    dict(
        name='info_only',
        display_name="Only Instructions",
        app_sequence=['informed_consent', 'instructions'],
        num_demo_participants=1,
        periods_per_block=12,
        participation_fee = 6,
    ),
    dict(
        name='matching_pennies',
        display_name="Matching Pennies game only",
        app_sequence=['matching_pennies'],
        num_demo_participants=2,
        periods_per_block=1,
        real_world_currency_per_point=0.0007,
        participation_fee = 6,
        expShortName="TestExp", # Replace with your values
        expId=0000000000, # Replace with your values
        sessId=0000000000, # Replace with your values
    ),
    dict(
            name='matching_pennies_static',
            display_name="Matching Pennies (static) game only",
            app_sequence=['matching_pennies_static'],
            num_demo_participants=2,
            periods_per_block=1,
            real_world_currency_per_point=0.0007,
            participation_fee = 6,
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
        app_sequence=['informed_consent', 'instructions','matching_pennies','survey', 'payment'],
        num_demo_participants=2,
        periods_per_block=12,
        real_world_currency_per_point=0.0007,
        participation_fee = 6,
        expShortName="CTG",
        expId=28, # Replace with your values
        sessId=235, # Replace with your values
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
        name='DICELAB',
        display_name='DICELab',
        participant_label_file='_rooms/dicelab.txt',
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
