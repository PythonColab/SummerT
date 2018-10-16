from bs4 import BeautifulSoup as bs
import requests
import os
base = "https://www.youtube.com/results?search_query="
qstring = "BB+ki+vines"
r = requests.get(base+qstring)
page = r.text
soup=bs(page,'html.parser')
vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
videolist=[]
for v in vids:
    tmp = 'https://www.youtube.com' + v['href']
    videolist.append(tmp)
    print(tmp)
"""from pytube import YouTube
count=0
for item in videolist:
 
    # increment counter:
    count+=1
 
    # initiate the class:
    yt = YouTube(item)
    print(yt.description)
 
    # have a look at the different formats available:
    #formats = yt.get_videos()
 
    # grab the video:
    #video = yt.get('mp4', '360p')
 
    # set the output file name:
    #yt.set_filename('Video_'+str(count))
 
    # download the video:
    #video.download('./')"""
os.system("start chrome \""+tmp+"\"")

