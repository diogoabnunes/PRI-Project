import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import csv
import re
#file = open(filename, encoding="utf8")
file = open("../documentos_resultado/races_joined.csv",encoding="utf8")
reader = csv.reader(file)
lines= len(list(reader))

# Load in the dataframe
df = pd.read_csv("../documentos_resultado/races_joined.csv")

title=""
race_text=""
qualifying_text=""

count_title=0
count_race_text=0
count_qualifying_text=0
# Start with one review
for row in range(lines-1):
    title +=" " + df.name[row]
    race_text +=" " + str(df.race_text[row])
    qualifying_text += " " + str(df.qualifying_text[row])

#media de palavras:
    count_title+=len(re.findall(r'\w+',  df.name[row]))
    count_race_text+=len(re.findall(r'\w+', str(df.race_text[row])))
    count_qualifying_text+=len(re.findall(r'\w+', str(df.qualifying_text[row])))

print("Title: " + str(int(count_title/lines)))
print("Race text: " + str(count_race_text/lines))
print("Qualifying text: " + str(count_qualifying_text/lines))


# Create and generate a word cloud image:
wordcloud_title = WordCloud(max_font_size=50, max_words=3,background_color="white").generate(title)
wordcloud_racetext = WordCloud(max_font_size=50, max_words=100,background_color="white").generate(race_text)
wordcloud_qualifyingtext = WordCloud(max_font_size=50, max_words=100,background_color="white").generate(qualifying_text)

# Display the generated image:

plt.imshow(wordcloud_racetext, interpolation='bilinear')
plt.axis("off")
plt.show()

plt.imshow(wordcloud_qualifyingtext, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud_racetext.to_file("../docs/common_words/races.png")
wordcloud_qualifyingtext.to_file("../docs/common_words/qualifying.png")