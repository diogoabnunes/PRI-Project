import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import csv
import re

file = open("../documentos_resultado/constructors_joined.csv",encoding="utf8")
reader = csv.reader(file)
lines= len(list(reader))

# Load in the dataframe
df = pd.read_csv("../documentos_resultado/constructors_joined.csv")

text = ""
count_text = 0

# Start with one review
for row in range(lines-1):
    text += " " + str(df.text[row])

    #media de palavras:
    count_text += len(re.findall(r'\w+', str(df.text[row])))

print("Text: " + str(int(count_text/lines)))


# Create and generate a word cloud image:
wordcloud_text = WordCloud(max_font_size=50, max_words=100,background_color="white").generate(text)

# Display the generated image:

plt.imshow(wordcloud_text, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud_text.to_file("../docs/common_words/constructors.png")