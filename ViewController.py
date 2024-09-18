import tkinter as tk
from ViewModel import ViewModel
from views.MyEntry import MyEntry

class ViewController:
    _view_model: ViewModel
    _main_view: tk.Tk
    _entry: tk.Entry
    _button: tk.Button
    _text: tk.Text
    _history: tk.Listbox

    def __init__(self):
        self._setup_ui()

    def run(self):
        self._main_view.mainloop()

    def bind(self, view_model: ViewModel):
        self._view_model = view_model

    # UI
    def _setup_ui(self):
        self._setup_main_view()
        self._setup_entry()
        self._setup_button()
        self._setup_text()
        self._setup_history()

    def _setup_main_view(self):
        self._main_view = tk.Tk()
        self._main_view.geometry("600x400")
        self._main_view.grid_columnconfigure(0, weight=1)  # 使第一列擴展
        self._main_view.grid_columnconfigure(1, weight=0)  # 使第二列不擴展，保持固定寬度
        self._main_view.grid_rowconfigure(1, weight=1)

    def _setup_entry(self):
        self._entry = MyEntry(self._main_view)
        self._entry.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="nsew")

    def _setup_button(self):
        self._button = tk.Button(self._main_view)
        self._button.config(text="查詢", command=self._tap_button)
        self._button.grid(row=0, column=4, padx=(0, 5), pady=5, columnspan=2, sticky="nsew")

    def _setup_text(self):
        self._text = tk.Text(self._main_view)
        self._text.config(state=tk.DISABLED)
        self._text.grid(row=1, column=0, padx=5, pady=(0, 5), rowspan=3, columnspan=4, sticky="nsew")

    def _setup_history(self):
        self._history = tk.Listbox(self._main_view)
        self._history.config(width=15)
        self._history.grid(row=1, column=4, padx=(2,8), pady=(2,8), rowspan=3, columnspan=2, sticky="nsew")
        self._history.config(background="white")

    # logic
    def _tap_button(self):
        text = self._entry.get()
        self._view_model.query(text)





