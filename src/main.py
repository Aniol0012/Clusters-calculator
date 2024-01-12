import numpy as np
import argparse
import utils

ROUND_PRECISION = 4
DEBUG = False


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2)) ** 2))


def calculate_distances(clusters, items):
    iteration_distances = []
    for item in items:
        item_distances = []
        for cluster in clusters:
            dist = euclidean_distance(item, cluster)
            item_distances.append(round(dist, ROUND_PRECISION))
        iteration_distances.append(item_distances)
    return iteration_distances


def assign_clusters(distances):
    assignments = []
    for item_distances in distances:
        min_distance = min(item_distances)
        min_indices = [i for i, d in enumerate(item_distances) if d == min_distance]
        assigned_cluster = min(min_indices)
        assignments.append(assigned_cluster)
    return assignments


def update_clusters(items, assignments, clusters):
    new_clusters = []
    for i in range(len(clusters)):
        assigned_items = [items[j] for j, a in enumerate(assignments) if a == i]
        if assigned_items:
            new_cluster = np.mean(assigned_items, axis=0).tolist()
            new_clusters.append(new_cluster)
        else:
            new_clusters.append(clusters[i])
    return new_clusters


def parse_arguments():
    parser = argparse.ArgumentParser(description="Clusters Calculator")
    parser.add_argument('-c', '--clusters', type=int, help='Number of clusters')  # TODO: implement number of clusters
    parser.add_argument('-i', '--items', type=int, help='Number of items')  # TODO: implement number of items
    parser.add_argument('-e', '--exam', type=int, help='Exam year')  # TODO: implement exam years
    parser.add_argument('-s', '--seed', type=int, help='Random seed')
    parser.add_argument('-r', '--round', type=int, help='Round precision')  # TODO: implement round precision
    parser.add_argument('-f', '--file', type=str, help='File with data')  # TODO: implement file with data
    parser.add_argument('-p', '--plot', action='store_true', help='Plot clusters')  # TODO: implement plot clusters
    parser.add_argument('-d', '--debug', action='store_true', help='Debug mode')
    args = parser.parse_args()

    DEBUG = args.debug

    if DEBUG:
        if args.clusters is not None:
            print(f"Number of clusters (-c): {args.clusters}")
        if args.items is not None:
            print(f"Number of items (-i): {args.items}")

    if args.seed is not None:
        np.random.seed(args.seed)

    return args


def read_data(file):
    if DEBUG:
        utils.dprint(f"Reading data from {file}")
        print(f"Reading data from {file}")

    with open(file, 'r') as f:
        lines = f.read().split('\n')

    items = []
    clusters = []
    iterations = 1
    section = None

    for line in lines:
        if line == '' or line.startswith('//'):
            continue
        elif line.startswith('#'):
            section = line[1:].strip()
        elif section == 'items':
            items.append([int(x) for x in line.split(',')])
        elif section == 'clusters':
            clusters.append([int(x) for x in line.split(',')])
        elif section == 'iterations':
            iterations = int(line)

    if items == [] or clusters == []:
        raise Exception("Items or clusters not found in file, please check the format in the README.md file")

    return items, clusters, iterations


def main():
    args = parse_arguments()

    if args.file is not None:
        file = args.file
    else:
        file = '../data/2018.txt'

    items, clusters, iterations = read_data(file)

    print(f"Items: {items}")
    print(f"Clusters: {clusters}")
    print(f"Iterations: {iterations}")
    print("────────────────────────────────────────────────────────────")

    for i in range(iterations):
        print(f"Iteration {i + 1}:")
        distances = calculate_distances(clusters, items)
        assignments = assign_clusters(distances)
        clusters = update_clusters(items, assignments, clusters)

        for index, (item_dist, assignment) in enumerate(zip(distances, assignments)):
            print(f"Item {index} distances: {item_dist} -> assigned to K{assignment + 1}")

        print("\nNew cluster positions:")
        for cluster, new_cluster_position in enumerate(clusters):
            print(f"K{cluster + 1}: {new_cluster_position}")

        print("────────────────────────────────────────────────────────────")


if __name__ == "__main__":
    main()
