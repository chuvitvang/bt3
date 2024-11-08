import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV và tính toán cơ bản
df = pd.read_csv("C:/Users/Admin/Downloads/dulieu.csv")
Gold, Silver, Bronze = df['Gold'].astype(float), df['Silver'].astype(float), df['Bronze'].astype(float)
Total_Gold = Gold + Silver / 2 + Bronze / 3
total_medals = Gold + Silver + Bronze
df['Total_Gold'], df['Total_medals'] = Total_Gold, total_medals

# Tính các chỉ số thống kê
stats = {
    'Gold': [Gold.mean(), Gold.median(), Gold.std(), Gold.min(), Gold.max()],
    'Silver': [Silver.mean(), Silver.median(), Silver.std(), Silver.min(), Silver.max()],
    'Bronze': [Bronze.mean(), Bronze.median(), Bronze.std(), Bronze.min(), Bronze.max()],
    'Total_Gold': [np.nan] * 5,
    'Total_medals': [total_medals.mean(), np.median(total_medals), np.std(total_medals), total_medals.min(), total_medals.max()]
}
stats_df = pd.DataFrame(stats, index=['Mean', 'Median', 'Std Dev', 'Min', 'Max'])

# Vẽ biểu đồ
plt.figure(figsize=(15, 4))
plt.subplot(1, 3, 1)
plt.bar(['Gold', 'Silver', 'Bronze'], [Gold.sum(), Silver.sum(), Bronze.sum()], color=['gold', 'silver', '#cd7f32'])
plt.title('Total Medals Count'); plt.xlabel('Medal Type'); plt.ylabel('Count')

plt.subplot(1, 3, 2)
plt.pie([Gold.sum(), Silver.sum(), Bronze.sum()], labels=['Gold', 'Silver', 'Bronze'], autopct='%1.1f%%', colors=['gold', 'silver', '#cd7f32'])
plt.title('Medal Distribution')

plt.subplot(1, 3, 3)
sns.histplot(total_medals, bins=10, kde=True, color='teal')
plt.title('Distribution of Total Medals'); plt.xlabel('Total Medals'); plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Lưu dữ liệu kết hợp với thống kê vào file CSV
df_combined = pd.concat([df, stats_df.reset_index().rename(columns={'index': 'Metric'})], ignore_index=True)
df_combined.to_csv("C:/Users/Admin/Downloads/dulieu_final.csv", index=False)
