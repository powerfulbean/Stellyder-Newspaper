# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:48:53 2018

@author: Jin Dou
"""
from Init import cNormalBFSConfig as Config
import queue
from StellyderBase import cStellyderEngineBase
import re
from bs4 import BeautifulSoup as BS
import requests as REQ


class cPatternMananger(object):
    def __init__(self):
        self.patternObjectDict = dict()
        self.patternDict = []
    
    def initPattern(self,file=None):
        self.patternDict = {
                "detailPage":r".*/\d*/\d*/\d*/(.*)(\.html)",
                "subTheme":r"(.*/[a-z|A-Z]*)+(index.html|)", 
                
                }
        
        for i in self.patternDict.keys():
            self.patternObjectDict[i] = re.compile(self.patternDict[i])
            
    def typeJudge(self, url):
        for i in self.patternObjectDict.keys():
            #print(url)
            if(url!=None):
                if (self.patternObjectDict[i].search(url)!=None):
                    return i
        
        return 'Other'
                

class cStellyderEngineTheme(cStellyderEngineBase):
    
    def __init__(self,root,header, config_filename,keyword = None):
        self.detailPageBuff = queue.Queue()
        self.subThemeBuff = queue.Queue()
        self.strangerBuff = list()
        self.Config = Config()
        self.root_url = root
        self.Pattern = cPatternMananger()
        self.header = header
        self.url_fetchResult = list()
        self.Config.Conf(config_filename)
        self.Pattern.initPattern()
        self.step = 0
        self.keyword = keyword;
        self.subtheme_record = list() # store the insert history of subThemeBuff
        self.detailpage_record = list() #  store the insert history of detailPageBuf
    
    def fetchUrl(self):
        print( "starting fetching new source url" )
        if(self.step == 0):
            response = REQ.get(self.root_url,headers=self.header)
            response.close()
            content = response.content
            objBs = BS(content,"lxml")  
            tag1 = objBs.find_all('a')
            for target1 in tag1:
                self.url_fetchResult.append(target1.get('href'))
        else:
            while not self.subThemeBuff.empty():
                target_url = self.subThemeBuff.get()
                response = REQ.get(target_url,headers=self.header)
                response.close()
                content = response.content
                objBs = BS(content,"lxml")  
                tag1 = objBs.find_all('a')
                for target1 in tag1:
                    self.url_fetchResult.append(target1.get('href'))
        
    def urlAnalysis(self,url_list=None):
        print( "starting Analyzing new source url" )
        url_list = self.url_fetchResult
        
        for i in url_list:
            url_type = self.Pattern.typeJudge(i)
            if ( url_type == 'subTheme'):
                flag,url = self._urlAnalysis_strategy_a(i,self.subtheme_record,self.keyword)
                if flag == 1:
                    self.subThemeBuff.put(url)
                else:
                    pass
            elif ( url_type == 'detailPage'):
                flag,url = self._urlAnalysis_strategy_a(i,self.detailpage_record)
                if flag == 1:
                    self.detailPageBuff.put(url)
                else:
                    pass
            else:
                self.strangerBuff.append(i)
        self.url_fetchResult.clear()
    
    def _urlAnalysis_strategy_a(self,url, subtheme_record, keyword = None): 
        
        # prevent loading webpage repeatly
        if( url not in subtheme_record):
            subtheme_record.append(url) 
        else:
            return 0 , None
        
        ###
        if(url.find("www.nytimes.com")!= -1):
            if( keyword != None):
                if (url.find(keyword) == -1):
                    print( "find non related" + url)
                    return -1, None
            return 1 , url
        elif ((url.find("www.")!=-1) or (url.find(".com")!=-1)):
            return -1 , None
        else:
            if(url.find("help.")!=-1):
                return -1 , None
            url = self.root_url + url
            return 1 ,url
    
    def _urlAnalysis_strategy_b(self,url, detailpage_record):
         
        if( url not in detailpage_record):
             detailpage_record.append(url) 
        else:
             return 0, None
        
        if(url.find("www.nytimes.com")!= -1):
            url = 'https://www.nytimes.com' +  url
            return 1 , url
        else:
            return 1 , url
        
    def engine(self):
        pass
        
    
    def testOutput(self,target1,target2):
        while not self.subThemeBuff.empty():
            target1.append(self.subThemeBuff.get())
        while not self.detailPageBuff.empty():
            target2.append(self.detailPageBuff.get())
            
    def fetchWebpageContent(self, target_url, target_root_folder='D:\\Appendix\\spyder_target\\',class_name =  "css-18sbwfn StoryBodyCompanionColumn"):
        #print(target_url)
        response = REQ.get(target_url,headers=self.header)
        response.close()
        content = response.content
        objBs = BS(content,"lxml")  
        tag1 = objBs.find_all('div',class_ = class_name)
        target = []
        title= objBs.find('title').string
        target.append('title:'+ title + '\n')
        for target1 in tag1:   # can try using .descendants
            level2 = target1.find_all('p')
            for target2 in level2:
                level3 = target2.strings
                for target3 in level3:
                    target.append(target3)
                target.append('\n')
            target.append('\n')
                
        title = title.replace('?','_q_')
        title= title.replace('|','__')
        title= title.replace('\\','__')
        title= title.replace('/','__')
        title= title.replace(':','__')
        title= title.replace('*','__')
        title= title.replace('"','__')
        title= title.replace('<','__')
        title= title.replace('>','__')
        
        
        
        with open(target_root_folder+title+'.txt', 'a', encoding='utf-8') as f:
            for i in target:
                if(i!=None):
                    f.write(i)

    
    