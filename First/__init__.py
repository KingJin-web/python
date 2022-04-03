# # 求100-1000之间的所有素数
# primes = []
# for i in range(100,1001):
# 	for j in range(2,int(i**(1/2))+1):
# 		if i % j == 0:
# 			break
# 	else:
# 		primes += [i]
# print(primes)


import matplotlib.pyplot as plt

labels = 'frogs', 'hogs', 'dogs', 'logs'
sizes = 15, 20, 45, 10
colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
explode = 0, 0.1, 0, 0
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
plt.show()
