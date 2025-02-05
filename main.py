def main():
  path = "books/frankenstein.txt"
  with open(path) as f:
    file_contents = f.read()
  print(file_contents)
  print(f'Number of words: {number_of_words(file_contents)}')


def number_of_words(text: str):
  words = text.split()
  return len(words)


if __name__ == "__main__":
  main()