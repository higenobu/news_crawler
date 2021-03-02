import requests
import json
from bs4 import BeautifulSoup

#----------------------パラメータ設定----------------------
max_text = 50   #とりたいニュース数
#----------------------------------------------------------

#-------------------------奈良新聞-------------------------
text_count = 0    #とったニュースの数
text = []    #ニュースのタイトルとリンク
page_count = 6    #奈良新聞ホームページリンクのページカウント(ページ5までので、6に設定します)
src = "https://www.nara-np.co.jp/news/?p="    #奈良新聞のURL(ページ番号抜き)

for i in range(1, page_count):    #奈良新聞のホームページのカウント(ページ1から5)
    response = requests.get(src + str(i))    #奈良新聞のホームページに入る
    soup = BeautifulSoup(response.text, "html.parser")    #HTMLコードをとる
    titles = soup.find_all(class_ = "item", limit = 10)    #1ページのニュースが10個しかないので、10個とります
    for title in titles:
        text.append(title.select_one("h3").getText())    #ニュースのタイトルをとる
        text.append(title.select_one("a").get("href"))   　#ニュースのリンクをとる
        text_count += 1
        print("奈良新聞の" + str(text_count) + "番目のニュース取れまhした")
        if text_count >= max_text:    #50個新聞とったらループを抜ける
            break

#--------------------JSONファイルに出力--------------------
with open("nara.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("奈良新聞のJSONファイル作りました！！！")    #終了メッセージ
#----------------------------------------------------------


#-------------------------京都新聞-------------------------
i = 0    #カウンターのリセット
text_count = 0
text = []
page_count = 4  #京都新聞ホームページリンクのページカウント(ページ3までので、4に設定します)
src = "https://www.kyoto-np.co.jp/subcategory/%E4%BA%AC%E9%83%BD%E5%BA%9C?page="    #京都新聞のURL(ページ番号抜き)

print(i)
for i in range(1, page_count):
    response = requests.get(src + str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("article", limit = 20)
    for title in titles:
        text.append(title.select_one("h3").getText())
        text.append("https://www.kyoto-np.co.jp" + title.select_one("a").get("href"))
        text.append(title.select_one("time").getText())    #ニュースの時間をとる
        text_count += 1
        print("京都新聞の" + str(text_count) + "番目のニュース取れました")
        if text_count >= max_text:
            break

#--------------------JSONファイルに出力--------------------
with open("kyoto.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("京都新聞のJSONファイル作りました！！！")
#----------------------------------------------------------