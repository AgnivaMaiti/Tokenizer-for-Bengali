import string

def tokenize(text):
  tokens = []
  for word in text.split():
    if all(c in string.ascii_lowercase or c.isdigit() for c in word):
      tokens.append(word)
    else:
      tokens.append(word.replace("।", " ").strip())
  return tokens

def main():
  text = input("এখানে আপনার পাঠ্য লিখুন: ")
  tokens = tokenize(text)
  print(tokens)

if __name__ == "__main__":
  main()
