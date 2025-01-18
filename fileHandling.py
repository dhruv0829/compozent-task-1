def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)

        with open(output_file, 'w') as file:
            file.write(f"Word count: {word_count}")

        print(f"Word count written to {output_file}")
    except FileNotFoundError:
        print(f"{input_file} not found.")


count_words_in_file('input.txt', 'output.txt')
