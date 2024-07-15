import pandas as pd
import matplotlib.pyplot as plt

# Διάβασμα των χρόνων απο το Times.csv
df = pd.read_csv('Times.csv')

# Εξαγωγή δεδομένων για κάθε δέντρο
kd_tree_data = df[df['Tree'] == 'Kd-tree']['Time'].tolist()
r_tree_data = df[df['Tree'] == 'R-tree']['Time'].tolist()
range_tree_data = df[df['Tree'] == 'Range-tree']['Time'].tolist()
oc_tree_data = df[df['Tree'] == 'Oc-tree']['Time'].tolist()

# Απεικόνιση δεδομένων σε γραφική παράσταση
query_count = list(range(1, 11))
plt.figure(figsize=(10, 6))
plt.plot(query_count, kd_tree_data, label='KD-tree', marker='o', color='blue')
plt.plot(query_count, r_tree_data, label='R-tree', marker='o', color='green')
plt.plot(query_count, range_tree_data, label='Range-tree', marker='o', color='orange')
plt.plot(query_count, oc_tree_data, label='Oc-tree', marker='o', color='red')
plt.xlabel('Queries')
plt.ylabel('Time (seconds)')
plt.title('Time Taken for Different Queries')
plt.xticks(rotation=45)
plt.legend()


# Υπολογισμός Μ.Ο χρόνων για κάθε δέντρο
average_kd_time = df[df['Tree'] == 'Kd-tree']['Time'].mean()
average_r_time = df[df['Tree'] == 'R-tree']['Time'].mean()
average_range_time = df[df['Tree'] == 'Range-tree']['Time'].mean()
average_oc_time = df[df['Tree'] == 'Oc-tree']['Time'].mean()
# Απεικόνιση δεδομένων σε διάγραμμα πίτας
trees = ['KD-tree', 'R-tree', 'Range-tree', 'Oc-tree']
average_times = [average_kd_time, average_r_time, average_range_time, average_oc_time]

plt.figure(figsize=(8, 8))
plt.pie(average_times, labels=trees, autopct='%1.1f%%', colors=['blue', 'green', 'orange', 'red'], startangle=90)
plt.title('Average Time for Each Tree Across All Queries')
plt.show()
