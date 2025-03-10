import re

def tokenize(text):
    text = text.replace("।", " ")
    text = re.sub(r"[^\w\s\u0980-\u09FF]", "", text)
    tokens = text.split()
    return tokens

def main():
    text = input("এখানে আপনার পাঠ্য লিখুন: ")
    tokens = tokenize(text)
    print("টোকেন:", tokens)

if __name__ == "__main__":
    main()
