# 抓幸福集企頁 (圖片 / 文字)
# 目標 1：抓到頁面使用的宮格
# 目標 2：將抓到的宮格轉成一張粗略的 wireframe
import urllib.request as req
import bs4
import re

url = 'https://www.etmall.com.tw/Activity/GroupSale'

# window: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
# mac: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36

# 建立 request 物件，附加 request headers 的資訊
request = req.Request(url, headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
})

# 請求讀取
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

# 用 BeautifulSoup 解析網頁 HTML 結構
root = bs4.BeautifulSoup(data, "html.parser")
scriptTags = root.find_all('script')
# scriptContent = str(scriptTags)

print(scriptTags)
# test = "title: '日本墨之君北海道利尻昆布補染液-黑.咖啡(10ml/支X3支)'"
# pattern =  r"title:\s*'([^']*)'"
# pattern = r"groupSaleProductList:\s*\[(.*?)\]"
# m1 = re.search(pattern, scriptContent, re.DOTALL)

# print(m1)
# if m1:
#     json_data = m1.group(1)
#     # 移除單引號內的反斜線
#     json_data = re.sub(r"\\'", "'", json_data)
#     print(json_data)
# else:
#     print("未找到 groupSaleProductList 資料")