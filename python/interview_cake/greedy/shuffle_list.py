import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    for i in range(len(the_list)):
      get_rand = get_random(0, len(the_list) - 1)
      # swap elements in the array
      the_list[i], the_list[get_rand] = the_list[get_rand], the_list[i]
    
    return the_list

sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)