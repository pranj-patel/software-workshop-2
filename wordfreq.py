# wordfreq.py

def read_input(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    return [line.strip() for line in data]

if __name__ == "__main__":
    filename = "test.txt"  # Hardcoded filename for now
    lines = read_input(filename)
    word_freq = {}
    for line in lines:
        words = line.split()
        for word in words:
            word = word.lower()  # Convert the word to lowercase
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    for word, freq in word_freq.items():
        print(f"{word} {freq}")
