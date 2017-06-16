import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from cython_metric import mydist
import time

c1 = 1
c2 = -1
n = 300
x1 = np.random.randn(n,100) + c1
x2 = np.random.randn(n,100) + c2

x = np.concatenate([x1, x2], axis = 0)
y = np.array([0 if x < n else 1 for x in range(2*n)])

classifier = KNeighborsClassifier(metric= mydist)

t1 = time.time()
classifier.fit(x,y)

res = classifier.predict(x)
t2 = time.time()

print(t2 - t1)
print("precision is : " + str(1 - np.abs(res - y).sum()*1./(2*n)))