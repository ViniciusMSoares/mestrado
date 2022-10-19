import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = "Mattermost"  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r"D:\vinis\Documents\Mestrado\acbot\errbot-mattermost-backend\data"
BOT_EXTRA_PLUGIN_DIR = r"D:\vinis\Documents\Mestrado\acbot\errbot-mattermost-backend\plugins"

BOT_LOG_FILE = r"D:\vinis\Documents\Mestrado\acbot\errbot-mattermost-backend\errbot.log"
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = (
    "@viniciussoares",
)  # Don't leave this as "@CHANGE_ME" if you connect your errbot to a chat system!!

import os
local_dir_path = os.path.dirname(__file__) 
BOT_DATA_DIR = os.path.join(local_dir_path, "data") 
BOT_EXTRA_PLUGIN_DIR = os.path.join(local_dir_path, "plugins")
BOT_EXTRA_BACKEND_DIR = os.path.join(local_dir_path, "..")

BOT_IDENTITY = {
  'team': 'main',
  'server': 'botconforto.cloud.mattermost.com',  # Grab this from your browser's URL field       
  'token': 'xs8ef6mohjd8pmamr4dka9ep8a',
 
  # Optional 
  'scheme': "https", 
  'port': 443,
  'timeout': 30
    }