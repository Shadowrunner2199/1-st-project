import numpy as np
def GenChis(h=1,k=0):
 B=[]
 for g in range(0,h):
  A=np.random.randint(100)
  B.append(A+k)
 return B
from matplotlib import pyplot as plt
Demons=['Dima', 'Grigoriy', 'Taras', 'Velzevul', 'Mefistofel', 'Baron Sub']
KolSoulsInCativity=GenChis(len(Demons))
xs=[i+0.1 for i, _ in enumerate(Demons)]
plt.bar(xs, KolSoulsInCativity)
plt.ylabel('Количество душ')
plt.title('Великие поработители')
plt.xticks([i + 0.1 for i, _ in enumerate(Demons)], Demons)
plt.show()
        
