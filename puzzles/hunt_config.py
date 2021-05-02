import datetime
from django.conf import settings
from django.utils import timezone

# included in various templates. NOTE, sometimes appears with a "the" before
# it, maybe check those are what you want.
HUNT_TITLE = 'Misremembered Puzzle Hunt'

# included in various templates and displayed on the static site
HUNT_ORGANIZERS = 'Misremembered Apple'

# included in various templates and set as reply-to for automatic emails
CONTACT_EMAIL = 'misremembered@misremembered.pythonanywhere.com'

# the sender from which automatic emails are sent; your mail sending service
# might require you set this to something (check settings/base.py to put your
# actual mail sending service credentials)
MESSAGING_SENDER_EMAIL = 'no-reply@misremembered.pythonanywhere.com'

# Change this to True to reveal the story page to everyone.
STORY_PAGE_VISIBLE = False
# Change this to True if any errata are added to errata.html.
ERRATA_PAGE_VISIBLE = False
# Change this to True when the wrapup exists.
WRAPUP_PAGE_VISIBLE = False
# Change this to True to start showing post-solve surveys to teams.
SURVEYS_AVAILABLE = False

ARCHIVE_PAGE_VISIBLE = False

HUNT_START_TIME = timezone.make_aware(datetime.datetime(
    year=2021,
    month=5,
    day=1,
    hour=18,
    minute=0,
))

HUNT_END_TIME = timezone.make_aware(datetime.datetime(
    year=2021,
    month=5,
    day=31,
    hour=0,
    minute=0,
))

HUNT_CLOSE_TIME = timezone.make_aware(datetime.datetime(
    year=2021,
    month=5,
    day=31,
    hour=0,
    minute=0,
))

MAX_GUESSES_PER_PUZZLE = 20
MAX_MEMBERS_PER_TEAM = 10

HINTS_ENABLED = True
HINTS_PER_DAY = 2
DAYS_BEFORE_HINTS = 3

# reasonable settings are datetime.timedelta(days=1), True; set to None, False
# to let teams get hints right away after signing up in the middle of the hunt;
# probably useful to try out the hint interface
TEAM_AGE_BEFORE_HINTS = datetime.timedelta(days=1)
CAP_HINTS_BY_TEAM_AGE = True

FREE_ANSWERS_ENABLED = False
DAYS_BEFORE_FREE_ANSWERS = 6
CAP_FREE_ANSWERS_BY_TEAM_AGE = True
# Free answers are given out each day after helpers.DAYS_BEFORE_FREE_ANSWERS.
FREE_ANSWERS_PER_DAY = [1, 2, 2]

# DEEP value used to indicate that you can see everything, e.g. the hunt is over.
DEEP_MAX = float('inf')

# These two slugs are used in a couple places to determine teams' progress
# through the major milestones of the hunt (e.g. to determine how much story
# they can view) and to classify puzzles as intro-round or not. They won't make
# sense for every hunt.

# Slug for the intro meta.
INTRO_META_SLUG = 'intro-meta'
# Slug for the metameta.
META_META_SLUG = 'meta-meta'
