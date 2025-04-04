import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]  
y2 = [1, 4, 9, 16, 25]  


plt.plot(x, y1, label="y = 2x", color='blue', linestyle='--', marker='o')

plt.plot(x, y2, label="y = x^2", color='red', linestyle='-', marker='s')

plt.title("Comparison of Two Functions")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

plt.legend()

plt.show()
