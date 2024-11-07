import numpy as np
import csv
import matplotlib.pyplot as plt

# Tải dữ liệu từ file CSV
with open("C:/Users/Admin/Downloads/dulieu.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# Giả sử dòng đầu tiên là tiêu đề
headers = data[0]
data = np.array(data[1:], dtype=object)  # Bỏ tiêu đề và chuyển dữ liệu còn lại thành mảng numpy

# Xác định chỉ số cột "Rank" (giả sử cột này đã tồn tại)
rank_col_index = headers.index('Rank')

# Chuyển các cột liên quan sang kiểu float (giả định 'Silver', 'Bronze', 'Gold' nằm ở cột 2, 3, 4)
countries = data[:, 1]
silver = data[:, 2].astype(float)
bronze = data[:, 3].astype(float)
gold = data[:, 4].astype(float)

# Tính Total Gold
total_gold = gold + silver / 2 + bronze / 3

# Tính Tổng medals
total_medals = gold + silver + bronze



# Sắp xếp dữ liệu theo Total Gold (giảm dần)
sorted_indices = np.argsort(-total_gold)
data_sorted = data[sorted_indices]  # Sắp xếp lại dữ liệu dựa trên chỉ số
total_gold_sorted = total_gold[sorted_indices]

# Cập nhật cột "Rank" có sẵn
rank = 1
for i in range(len(total_gold_sorted)):
    if i > 0 and total_gold_sorted[i] == total_gold_sorted[i - 1]:
        data_sorted[i, rank_col_index] = data_sorted[i - 1, rank_col_index]  # Giữ nguyên hạng cho các giá trị bằng nhau
    else:
        data_sorted[i, rank_col_index] = str(rank)
    rank += 1

# Thêm cột "Total_Gold" vào dữ liệu đã sắp xếp
data_sorted = np.column_stack((data_sorted, total_gold_sorted))

#phân tích dữ liệu
mean_total_gold = np.mean(total_gold_sorted)
median_total_gold = np.median(total_gold_sorted)
std_dev_total_gold = np.std(total_gold_sorted)
min_total_gold = np.min(total_gold_sorted)
max_total_gold = np.max(total_gold_sorted)

mean_gold = np.mean(gold)
median_gold = np.median(gold)
std_dev_gold = np.std(gold)
min_gold = np.min(gold)
max_gold = np.max(gold)

mean_silver = np.mean(silver)
median_silver = np.median(silver)
std_dev_silver = np.std(silver)
min_silver = np.min(silver)
max_silver = np.max(silver)

mean_bronze = np.mean(bronze)
median_bronze = np.median(bronze)
std_dev_bronze = np.std(bronze)
min_bronze = np.min(bronze)
max_bronze = np.max(bronze)

# In kết quả thống kê
print("Thống kê cho huy chương vàng:")
print(f"Trung bình huy chương vàng: {mean_gold:.2f}")
print(f"Trung vị huy chương vàng: {median_gold:.2f}")
print(f"Độ lệch chuẩn huy chương vàng: {std_dev_gold:.2f}")
print(f"Huy chương vàng ít nhất: {min_gold}")
print(f"Huy chương vàng nhiều nhất: {max_gold}\n")

print("Thống kê cho huy chương bạc:")
print(f"Trung bình huy chương bạc: {mean_silver:.2f}")
print(f"Trung vị huy chương bạc: {median_silver:.2f}")
print(f"Độ lệch chuẩn huy chương bạc: {std_dev_silver:.2f}")
print(f"Huy chương bạc ít nhất: {min_silver}")
print(f"Huy chương bạc nhiều nhất: {max_silver}\n")

print("Thống kê cho huy chương đồng:")
print(f"Trung bình huy chương đồng: {mean_bronze:.2f}")
print(f"Trung vị huy chương đồng: {median_bronze:.2f}")
print(f"Độ lệch chuẩn huy chương đồng: {std_dev_bronze:.2f}")
print(f"Huy chương đồng ít nhất: {min_bronze}")
print(f"Huy chương đồng nhiều nhất: {max_bronze}")

print(f"Trung bình tổng số huy chương: {mean_total_gold:.2f}")
print(f"Trung vị tổng số huy chương: {median_total_gold:.2f}")
print(f"Độ lệch chuẩn tổng số huy chương: {std_dev_total_gold:.2f}")
print(f"Quốc gia có số huy chương ít nhất: {min_total_gold}")
print(f"Quốc gia có số huy chương nhiều nhất: {max_total_gold}")

# Thêm tiêu đề cho cột "Total_Gold"
headers.append('Total_Gold')
# Lưu dữ liệu đã sắp xếp vào file CSV
output_filename = "C:/Users/Admin/Downloads/final_data_array.csv"
with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)  # Ghi tiêu đề
    writer.writerows(data_sorted)  # Ghi dữ liệu đã sắp xếp
