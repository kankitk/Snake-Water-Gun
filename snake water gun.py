import random, time
comp,d,player,i=0,0,0,1
def win(s1,s2):
    r1="computer"
    r2="you"
    if s1==s2:
        return "draw"
    if s1 == "s":
        if s2 == "w":
            return "computer"
        if s2 == "g":
            return "you"
    if s1 == "w":
        if s2 == "g":
            return "computer"
        if s2 == "s":
            return "you"
    if s1 ==  "g":
        if s2 == "s":
            return "computer"
        if s2 == "w":
            return "you"
print("eneter S for snake, W for water, G for gun\n")
while (i<=10):
    ran="ankit"

    y=input(f"round {i}\n")
    y=y.lower()
    string1=["s","w","g"]
    if y not in string1:
        print ("wrong input, please try again")
        continue
    c=random.choice(string1)
    ran=win(c,y)
    print (c)
    if ran=="draw":
        d=d+1
        print ("DRAW")
    elif ran=="computer":
        comp=comp+1
        print("COMPUTER WINS")
    else:
        player=player+1
        print ("YOU WIN")
    print (f"computer = {comp},     your = {player},    draw = {d}\n\n")
    i=i+1
if comp>player:
    print("******sorry! you loose******\n\n")
elif comp == player:
    print("******match draw******\n\n")
else:
    print("******hurray! you won******\n\n")
time.sleep(3)
