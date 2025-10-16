import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = np.random.rand(100,1) * 10 #creating random values 
y = 3.5 * X + 5 + np.random.randn(100, 1) * 2  # add noise
ones = np.ones((100,1))
X_b = np.hstack((ones, X))# add column of 1s
 
beta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

print("Coefficeint of [c, m] is : ",beta.ravel())

y_pred = X_b.dot(beta)

plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, y_pred, color='red', label='Best Fit Line', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.title('Simple Linear Regression from Scratch')
plt.legend()
plt.show()

