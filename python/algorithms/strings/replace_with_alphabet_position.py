def alphabet_position(text):
  res_builder = []
  for let in text.lower().replace(' ', ''):
    if let.isalpha():
      res_builder.append(str(ord(let) - 96))
  return " ".join(res_builder)

print(alphabet_position("The sunset sets at twelve o' clock."))