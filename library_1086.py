import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {'kategori': ['A', 'B', 'C', 'D', 'E'],
        'nilai': [20, 35, 30, 25, 40],
        'status':[0, 1, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(10, 6))
#sns.barplot(x='kategori', y='nilai', data=data,  color='red')
plt.pie(df['nilai'], labels=df['kategori'], autopct='%1.1f%%')
plt.title('diagram')
plt.axis('equal')
plt.show()
