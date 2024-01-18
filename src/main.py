import numpy as np
import argparse
import utils
import config

ROUND_PRECISION = config.DEFAULT_ROUND_PRECISION
DEBUG = config.DEFAULT_DEBUG


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
            new_clusters.append([round(coord, ROUND_PRECISION) for coord in new_cluster])
        else:
            new_clusters.append([round(coord, ROUND_PRECISION) for coord in clusters[i]])
    return new_clusters


def parse_arguments():
    global DEBUG, ROUND_PRECISION

    parser = argparse.ArgumentParser(description="Clusters Calculator")
    parser.add_argument('-c', '--clusters', type=int, help='Number of clusters')
    parser.add_argument('-i', '--items', type=int, help='Number of items')
    parser.add_argument('-t', '--iterations', type=int, help='Number of iterations')
    parser.add_argument('-s', '--seed', type=int, help='Random seed')
    parser.add_argument('-r', '--round', type=int, help='Round precision')
    parser.add_argument('-f', '--file', type=str, help='File with data')
    parser.add_argument('-n', '--new_random_file', type=str, help='Generate new random file')
    parser.add_argument('-p', '--plot', action='store_true', help='Plot clusters')
    parser.add_argument('-d', '--debug', action='store_true', help='Debug mode')
    args = parser.parse_args()

    DEBUG = args.debug
    if args.round is not None:
        ROUND_PRECISION = args.round

    if args.seed is not None:
        np.random.seed(args.seed)

    if DEBUG:
        utils.print_parameter_usage(args)

    return args


def read_data(file):
    if DEBUG:
        utils.dprint(f"Reading data from {file}")

    try:
        with open(file, 'r') as f:
            lines = f.read().split('\n')
    except FileNotFoundError:
        with open(f"../data/{file}", 'r') as f:
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

    # The -f parameter overwrites -n
    if args.new_random_file is not None:
        file = utils.add_txt_extension(args.new_random_file)
        utils.generate_random_file(file)
    elif args.file is not None:
        file = utils.add_txt_extension(args.file)
    else:
        file = utils.add_txt_extension(config.DEFAULT_FILE)

    items, clusters, iterations = read_data(file)

    if args.clusters is not None:
        clusters = utils.get_coords(args.clusters, "cluster")

    if args.items is not None:
        items = utils.get_coords(args.items, "item")

    if args.iterations is not None:
        iterations = args.iterations

    utils.print_ln()
    print(f"Items: {items}")
    print(f"Clusters: {clusters}")
    print(f"Iterations: {iterations}")
    utils.print_ln()

    for i in range(iterations):
        print(f"Iteration {i + 1}:")
        distances = calculate_distances(clusters, items)
        assignments = assign_clusters(distances)
        clusters = update_clusters(items, assignments, clusters)

        for index, (item_dist, assignment) in enumerate(zip(distances, assignments)):
            print(f"Item {index} distances: {item_dist} -> assigned to K{assignment + 1}")

        print("\nNew cluster positions:")
        for cluster, new_cluster_position in enumerate(clusters, 1):
            print(f"K{cluster}: {new_cluster_position}")

        utils.print_ln()

        if args.plot:
            utils.plot_clusters(items, assignments, clusters, i + 1)


if __name__ == "__main__":
    main()
