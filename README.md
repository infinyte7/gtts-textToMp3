# gtts-textToMp3
Create and save text to mp3 using python gtts

```
pip install gTTS
```

### 1. Create audio for missing words of HSK words
Change file name or contents for new words
```
in_HSK2012_all_missing-audios.o.txt
```

```python
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
```

### 2. Copy that file to ``` collection.media ``` folder

### 3. In new words or missing audio note add this
```
[sound:cmn-HANZI.mp3]
```
HANZI will chinese characters. 

Example:
```
[sound:cmn-比如.mp3]
```

# License 
[audio-cmn](https://github.com/infinyte7/audio-cmn)

