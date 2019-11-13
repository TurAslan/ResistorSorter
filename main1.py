import math

R = (10115, 10125, 9998,10071,9937,9941,9973,9862,9853,9950,9988,9993,10067,9956,9975,10072,10012,10075,9865,9953,10037,9865,10051,9999,9984,10053,10007)
R1 = (10115, 10125, 9998,10071,9937,9941,9973,9862,10072,10012,10075,9865,)
unique_pairs = []

def digits(num):
  if num == 0:
    return 1
  return int(math.log10(num))

def index_remover(list_of_indexes, to_remove):
  global unique_pairs
  to_return = []
  to_remove = [to_remove]  
  for i in range(len(list_of_indexes)):
    if to_remove[0] in list_of_indexes[i]:
      temp = list(list_of_indexes[i])
      del temp[temp.index(to_remove[0])]
      to_remove += temp
  for j in range(len(list_of_indexes)):
    if len(list_of_indexes[i]) < 1:
      continue
    elif list_of_indexes[j][0] not in to_remove and list_of_indexes[j][1] not in to_remove:
      to_return += [list_of_indexes[j]]
    else:
      unique_pairs += [list_of_indexes[j]]
  return to_return

def available_resistors(magnitude, tolerance=3):
  global unique_pairs
  nominals = (0, 1, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2, 2.2, 2.4, 2.7, 3, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1)
  resistors = []
  for num in nominals:
    resistors += [(float(magnitude*num)-tolerance, float(magnitude*num)+tolerance, float(magnitude*num))]
  return resistors
# -------------------------------------------------------------
def find_uniques(pairs, possible_combinations):
  most_combinations = []
  combo = []
  ignore = []
  i = 0
  while len(most_combinations) < possible_combinations:
    already_selected_indexes = ()
    print('inside')
    for pair in pairs:
      print(pair)
      if not combo and pair in ignore:
        continue
      if pair[0] in already_selected_indexes or pair[1] in already_selected_indexes:
        continue
      combo += [pair] 
      already_selected_indexes += pair
      print('combo ', combo)
    if len(combo) > len(most_combinations):
      most_combinations = combo
    ignore += [pairs[i]]
    i += 1
  return most_combinations

# ---------------------------------------------------------------
def sorter(unsorted_resitances):
  global unique_pairs
  unique_pairs = [] 
  ignore_indexes = []
  pair_indexes = []
  for i in range(len(unsorted_resitances)):
    for j in range(len(unsorted_resitances)):

      if i==j:
        continue
      if (i, j) in ignore_indexes or (j, i) in ignore_indexes:
        continue

      difference = abs(unsorted_resitances[i] - unsorted_resitances[j])
      for standard_resistances in available_resistors(10**digits(difference)):
        if standard_resistances[1] > difference > standard_resistances[0]:
          print(unsorted_resitances[i], unsorted_resitances[j], difference, standard_resistances[2])
          pair_indexes += [(i,j)]
          break

      ignore_indexes += [(i, j)]
  
  #print('ignore:', ignore_indexes)
  print('pairs: ', pair_indexes)
  print('uniques: ', find_uniques(pair_indexes, len(unsorted_resitances)/2))

  
  # #while len(pair_indexes) > 0:
  # for n in range(5):
  #   num0 = len(unsorted_resitances)*[0]
  #   for i in pair_indexes:
  #     for possible_nums in range(len(unsorted_resitances)):
  #       num0[possible_nums] += i.count(possible_nums)
  #   for j in range(len(num0)):
  #     if num0[j] == 0:
  #       num0[j] = 9999
  #   print('count: ', num0)
  #   min0 = num0.index(min(num0))
  #   print('min0: ', min0)
  #   pair_indexes = index_remover(pair_indexes, min0)
  #   print('pairs: ', pair_indexes)
  # print('\nUnique pairs: ', unique_pairs)
