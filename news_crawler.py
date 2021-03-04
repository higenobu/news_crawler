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
        text.append("https://www.nara-np.co.jp/news/" + title.select_one("a").get("href"))    #ニュースのリンクをとる
        text_count += 1
        print("奈良新聞の" + str(text_count) + "番目のニュース取れました")
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
        #text.append(title.select_one("time").getText())    #ニュースの時間をとる
        text_count += 1
        print("京都新聞の" + str(text_count) + "番目のニュース取れました")
        if text_count >= max_text:
            break

#--------------------JSONファイルに出力--------------------
with open("kyoto.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("京都新聞のJSONファイル作りました！！！")
#----------------------------------------------------------


#-------------------------中日新聞-------------------------
i = 0    #カウンターのリセット
text_count = 0
text = []
page_count = 4  #中日新聞ホームページリンクのページカウント(ページ3までので、4に設定します)
src = "https://www.chunichi.co.jp/local/shiga/"    #中日新聞(滋賀)のURL(ページ番号抜き)

print(i)
for i in range(1, page_count):
    response = requests.get(src + str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all(class_ = "detail-ttl", limit = 20)
    for title in titles:
        text.append(title.select_one("a").getText())
        text.append("https://www.chunichi.co.jp" + title.select_one("a").get("href"))
        text_count += 1
        print("中日新聞滋賀地方の" + str(text_count) + "番目のニュース取れました")
        if text_count >= max_text:
            break

#--------------------JSONファイルに出力--------------------
with open("shiga.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("中日新聞滋賀地方のJSONファイル作りました！！！")
#----------------------------------------------------------


#-----------------------わかやま新報-----------------------
i = 0    #カウンターのリセット
text_count = 0
text = []
page_count = 6  #わかやま新報ホームページリンクのページカウント(ページ5までので、6に設定します)
src = "https://www.wakayamashimpo.co.jp/category/news/page/"    #わかやま新報のURL(ページ番号抜き)

print(i)
for i in range(1, page_count):
    response = requests.get(src + str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all(class_ = "post_title icon_list_blue", limit = 10)
    for title in titles:
        text.append(title.select_one("a").getText())
        text.append(title.select_one("a").get("href"))
        text_count += 1
        print("わかやま新報の" + str(text_count) + "番目のニュース取れました")
        if text_count >= max_text:
            break

#--------------------JSONファイルに出力--------------------
with open("wakayama.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("わかやま新報のJSONファイル作りました！！！")
#----------------------------------------------------------


#--------------------日本経済新聞(大阪)--------------------
i = 0    #カウンターのリセット
text_count = 0
text = []
src = "https://www.nikkei.com/local/osaka/?bn="    #日本経済新聞(大阪)のURL(ページ番号抜き)

print(i)
for i in [1, 21, 41]:
    response = requests.get(src + str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all(class_ = "m-miM09_title", limit = 20)
    for title in titles:
        text.append(title.select_one("span").getText())
        text.append("https://www.nikkei.com/" + title.select_one("a").get("href"))
        text_count += 1
        print("日本経済新聞(大阪)の" + str(text_count) + "番目のニュース取れました")
        if text_count >= max_text:
            break

#--------------------JSONファイルに出力--------------------
with open("osaka.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("日本経済新聞(大阪)のJSONファイル作りました！！！")
#----------------------------------------------------------


#--------------------日本経済新聞(兵庫)--------------------
i = 0    #カウンターのリセット
text_count = 0
text = []
src = "https://www.nikkei.com/local/hyogo/?bn="    #日本経済新聞(大阪)のURL(ページ番号抜き)

print(i)
for i in [1, 21, 41]:
    response = requests.get(src + str(i))
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all(class_ = "m-miM09_title", limit = 20)
    for title in titles:
        text.append(title.select_one("span").getText())
        text.append("https://www.nikkei.com/" + title.select_one("a").get("href"))
        text_count += 1
        print("日本経済新聞(兵庫)の" + str(text_count) + "番目のニュース取れました")
        if text_count >= max_text:
            break

#--------------------JSONファイルに出力--------------------
with open("hyogo.json", "w", encoding = "utf-8") as f:
    json.dump(text, f)
print("日本経済新聞(兵庫)のJSONファイル作りました！！！")
#----------------------------------------------------------