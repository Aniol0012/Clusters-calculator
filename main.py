import numpy as np
import argparse

from data import exams_data

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


def main():
    parser = argparse.ArgumentParser(description="Clusters Calculator")
    parser.add_argument('-c', '--clusters', type=int, help='Number of clusters')  # TODO: implement number of clusters
    parser.add_argument('-i', '--items', type=int, help='Number of items')  # TODO: implement number of items
    parser.add_argument('-e', '--exam', type=int, help='Exam year')  # TODO: implement exam years
    parser.add_argument('-s', '--seed', type=int, help='Random seed')
    parser.add_argument('-r', '--round', type=int, help='Round precision')  # TODO: implement round precision
    parser.add_argument('-f', '--file', type=str, help='File with data')  # TODO: implement file with data
    parser.add_argument('-n', '--n-iterations', type=int,
                        help='Number of iterations')  # TODO: implement number of iterations
    parser.add_argument('-p', '--plot', action='store_true', help='Plot clusters')  # TODO: implement plot clusters
    parser.add_argument('-d', '--debug', action='store_true', help='Debug mode')
    args = parser.parse_args()

    DEBUG = args.debug

    iterations = args.n_iterations
    if iterations is None:
        iterations = 1

    if DEBUG:
        print(f"Number of clusters: {args.clusters}")
        print(f"Number of points: {args.points}")

    items, clusters, iterations = exams_data.exam_2018()

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
