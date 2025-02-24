
import threading
from bot import Bot  # Adjust based on your actual bot class

def run_bot():
    bot = Bot()
    bot.run()  # Replace with the appropriate method

thread = threading.Thread(target=run_bot, daemon=True)
thread.start()
