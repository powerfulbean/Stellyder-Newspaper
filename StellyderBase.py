# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 17:11:24 2018

@author: Jin Dou
"""
from Init import cNormalBFSConfig as Config
import queue
from abc import ABCMeta, abstractmethod
import six



@six.add_metaclass(ABCMeta)
class cStellyderEngineBase(object):
    def __init__(self, config_filename): 
        pass
    
    @abstractmethod    
    def fetchUrl(self):
        pass
    @abstractmethod    
    def urlAnalysis(self,url_list):
        pass
        
    @abstractmethod
    def engineStart(self):
        pass