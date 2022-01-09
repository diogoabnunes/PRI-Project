import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import csv
import re

file = open("../documentos_resultado/circuits_joined.csv")
reader = csv.reader(file)
lines= len(list(reader))

# Load in the dataframe
df = pd.read_csv("../documentos_resultado/circuits_joined.csv")

circuit_text=""
count_circuit_text=0

# Start with one review
for row in range(lines-1):
    
    if type(df.text[row]) is not float:
      circuit_text +=" " + df.text[row]

#media de palavras:
    count_circuit_text+=len(re.findall(r'\w+', str(df.text[row])))

print("Circuit text: " + str(count_circuit_text/lines))


# Create and generate a word cloud image:
wordcloud_circuit_text = WordCloud(max_font_size=50, max_words=100,background_color="white").generate(circuit_text)

# Display the generated image:

plt.imshow(wordcloud_circuit_text, interpolation='bilinear')
plt.axis("off")
plt.show()

# Save the image in the img folder:
wordcloud_circuit_text.to_file("../docs/common_words_circuit.png")
