import urllib.request
import urllib.parse
import tkinter
import os
from tkinter import *
import tkinter.messagebox
import re
# web=input('请输入要生成的语句：')
# try:
#     os.chdir(r'C:\Users\dtm\Desktop')
#     os.mkdir('voice')
#     os.chdir('C:\\Users\\dtm\\Desktop\\voice')
# except FileExistsError:
#     os.chdir('C:\\Users\\dtm\\Desktop\\voice')
# headers={
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
#     'refer  er':'http://fanyi.baidu.com/'
# }
# web_side=urllib.parse.quote(web)
# url='http://fanyi.baidu.com/gettts?lan=zh&text={}&spd=5&source=web'.format(web_side)
# req=urllib.request.urlopen(url)
# res=req.read()
# with open('{}.mp3'.format(web),'wb')as f:
#     f.write(res)
root = Tk()
root.title("语音一键生成")
Label(root, text="语音内容").grid(row=0)
photo = PhotoImage(file='Logo.png')
imgLabel = Label(root, image=photo)
imgLabel.grid(row=0, column=2, padx=10, pady=5)
text = Text(root, width=35, height=6)
text.grid(row=0, column=1)


def show():
    web = text.get("0.0", "end")
    web = str(web).replace('\n', '')
    try:
        os.chdir('C:\\Users\\dtm\\Desktop')
        os.mkdir('voice')
        os.chdir('C:\\Users\\dtm\\Desktop\\voice')
    except FileExistsError:
        os.chdir('C:\\Users\\dtm\\Desktop\\voice')
    web_side = urllib.parse.quote(web)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'referer': 'http://fanyi.baidu.com/'
    }
    url = 'http://fanyi.baidu.com/gettts?lan=zh&text={}&spd=5&source=web'.format(
        web_side)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/63.0.3239.132 Safari/537.36',
        'referer': 'http://fanyi.baidu.com/'
    }
    req = urllib.request.Request(url)
    req.add_header('user-agent', headers['user-agent'])
    req.add_header('referfer', headers['referer'])
    req = urllib.request.urlopen(req)
    with open('{}.mp3'.format(web), 'wb')as f:
        f.write(req.read())
        f.close()


Button(root, text="开始生成", width=10, command=show).grid(
    row=3, column=1, sticky=W, padx=10, pady=5)
Button(root, text="退出程序", width=10, command=root.quit).grid(
    row=3, column=2, sticky=E, padx=10, pady=5)
mainloop()
