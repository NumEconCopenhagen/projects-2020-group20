import numpy as np
import matplotlib.pyplot as plt

# Data
n_groups = 10
Home_Win = (0, 0, 0, 0, 0, 0, 0.2, 0.3, 0.4, -0.2591842105263158)
Draw = (0, 0, 0, 0, 0, 0, 0.1, 0.2, 0.3, -0.01960526315789468)
Away_Win = (0, 0, 0, 0, 0, 0, 0, 0.02, 0.1, 0.050473684210526226)

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


