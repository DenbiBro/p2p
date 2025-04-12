import tkinter as tk
from threading import Thread
from global_state import global_state
from update_symbols import update_symbols
from CONSTANTS import SYMBOLS
from logger import logger
import time

class ArbitrageGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Arbitrage Monitor")

        # Список валютних пар
        self.symbols_label = tk.Label(root, text="Валютні пари для арбітражу:")
        self.symbols_label.pack()

        self.symbols_list = tk.Listbox(root, height=15, width=50)
        self.symbols_list.pack()

        # Кнопки керування
        self.update_button = tk.Button(root, text="Оновити пари", command=self.update_pairs)
        self.update_button.pack()

        self.start_button = tk.Button(root, text="Запустити", command=self.start_program)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Зупинити", command=self.stop_program, state=tk.DISABLED)
        self.stop_button.pack()

        # Статус
        self.status_label = tk.Label(root, text="Статус: Зупинено", fg="red")
        self.status_label.pack()

    def update_pairs(self):
        try:
            updated_symbols = update_symbols()
            self.symbols_list.delete(0, tk.END)
            for symbol in updated_symbols:
                self.symbols_list.insert(tk.END, symbol)
            logger.info("Список валютних пар оновлено успішно")
        except Exception as e:
            logger.error(f"Помилка при оновленні пар: {e}")
            self.status_label.config(text="Помилка при оновленні пар", fg="red")

    def start_program(self):
        if not global_state.get_running():
            global_state.set_running(True)
            self.status_label.config(text="Статус: Запущено", fg="green")
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            Thread(target=self.run_logic).start()
            logger.info("Програма запущена")

    def stop_program(self):
        if global_state.get_running():
            global_state.set_running(False)
            self.status_label.config(text="Статус: Зупинено", fg="red")
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            logger.info("Програма зупинена")

    def run_logic(self):
        try:
            while global_state.get_running():
                logger.info("Основна логіка працює...")
                time.sleep(5)
        except Exception as e:
            logger.error(f"Помилка в основній логіці: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ArbitrageGUI(root)
    root.mainloop()