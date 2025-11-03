from collections import Counter
import matplotlib.pyplot as plt

responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

freq = Counter(responses)
total = len(responses)
percentages = {k: (v/total)*100 for k, v in freq.items()}


plt.bar(freq.keys(), freq.values(), color='teal')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.title('Response Frequencies')
for rating, value in freq.items():
    plt.text(rating, value+0.2, f"{value} ({percentages[rating]:.1f}%)", ha='center')
plt.show()
