def merge(string1, string2):

  if not string1:
    if not string2:
      return ""
    return string2
  elif not string2:
    return string1
  elif string1[0] > string2[0]:
    return string2[0] + merge(string1, string2[1:])
  
  return string1[0] + merge(string1[1:], string2)
  