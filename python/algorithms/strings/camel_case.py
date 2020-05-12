def camel_case(string):
  res = []
  string_list = string.split()
  for word in string_list:
    res.append(word[0].upper() + word[1:])
  return "".join(res)
  
print(camel_case("camel case method"))
    