from tkinter import Entry
import tkinter as tk
from tkinter.font import Font

class MyEntry(Entry):
    def __init__(self, parent, *args, **kwargs):
        # 初始化父類別
        super().__init__(parent, *args, **kwargs)
        font = Font(size=14)
        self.config(font=font)

