import numpy as np
import matplotlib.pyplot as plt

q = np.linspace(0, 100, 10000)
r = 1
h = 6.5821
alpha = q*r/h
f = 3*1/(alpha*alpha*alpha)*(np.sin(alpha)-alpha*np.cos(alpha))

plt.figure(figsize=(8, 8))
plt.plot(q, f)
plt.xlabel('|q|', fontsize=18)
plt.ylabel('F|q^2|', fontsize=18)

plt.savefig('repo_high_ene.png')
plt.show()
