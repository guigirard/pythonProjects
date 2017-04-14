import pandas as pd
from nltk.corpus import stopwords
import nltk.tokenize

r = open("./files/TMNT/reviews%2Freviews_com.ludia.tmnt_201704.csv", "rt", encoding="utf16")
df = pd.read_csv(r)

cols = list(df.loc[:, 'Package Name':'Device']) + list(df.loc[:, 'Star Rating':'Review Text'])
df_working = df[cols]
df_working = df_working.dropna(subset=['Review Text'])
corpus = df_working['Review Text']


tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

tokenizedDF = tokenizer.tokenize(str(corpus))
print(tokenizedDF)

stops = set(nltk.stopwords.words('english'))
