import requests
from bs4 import BeautifulSoup

filename = 'gis4g_articles.txt'
with open(filename, 'w', encoding='utf-8') as file_object:
    url = "http://gis4g.pku.edu.cn"
    r = requests.get(url, timeout = 30)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'lxml')
    tagcloud = soup.find('div', class_="tagcloud")
    tags = tagcloud.find_all('a')
    # 处理各个tag
    for tag in tags:
        tagname = tag.get_text()
        taglink = str(tag.get('href'))
        file_object.write(f'\n######{tagname}######\n\n')
        print(f'\n######{tagname}######\n')
        url = taglink

        while True:
            r = requests.get(url, timeout = 30)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'lxml')
            for article, abstract in zip(soup.find_all('h2', class_ = "entry-title post-title"), soup.find_all('div', class_ = "entry-content")):
                info = article.find('a')
                info1 = abstract.find('p')
                if info:
                    title = info.get_text()
                    link = str(info.get('href'))
                    file_object.write(f'标题：{title}\n')
                    file_object.write(f'链接：{link}\n')
                    print(f'标题：{title}')
                    print(f'链接：{link}')
                if info1:
                    abstract = info1.get_text()
                    file_object.write(f'摘要：{abstract}\n\n')
                    print(f'摘要：{abstract}\n')

            # 下一页
            Next = soup.find('a', class_="next page-numbers")
            if Next:
                url = str(Next.get('href'))
            else:
                break # 读到最后一页
