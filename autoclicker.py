import time
import threading
import pyautogui
import keyboard

class AutoClicker:
    def __init__(self, interval=0.1, button="left"):
        self.interval = interval
        self.button = button
        self.running = False
        self.thread = None

    def _click_loop(self):
        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.interval)

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._click_loop, daemon=True)
        self.thread.start()
        print("Auto clicker started. Press F6 to stop.")

    def stop(self):
        self.running = False
        print("Auto clicker stopped.")

    def toggle(self):
        if self.running:
            self.stop()
        else:
            self.start()


def main():
    clicker = AutoClicker(interval=0.10)

    keyboard.add_hotkey("f6", clicker.toggle)
    keyboard.add_hotkey("esc", lambda: (clicker.stop(), exit()))

    print("Auto Clicker")
    print("F6: start/stop")
    print("Esc: exit")
    print("Move mouse to the click target before pressing F6.")

    while True:
        time.sleep(0.1)


if __name__ == "__main__":
    main()
