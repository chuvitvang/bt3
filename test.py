import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv("C:/Users/Admin/Downloads/dulieu.csv")

# Lấy dữ liệu từ các cột vào các mảng
Gold = df['Gold'].values.astype(float)
Silver = df['Silver'].values.astype(float)
Bronze = df['Bronze'].values.astype(float)

# Tính tổng huy chương vàng và tổng huy chương
Total_Gold = Gold + Silver / 2 + Bronze / 3
total_medals = Gold + Silver + Bronze

# Tính các chỉ số thống kê cơ bản
mean_total_medals = np.mean(total_medals)
median_total_medals = np.median(total_medals)
std_dev_total_medals = np.std(total_medals)
min_total_medals = np.min(total_medals)
max_total_medals = np.max(total_medals)

mean_gold = np.mean(Gold)
median_gold = np.median(Gold)
std_dev_gold = np.std(Gold)
min_gold = np.min(Gold)
max_gold = np.max(Gold)

mean_silver = np.mean(Silver)
median_silver = np.median(Silver)
std_dev_silver = np.std(Silver)
min_silver = np.min(Silver)
max_silver = np.max(Silver)

mean_bronze = np.mean(Bronze)
median_bronze = np.median(Bronze)
std_dev_bronze = np.std(Bronze)
min_bronze = np.min(Bronze)
max_bronze = np.max(Bronze)

#vẽ biểu đồ
plt.figure(figsize=(10, 5))
plt.bar(['Gold', 'Silver', 'Bronze'], [np.sum(Gold), np.sum(Silver), np.sum(Bronze)], color=['gold', 'silver', '#cd7f32'])
plt.title('Total Medals Count')
plt.xlabel('Medal Type')
plt.ylabel('Count')
plt.show()

# Tạo pie chart (biểu đồ tròn) thể hiện tỉ lệ phân bố huy chương
plt.figure(figsize=(8, 8))
plt.pie([np.sum(Gold), np.sum(Silver), np.sum(Bronze)], labels=['Gold', 'Silver', 'Bronze'], autopct='%1.1f%%', colors=['gold', 'silver', '#cd7f32'])
plt.title('Medal Distribution')
plt.show()

# Tạo histogram (biểu đồ histogram) cho tổng số huy chương mỗi quốc gia
plt.figure(figsize=(10, 6))
sns.histplot(total_medals, bins=10, kde=True, color='teal')
plt.title('Distribution of Total Medals')
plt.xlabel('Total Medals')
plt.ylabel('Frequency')
plt.show()

# Thêm cột Total_Gold và Total_medals vào DataFrame chính
df['Total_Gold'] = Total_Gold
df['Total_medals'] = total_medals

# Tạo DataFrame chứa các kết quả thống kê
stats_data = {
    'Gold': [mean_gold, median_gold, std_dev_gold, min_gold, max_gold],
    'Silver': [mean_silver, median_silver, std_dev_silver, min_silver, max_silver],
    'Bronze': [mean_bronze, median_bronze, std_dev_bronze, min_bronze, max_bronze],
    'Total_Gold': ['', '', '', '', ''],
    'Total_medals': [mean_total_medals, median_total_medals, std_dev_total_medals, min_total_medals, max_total_medals]
}
stats_df = pd.DataFrame(stats_data, index=['Mean', 'Median', 'Std Dev', 'Min', 'Max'])

# Gộp DataFrame chính với DataFrame chứa thống kê dưới dạng hàng mới
df_combined = pd.concat([df, stats_df.reset_index().rename(columns={'index': 'Metric'})], ignore_index=True)
# Lưu dữ liệu vào file CSV
df_combined.to_csv("C:/Users/Admin/Downloads/dulieu_final.csv", index=False)
