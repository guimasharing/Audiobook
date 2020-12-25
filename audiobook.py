import pyttsx3
import fitz

speaker = pyttsx3.init()
speaker.setProperty('rate', 120)
speaker.say("我是电子书阅读器1.0")
with fitz.open('sgyy01.pdf') as doc:
    text = ""
    for page in doc:
        text = page.getText()
        print("现在读的是第{}页".format(page.number+1))
        speaker.say("现在读的是第{}页".format(page.number+1))
        print(text)
        speaker.say(text)
        speaker.runAndWait()
        speaker.stop()
