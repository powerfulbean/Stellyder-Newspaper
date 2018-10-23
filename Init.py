# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:37:12 2018

@author: Jin Dou
"""
import numpy as np
from configparser import ConfigParser
from abc import ABCMeta, abstractmethod
import six
from argparse import ArgumentParser

def get_random_userAgent(file_address):
    random_ua = ''
    try:
        with open(file_address) as f:
            lines = f.readlines()
        if len(lines) > 0:
            prng = np.random.RandomState()
            index = prng.permutation(len(lines) - 1)
            idx = np.asarray(index, dtype=np.integer)[0]
            random_ua = lines[int(idx)]
            if(random_ua[-1].encode()==b'\n'):
                print('cut off b\'\\n\'')
                random_ua = random_ua[:-1]
    except Exception as ex:
        print('Exception in random_ua')
        print(str(ex))
    return random_ua

@six.add_metaclass(ABCMeta)
class cStellyderConfigBase(object):
    
    def __init__(self):
        pass
        
    def Conf(self,config_file=None):
        if(config_file==None):
            print("please assign a .conf file name to load_conf function \n")
            return -1
        else:
            self.load_conf(config_file)
    
    @abstractmethod
    def load_conf(self):pass
        
        
class cNormalBFSConfig(cStellyderConfigBase):
    def __init__(self):
        self.url_list_file = []
        self.output_directory = []
        self.max_depth = 0
        self.crawl_interval = 0
        self.crawl_timeout = 0.0
        self.target_url = []
        self.thread_count = 0
        self.url_list = []
        
    def load_conf(self,config_file=None):
        print(config_file)
        
        config = ConfigParser()
        config.read(config_file, encoding='utf-8')
        self.url_list_file = config.get('normal_bfs', 'url_list_file')
        self.output_directory = config.get('normal_bfs', 'output_directory')
        self.max_depth = int(config.get('normal_bfs', 'max_depth'))
        self.crawl_interval = int(config.get('normal_bfs', 'crawl_interval'))
        self.crawl_timeout = float(config.get('normal_bfs', 'crawl_timeout'))
        self.target_url = config.get('normal_bfs', 'target_url')
        self.thread_count = int(config.get('normal_bfs', 'thread_num'))
        
        f = open(self.url_list_file, 'r')
        for line in f:
            self.url_list.append(line.split('\n')[0])
        f.close()
        
        print('url_list_file: ' + self.url_list_file)
        print('output_directory: ' + self.output_directory)
        print('max_depth: %d' % self.max_depth)
        print('crawl_interval: %d' % self.crawl_interval)
        print('crawl_timeout: %f' % self.crawl_timeout)
        print('target_url: ' + self.target_url)
        print('thread_count: %d' % self.thread_count)
        print('urls:')
        print(self.url_list)        