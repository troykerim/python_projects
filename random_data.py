import random
import pandas as pd
import matplotlib.pyplot as plt

random.seed(42)

# Generate 100 (X, Y) pairs
x = [random.uniform(0, 100) for _ in range(100)]
y = [random.uniform(0, 100) for _ in range(100)]

df = pd.DataFrame({'X': x, 'Y': y})
# Diplay the first 5 datapoints
print(df.head(),"\n")

# display all data points
#with pd.option_context('display.max_rows', None):
#    print(df)
    
    
# plt.scatter(df['X'], df['Y'], color='blue')
# plt.title('(X, Y) Coordinates')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.grid(True)
# plt.show()

#print(df.describe())  # Summary statistics for data, will show (count, mean, std, min, 25%, 50%, 75%, max)

#print(df.mean())      # Mean of X and Y
#print(df.median())    # Median values
#print(df.std())       # Standard deviation

# Categorize each point into a quadrant
def get_quadrant(row):
    if row['X'] >= 50 and row['Y'] >= 50:
        return 'Q1'
    elif row['X'] < 50 and row['Y'] >= 50:
        return 'Q2'
    elif row['X'] < 50 and row['Y'] < 50:
        return 'Q3'
    else:
        return 'Q4'

df['quadrant'] = df.apply(get_quadrant, axis=1)
print(df['quadrant'].value_counts())

plt.scatter(df['X'], df['Y'], c='blue', edgecolor='k')
plt.title('Scatter Plot of Random Coordinates')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()