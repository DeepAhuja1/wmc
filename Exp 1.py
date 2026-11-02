import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

# Input
N = int(input("Enter Cluster Size N: "))
R = float(input("Enter Cell Radius R: "))

# Reuse distance
D = R * np.sqrt(3 * N)

# Colors for frequency groups (Presentable light pastel shades)
colors = ['#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF', '#E8BAFF', '#E0E0E0']

fig, ax = plt.subplots(figsize=(11, 9))

rows = 7
cols = 7

f1_positions = []

# Draw hexagonal cells
for row in range(rows):
    for col in range(cols):

        # Position of each hexagon
        x = np.sqrt(3) * R * (col + 0.5 * (row % 2))
        y = 1.5 * R * row

        # Frequency group
        group = (col + 2 * row) % N

        # Draw hexagon
        hexagon = RegularPolygon(
            (x, y),
            numVertices=6,
            radius=R,
            orientation=0,
            facecolor=colors[group % len(colors)],
            edgecolor='black',
            linewidth=1.5
        )

        ax.add_patch(hexagon)

        # Frequency label
        ax.text(
            x, y,
            "f" + str(group + 1),
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold'
        )

        # Store positions of f1 cells
        if group == 0:
            f1_positions.append((x, y))

# Draw reuse distance line between two f1 cells
if len(f1_positions) >= 2:

    x1, y1 = f1_positions[0]

    # Find f1 cell closest to theoretical reuse distance
    x2, y2 = min(
        f1_positions[1:],
        key=lambda p: abs(
            np.sqrt((p[0] - x1)**2 + (p[1] - y1)**2) - D
        )
    )

    ax.plot(
        [x1, x2],
        [y1, y2],
        'k--',
        linewidth=2.5
    )

    # Middle point of line
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    ax.text(
        mid_x,
        mid_y,
        "D = " + str(round(D, 2)),
        fontsize=12,
        fontweight='bold',
        bbox=dict(facecolor='white', edgecolor='black')
    )

# Title
plt.title(
    "Frequency Reuse (N = " + str(N) +
    ", R = " + str(R) +
    ", D = " + str(round(D, 2)) + ")",
    fontsize=16,
    fontweight='bold'
)

ax.set_aspect('equal')
ax.autoscale_view()
ax.axis('off')

plt.show()
