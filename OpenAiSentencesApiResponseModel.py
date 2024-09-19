from dataclasses import dataclass
from dataclasses import fields
from typing import List
from dataclass_wizard import JSONWizard

# api 回應物件
@dataclass
class Sentence:
    english: str
    chinese: str

@dataclass
class Translate(JSONWizard):
    english_explain: str
    chinese_explain: str
    sentences: List[Sentence]

@dataclass
class ResponseModel(JSONWizard):
    query_word: str
    translates: List[Translate]
