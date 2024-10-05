import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

chunk_size = 159

data_iter = pd.read_csv(r'C:\Users\User\Downloads\World happiness report\2015.csv', chunksize=chunk_size)

avg_happiness_by_region = {}

chunks = []

for chunk in data_iter:
    chunk_avg = chunk.groupby('Region')['Happiness Score'].mean().to_dict()
    for region, score in chunk_avg.items():
        if region in avg_happiness_by_region:
            avg_happiness_by_region[region].append(score)
        else:
            avg_happiness_by_region[region] = [score]
    chunks.append(chunk)
for region in avg_happiness_by_region:
    avg_happiness_by_region[region] = sum(avg_happiness_by_region[region]) / len(avg_happiness_by_region[region])

avg_happiness_df = pd.DataFrame(list(avg_happiness_by_region.items()), columns=['Region', 'Average Happiness Score'])
avg_happiness_df = avg_happiness_df.sort_values(by='Average Happiness Score', ascending=False)

print("Average Happiness Score by Region:")

print(avg_happiness_df)

plt.figure(figsize=(12, 6))
sns.barplot(x='Average Happiness Score', y='Region', data=avg_happiness_df, color='blue')
plt.xlabel('Average Happiness Score')
plt.ylabel('Region')
plt.title('Average Happiness Score by Region')
plt.show()

data = pd.concat(chunks)

plt.figure(figsize=(12, 6))
plt.hist(data['Happiness Score'], bins=20, color='lightblue', edgecolor='black')
plt.xlabel('Happiness Score')
plt.ylabel('Frequency')
plt.title('Distribution of Happiness Scores')
plt.grid(axis='y')
plt.show()
