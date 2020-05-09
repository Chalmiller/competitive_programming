def tower_builder(n_floors):
    end_length = n_floors*2 - 1 #(12 - 1)
    up = 0
    stairs = []
    for i in range(end_length, -1, -2):
      stairs.append(' ' * up + '*'*(i) + ' ' * up)
      up += 1
    return stairs[::-1]
      
        

print(tower_builder(6))