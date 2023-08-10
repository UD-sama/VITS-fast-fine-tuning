import speech_recognition as sr
import keyboard
def speech_to_text():
    recognizer = sr.Recognizer()
    while True:

        while True:


                print("開始錄音...")
                with sr.Microphone() as source:
                 audio = recognizer.listen(source)
                print("錄音結束，開始識別...")
                try:
                    text = recognizer.recognize_google(audio, language="zh-TW")
                    print("你說的話是：", text)
                    return text
                    break
                except sr.UnknownValueError:
                    print("無法識別你說的話")

                except sr.RequestError as e:
                    print("發生錯誤： {0}".format(e))




