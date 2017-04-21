from glob import glob
import pandas as pd
from nltk.corpus import stopwords
import nltk.tokenize
from collections import Counter

path = "./files/TMNT"
allfiles = glob(path + "/*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allfiles:
    r = open(file_, "rt", encoding="utf16")
    df = pd.read_csv(r)
    list_.append(df)
df = pd.concat(list_)

cols = list(df.loc[:, 'Package Name':'Device']) + list(df.loc[:, 'Star Rating':'Review Text'])
df_working = df[cols]
df_working = df_working.dropna(subset=['Review Text'])
df_corpus = df_working['Review Text']

tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')

df_tokenized = tokenizer.tokenize(str(df_corpus))

languages = {'english', 'spanish', 'russian', 'portuguese'}

stops = []

for lang in languages:
    stops.append(set(stopwords.words(lang)))

filtered_words = [w for w in df_tokenized if w not in stops]

freqs = Counter(filtered_words)

df_word = pd.DataFrame.from_dict(freqs, orient="index").reset_index().sort(0, ascending=False)
print(df_word)
