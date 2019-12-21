import speech_recognition as sr
import os
import sys
import webbrowser


def talk(phrase):
    print(phrase)
    os.system("say " + phrase)


def setCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Hy, please, talk')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("Please, try again")
        command = setCommand()
    return command


def make(command):
    if ('open' in command):
        talk('One second, please')
        before_keyword, keyword, after_keyword = command.partition('open')
        url = 'https://' + after_keyword + ".com"
        print(url.replace(" ", ""))
        webbrowser.open(url)
    elif 'stop' in command:
        talk('Sure, bye')
        sys.exit()


make(setCommand())
