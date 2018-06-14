#coding=utf-8
import urllib
import urllib2
import re
import csv
import time

labels = ['zh-cn','vi','id','ms']
with open('test.csv','w') as w:
    for page in range(482,2000):
        final = []
        for label in labels:
            url = "https://www.ted.com/talks/" + str(page) + "/transcript.json?language=" + label
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
            headers = { 'User-Agent' : user_agent }

            try:
                request = urllib2.Request(url,headers = headers )
                response = urllib2.urlopen(request)
                # print(response.read())


                content = response.read()
                pattern = re.compile('"text":"(.*?)"',re.S)
                items = re.findall(pattern,content)
                zh = []
                for item in items:
                    zh.append(item)
                cn =''.join(zh).replace(",",'，')
                final.append(cn)
            except urllib2.URLError,e:
                # print(e)
                final.append("None")
            time.sleep(1)
        both = ','.join(final)
        print(str(page) + "," +both)
        w.write(str(page) + "," +both)
