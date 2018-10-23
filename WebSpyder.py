# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:23:43 2018

@author: Jin Dou
"""


import Init 
from Init import cNormalBFSConfig
from StellyderEngine import cStellyderEngineTheme as SpyderEngine

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
target_url ='https://www.nytimes.com/section/health'
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

Engine = SpyderEngine(target_url, headers,config_folder+'bfs.conf','health')

o1 = []
o2 = []
o3 = []

print("Engine Start: the max_depth is "+ str(Engine.Config.max_depth)+'\n')

while (Engine.step< Engine.Config.max_depth):
    print("depth: " + str(Engine.step+1) + " started\n" )
    Engine.fetchUrl()
    Engine.urlAnalysis()
#    temp1=[]
#    temp2 = []
#    Engine.testOutput(temp1,temp2)
#    o3.append(Engine.strangerBuff)
#    o1.append(temp1)
#    o2.append(temp2)
    print("Starting Fetching Web Page")
    while not Engine.detailPageBuff.empty():
        Engine.fetchWebpageContent(Engine.detailPageBuff.get())
    Engine.step += 1
    print('\n')
        





        


    