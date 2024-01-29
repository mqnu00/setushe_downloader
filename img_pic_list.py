import base_data
import tool


def download_img():
    data = tool.get_path_and_name(base_data.path)
    for i in data:
        print(i)
        folder_path = i['folder_path']
        json_name = i['json_name']
        info = tool.get_json(
            path=folder_path,
            name=json_name
        )
        image_urls = info['image_urls']
        count = int(info['count'])
        for image_url, cnt in zip(image_urls, range(1, count + 1)):
            if tool.path_exist(tool.path_merge([folder_path, f'{cnt}.jpg'])):
                print(f'{cnt}.jpg-exist!')
                continue
            img_content = tool.get_html_content(image_url)
            tool.write_file(
                path=folder_path,
                name=f'{cnt}.jpg',
                data=img_content
            )
            print(f'{info["title"]}-{cnt}.jpg-done!')


if __name__ == '__main__':
    download_img()
    pass
