import requests
import re

def get_html(url):
    content=requests.get(url).text
    return content

def flag_finder(content,mask):
    pattern = re.compile(mask)
    return pattern.findall(content)

if __name__ == '__main__':
    file = open('flags.txt','w')
    flags = flag_finder(get_html('https://vk.com/lifetrainings'),r'(CTF{[a-z|A-z|0-9]*})')
    for i in flags: file.write(i + '\n')