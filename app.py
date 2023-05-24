# 抓幸福集企頁 (圖片 / 文字)
# 目標 1：抓到頁面使用的宮格
# 目標 2：將抓到的宮格轉成一張粗略的 wireframe
import urllib.request as req
import bs4
import re

url = 'https://www.etmall.com.tw/Activity/GroupSale'

# 建立 request 物件，附加 request headers 的資訊
request = req.Request(url, headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
})

# 請求讀取
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 用 BeautifulSoup 解析網頁 HTML 結構
root = bs4.BeautifulSoup(data, "html.parser")
scriptTags = root.find_all('script')
scriptContent = str(scriptTags)

pattern = r"Title"
m1 = re.findall(pattern, scriptContent)

if m1:
    print("找到符合條件的字：")
    for match in m1:
        print(match)
else:
    print("未找到符合條件的字。")

# allPDLayout = root.select('div[class^="PD_layout layout_"]')
# colDivs = []

# for pdLayout in allPDLayout:
#     hasAttribute = pdLayout.has_attr('data-pd-col-pc')
#     deskColNum = pdLayout.get('data-pd-col-pc')
#     pdWrapper = pdLayout.find('ul', {'class': 'PD_wrapper'})
    
#     # 判斷屬性值是否為空值或非數字
#     if not hasAttribute or not deskColNum.isdigit():
#         print('data-pd-col-pc 的值有誤')
#     else:
#         # 將抓到的 deskColNum 塞進去 template，並塞進去 html
#         template = f'<div data-col="{deskColNum}"></div>'
#         colDivs.append(template)
        