import matplotlib.pyplot as plt
import seaborn as sns
from numpy import random

# sns.distplot([0, 1, 2, 3, 4, 5]) #แบบมีฮิสโตแรกม
# sns.distplot([0, 1, 2, 3, 4, 5],hist=False)
# plt.show()

# sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True, kde=False)
# plt.show()

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()