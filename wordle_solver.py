def get_word(filename: str):
    with open(filename) as f:
        for line in f:
            guess_list.append(line.strip())
