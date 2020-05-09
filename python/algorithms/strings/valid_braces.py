def validBraces(string):
  stack = []
  for brace in string[1:]:
      if stack:  
          if brace == ')' and stack[-1] == '(':
              stack.pop()
          elif brace == '}' and stack[-1] == '{':
              stack.pop()
          elif brace == ']' and stack[-1] == '[':
              stack.pop()
          else:
            return False
      else:
          stack.append(brace)
  return stack == []

print(validBraces("())({}}{()][]["))