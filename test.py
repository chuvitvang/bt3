import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV và chuyển đổi dữ liệu sang array NumPy
df = pd.read_csv("C:/Users/Admin/Downloads/dulieu.csv")  # Đọc dữ liệu từ file CSV
Gold = df['Gold'].values.astype(float)  # Chuyển cột Gold thành array NumPy
Silver = df['Silver'].values.astype(float)  # Chuyển cột Silver thành array NumPy
Bronze = df['Bronze'].values.astype(float)  # Chuyển cột Bronze thành array NumPy

# Tính tổng huy chương vàng và tổng huy chương
Total_Gold = Gold + Silver / 2 + Bronze / 3  # Tổng huy chương vàng có tính trọng số
total_medals = Gold + Silver + Bronze  # Tổng số huy chương

# Thêm cột Total_Gold và Total_medals vào DataFrame chính
df['Total_Gold'], df['Total_medals'] = Total_Gold, total_medals

# Tính các chỉ số thống kê cơ bản cho từng loại huy chương
# Tính toán trực tiếp với array 
stats = {
    'Gold': [np.mean(Gold), np.median(Gold), np.std(Gold), np.min(Gold), np.max(Gold)],
    'Silver': [np.mean(Silver), np.median(Silver), np.std(Silver), np.min(Silver), np.max(Silver)],
    'Bronze': [np.mean(Bronze), np.median(Bronze), np.std(Bronze), np.min(Bronze), np.max(Bronze)],
    'Total_Gold': [np.nan] * 5,  # Dữ liệu k có cho Total_Gold
    'Total_medals': [np.mean(total_medals), np.median(total_medals), np.std(total_medals), np.min(total_medals), np.max(total_medals)]
}

# Tạo DataFrame 
stats_df = pd.DataFrame(stats, index=['Mean', 'Median', 'Std Dev', 'Min', 'Max'])

# Vẽ các biểu đồ

plt.figure(figsize=(15, 4))  # Thiết lập kích thước của biểu đồ

# Biểu đồ cột (Bar chart) cho tổng huy chương từng loại
plt.subplot(1, 3, 1)  # Vị trí đầu tiên trong lưới biểu đồ
plt.bar(['Gold', 'Silver', 'Bronze'], [np.sum(Gold), np.sum(Silver), np.sum(Bronze)], color=['gold', 'silver', '#cd7f32'])  # Vẽ bar chart
plt.title('Total Medals Count')  # Tiêu đề biểu đồ
plt.xlabel('Medal Type')  # Nhãn trục X
plt.ylabel('Count')  # Nhãn trục Y

# Biểu đồ tròn (Pie chart) thể hiện tỷ lệ huy chương từng loại
plt.subplot(1, 3, 2)  # Vị trí thứ hai trong lưới biểu đồ
plt.pie([np.sum(Gold), np.sum(Silver), np.sum(Bronze)], labels=['Gold', 'Silver', 'Bronze'], autopct='%1.1f%%', colors=['gold', 'silver', '#cd7f32'])  # Vẽ pie chart
plt.title('Medal Distribution')  # Tiêu đề biểu đồ

# Biểu đồ histogram cho tổng số huy chương
plt.subplot(1, 3, 3)  # Vị trí thứ ba trong lưới biểu đồ
sns.histplot(total_medals, bins=10, kde=True, color='teal')  # Vẽ histogram với 10 bins
plt.title('Distribution of Total Medals')  # Tiêu đề biểu đồ
plt.xlabel('Total Medals')  # Nhãn trục X
plt.ylabel('Frequency')  # Nhãn trục Y
plt.tight_layout()  # Tự động căn chỉnh các biểu đồ
plt.show()  # Hiển thị tất cả các biểu đồ

# Gộp DataFrame chính với DataFrame chứa thống kê
df_combined = pd.concat([df, stats_df.reset_index().rename(columns={'index': 'Metric'})], ignore_index=True)  # Kết hợp các thống kê vào DataFrame chính
# Lưu kết quả vào file CSV
df_combined.to_csv("C:/Users/Admin/Downloads/dulieu_final.csv", index=False)  # Lưu dữ liệu vào file CSV
