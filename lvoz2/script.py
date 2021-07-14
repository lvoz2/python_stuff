print("Hello, Python has worked for once!")
print("We are all happy!!")
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import BernoulliRBM
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
model = BernoulliRBM(n_components=2)
model.fit(X)
# Plotting

plt.figure(figsize=(4.2, 4))
for i, comp in enumerate(model.components_):
    plt.subplot(10, 10, i + 1)
    print(comp)
    plt.imshow(comp.reshape((8, 8)), cmap=plt.cm.gray_r,
               interpolation='nearest')
    plt.xticks(())
    plt.yticks(())
plt.suptitle('100 components extracted by RBM', fontsize=16)
plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)

plt.show()
