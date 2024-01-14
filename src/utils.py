import matplotlib.pyplot as plt
import numpy as np


def dprint(string):
    print(f"DEBUG -> {string}")


def print_ln(length=60):
    print("─" * length)


def print_parameter_usage(args):
    if args.clusters is not None:
        dprint(f"Number of clusters (-c): {args.clusters}")
    if args.items is not None:
        dprint(f"Number of items (-i): {args.items}")
    if args.seed is not None:
        dprint(f"Seed given (-s): {args.seed}")
    if args.round is not None:
        dprint(f"Round precision (-r): {args.round}")
    if args.file is not None:
        dprint(f"Data file (-f): {args.file}")
    print_ln()


def plot_clusters(items, assignments, clusters, iteration):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    clusters_items = []

    for i, cluster in enumerate(clusters):
        cluster_items = [items[j] for j, a in enumerate(assignments) if a == i]
        clusters_items.append(cluster_items)

    if clusters_items:
        for i, cluster_items in enumerate(clusters_items):
            if cluster_items:
                x_items, y_items = zip(*cluster_items)
                plt.scatter(x_items, y_items, c=colors[i % len(colors)], marker='o', label=f'Cluster {i + 1}')

                plt.scatter(clusters[i][0], clusters[i][1], c=colors[i % len(colors)], marker='x', s=100)

        plt.title(f'Cluster Plot iteration {iteration}')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("No clusters to plot")


def add_txt_extension(file):
    if not file.endswith('.txt'):
        file += '.txt'
    return file


def generate_random_file(file):
    clusters = np.random.randint(1, 100)
    items = np.random.randint(1, 100)
    iterations = np.random.randint(1, 100)

    if '../data/' is not None:
        file = '../data/' + file

    with open(file, 'w') as f:
        f.write('# items\n')
        for i in range(items):
            f.write(f'{np.random.randint(0, 100)}, {np.random.randint(0, 100)}\n')
        f.write('\n# clusters\n')
        for i in range(clusters):
            f.write(f'{np.random.randint(0, 100)}, {np.random.randint(0, 100)}\n')
        f.write('\n# iterations\n')
        f.write(f'{iterations}\n')
