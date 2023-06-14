import urllib.request as req
# 用 BeautifulSoup 解析網頁 HTML 結構，不解析 json
# import bs4
import pygsheets
import json
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

auth_file = "credentials.json"
gc = pygsheets.authorize(service_file = auth_file)

# setting sheet
sheet_url = "https://docs.google.com/spreadsheets/d/13Tl9G1kHYdPiRl0JBekaVnqgoUaxtbTb-o4hh01LWok/edit#gid=0" 
sheet = gc.open_by_url(sheet_url)

#選取by名稱
sheet_sheet01 = sheet.worksheet_by_title("Sheet01")

url = 'https://24h.pchome.com.tw/onsale/v5/data/data.json'

# 建立 request 物件，附加 request headers 的資訊
request = req.Request(url, headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})

# 請求讀取
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 把原始資料解析成字典/列表
data = json.loads(data)
block_1_products = data["OnsaleJson"][0]["Nodes"]

block_1_title = []
block_1_desc = []

# 在 python 裡遍歷 list 不會拿到 1,2,3，而是第一個 dict，第二個 dict...
for key in block_1_products:
    block_1_title.append(key["Img"]["Title"])
    block_1_desc.append(key["Link"]["Text1"])
    # sheet_sheet01.update_values('A3', [['3'],['4'],['5'],['6']]) # 直的

# 创建 FormatBuilder 对象并设置字体样式
format_builder = pygsheets.FormatBuilder()
format_builder.set_font_bold(True)

sheet_sheet01.update_value('A1', "品名")
sheet_sheet01.update_value('B1', "品名描述")
sheet_sheet01.update_value('C1', "價格")
# sheet_sheet01.update_values('B1', [block_1_title])
# sheet_sheet01.update_values('B2', [block_1_desc])
# sheet_sheet01.update_values('A3', [['3'],['4'],['5'],['6']]) # 直的


# def gsheet(self, stocks):
#     # 由於Google擁有許多的雲端服務，所以需要先定義存取的Scope(範圍)，也就是Google Sheet(試算表)
#     scopes = ["https://spreadsheets.google.com/feeds"]

#     # 讀取Google Sheets API憑證(credentials.json)，並且傳入所要存取的Scope(範圍)，來進行驗證
#     credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scopes)

#     # 進行Google Sheets API的授權
#     client = gspread.authorize(credentials)

#     # 傳入Google Sheet(試算表)的Key(金鑰)
#     sheet = client.open_by_key("13Tl9G1kHYdPiRl0JBekaVnqgoUaxtbTb-o4hh01LWok").sheet1

#     response = req.get("https://tw.stock.yahoo.com/q/q?s=2451")
    
#     data = bs4.BeautifulSoup(response.text, "lxml")

#     tables = data.find_all('table')[2]
#     ths = tables.find_all('th')[0:11]
#     titles = ('資料日期',) + tuple(th.getText() for th in ths)
#     sheet.insert_row(titles, 1)
    
#     # 將資料寫入Google Sheet
#     for stock in stocks:
#         sheet.append_row(stock)