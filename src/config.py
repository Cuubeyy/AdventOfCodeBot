import os
import pytz
import logging

YEAR = 2025
GITHUB_LINK = "https://github.com/Cuubeyy/AdventOfCodeBot"
SESSION_COOKIE = os.environ['SESSION_COOKIE']
LEADERBOARD = os.environ['LEADERBOARD_ID']
URL = f"https://adventofcode.com/{YEAR}/leaderboard/private/view/{LEADERBOARD}.json"
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
COMMAND_PREFIX = '*'
UTC = pytz.timezone('UTC')
EST = pytz.timezone('Europe/Berlin')

logging.basicConfig(level=logging.DEBUG)
