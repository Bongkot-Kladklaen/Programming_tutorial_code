import curses
# def add_to_corpus_index(corpus_index,word,next_word):
#     for el in corpus_index:
#         if el[0] == word:
#             el[1].append(next_word)
#             return corpus_index
#     corpus_index.append([word,[next_word]])

def add_all_to_corpus_index(corpus_index, corpus):
    splitted_text = corpus.split()
    for i in range(len(splitted_text) - 1):
        current_word, next_word = splitted_text[i], splitted_text[i + 1]
        add_to_corpus_index(corpus_index,current_word,next_word)

# def lookup(corpus_index, word):
#     for i in corpus_index:
#         if i[0] == word:
#             return i[1]

def string_hash(key,hash_table):
    hashed_value = 0
    for k in key:
      hashed_value += ord(k)
    hashed_value %= len(hash_table)  
    return hashed_value

def create_hash_table(size):
    hash_table = []
    for _ in range(size):
        hash_table.append(None)
    return hash_table

def add_to_hash_table(key, value, hash_table):
     item = string_hash(key,hash_table)
     hash_table[item] = [key,value]

def lookup(key, hash_table):
    slot = string_hash(key,hash_table)
    if(hash_table[slot] == None):
        return None
    else:
        return hash_table[slot][1]
def add_to_corpus_index(key,next_word,corpus_index):
    if key not in corpus_index:
        corpus_index[key] = {next_word:1}
    else:
        if next_word in corpus_index[key]:
            corpus_index[key][next_word] += 1 
        else:
            corpus_index[key][next_word] = 1

def init_corpus_stats(corpus_index, corpus):
    split_text = corpus.split()
    for i in range(len(split_text) -1 ):
        current_word, next_word = split_text[i],split_text[i + 1]
        add_to_corpus_index(current_word,next_word,corpus_index)

def predict(word,corpus_stats):
    if word in corpus_state:
        return max(corpus_state[word], key = corpus_state[word].get)
    else:
        return ""

def load_corpus(file_name):
    with open(file_name,'r') as f:
        return f.read()



corpus = load_corpus("corpus.txt")
corpus_state = {}
init_corpus_stats(corpus_state, corpus) 
screen = curses.initscr()
curses.noecho()
text_buffer = ''

while True:
    c = screen.getkey()

    if ord(c) == 27:
        break
    elif  c == "\\t":
        begin = text_buffer.strip().rfind('') + 1
        last_word = text_buffer[begin: ].strip()
        next_word = predict(last_word, corpus_state)
        screen.addstr('' + next_word)
        text_buffer = next_word
    else:
        screen.addch(c)
        text_buffer += c

# while word != 'exit':
#     word = input('Enter Word: ')
#     next_word = predict(word,corpus_state)
#     if word == 'exit':
#         print("Exit to program")
#     else:
#         print(f"Result = {next_word}")
