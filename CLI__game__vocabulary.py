import random
game_cnt  =  1
while game_cnt > 0:
    # // input
    print('\n\tGame:', game_cnt)
    s  =  0
    meanings  =  []
    answers = []
    num_of_words = int(input('Number of words  =  '))
    times_words = int(input('How many times words should be repeated?: '))
    num_of_questions  =  num_of_words * times_words
    while s < num_of_words:
        print('\n',s+1,')')
        meaning = input('The meaning of the word:   ')
        meanings.append(meaning)
        answer = input("The word:   ")
        answers.append(answer)
        s = s+1


    # // G_A_M_E
    print('\n'*30)
    print('game starting...')
    o = 0
    mark = 0
    while o < num_of_questions:
        choosing = random.choice(meanings)
        choice = meanings.index(choosing)
        c_ans = answers[choice]
        print('\n',choosing)
        ans = input('ans:   ')
        if ans == c_ans:
            print('\n'*30, '++++++++\n   correct   ')
            mark +=  1
        else:
            print('\n'*30, '--------\n   wrong   ')
        o = o+1
    print('\n your mark is',mark,'/',num_of_questions)
    game_cnt +=  1
