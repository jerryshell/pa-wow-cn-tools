import json
import requests
import bs4


def get_cn_by_id(id):
    url = 'https://www.wowhead.com/wotlk/cn/spell=' + id
    print(url)

    headers = {
        'authority': 'www.wowhead.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'dnt': '1',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers)
    # print(response.text)

    soup = bs4.BeautifulSoup(response.text, features='lxml')
    # print(soup)

    title = soup.select_one('.heading-size-1')
    # print(title)

    title_text = title.text
    # print(title_text)

    return title_text


def save(data):
    with open('[翻译]spell_专业制造法术书技能_名称.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


with open('[翻译]spell_专业制造法术书技能_名称.json') as f:
    data = json.load(f)

snapshot_counter = 0
for item in data:
    id = item['key']
    print(id)

    if int(id) >= 968000:
        print('skip: int(id) >= 968000')
        continue

    if item['translation'] != '':
        print('skip: item.translation != ""')
        continue

    cn = get_cn_by_id(id)
    print(cn)

    if cn == 'WotLK 技能':
        print('skip: WotLK 技能')
        continue

    item['translation'] = cn
    item['stage'] = 1

    snapshot_counter += 1
    if snapshot_counter >= 10:
        snapshot_counter = 0
        save(data)

save(data)
