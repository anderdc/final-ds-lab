#This script is to parse transcribed text between TWO participants
#set these variables to the names of the participants (all lower case) + the colon 
#***************************
prompter = 'b:'     #prompter MUST be the person who starts speaking first
speaker = 's:'
#**************************

#returns the text of a file in a string
def readFile(filename: str):
    with open(filename) as file:
        text = ''
        for line in file:
            line = line.lower().strip().split()
            for word in line:
                if word != '\n':
                    text = text + word + ' '
                else:      # replace any newlines w/ a space
                    pass           
    return text


#function that returns two lists, the 1st w/ socrates' dialogue & the 2nd w/ crito's dialogue
#for some reason the very last line of the book is not captured
def separate():
    #***************************
    text = readFile('./data/mrbeast.txt') # change the file to parse the transcript you want
    #***************************

    soc = list()
    crit = list()
    flag = 's'      #set to s b/c he socrates starts talking first, will be set to c when crito is talking

    text = text.split()
    dialogue = ''
    for word in text:
        if word == prompter:
            flag = 's'
            if dialogue != '':
                crit.append(dialogue)
            dialogue = ''
                
        elif word == speaker:
            flag = 'c'
            if dialogue != '':
                soc.append(dialogue)
            dialogue = ''

        else:
            if dialogue == '':
                dialogue = word
            else:
                dialogue = dialogue + ' ' + word

    return (soc, crit)



def main():
    soc, crit = separate()
    #***************************
    with open('train/mrbeast_train.json', 'w') as file:
    #***************************
        # file.write('{\"training_data\": [\n')
        for s, c in zip(soc, crit):
            file.write(f'{{\"prompt\": \"{c}\", \"completion\": \"{s}\"}}')    
            file.write('\n')
            # file.write(',\n')                                                   
        # file.write(']}')
            

main()
