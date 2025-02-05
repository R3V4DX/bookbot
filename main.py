def main():
  path = "books/frankenstein.txt"
  with open(path) as f:
    file_contents = f.read()
  report(path, number_of_words(file_contents), sign_count(file_contents))
  # print(file_contents)
  # print(f'Number of words: {number_of_words(file_contents)}')
  # print(f'Count of letters and symbols: {sign_count(file_contents)}')


def number_of_words(text: str):
  words = text.split()
  return len(words)


def sign_count(text: str):
  counts = {}
  for s in text:
    s = s.lower()
    if s not in counts.keys():
      counts[s] = 1
    else:
      counts[s] += 1
  return counts


def report(path: str, word_count: int, sign_count: dict):
  print(f'--- Begin report of {path} ---')
  print(f'{word_count} words found in the document')
  for k in sign_count:
    if (k.isalpha()):
      print(f"The '{k}' character was found {sign_count[k]} times")
  print(f'--- End report ---')


if __name__ == "__main__":
  main()