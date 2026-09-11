#This code produces the bar graph for the measurements lab
import matplotlib.pyplot as plt

# Data
measurements = [1, 2, 3, 4, 5]
densities = [0.526, 0.805, 0.887, 0.909, 0.927]
average = sum(densities) / len(densities)
true_density = 1.00

# Create figure
fig, ax = plt.subplots(figsize=(9, 6))

# Bar chart of measured densities
bars = ax.bar(measurements, densities, color='#4C72B0', width=0.6, zorder=3)

# Reference lines
avg_line = ax.axhline(average, color='#DD8452', linestyle='--', linewidth=2, zorder=4,
                       label=f'Average = {average:.3f} g/mL')
true_line = ax.axhline(true_density, color='#55A868', linestyle='-', linewidth=2, zorder=4,
                        label=f'True density = {true_density:.2f} g/mL')

# Titles and labels
ax.set_title("Density of Water at 22.0\u00b0C Obtained with a Graduate Cylinder", fontsize=13, pad=15)
ax.set_xlabel("Measurement", fontsize=12)
ax.set_ylabel("Density (g/mL)", fontsize=12)
ax.set_xticks(measurements)
ax.set_ylim(0, 1.15)
ax.grid(axis='y', linestyle=':', alpha=0.5, zorder=0)

# Legend (key) in top right
ax.legend(loc='upper right', frameon=True, fontsize=10)

# Data labels on top of bars
for bar, val in zip(bars, densities):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 0.02, f'{val:.3f}', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('water_density_plot.png', dpi=200)
plt.show()