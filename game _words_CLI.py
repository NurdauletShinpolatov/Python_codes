
import random
n  =  1
while n>0:
    print('\n',n,'shi oyin')
    s = 0
    meanings = []
    answers = []
    num_of_words = int(input('num_of_words = '))
    times_words = int(input('times_words = '))
    num_of_questions = num_of_words*times_words
    while s<num_of_words:
        print('\n',s+1,')')
        meaning = input('The meaning of the word:   ')
        meanings.append(meaning)
        answer = input("The word:   ")
        answers.append(answer)
        s = s+1
    print('game starting...')
    o = 0
    mark = 0
    while o<num_of_questions:
        choosing = random.choice(meanings)
        choice = meanings.index(choosing)
        c_ans = answers[choice]
        print('\n',choosing)
        ans = input('ans:   ')
        if ans == c_ans:
            print('++++++++\n   correct   ')
            mark = mark+1
        else:
            print('--------\n   wrong   ')
        o = o+1
    print('\n your mark is',mark,'/',num_of_questions)
    n = n+1
