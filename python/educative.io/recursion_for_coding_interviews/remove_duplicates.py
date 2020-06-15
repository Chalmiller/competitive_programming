def removeDuplicates(string):

  if not string:
    return ""
  elif len(string) == 1:
    return string
  elif string[0] == string[1]:
    return removeDuplicates(string[1:])
  
  return string[0] + removeDuplicates(string[1:])