from gtts import gTTS

def textToMp3(text):
    tts = gTTS(text, lang="zh-cn")
    tts.save("cmn-"+text+".mp3")

with open("in_HSK2012_all_missing-audios.o.txt", encoding="utf8") as f:
    for line in f:
        for word in line.split():
            try:
                textToMp3(word)
                print(word)
            except Exception:
                pass
