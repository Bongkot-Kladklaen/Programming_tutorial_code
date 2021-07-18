def fine_next_word(text,word,start_pos):
    word_pos = text.find(word, start_pos)
    if (word_pos != -1): 
        text = text[word_pos + len(word) + 1:]
        if(text.find(" ") != -1):
            next_word = text[:text.find(" ")]
            start_pos = text.find(' ') + 1
        else:
            next_word = text
            start_pos = -1
        print(next_word)
        return start_pos,text
    else:
        print('')
        return '',-1

def find_all(text,word):
    start_pos = 0
    while start_pos != -1:
        start_pos,text = fine_next_word(text,word,start_pos)
        
text = 'Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning but still keep coding.'
# start_pos = 0
# start_pos,text = fine_next_word(text,word,start_pos)
find_all(text,'keep')
find_all(text,'at')
# start_pos,text = fine_next_word(text,word,start_pos)
