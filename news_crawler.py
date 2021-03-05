import requests
import json
from bs4 import BeautifulSoup

#----------------------パラメータ設定----------------------
max_text = 50   #とりたいニュース数
#----------------------------------------------------------


def crawl(p_count, src, limit, tag1, tag2):    #クローラ(主に日本経済新聞かを確認)
    t_count = 0    #とったニュースの数
    if(p_count == "nikkei"):    #日本経済新聞の場合
        for i in [1, 21, 41]:
            t_count = text_chatch(i, src, limit, tag1, tag2, t_count)    #カウンターの更新とテキストの書き込み
        
    else:    #日本経済新聞でないの場合
        for i in range (1, p_count):
            t_count = text_chatch(i, src, limit, tag1, tag2, t_count)    #カウンターの更新とテキストの書き込み


def text_chatch(i, src, limit, tag1, tag2, t_count):    #ニュースのタイトルをとる
    response = requests.get(src + str(i))    #リンク先につながる
    soup = BeautifulSoup(response.text, "html.parser")    #HTMLコードをとる
    titles = soup.find_all(class_ = tag1, limit = limit)    #1ページのニュースを limit 個まで取る(1ページのニュース数はサイトにより異なる)
    for title in titles:
        t_text.append(title.select_one(tag2).getText())    #ニュースのタイトルを取り、文字列に入れる
        u_text.append(url_catch(src, title.select_one("a").get("href")))    #ニュースのリンク先を取り、文字列に入れる
        t_count += 1    #とった新聞のカウンターを増やす
        if t_count >= max_text:    #とりたいニュースの数を達した場合
            break    #ループを中断する
    return t_count    #とった新聞数のカウンターを戻す(14、19行)
    

def url_catch(src, link_to):    #ニュースのリンク先をとる
    if(link_to.startswith("https://www")):    #とったリンク先が完全なURLの場合はそのまま戻す
        return link_to
    else:    #とったリンク先は完全なURLでない場合、新聞のURLをまとめてから戻す
        s_index = src.find("/", 8)    # ”https://” 以後の "/" の位置を探す
        if (src.find("nara") != -1):    #奈良新聞の場合(奈良新聞のニュース一覧ページとニュースのページ若干違うのでここで処理する)
            return (src[:src.find("/",-1) - 2] + link_to)
        else:    #奈良新聞でないの場合
            return (src[:s_index] + link_to)
    

def json_output(f_name, text):    #JSONファイルの出力
    with open(f_name, "w", encoding = "utf-8") as f:
        json.dump(text, f)
    print(f_name + "生成しました！！！")


#-------------------------奈良新聞-------------------------
t_text = []    #タイトル文字列のリセット
u_text = []    #URL文字列のリセット
page_count = 6    #奈良新聞ホームページリンクのページカウント(ページ5までので、6に設定します)
limit = 10    #1ページのニュースが10個しかないので、10個とります
n_class = "item"    #新聞のclass
t_tag = "h3"    #タイトルのタッグ

crawl(page_count, "https://www.nara-np.co.jp/news/?p=", limit, n_class, t_tag)
#--------------------JSONファイルに出力--------------------
json_output("t_nara.json", t_text)
json_output("u_nara.json", u_text)
#----------------------------------------------------------


#-------------------------京都新聞-------------------------
t_text = []    #タイトル文字列のリセット
u_text = []    #URL文字列のリセット
page_count = 4    #京都新聞ホームページリンクのページカウント(ページ3までので、4に設定します)
limit = 20    #1ページのニュースが20個しかないので、20個とります
n_class = "m-articles-item"    #新聞のclass
t_tag = "h3"    #タイトルのタッグ

crawl(page_count, "https://www.kyoto-np.co.jp/subcategory/%E4%BA%AC%E9%83%BD%E5%BA%9C?page=", limit, n_class, t_tag)
#--------------------JSONファイルに出力--------------------
json_output("t_kyoto.json", t_text)
json_output("u_kyoto.json", u_text)
#----------------------------------------------------------


#-------------------------中日新聞-------------------------
t_text = []    #タイトル文字列のリセット
u_text = []    #URL文字列のリセット
page_count = 4  #中日新聞ホームページリンクのページカウント(ページ3までので、4に設定します)
limit = 20    #1ページのニュースが20個しかないので、20個とります
n_class = "detail-ttl"    #新聞のclass
t_tag = "a"    #タイトルのタッグ

crawl(page_count, "https://www.chunichi.co.jp/local/shiga/", limit, n_class, t_tag)
#--------------------JSONファイルに出力--------------------
json_output("t_shiga.json", t_text)
json_output("u_shiga.json", u_text)
#----------------------------------------------------------


#-----------------------わかやま新報-----------------------
t_text = []    #タイトル文字列のリセット
u_text = []    #URL文字列のリセット
page_count = 6  #わかやま新報ホームページリンクのページカウント(ページ5までので、6に設定します)
limit = 10    #1ページのニュースが20個しかないので、20個とります
n_class = "post_title icon_list_blue"    #新聞のclass
t_tag = "a"    #タイトルのタッグ

crawl(page_count, "https://www.wakayamashimpo.co.jp/category/news/page/", limit, n_class, t_tag)
#--------------------JSONファイルに出力--------------------
json_output("t_wakayama.json", t_text)
json_output("u_wakayama.json", u_text)
#----------------------------------------------------------


#--------------------日本経済新聞(大阪)--------------------
t_text = []    #タイトル文字列のリセット
u_text = []    #URL文字列のリセット
page_count = "nikkei"
limit = 20    #1ページのニュースが20個しかないので、20個とります
n_class = "m-miM09_title"    #新聞のclass
t_tag = "span"    #タイトルのタッグ

crawl(page_count, "https://www.nikkei.com/local/osaka/?bn=", limit, n_class, t_tag)
#--------------------JSONファイルに出力--------------------
json_output("t_osaka.json", t_text)
json_output("u_osaka.json", u_text)
#----------------------------------------------------------


#--------------------日本経済新聞(兵庫)--------------------
t_text = []    #タイトル文字列のリセット
u_text = []    #URL文字列のリセット
page_count = "nikkei"
limit = 20    #1ページのニュースが20個しかないので、20個とります
n_class = "m-miM09_title"    #新聞のclass
t_tag = "span"    #タイトルのタッグ

crawl(page_count, "https://www.nikkei.com/local/hyogo/?bn=", limit, n_class, t_tag)
#--------------------JSONファイルに出力--------------------
json_output("t_hyogo.json", t_text)
json_output("u_hyogo.json", u_text)
#----------------------------------------------------------