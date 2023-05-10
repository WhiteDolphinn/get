import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

from textwrap import wrap

with open('settings.txt') as file:
    settings=[float(i) for i in file.read().split('\n')]

data_v  = np.loadtxt('data.txt', dtype=int) * 3.3/256

delta_t = settings[1]
data_t  = np.array([i*delta_t for i in range(data_v.size)])

print(data_v)
print(data_t)


fig, plot = plt.subplots(figsize=(10, 8), dpi=500)

plot.axis([data_v.min(), data_t.max(), data_v.min(), data_v.max()+0.2])

plot.plot(data_t, data_v, c='#FFD0D0', linewidth=2, label = 'V(t)')

skip_amnt = 200
plot.scatter(data_t[0:data_v.size:skip_amnt], data_v[0:data_v.size:skip_amnt], marker = 'o', c = 'red', s=100)

plot.xaxis.set_major_locator(tck.MultipleLocator(1))
plot.xaxis.set_minor_locator(tck.MultipleLocator(0.25))

plot.yaxis.set_major_locator(tck.MultipleLocator(0.5))
plot.yaxis.set_minor_locator(tck.MultipleLocator(0.1))

plot.grid(which='major', color = 'black')
plot.minorticks_on()
plot.grid(which='minor', color = 'gray', linestyle = ':')


plot.set_title("\n".join(wrap('Процесс заряжания/разряжания конденсатора в RC цепи', 60)), loc = 'center')

plot.set_ylabel("Напряжение, В")
plot.set_xlabel("Время, с")

plot.annotate('Время зарядки = 6.00 с', xy=(250, 130), xycoords='figure points', fontsize = 14)
    
plot.annotate('Время разрядки = 4.00 с',xy=(250, 100), xycoords='figure points', fontsize = 14)

plot.legend(shadow = False, loc = 'upper right', fontsize = 30)

fig.savefig('8_result.png')
fig.savefig('8_result.svg')
exit()