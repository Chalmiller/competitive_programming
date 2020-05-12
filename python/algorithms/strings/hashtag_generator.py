def generate_hashtag(s):
  if not s:
    return False
  else:
    return '#' + s.title().replace(' ', '') if len('#' + s.title().replace(' ', '')) < 140 else False

print(generate_hashtag(" Hello there thanks for trying my Kata"))
