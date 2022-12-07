import random, turtle, time


pen = turtle.Turtle() #// for writing
pen.hideturtle()
turtle.delay(0)
turtle.bgcolor("grey")
status = "main menu"
index = 0
list_words = []
list_definitions = []
end_of_words = False


#__SM__// settings of a pen turtle that writes and draws
def pen_settings(color="white", up_down="down", pensize=3, speed=0):
    global status
    pen.color(color)
    if up_down == "down":
        pen.down()
    else:
        pen.up()
    pen.pensize(pensize)
    pen.speed(speed)
pen_settings(up_down="up")


#__SM__// draws a rectangle by pos and size that are tuple ( revise / quizz )
def draw_rectangle(pos, size, color="white", pensize=3):
    global status
    pen.goto((pos[0]-0.5*size[0]+30), (pos[1]-0.5*size[1])) #// going to position
    pen_settings(up_down="down", color=color, pensize=pensize)
    for i in (size[0], size[1], size[0], size[1]):  #/
        pen.fd(i-60)                                #// drawing 
        pen.circle(30,90)                           #/
    pen_settings(up_down="up")


#__SM__// procedure that is used to write in screen
def write(string, pos=(0,170), clear=True, color="white", align="center"):
    global status
    pen.color(color)
    pen.goto(pos[0],pos[1])
    if clear:
        pen.clear()
    if len(string) > 50: #// to go to the next line if the sentence is long
        for i in range(1, int(len(string)/50)+1):
            index = string.find(" ", i*50)
            string = list(string)
            string[index] = " \n"
            string = "".join(string)
    pen.write(string, align=align, font=("Arial", 20, "normal"))    


#__SM__//function that takes place when the screen is clicked
def clicked(x, y):
    global status, index, end_of_words
    if status == "main menu":
        if (x<100 and x>-100) and (y>120 and y<180):    # R
            draw_rectangle((0,140),(200,60), color="green")
            time.sleep(0.2)
            revise()
        elif (x<100 and x>-100) and (y>60 and y<120):   # Qz
            draw_rectangle((0,80),(200,60), color="green")
            time.sleep(0.2)
            quizz()
        elif (x<100 and x>-100) and (y>-10 and y<60):   # A
            draw_rectangle((0,20),(200,60), color="green")
            time.sleep(0.2)
            add_words()
        elif (x<100 and x>-100) and (y>-70 and y<-10):  # Qt
            draw_rectangle((0,-40),(200,60), color="green")
            time.sleep(0.2)
            quit()
    elif status == "quizz" or status == "add words":
        if (x<85 and x>-85) and (y>50 and y<110):    # back to main menu
                draw_rectangle((0,80),(170,60), color="green")
                time.sleep(0.2)
                main_menu()
                
    elif status == "revise":
        draw_rectangle((150,-100),(150,60))
        write("Next", pos=(150,-110), clear=False)

        draw_rectangle((-150,-100),(150,60))
        write("Previous", pos=(-150,-110), clear=False)
        
        if (x<225 and x>75) and (y>-130 and y<-70) and ( not end_of_words ):
            draw_rectangle((150,-100),(150,60), color="green")
            time.sleep(0.1)
            write("Next", pos=(150,-110), clear=False)
            index += 1
        elif (x>-225 and x<-75) and (y>-130 and y<-70) and ( not end_of_words ):
            draw_rectangle((-150,-100),(150,60),color="green")
            time.sleep(0.1)
            write("Previous", pos=(-150,-110), clear=False)
            index -= 1
        if end_of_words:
            if (x<85 and x>-85) and (y>50 and y<110):
                draw_rectangle((0,80),(170,60), color="green")
                time.sleep(0.2)
                main_menu()
            elif (x<85 and x>-85) and (y>-10 and y<60):
                draw_rectangle((0,20),(170,60), color="green")
                time.sleep(0.2)
                if index < 0:
                    index += 1
                else:
                    index -= 1
                end_of_words = False
        if status == "revise":
            try:
                write(list_words[index]+" -- "+list_definitions[index], pos=(-300, 130), align="left", color="black")
            except IndexError:
                end_of_words = True            
            if end_of_words:
                write("Main menu", pos=(0,70))    
                draw_rectangle((0,80),(170,60))

                draw_rectangle((0,20),(170,60))
                write("Previous", pos=(0,10), clear=False)
            else:
                draw_rectangle((150,-100),(150,60))
                write("Next", pos=(150,-110), clear=False)

                draw_rectangle((-150,-100),(150,60))
                write("Previous", pos=(-150,-110), clear=False)


#__SM__// Function which read words & definitions from file and adds them to lists
def read_from_file_to_lists():
    global list_definitions, list_words, end_of_words
    with open("List__of__words.txt", "r") as file:
        word = file.readline()
        while word != "":
            definition = file.readline()
            new_line = file.readline()

            list_words.append(word.strip())
            list_definitions.append(definition.strip())
            
            word = file.readline()


def main_menu():
    global status, end_of_words, index
    status = "main menu"
    end_of_words = False
    index = 0
    write("", clear=True)
    write("Revise", pos=(0,130), clear=False)
    write("Quizz", pos=(0,70), clear=False)
    write("Add words", pos=(0,10), clear=False)
    write("Quit", pos=(0,-50), clear=False)

    draw_rectangle((0,140),(200,60))    #// Revise
    draw_rectangle((0,80),(200,60))     #// Quizz
    draw_rectangle((0,20),(200,60))     #// Add words
    draw_rectangle((0,-40),(200,60))    #// Quit


def add_words():
    global status
    status = "add words"
    pen.clear()
    with open("List__of__words.txt", "a") as file:
        num_words = turtle.numinput("Input", "Number of words you want to enter: ")
        if num_words == None:
            main_menu()
        else:
            num_words = int(num_words)
            list_words = []
            for i in range(num_words):
                word = turtle.textinput("Input", "The new word: ")
                if word == None:
                    main_menu()
                    break
                else:
                    list_words.append(word)
                    definition = turtle.textinput("Input", "The definition of the word: ")
                    if definition == None:
                        main_menu()
                    else:
                        file.write(word)
                        file.write("\n"+definition)
                        file.write("\n\n")
                        write(str(i+1)+" / "+str(num_words)+" words")
                        for j in range(i+1):
                            write(list_words[j], clear=False, pos=(100, 130-j*25), align="left", color="black")
            if word != None:
                write("Main menu", pos=(0,70), clear=False)    
                draw_rectangle((0,80),(170,60))


            
def quizz():
    global status
    status = "quizz"
    pen.clear()

    #// filling the lists worsd & definitions read from file
    read_from_file_to_lists()

    #// quizz
    num_words = turtle.numinput("Input", "Enter number of latest words that you want to revise:")
    if num_words == None:
        main_menu()
    else:
        num_words = int(num_words)
        for i in range(num_words):
            random_word = random.choice(list_definitions)
            write(random_word)
            user_answer = turtle.textinput("INPUT", "Enter the word that matches the definition:")
            if user_answer == None:
                main_menu()

                break
            elif user_answer.lower() == list_words[list_definitions.index(random_word)].lower():
                write("Correct", color="green")
                time.sleep(0.85)
            else:
                write("Incorrect", color="red")
                time.sleep(0.85)
        if user_answer != None:
            write("Main menu", pos=(0,70))    
            draw_rectangle((0,80),(170,60))

def revise():
    global status, index, list_words, list_definitions
    status = "revise"
    pen.clear()
    list_words = []
    list_definitions = []
    
    read_from_file_to_lists()
    index = 0
    write(list_words[index]+" -- "+list_definitions[index], clear=False, pos=(-300, 130), align="left", color="black")
    index = 1

    draw_rectangle((150,-100),(150,60))
    write("Next", pos=(150,-110), clear=False)

    draw_rectangle((-150,-100),(150,60))
    write("Previous", pos=(-150,-110), clear=False)
    

main_menu()
turtle.onscreenclick(clicked)
