import threading

class GlobalState:
    def __init__(self):
        self.is_running = False
        self.lock = threading.Lock()

    def set_running(self, value):
        with self.lock:
            self.is_running = value

    def get_running(self):
        with self.lock:
            return self.is_running

# Глобальний об'єкт стану
global_state = GlobalState()