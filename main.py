import base_data
from img_package import package_result
from img_package_info import read_img_package_info
from img_pic_list import download_img

if __name__ == '__main__':
    package_result(search_name=base_data.search_name)
    read_img_package_info()
    download_img()