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
block_1_final_price = []
block_1_marketing_price = []
block_1_url = []

# 在 python 裡遍歷 list 不會拿到 1,2,3，而是第一個 dict，第二個 dict...
for key in block_1_products:
    block_1_title.append([key["Img"]["Title"]])
    block_1_desc.append([key["Link"]["Text1"]])
    block_1_final_price.append([key["Link"]["Text2"]])
    block_1_marketing_price.append([key["Link"]["Text6"]])
    block_1_url.append([key["Link"]["Url"]])

data = ["商品名稱", "商品描述", "商品特價", "商品原價", "商品連結"]
columns = ['A', 'B', 'C', 'D', 'E']

for i in range(len(data)):
    cell = columns[i] + '1'
    sheet_sheet01.update_value(cell, data[i])

sheet_sheet01.update_values('A2', block_1_title)
sheet_sheet01.update_values('B2', block_1_desc)
sheet_sheet01.update_values('C2', block_1_final_price)
sheet_sheet01.update_values('D2', block_1_marketing_price)
sheet_sheet01.update_values('E2', block_1_url)