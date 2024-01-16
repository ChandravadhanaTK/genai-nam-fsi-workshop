import matplotlib.pyplot as plt

# Data
days = [1, 2, 3, 4, 5]
enfield = [50, 40, 70, 80, 20]
honda = [80, 20, 20, 50, 60]
yahama = [70, 20, 60, 40, 60]
ktm = [80, 20, 20, 50, 60]
colors = ['r', 'y', 'g', 'b']
bike_names = ['Enfield', 'Honda', 'Yahama', 'KTM']

# Create a single figure
fig, axs = plt.subplots(len(days), 1, figsize=(6, 6 * len(days)))

# Plotting pie charts for each day
for i, day in enumerate(days):
    distances = [enfield[i], honda[i], yahama[i], ktm[i]]
    ax = axs[i]
    ax.pie(distances, labels=bike_names, colors=colors,startangle=90,shadow=True,explode=(0,0,0.1,0),
        radius=1.2,autopct='%1.1f%%')
    ax.set_title(f"Day {day}")
    ax.legend(title="List of bikes details")

plt.show()
