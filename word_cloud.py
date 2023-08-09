import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


w = WordCloud()

# manually remove a few persistent words arising from poor math formatting in txt files.
stop_words = list(w.stopwords)
custom_stop_words = [
    "example",
    "definition",
    "ffi",
    "uvv",
    "trm",
    "ffX"
]

stop_words = set(stop_words + custom_stop_words)


# read in thesis. Note I removed the french abstract
# prior to reading it in to avoid special characters

with open("thesis.txt", encoding="utf8") as f:
  thesis = f.read()


# replace linebreaks with spaces
thesis = re.sub("[\r\n]", " ", thesis)

# replace all characters except alpha and spaces with spaces
thesis = re.sub("[^a-zA-Z\s]", " ", thesis)


wordcloud = WordCloud(
    background_color="white",
    min_word_length=3,
    width=1600,
    height=800,
    collocations=True,
    stopwords=stop_words,
    contour_color="white"
)

wordcloud.generate(thesis)


plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
# plt.show()
plt.savefig('wordcloud.png')
