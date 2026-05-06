# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| fig-align: center
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

points = np.array([
    [-2,2],
    [2,1],
    [1,-1],
    [-3,-2],
    [2,-3]
])

# Create a graph
G = nx.Graph()

# Add nodes with positions
for i, (x, y) in enumerate(points):
    G.add_node(chr(i+65), pos=(x, y))

# Get positions dictionary
pos = nx.get_node_attributes(G, 'pos')

# Draw the graph
plt.figure(figsize=(4, 4))
nx.draw_networkx_nodes(G, pos, node_color='black', node_size=300)
nx.draw_networkx_labels(G, pos, font_color='white')

plt.axis('off')
plt.show()
#
#
#
#
#
#| output: asis
from scipy.spatial.distance import cdist

# Compute squared distances
grid = cdist(points, points, metric='sqeuclidean')
grid = grid.astype(int)

# Build LaTeX string with sqrt symbols
latex_matrix = r'\begin{equation*}\mathbf{M} = \begin{bmatrix}'
rows = [' & '.join(r'\sqrt{' + str(int(val)) + r'}' for val in row) for row in grid]
latex_matrix += r' \\ '.join(rows)
latex_matrix += r'\end{bmatrix}\end{equation*}'
print(latex_matrix)
#
#
#
#
#| output: asis
from scipy.stats import rankdata

# Compute squared distances
perm = rankdata(grid, method='min', axis=-1)
perm = perm.astype(int)

# Build LaTeX string 
latex_matrix = r'\begin{equation*}\mathbf{\Pi^{-1}} = \begin{bmatrix}'
rows = [' & '.join(str(int(val)) for val in row) for row in perm]
latex_matrix += r' \\ '.join(rows)
latex_matrix += r'\end{bmatrix}\end{equation*}'
print(latex_matrix)
```
#
#
#
#
#| output: asis
sets = [perm < perm[:, [j]] for j in range(5)]
# Build LaTeX string 
latex_matrix = r'\begin{gather*}'
for i in range(5):
    if i == 3:  # After the 3rd matrix (index 2), break to new line
        latex_matrix += r'\\[2em]'
    elif i > 0:
        latex_matrix += r'\quad'
    latex_matrix += r'\mathbf{S}_{' + chr(65 + i) + r'} = \begin{bmatrix}'
    rows = [' & '.join(str(int(val)) for val in row) for row in sets[i]]
    latex_matrix += r' \\ '.join(rows)
    latex_matrix += r'\end{bmatrix}'
latex_matrix += r'\end{gather*}'
print(latex_matrix)
#
#
#
#
#
#| output: asis
u = np.ones(5, dtype=int)
u[2] = 0

outputs = []
u_steps = [u]
while np.any(u):
    prod = u @ sets[2]
    outputs.append(prod.copy())
    j = np.argmax(prod)
    u = np.bitwise_not(np.bitwise_or(np.bitwise_not(u), sets[2][:, j]))
    u_steps.append(u)

# Build LaTeX string 
out = ""
for step, (prod, u_step) in enumerate(zip(outputs, u_steps[:-1])):
    out += f"**Round {step + 1}**" + '\n'
    out += r'\begin{gather*}'
    out += r'\begin{bmatrix}'
    out += r''.join(' & '.join(str(int(val)) for val in u_step))
    out += r'\end{bmatrix}'

    latex_matrix = r'\begin{bmatrix}'
    rows = [' & '.join(str(int(val)) for val in row) for row in sets[2]]
    latex_matrix += r' \\ '.join(rows)
    latex_matrix += r'\end{bmatrix}'

    out += latex_matrix + r'= \begin{bmatrix}'
    out += r''.join(' & '.join(str(int(val)) for val in prod))
    out += r'\end{bmatrix}' + '\n'

    out += r'\\[1em]'
    out += r'\end{gather*}' + '\n'
    covered_elements = [chr(65+a) for a in np.where(sets[2][:, np.argmax(prod)])[0]]
    out+= f"Select column {chr(65 + np.argmax(prod))}, which covers {', '.join(covered_elements)}." + '\n\n'
print(out)
#
#
#
#
#
#
