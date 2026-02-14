words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

def multiple_rep(data):
    for key, value in words.items():
        print(key * value)

multiple_rep(words)
