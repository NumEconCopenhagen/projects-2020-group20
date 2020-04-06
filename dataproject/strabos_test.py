# Funtkion
import numpy as np
import matplotlib.pyplot as plt

# Data
n_groups = 10
Away_Win = (-31.42, -13.66, 4.01, -12.16, 2.59, 6.03, 2.83, -18.97, -15.11, -1.96)
Draw = (-7.5, 6.94, -8.17, 4.48, -19.74, -4.02, 2.62, -12.02, 4.96, -25.92)
Home_Win = (9.48, 0.73, -4.01, -11.22, 2.21, -0.72, -9.81, 6.56, 2.89, 5.05)


# Plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 1

rects1 = plt.bar(index, Home_Win, bar_width,
alpha=opacity,
color='violet',
label='Home Win')

rects2 = plt.bar(index + bar_width, Draw, bar_width,
alpha=opacity,
color='hotpink',
label='Draw')

rects3 = plt.bar(index + bar_width + bar_width, Away_Win, bar_width,
alpha=opacity,
color='magenta',
label='Away Win')

plt.xlabel('Season')
plt.ylabel('Profit in %')
plt.title('Premier League')
plt.xticks(index + bar_width, ('09/10', '10/11', '11/12', '12/13', '13/14', '14/15', '15/16', '16/17', '17/18', '18/19'))
plt.legend()
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Helvetica'

plt.tight_layout()
plt.show()


