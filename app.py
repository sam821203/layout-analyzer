# 抓 momo 活動頁面
# 目標 1：抓到頁面使用的宮格
# 目標 2：將抓到的宮格轉成一張粗略的 wireframe
import urllib.request as req
import bs4
import os
import shutil

from flask import Flask, render_template
# from openpyxl import Workbook
# from openpyxl.styles import Alignment, PatternFill
# from openpyxl.utils import get_column_letter

# 建立應用程式的物件
# __name__ 代表目前執行的模組
# render 上的 gunicorn app:app，app:app 代表模組名稱:變數名稱
app = Flask(__name__)

# 抓取 momo 活動頁網頁原始碼
url = 'https://www.momoshop.com.tw/edm/cmmedm.jsp?lpn=O3XZkrInHiH&n=1'

# 建立 request 物件，附加 request headers 的資訊
request = req.Request(url, headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 解析網頁 HTML 結構
root = bs4.BeautifulSoup(data, 'html.parser')

# 找到活動頁名稱
spName = root.title.string

allPDLayout = root.select('div[class^="PD_layout layout_"]')
colDivs = []

for pdLayout in allPDLayout:
    hasAttribute = pdLayout.has_attr('data-pd-col-pc')
    deskColNum = pdLayout.get('data-pd-col-pc')
    pdWrapper = pdLayout.find('ul', {'class': 'PD_wrapper'})
    
    # 判斷屬性值是否為空值或非數字
    if not hasAttribute or not deskColNum.isdigit():
        print('data-pd-col-pc 的值有誤')
    else:
        # 將抓到的 deskColNum 塞進去 template，並塞進去 html
        template = f'<div data-col="{deskColNum}"></div>'
        colDivs.append(template)
        
# 使用 join() 方法將列表中的字串合併為一個完整的 HTML 字串
html = '\n'.join(colDivs)

# 先刪除已存在的 index.html
if os.path.exists('index.html'):
    os.remove('index.html')

with open('index.html', 'w') as f:
    f.write(html)

# 創建 templates 資料夾
def create_templates_dir(html):
  if not os.path.exists('templates'):
    os.mkdir('templates')
  # 移動 index.html 到 templates 資料夾中
  shutil.move('index.html', 'templates/index.html')
  
create_templates_dir(html)

# 函式的裝飾(Decorator): 以函式為基礎，提供附加的功能
# "/" 代表網站的根目錄
@app.route("/")
def home():
  # 這裡會去尋找 Flask 應用程式的 templates 資料夾下的 index.html 檔案
  return render_template("index.html")

# 如果以 app.py 主程式執行
if __name__ == "__main__":
  app.run() # 立刻啟動伺服器