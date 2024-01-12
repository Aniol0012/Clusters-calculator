# Clusters-calculator
Simple script made to automatize the centroid calculator for K-Means algorithm using euclidean distance.

> [!IMPORTANT]
> This scripts is heavily related to this [repository](https://github.com/Aniol0012/IA-Practica2).

# Requirements
```shell
$ pipx install -r requirements.txt
```
> [!NOTE]
> You can use pip instead of pipx, but I recommend using pipx to avoid conflicts with other projects

## How to use
1. Clone the repository
2. Run the script
3. Enter the number of clusters
4. Enter the number of points
5. Enter the points
6. Enter the initial centroids
7. Wait for the result
8. Enjoy!

## Example
```shell
$ python3 main.py
Enter the number of clusters: 2
Enter the number of points: 4
Enter the points:
1 1
1 2
2 1
2 2
Enter the initial centroids:
1 1
2 2
Centroids:
1.5 1.5
1.5 1.5
```

## License
[MIT](./LICENSE)
