import requests
import ApiKey

# api 請求物件
class OpenAiSentencesApi:
    _demo_response = {
        "query_word": "result",
        "translates": [
            {
                "english_explain": "something that happens or exists because of something else",
                "chinese_explain": "結果；後果",
                "sentences": [
                    {
                        "english": "The road has been widened, but the result is just more traffic.",
                        "chinese": "道路被拓寬，但結果車流量卻更大了。"
                    },
                    {
                        "english": "His broken leg is the direct result of his own carelessness.",
                        "chinese": "他自己的粗心大意直接導致他摔斷了腿。"
                    },
                    {
                        "english": "I tried to repaint the kitchen walls with disastrous results.",
                        "chinese": "我試圖重新粉刷一下廚房的牆，結果卻弄得一塌糊塗。"
                    }
                ]
            },
            {
                "english_explain": "a good or pleasing effect",
                "chinese_explain": "成效；成果",
                "sentences": [
                    {
                        "english": "We've spent a lot of money on advertising and we're beginning to see the results.",
                        "chinese": "我們已經花了很多錢來做廣告，我們的付出現在開始見成效了。"
                    },
                    {
                        "english": "She's an excellent coach who knows how to get results.",
                        "chinese": "她是個優秀的教練，知道如何取得好的訓練效果。"
                    },
                ]
            }
        ]
    }
    _requestRule = f"你是英漢字典我查單字的時候用以下 json 格式回我: {_demo_response}"
    _model = "gpt-3.5-turbo-1106"
    _response_format = {"type": "json_object"}
    _max_tokens = 1000
    _url = "https://api.openai.com/v1/chat/completions"

    def send_request(self, query) -> dict:
        print(f"send query {query}")
        parameters = self._assemble_request_parameters(query=query)
        headers = self._get_request_header()
        response = requests.post(self._url, headers=headers, json=parameters, verify=False)  # 使用 json 參數傳送資料
        print("status code =", response.status_code)
        return response.json()

    def _assemble_request_parameters(self, query: str) -> dict:
        parameters = {
            "model": self._model,
            "response_format": self._response_format,
            "max_tokens": self._max_tokens,
            "messages": [
                {
                    "role": "system",
                    "content": self._requestRule
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
        return parameters

    @staticmethod
    def _get_request_header() -> dict:
        key = ApiKey.ApiKey
        bearer = f"Bearer {key}"
        return {
            "Content-type": "application/json",
            "Authorization": bearer
        }
