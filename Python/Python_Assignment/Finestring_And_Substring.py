
#? Version 1
# text = 'Today is Sunday. I stay at home and keep coding. '
# word = 'keep'
# text = text[text.find(word) + len(word) + 1:]
# next_word = text[:text.find(" ")]
# print(next_word)

#? Version 2
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

text = 'Today is Sunday. I stay at home and keep coding. Today is Monday. I stay at office and keep cleaning but still keep coding. '
word = 'keep'
start_pos = 0


start_pos,text = fine_next_word(text,word,start_pos)
# start_pos,text = fine_next_word(text,word,start_pos)
# start_pos,text = fine_next_word(text,word,start_pos)


