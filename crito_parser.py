#This script is to parse the crito text into two lists, one for crito & one for socrates

#generator function which returns the text w/ out newlines as a string 
def readFile(filename: str):
    with open(filename) as file:
        text = ''
        for line in file:
            line = line.lower().strip().split()
            for word in line:
                if word != '\n':
                    text = text + word + ' '
                else:                    # replace any newlines w/ a space
                    word = ''
                    text = text + word             
    return text


#function that returns two lists, the 1st w/ socrates' dialogue & the 2nd w/ crito's dialogue
#for some reason the very last line of the book is not captured
def separate():
    text = readFile('data/crito.txt')
    soc = list()
    crit = list()
    flag = 's'      #set to s b/c he socrates starts talking first, will be set to c when crito is talking

    text = text.split()
    dialogue = ''
    for word in text:
        if word == 'socrates:':
            flag = 's'
            if dialogue != '':
                crit.append(dialogue)
            dialogue = ''
                
        elif word == 'crito:':
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
    with open('train/crito_train.json', 'w') as file:
        file.write('{\"training_data\": [\n')
        for s, c in zip(soc[1:], crit[1:]):
            file.write(f'{{\"prompt\": \"{c}\", \"completion\": \"{s}\"}}')     #store data in a way where crito is prompt
            
            file.write(',\n')                                                    # and socrates is the completion
        file.write(']}')
            


main()
