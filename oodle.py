import random
print('Game instructions are---->')
print('if * is appeard in your guess ,then that letter is correct and in correct position with  word.')
print('if @ is appeard in your guess , then that letter is present in the word but not in correct position with the word.')
print('if ? is appeard in your guess, then that letter is not there in the word.')
f=open("words.txt","r")
alltxt=f.read().split("\n")
word=random.choice(alltxt)
print(word)
print("Welcome to the wordle game ")
print("Guess the word :")
def check(w,wg):
    if w==wg:
        print("* "*len(w))
        print("Congratulation you guessed correctly")
        return 0
    else:
        s=""
        for x in wg:
            if x in w:
                if wg.index(x)==w.index(x):
                    s+="* "
                    w=w[w.index(x)+1:]
                    wg=wg[wg.index(x)+1:]
                else:
                    s+="@ "
                    w=w.replace(x," ",1)
                    wg=wg.replace(x," ",1)
            else:
                s+="? "
        print(s)
i=1
while i<=6:
    wordg=input("Enter the word: ")
    if wordg in alltxt and wordg.isalpha():
        l=check(word,wordg)
        if l==0:
            break
        i+=1
    else:
        print("Enter a valid word")
else:
    print("Better luck next time")

    
