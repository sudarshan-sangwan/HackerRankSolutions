import numpy as np

m, n = [int(i) for i in input().strip().split(' ')]

X = []
Y = []
for i in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])

q = int(input().strip())

X1 = []
for x in range(q):
    X1.append(input().strip().split(' '))

X = np.array(X, float)
Y = np.array(Y, float)
X_new = np.array(X1, float)

X_R = X - np.mean(X, axis=0)
Y_R = Y - np.mean(Y)

b = np.dot(np.linalg.inv(np.dot(X_R.T, X_R)), np.dot(X_R.T, Y_R))

X1_R = X_new-np.mean(X,axis=0)
Y1_R = np.dot(X1_R, b)
Y1 = Y1_R + np.mean(Y)

for y in Y1:
    print(round(float(y), 2))
