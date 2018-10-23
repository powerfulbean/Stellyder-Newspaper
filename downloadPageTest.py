# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:23:43 2018

@author: Jin Dou
"""


import Init 
from Init import cNormalBFSConfig
from StellyderEngine import cStellyderEngineTheme as SpyderEngine
from bs4 import BeautifulSoup as BS
import requests as REQ

config_folder = './config/'
user_agent_data_file = 'User_Agent_data.txt'


#config basic option
objConfig = cNormalBFSConfig()
objConfig.Conf(config_folder+'bfs.conf')

#config user_agent 
user_agent = Init.get_random_userAgent(config_folder+user_agent_data_file)
#user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
referer = 'https://www.google.com'
target_url='https://www.google.com/search?q=cancer&ie=&oe='
target_url = 'https://www.nytimes.com/'
target_url ='https://www.nytimes.com/2018/10/16/health/genetic-testing-mutations.html'
headers = {
        'user-agent': user_agent,
#        'referer': referer,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'x-client-data': 'CJC2yQEIpbbJAQjEtskBCKmdygEIuZ3KAQjXncoBCNmdygEIqKPKARj5pcoB',
        'cache-control':'max-age=0',
        'upgrade-insecure-requests': '1'
#        ':method':' GET',
#        ':path': '/',
#        ':scheme':' https'
    }


response = REQ.get(target_url,headers=headers)
response.close()
content = response.content
objBs = BS(content,"lxml")  
tag1 = objBs.find_all('div',class_ = "css-18sbwfn StoryBodyCompanionColumn")
target = []
for target1 in tag1:   # can try using .descendants
    level2 = target1.find_all('p')
    for target2 in level2:
        level3 = target2.strings
        for target3 in level3:
            target.append(target3)#find('h3',class_='r').find('a').get('href')) #网页里看是 h3 这里变成div了
        target.append('\n')
    target.append('\n')

title= objBs.find('title').string
with open('D:\\Appendix\\spyder_target\\'+title+'.txt', 'a') as f:
    for i in target:
        if(i!=None):
            f.write(i)