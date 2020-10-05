from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")
from wordcloud import WordCloud 

# the language will change depending on the context, adjust this as needed.
stopwords = set(stopwords.words('spanish', 'english')) 

# this list can also be updated or modified as needed.
stopwords.update(["ra", "ga", "na", "ani", "em", "ki", "ah","ha","la","eh","ne","le"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="black", colormap='Set3').generate(text)

# Display the generated image:
# the matplotlib way: 
plt.figure( figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# saving the wordcloud as image is optional
#print('Enter name for image')
#imname = input()
#plt.savefig(imname, format="jpg", facecolor='black', bbox_inches='tight')

plt.show()