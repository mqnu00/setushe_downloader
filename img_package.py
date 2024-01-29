from bs4 import BeautifulSoup
from tool import get_html_content, save_list
import base_data


def get_page_count(search_url):
    html_content = get_html_content(search_url)
    soup = BeautifulSoup(html_content, 'html.parser')
    page_count = str(soup.findAll('div', class_='mdui-row')[-1].p.text)
    page_count = page_count[page_count.find('/') + 1:page_count.find('页')]
    return int(page_count)


def get_package_list(search_url):
    package_url_list = list()
    html_content = get_html_content(search_url)
    soup = BeautifulSoup(html_content, 'html.parser')
    package_url_content = soup.findAll('div', class_='mdui-col-md-2 mdui-col-sm-3 mdui-col-xs-4')
    for i in package_url_content:
        package_url_list.append(base_data.base_url + i.a.get('href'))
    return package_url_list


def package_result(search_name):
    search_url = 'http://setushe.com/search/tt/{}/{}.html'
    page_count = get_page_count(search_url.format(search_name, 1))
    package_url_list = list()
    for i in range(1, page_count + 1):
        now_url = search_url.format(base_data.search_name, i)
        print(now_url)
        res = get_package_list(now_url)
        print(len(res))
        package_url_list += res
        print(f'page-{i}-done!')
    save_list(
        path=base_data.path,
        name=base_data.img_package_filename,
        data=package_url_list
    )
    print(len(package_url_list))


if __name__ == '__main__':
    package_result(search_name=base_data.search_name)
