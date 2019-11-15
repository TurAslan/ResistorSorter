import math
import statistics
import values


# returns the number of tens in a number
def digits(num):
    if num == 0:
        return 1
    return int(math.log10(num))


# given a magnitude and a tolerance returns a list of range of standard resistors
def available_resistors(magnitude, tolerance=0.1):
    nominals = (0, 1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8,
                7.5, 8.2, 9.1)
    resistors = []
    ignore_resistors = ()  # fill missing resistor values
    for num in nominals:
        if int(magnitude*num) in ignore_resistors:
            continue
        resistors += [(float(magnitude * num) - tolerance, float(magnitude * num) + tolerance, float(magnitude * num))]
    return resistors


# displays the pairs, their index in the resistor list and the difference between the two resistors in a pair
def display():
    for pair in values.PairData.unique_pairs:
        if values.PairData.R[pair[0]] > values.PairData.R[pair[1]]:
            print(values.PairData.R[pair[0]], values.PairData.R[pair[1]], '[' + str(pair[0]) + ':' + str(pair[1]) + ']',
                  abs(values.PairData.R[pair[0]]-values.PairData.R[pair[1]]))
        else:
            print(values.PairData.R[pair[1]], values.PairData.R[pair[0]], '[' + str(pair[1]) + ':' + str(pair[0]) + ']',
                  abs(values.PairData.R[pair[1]] - values.PairData.R[pair[0]]))


# takes in the list of resistors and returns a list with pairs of all possible resistor combinations
def sorter(unsorted_resistances):
    ignore_indexes = []
    pair_indexes = []
    values.PairData.temp_pairs = []
    values.PairData.unique_pairs = []

    for i in range(len(unsorted_resistances)):
        for j in range(len(unsorted_resistances)):

            if i == j:
                continue
            if (j, i) in ignore_indexes:
                continue

            difference = abs(unsorted_resistances[i] - unsorted_resistances[j])
            for standard_resistances in available_resistors(10 ** digits(difference)):
                if standard_resistances[1] > difference > standard_resistances[0]:
                    print(unsorted_resistances[i], unsorted_resistances[j], difference, standard_resistances[2])
                    pair_indexes += [(i, j)]
                    break

            ignore_indexes += [(i, j)]
    return pair_indexes


# takes in the list of pair from sorter() and returns a list of number of times resistors had pairs with other resistors
def find_min_pairs(pairs, num_of_resistors):
    num0 = num_of_resistors * [0]
    for i in pairs:
        for possible_nums in range(num_of_resistors):
            num0[possible_nums] += i.count(possible_nums)
    for j in range(len(num0)):
        if num0[j] == 0:
            num0[j] = 9999
    # print(num0)
    return num0


# takes in the list of pairs from sorter() and returns a list of unique pairs where if a resistor value was used,
# it will not be used again in any pair
def recursion_loop(pairs, num_of_resistors):
    if len(values.PairData.unique_pairs) > int(num_of_resistors/2)-1:
        return

    num_of_pairs = find_min_pairs(pairs, num_of_resistors)

    if statistics.mean(num_of_pairs) == 9999:
        if len(values.PairData.temp_pairs) > len(values.PairData.unique_pairs):
            values.PairData.unique_pairs = tuple(values.PairData.temp_pairs)
            print('unique: ', values.PairData.unique_pairs)
        return
    for i in range(len(num_of_pairs)):
        if num_of_pairs[i] == 9999:
            continue
        index_of_current_resistor = i
        break

    for j in range(num_of_pairs[index_of_current_resistor]):
        if j > 0:
            del values.PairData.temp_pairs[-1]
        values.PairData.temp_pairs += [pairs[j]]
        # print('temp: ', values.PairData.temp_pairs)

        recursion_loop(remove_resistors(pairs, pairs[j]), num_of_resistors)
    del values.PairData.temp_pairs[-1]


# takes in the list of pairs from sorter() and removes all pairs where resistors from pair_to_remove were used
def remove_resistors(pairs, pair_to_remove):
    combo = []
    for pair in pairs:
        if pair[0] in pair_to_remove or pair[1] in pair_to_remove:
            continue
        combo += [pair]
    return combo


def main():
    recursion_loop(sorter(values.PairData.R), len(values.PairData.R))
    display()


if __name__ == '__main__':
    main()
