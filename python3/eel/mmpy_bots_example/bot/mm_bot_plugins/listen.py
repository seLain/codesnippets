# -*- coding: utf-8 -*-

import re, json, inspect
import requests
from mattermost_bot.bot import listen_to
from mattermost_bot.bot import respond_to
from mattermost_bot.utils import allow_only_direct_message

import eel

@respond_to('.*', re.IGNORECASE)
def respond_to(message):
    eel.js_update_message(message.get_username(), message.get_message())