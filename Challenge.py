# adds "un" to the string "happy"
word = ("happy")
def add_prefix_un(word):
    return "un" + word

prefix_word = add_prefix_un(word)
print(prefix_word)

# adds "un" to the string "manageable"
word = ("manageable")
def add_prefix_un(word):
    return "un" + word

prefix_word = add_prefix_un(word)
print(prefix_word)

# adds prefix "en" to word group
vocab_words = (['en', 'close', 'joy', 'lighten'])
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    word_groups = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(word_groups)

word_group = make_word_groups(vocab_words)
print(word_group)

# adds prefix "pre" to word group
vocab_words = (['pre', 'serve', 'dispose', 'position'])
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    word_groups = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(word_groups)

word_group = make_word_groups(vocab_words)
print(word_group)

# adds prefix "auto" to word group
vocab_words = (['auto', 'didactic', 'graph', 'mate'])
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    word_groups = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(word_groups)

word_group = make_word_groups(vocab_words)
print(word_group)

# adds prefix "inter" to word group
vocab_words = (['inter', 'twine', 'connected', 'dependent'])
def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]
    word_groups = [prefix + word for word in words]
    return prefix + " :: " + " :: ".join(word_groups)

word_group = make_word_groups(vocab_words)
print(word_group)

# remove a suffix from the word "heaviness"
word = ("heaviness")

def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4]
        if root_word.endswith("i"):
            root_word = root_word[:-1] + "y" + root_word[-1:]
        return root_word
    else:
        return word

suffix_word = remove_suffix_ness(word.replace("i", "y"))
print(suffix_word)

# remove a suffix from the word "sadness"
word = ("sadness")

def remove_suffix_ness(word):
    if word.endswith("ness"):
        root_word = word[:-4]
        if root_word.endswith("i"):
            root_word = root_word[:-1] + "y" + root_word[-1:]
        return root_word
    else:
        return word

suffix_word = remove_suffix_ness(word.replace("i", "y"))
print(suffix_word)

# extracts and transforms the adjective "bright" to the verb "brighten"
sentence = ('I need to make that bright')
index = -1

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    return adjective + "en"
    
extract_word = adjective_to_verb(sentence, index)
print(extract_word)

# extracts and transforms the adjective "dark" to the verb "darken"
sentence = ('It got dark as the sun set.')
index = 2

def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index]
    return adjective + "en"
    
extract_word = adjective_to_verb(sentence, index)
print(extract_word)