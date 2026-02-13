text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

listed_text = text.split()
result = []

for word in listed_text:
    if word.endswith('.') or word.endswith(','):
        result.append(word[:-1] + 'ing' + word[-1])
    else:
        result.append(word + 'ing')

result = ' '.join(result)
print(result)
