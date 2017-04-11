import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Wikipedia data (https://en.wikipedia.org/wiki/World_population)
years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]

# Fake data
deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3, 3.1, 3.3, 3.5, 3.8, 4, 4.3]

'''
plt.plot(years, pops, '--', color=(255/255, 100/255, 100/255))
plt.plot(years, deaths, color=(.6, .6, 1))
plt.ylabel("Population (billions)")
plt.xlabel("Years")

plt.title("Population Growth")
plt.show()
'''
'''
lines = plt.plot(years, pops, years, deaths)
plt.grid(True)

plt.setp(lines, color=(1, .4, .4), marker="o")

plt.show()

# -----------------------------------------
# This is only fake data
labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Perl'
sizes = [33, 52, 12, 17, 62, 48]
separated = (.1, .03, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')
plt.show()

# -----------------------------------------
raw_data = {"names": ["Nick", "Panda", "S", "Ari", "Valos"],
            "jan_ir": [143, 122, 101, 106, 365],
            "feb_ir": [122, 132, 144, 98, 62],
            "mar_ir": [65, 88, 12, 32, 65]}

df = pd.DataFrame(raw_data, columns=["names", "jan_ir", "feb_ir", "mar_ir"])
df["total_ir"] = df["jan_ir"] + df["feb_ir"] + df["mar_ir"]

color = [(1, .4, .4), (1, .6, 1), (.5, .3, 1), (.3, 1, .5), (.7, .7, .2)]

plt.pie(df["total_ir"],
        labels=df["names"],
        colors=color,
        autopct="%1.1f%%")

plt.axis("equal")

plt.show()
'''

col_count = 3
bar_width = .2

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width,
             alpha=.4,
             label="Korea")
c1 = plt.bar(index + bar_width, canada_scores, bar_width,
             alpha=.4,
             label="Canada")
ch1 = plt.bar(index + bar_width * 2, china_scores, bar_width,
              alpha=.4,
              label="China")
f1 = plt.bar(index + bar_width * 3, france_scores, bar_width,
             alpha=.4,
             label="France")


def create_labels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2, height * 1.05,
                 "%d" % int(height),
                 ha="center", va="bottom")

create_labels(k1)
create_labels(c1)
create_labels(ch1)
create_labels(f1)

plt.ylabel("Mean score in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test Scores by Country")

plt.xticks(index + bar_width * col_count / 2, ("Mathematics", "Reading", "Science"))
plt.legend(frameon=False, bbox_to_anchor=(1, 1), loc=2, prop={'size': 7})
plt.grid(True)

'''
for item in k1:
    print(item.get_height())
    print(item.get_width())
    print(item.get_x())
'''

plt.show()
