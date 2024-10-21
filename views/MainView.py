import tkinter as tk
from ViewModel import ViewModel
from views.MyEntry import MyEntry
from tkinter.font import Font
import threading

class MainView:
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
        self._view_model.bind_to(self._update_ui)

    # === UI ===
    def _setup_ui(self):
        self._setup_main_view()
        self._setup_entry()
        self._setup_button()
        self._setup_text()
        self._setup_history()

    def _setup_main_view(self):
        self._main_view = tk.Tk()
        self._main_view.title("final_exam_report")
        self._main_view.geometry("600x400")
        self._main_view.grid_columnconfigure(0, weight=1)  # 使第一列擴展
        self._main_view.grid_columnconfigure(1, weight=0)  # 使第二列不擴展，保持固定寬度
        self._main_view.grid_rowconfigure(1, weight=1)

    # 輸入欄位
    def _setup_entry(self):
        self._entry = MyEntry(self._main_view)
        self._entry.grid(row=0, column=0, padx=5, pady=5, columnspan=4, sticky="nsew")

    # 查詢按鈕
    def _setup_button(self):
        self._button = tk.Button(self._main_view)
        self._button.config(text="查詢", command=self._tap_button)
        self._button.grid(row=0, column=4, padx=(0, 5), pady=5, columnspan=2, sticky="nsew")

    # 查詢結果
    def _setup_text(self):
        self._text = tk.Text(self._main_view)
        font = Font(size=15)
        self._text.config(state=tk.DISABLED, font=font)
        self._text.grid(row=1, column=0, padx=5, pady=(0, 5), rowspan=3, columnspan=4, sticky="nsew")

    # 歷史紀錄
    def _setup_history(self):
        self._history = tk.Listbox(self._main_view)
        font = Font(size=15)
        self._history.config(width=15, font=font)
        self._history.grid(row=1, column=4, padx=(2,8), pady=(2,8), rowspan=3, columnspan=2, sticky="nsew")
        self._history.bind('<<ListboxSelect>>', self._on_select)

    # === logic ===
    # 點擊查詢按鈕
    def _tap_button(self):
        self._display_querying()
        text = self._entry.get()
        threading.Thread(target=self._view_model.query, args=(text,)).start()

    def _display_querying(self):
        self._text.config(state=tk.NORMAL)
        self._text.delete(1.0, tk.END)
        self._text.insert(tk.END, "查詢中...")
        print("display")
        self._text.config(state=tk.DISABLED)
        self._main_view.update_idletasks()

    def _update_ui(self):
        self._main_view.after(0, self._update_history)
        self._main_view.after(0, self._update_text)

    # 更新歷史紀錄
    def _update_history(self):
        self._history.delete(0, tk.END)
        for word in self._view_model.query_history:
            self._history.insert(tk.END, word)

    # 更新查詢
    def _update_text(self):
        self._text.config(state=tk.NORMAL)
        self._text.delete(1.0, tk.END)
        print("type:", type(self._view_model.data))
        if self._view_model.data is None:
            self._text.insert(tk.END, "資料異常")
            return
        data = self._view_model.data
        self._text.insert(tk.END, data.query_word + "\n\n")
        for translate in data.translates:
            self._text.insert(tk.END, translate.chinese_explain + "\n")
            self._text.insert(tk.END, "===================" + "\n\n")
            self._text.insert(tk.END, translate.english_explain + "\n\n")
            for sentence in translate.sentences:
                self._text.insert(tk.END, sentence.english + "\n")
                self._text.insert(tk.END, sentence.chinese + "\n\n")
            self._text.insert(tk.END, "\n\n")
        self._text.config(state=tk.DISABLED)

    def _on_select(self, event):
        # 取得 Listbox 中的選定項目
        widget = event.widget
        selection = widget.curselection()
        if selection:
            index = selection[0]
            value = widget.get(index)
            self._display_querying()
            threading.Thread(target=self._view_model.query, args=(value,)).start()