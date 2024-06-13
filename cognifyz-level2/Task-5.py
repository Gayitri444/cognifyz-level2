def count_word_occurrences(file_path):
    word_counts = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    word = word.lower()
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print("File not found.")
        return None
    return word_counts

def display_word_counts(word_counts):
    if word_counts is None:
        return
    sorted_word_counts = sorted(word_counts.items())
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

def main():
    file_path = input("Enter the path to the text file: ")
    word_counts = count_word_occurrences(file_path)
    if word_counts:
        print("Word counts (alphabetical order):")
        display_word_counts(word_counts)

if __name__ == "__main__":
    main()