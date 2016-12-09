import csv
from random import random
import math
from collections import Counter

# This is a machine learning case study in which a program is given an RGB
# colour definition from which it has to name the colour as a human would
# identify as. To simplify the problem, the RGB space has been divided into
# 9 basic colours.
#
# This script implements the ML algorithm known as k-nearest neighbour.


dataset_filename = 'colors.csv'


def load_colours(filename):
    """
    Load the colours from the CSV file into a tuple of colour and name. This is
    implemented as a generator which returns the colour tuple, consisting of the
    RGB values and colour name.
    :param filename: input colour CSV file.
    :return: tuple of colour and name.
    """
    with open(filename) as dataset_file:
        # csv.reader() returns an iterator over the lines in a CSV file. Each
        # value returned by the iterator is a list of strings.
        lines = csv.reader(dataset_file)
        # Convert the lines in the file to a tuple of colour and name; using a
        # generator expression.
        for line in lines:
            yield tuple(float(y) for y in line[0:3]), line[3]


# Test the load_colours() generator.
# for colour, name in load_colours(dataset_filename):
#     print('RGB {} is named {}'.format(colour, name))


def generate_colours(count=100):
    """
    Generate random colour RGB space.  Implemented as a generator that yields
    the random colours as a tuple in RGB space.
    :param count: Number of random colours to generate.
    :return: tuple of random colours in RGB space.
    """
    for i in range(count):
        yield (random(), random(), random())


# Test the generate_colours() generator.
# print('\nRandom colours:')
# for colour in generate_colours(5):
#     print(colour)


def colour_distance(colour1, colour2):
    """
    Calculate the 'distance' between two colours. This is implemented by mapping
    the colour RGB space onto x,y,z axes.
    :param colour1: first RGB colour point.
    :param colour2: second RGB colour point.
    :return: distance between the two colour points in RGB space.
    """
    # zip() yields an iterator of tuples containing one element from each input
    # iterable.
    channels = zip(colour1, colour2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2
    return math.sqrt(sum_distance_squared)


# Test the colour_distance function.
# print('\nColour distance: {}\n'.format(colour_distance((1, 1, 1), (4, 5, 6))))


def nearest_neighbours(model_colours, num_neighbours):
    """
    Coroutine used to implement the k-nearest neighbour calculation.
    :param model_colours: list of colours to be used as a model.
    :param num_neighbours: number of neighbours to query.
    :return:
    """
    model = list(model_colours)
    # Accept a tuple of colour values.
    target = yield
    while True:
        # New list sorted by distance in ascending order.
        distances = sorted(
            ((colour_distance(c[0], target), c) for c in model),
        )
        # Yield the target's k-nearest neighbours in the model, i.e. yield the
        # ((r, g, b), colour_name) tuple for the k values with the lowest
        # distance.
        target = yield [
            d[1] for d in distances[0:num_neighbours]
        ]


# Test the code so far.
# model_colours = load_colours(dataset_filename)
# target_colours = generate_colours(3)
# get_neighbours = nearest_neighbours(model_colours, 5)
# next(get_neighbours)
#
# for colour in target_colours:
#     distances = get_neighbours.send(colour)
#     print(colour)
#     for d in distances:
#         print(colour_distance(colour, d[0]), d[1])


def write_results(filename='output.csv'):
    """
    Output the results to a CSV file. Implemented as a coroutine that accepts
    (colour, name) tuple to write out to the file.
    :param filename: output CSV file name.
    :return:
    """
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        while True:
            colour, name = yield
            writer.writerow(list(colour) + [name])


# Test write_results() coroutine.
# results = write_results()
# next(results)
# for i in range(3):
#     print(i)
#     results.send(((i, i, i), i * 10))


def name_colours(get_neighbours):
    """
    Return the most common colour out of the values returned from the
    nearest_neighbours() coroutine.
    :param get_neighbours: instance of the nearest_neighbours() coroutine. Used
    to proxy all of the values sent to it though at instance.
    :return: The most common colour.
    """
    colour = yield
    while True:
        near = get_neighbours.send(colour)
        name_guess = Counter(n[1] for n in near).most_common(1)[0][0]
        colour = yield name_guess


def process_colours(dataset_filename='colors.csv'):
    """
    Initiate the colour processing using the training data set file.
    :param dataset_filename: training data set file of colours.
    :return: None
    """
    # Object used to load the training data set into the model
    model_colours = load_colours(dataset_filename)
    # Object used to calculate the k-nearest neighbours
    get_neighbours = nearest_neighbours(model_colours, 5)
    # Object used to get the most common colour name from the nearest neighbours
    get_colour_name = name_colours(get_neighbours)
    # Object used to write the results out to the output file
    output = write_results()
    # Advance all coroutines to their first yield
    next(output)
    next(get_neighbours)
    next(get_colour_name)

    # Generate random colours and get their names
    for colour in generate_colours():
        # Get the name of the colour corresponding to the random colour
        name = get_colour_name.send(colour)
        # Write the output to file
        output.send((colour, name))


if __name__ == '__main__':
    process_colours()
