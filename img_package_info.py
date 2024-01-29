from bs4 import BeautifulSoup

import base_data
import tool
from tool import get_html_content, get_url_parser, get_list


def get_img_info(info_url):
    html_content = get_html_content(info_url)
    while type(html_content) is bool:
        html_content = get_html_content(info_url)

    soup = BeautifulSoup(html_content, 'html.parser')

    info = soup.find('div', class_='detail-header-info')
    title = info.h2.text
    others = info.select('p')
    pic_url = base_data.base_url + info.select('a')[1].get('href')

    info = dict()
    info['title'] = title
    info['info_url'] = info_url

    res = get_url_parser(info_url)
    path_list = res.path.split('/')
    path = ''
    for i in path_list:
        if i == '':
            continue
        path += '/'
        path += i
        if i == 'tt':
            path += '/'
            path += 'reader'
    res = res._replace(path=path)
    info['pic_url'] = res.geturl()

    for i in others:
        i = str(i.text)
        if i.find('图数') != -1:
            count = i[i.find('：') + 1:i.find('p')]
            info['count'] = count
        if i.find('作者') != -1:
            author = i[i.find('：') + 1:]
            info['author'] = author
        if i.find('出品') != -1:
            typ = i[i.find('：') + 1:]
            info['type'] = typ
    return info


def get_img_download_url_list(pic_url):
    html_content = get_html_content(pic_url)
    soup = BeautifulSoup(html_content, 'html.parser')
    image_urls = soup.findAll('img', class_='tutu-img detail-image')
    res = list()
    for image_url in image_urls:
        url = base_data.pic_bed + image_url['data-src']
        res.append(url)
    return res


def read_img_package_info():
    img_package_list = get_list(
        path=base_data.path,
        name=base_data.img_package_filename
    )
    for i, j in zip(img_package_list, range(1, len(img_package_list) + 1)):
        info = get_img_info(i)
        info['image_urls'] = get_img_download_url_list(info['pic_url'])
        tool.save_json(
            path=tool.path_merge([base_data.path, info['title']]),
            name=info['title'] + '.json',
            data=info
        )
        print(f'{j}-done!')


if __name__ == '__main__':
    read_img_package_info()
