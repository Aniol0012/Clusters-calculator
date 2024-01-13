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
1. Install the requirements
1. Check the help panel of the script

````shell
$ python3 main.py -h
````

### Example

```shell
$ python3 main.py ../data/2018.txt -r 3 -d -p  
```

## Data file format

The data file must be a text file with the following format:

```
// Example file

# items
1, 2
3, 4
5, 6

# centroids
1, 2

# iterations
10
```

Note that the use of the '//' symbol can be used to add comments to the file.

> [!TIP]
> You can use the [default file](data/2018.txt) as an example


## License

[MIT](./LICENSE)
