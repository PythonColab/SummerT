import speech_recognition as sr
from time import ctime
import time
import os
import wikipedia
import numpy as np
import pyttsx3
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs
import requests
from chatterbot import ChatBot
from tkinter import *

chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)
chatbot.train("chatterbot.corpus.english")

print("Hi I am Alfred, Whats Your Name : ")
name=input("Enter The Name : ")
window = Tk()
window.title("ALFRED")
window.geometry('750x400')
filename = PhotoImage(file = "jar3.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
logo = PhotoImage(file="jar2.gif")
lb1 = Label(window, text="ALFRED",height=3,bg="Black",fg="RED",font=("Times",12))
lb1.grid(column=0, row=0,columnspan=4)
lb2 = Label(window,anchor="nw",text="Click Speak/Enter for Starting",height=15,width=65,borderwidth=4, relief="sunken",justify=LEFT,bg="Cyan",fg="GREEN")
lb2.configure(font=("Comic Sans MS",8))
lb2.grid(column=0, row=1)
lb3 = Label(window,height=2)
lb3.grid(row=2)
def p(res):
    text = lb2.cget("text") +"\n"+res
    lb2.configure(text=text)
    
def speak(audioString):
    p(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    time.sleep(6)
    engine.runAndWait()
     
def recordAudio():
    r = sr.Recognizer()
    speak("Say something!")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        p("You said: " + data)
    except sr.UnknownValueError:
        lb2.configure(fg="RED")
        p("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        lb2.configure(fg="RED")
        p("Could not request results from Speech Recognition service; {0}".format(e))
     
    return data
     
def jarvis(data,name):
    if "how are you" in data:
        speak("I am fine")
     
    elif "what time is it" in data:
        speak(ctime())
     
    elif "where is" in data:
        data = data.split(" ")
        location = str(data[2])
        speak("Hold on "+name+", I will show you where " + location + " is.")
        os.system("start chrome \"www.google.nl/maps/place/" + location + "/&amp;\"")

    elif "open Chrome" in data:
        speak("Hold on "+name+", Opening Chrome")
        os.system("start chrome \"www.google.com\"")

    elif "search" in data:
        str1 = data.strip('search')
        speak("Hold on "+name+", Opening Chrome")
        os.system("start chrome \"https://www.google.co.in/search?q="+str1+"\"")

    elif "play video" in data:
        str1 = data.strip('play video')
        base = "https://www.youtube.com/results?search_query="
        qstring = str1.replace(" ","+")
        r = requests.get(base+qstring)
        page = r.text
        soup=bs(page,'html.parser')
        vids = soup.findAll('a',attrs={'class':'yt-uix-tile-link'})
        videolist=[]
        print("\n\nYOUTUBE LOG : \n")
        for v in vids:
            tmp = 'https://www.youtube.com' + v['href']
            videolist.append(tmp)
            print(tmp)
        speak("Hold on "+name+", Opening Chrome")
        os.system("start chrome \""+videolist[0]+"\"")
        p("For more visit cmd Youtube LOG")
        
    elif "google" in data:
        str1 = data.strip('google')
        speak("Hold on "+name+", Searching Google")
        USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
 
 
        def fetch_results(search_term, number_results, language_code):
            assert isinstance(search_term, str), 'Search term must be a string'
            assert isinstance(number_results, int), 'Number of results must be an integer'
            escaped_search_term = search_term.replace(' ', '+')
         
            google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results, language_code)
            response = requests.get(google_url, headers=USER_AGENT)
            response.raise_for_status()
         
            return search_term, response.text
         
        if __name__ == '__main__':
            keyword, html = fetch_results(str1, 10, 'en')
           
        def parse_results(html, keyword):
            soup = BeautifulSoup(html, 'html.parser')
         
            found_results = []
            rank = 1
            result_block = soup.find_all('div', attrs={'class': 'g'})
            for result in result_block:
         
                link = result.find('a', href=True)
                title = result.find('h3', attrs={'class': 'r'})
                description = result.find('span', attrs={'class': 'st'})
                if link and title:
                    link = link['href']
                    title = title.get_text()
                    if description:
                        description = description.get_text()
                        
                    if link != '#':
                        found_results.append({'link': link,'keyword': keyword, 'rank': rank, 'title': title, 'description': description})
                        rank += 1
            return found_results
        s=parse_results(html, keyword)
        count=0
        for i in s[:2]:
            p(str(i['rank'])+" :")
            p("Keyword : "+str(i['keyword']))
            p("Title : "+str(i['title']))
            p("Description : "+str(i['description']))
            p("Full Link : "+str(i['link']))
        p("For more visit cmd GOOGLE LOG")
        print("\n\nGOOGLE LOG : \n")
        for i in s:
            print(str(i['rank'])+" :")
            print("Keyword : "+str(i['keyword']))
            print("Title : "+str(i['title']))
            print("Description : "+str(i['description']))
            print("Full Link : "+str(i['link']))

    elif "wiki" in data:
        str1 = data.strip('wiki')
        speak("Hold on "+name+", Searching in wikipedia")
        possibles = ['Plot','Synopsis','Plot synopsis','Plot summary', 'Story','Plotline','The Beginning','Summary','Content','Premise']
        possibles_edit = [i + 'Edit' for i in possibles]
        all_possibles = possibles + possibles_edit
        try:
            wik = wikipedia.WikipediaPage(title=str1).summary
            p(wik)
        except:
            wik = np.NaN
        try:
            for j in all_possibles:
                if wik.section(j) != None:
                    plot_ = wik.section(j).replace('\n','').replace("\'","")
                    p(plot)
        except:
            plot= np.NaN
        p("For more visit cmd WIKI LOG")
        print("\n\nWIKI LOG : \n")
        print(wik)
        print(plot)

    else:
        speak(chatbot.get_response(data).text);
       
def clicked():
    lb2.configure(fg="GREEN")
    lb2.configure(text="")
    data = txt.get()
    jarvis(data,name)
def clicked1(name):
    lb2.configure(fg="GREEN")
    lb2.configure(text="")
    speak("Hi "+name+", what can I do for you?")
    data = recordAudio()
    jarvis(data,name)
btn = Button(window, text="SPEAK", command= lambda: clicked1(name),width=50,height=3,bg="BLUE",fg="WHITE")
btn.grid(column=0, row=3,rowspan=3)
lb4 = Label(window,image=logo)
lb4.grid(row=1,column=2,columnspan=2)
txt = Entry(window,width=40,bg="RED",fg="WHITE")
txt.grid(column=2,row=3)
btn1 = Button(window, text="Enter", command=clicked,width=30,bg="BLUE",fg="WHITE")
btn1.grid(column=2, row=5)
window.mainloop()
