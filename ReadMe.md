# 開發文件
---
###專題主題與簡介
--
英文單字查詢工具<br><br><br>
###小組分工
--
####李能安
* 投影片製作
* 申請 openAI api 金鑰

####林睿傳
* 開發文件
* 外觀設計

####郭思延
* 使用手冊
* 交互邏輯規劃

####楊景翔
* 介紹海報
* 後期測試

####董奕辰
* 專案報告人
* 時程規劃及成員協調

####譚培成
* 初期規劃
* 資料統整


<br><br><br>
###開發環境
--
IDE: PyCharm<br>
version: python 3.12

<br><br><br>
###系統開發流程
--
企劃發想<br>
初期規劃<br>
制定規格<br>
設計交互邏輯<br>
外觀設計<br>
程式開發<br>
功能驗收<br>
測試<br>
修正錯誤<br>
開發完成<br>


<br><br><br>
###程式設計主要技巧
--
外觀部分使用 tkinter 套件<br>

資料部分使用 MVVM 架構（MVVM（Model-View-ViewModel），將應用程式分為三個主要部分，以提高可維護性和可擴展性。<br>

* Model（模型）：負責管理應用程式的數據和商業邏輯。它與應用的資料來源互動，例如從 API 獲取數據，並將數據處理後提供給 ViewModel。<br>

* View（視圖）：指的是使用者介面，直接與使用者互動。View 顯示從 ViewModel 獲取的數據，並將使用者的操作事件傳遞給 ViewModel。<br>

* ViewModel（視圖模型）：位於 Model 和 View 之間。ViewModel 負責處理來自 Model 的數據並進行格式化，以便 View 能夠顯示。它也處理來自 View 的使用者輸入，並將相應的變更傳回 Model。ViewModel 通常透過資料綁定與 View 進行互動。<br>

view 和 viewModel 使用 callBack 來綁定資料變動事件


<br><br><br>
###原始碼重點解說
--
#### MainView.py & MyEntry.py: 
主要是外觀，使用 tkinter 套件繪製輸入欄位，查詢按鈕，查詢結果，歷史紀錄四個部分

#### OpenAiSentencesApi.py:
負責對 openAI 的接口，負責發送請求和解析資料

#### OpenAiSentencesApiResponseModel.py:
api 資料的 json response 的反序列化（Deserialization) 物件<br>
方便操作及取得資料

#### main.py:
程式執行入口

#### ApiKey.py:
存放 openAI 的金鑰

### 套件使用
--
`tkinter` 內建的 ＵＩ套件 不需安裝
`dataclass_wizard`: 解析 json 物件 <br>
`requests`: 請求 api<br>
其餘套件為相依套件

<br><br><br><br>
#使用手冊 
---
需有程式安裝、執行說明；程式功能介紹、操作說明。

### 安裝環境
mac: `brew install python-tk`<br>

### 安裝套件
`pip install -r requirements.txt`

### 執行
複製 APIKey.py 檔案到專案資料夾下面
放在 main.py 旁邊<br>
執行`python main.py`

### 程式功能介紹
查詢單字，給出中英文翻譯<br>
還有中英對照例句<br>
右側有查詢歷史紀錄<br>
點擊歷史紀錄可以查詢之前查過的單字

### 操作說明
<這裡請同學幫我補上 謝謝>











