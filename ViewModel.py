from os import error

from OpenAiSentencesApi import OpenAiSentencesApi
from OpenAiSentencesApiResponseModel import *
import json

class ViewModel:
    _callbacks: list[callable] = []
    data: ResponseModel | None = None
    query_history: list[str] = []

    def bind_to(self, callback: callable):
        """將視圖的回調函數綁定到模型"""
        self._callbacks.append(callback)

    def set_data(self, new_data: ResponseModel | None):
        """當數據更改時通知所有回調函數"""
        self.data = new_data

        if new_data is None:
            return
        if new_data.query_word in self.query_history:
            self.query_history.remove(new_data.query_word)
        self.query_history.insert(0, new_data.query_word)
        # 保持記憶 10 筆資料
        self.query_history = self.query_history[:10]

    def notify_callback(self):
        for callback in self._callbacks:
            callback()

    def query(self, vocabulary: str):
        api_object = OpenAiSentencesApi()
        response = api_object.send_request(query=vocabulary)
        content = response["choices"][0]["message"]["content"]
        self.set_data(new_data=None)
        if content is None:
            self.set_data(new_data=None)
            self.notify_callback()
            return
        try:
            obj = ResponseModel.from_dict(json.loads(content))
            self.set_data(new_data=obj)
            self.notify_callback()
        except Exception as e:
            print(e)
            print(content)
            self.set_data(new_data=None)
            self.notify_callback()
