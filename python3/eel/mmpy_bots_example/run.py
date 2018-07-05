import eel
from bot.mm_bot import MMBot

# Give folder containing web files
eel.init('web')

# Set up bot, and runs as subprocess
bot = MMBot()
eel.spawn(bot.run)

# Start
eel.start('main.html', size=(300, 600))
