# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:39:59 2018

@author: Jin Dou
"""
import re
subtheme = "https://www.nytimes.com/pages/opinion/index.html"
subtheme = "https://www.nytimes.com/pages/opinion"
subtheme  = "#collection-health"
articlepage = "/2018/10/15/opinion/sears-bankruptcy-amazon-retail-disruption.html"
articlepage="https://www.nytimes.com/2018/10/15/well/live/should-you-have-knee-replacement-surgery.html"

pattern = re.compile(r"https://www\.[a-z|A-Z]*\.com/.*(index\.html|.)")
pattern = re.compile(r".*/\d*/\d*/\d*/(.*)(\.html)")
pattern = re.compile(r"(.*/[a-z|A-Z]*)+(index.html|)")

match = pattern.search(subtheme)

print(match)

