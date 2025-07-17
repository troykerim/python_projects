import matplotlib.pyplot as plt


# plt.plot([1, 2, 3, 4])
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Displaying a line')
plt.grid(visible=True)
plt.show()


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # 'ko', '-k'
plt.title('Displaying another line')
plt.axis((0, 6, 0, 20))
plt.show()

# Displaying bars 

