def find_string_anagrams(str, pattern):
  result_indexes = []
  match = 0
  win_length = len(pattern)
  counter_dict = {}

  for s in pattern:
    if s not in counter_dict:
      counter_dict[s] = 0
    counter_dict[s] += 1

  for win_start in range(len(str) - win_length + 1):
    sub_str = str[win_start : ]
  
  return result_indexes
