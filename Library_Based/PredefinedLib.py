from langdetect import detect_langs
import requests
from bs4 import BeautifulSoup
import os
info={}
if not os.path.exists('Language.txt'):
    lang=requests.get("https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes")
    lan_table=BeautifulSoup(lang.text,'html.parser')
    table_con= lan_table.find_all("table",class_='wikitable')

    lang_det=table_con[0]

    table=lang_det.find_all('tr')
    table=table[0:]
    key= [x.find('td').text.strip() for x in table if x.find('td')]
    key=[x if not('\xa0' in x) else x.replace('\xa0','') for x in key]
    val=[x.find('td').get('id') for x in table if x.find('td')]


    with open('Language.txt','w') as f:
        for i in range(len(key)):
            f.write(val[i]+":\t"+key[i]+'\n')

        
else:
    with open('Language.txt','r') as f:
        info=f.readlines()
    info_ref=[x.replace('\t','').replace('\n','') for x in info]


    lang_info={}
    for x in info_ref:
        ind=x.index(':')
        lang_info[x[:ind]]=x[ind+1:]
    
    sen=input("Enter Something Bruh==>>")
    sen=sen.replace('!','').replace('@','').replace('#','').replace('$','').replace('%','').replace('^','').replace('&','').replace('*','')
    
    print(lang_info['en'])
    
    res=detect_langs(sen)
    print(res)
    res=str(res[0])
    print("It's\t"+lang_info[res[:res.index(':')]])
