from PIL import Image
questionHaligtree = Image.open(r"C:\Program Files\Final Project\Haligtree.png")
questionHighnoon = Image.open(r"C:\Program Files\Final Project\McCree.png")
questionAthens = Image.open(r"C:\Program Files\Final Project\Socrates.png")
questionMoonwalk = Image.open(r"C:\Program Files\Final Project\Moonwalk.png")
questionDay = Image.open(r"C:\Program Files\Final Project\DDay.png")
triviaGame = Image.open(r"C:\Program Files\Final Project\Trivia.png")


triviaGame.show()
print('Welcome to the Multi category trivia game')
answer = input('Please select a category when you are ready to play: videogames, random, history, movies, music: ')
score=0
total_questions=5
 
if answer.lower()=='random':
    answer=input('Question 1: What year did the originial Xbox come out:"\n"A:1998"\n"B:2001"\n"C:2004"\n"D:2006 ')
    if answer.lower()=='b':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 2: True or false(Enter t or f)Q cross between a horse and a zebra is called a "Hobra  ')
    if answer.lower()=='f':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 3: What is the name of the largest ocean on Earth?"\n"A:Bering"\n"B:Mediterranean"\n"C:Arctic"\n"D:Pacific:  ')
    if answer.lower()=='d':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 4: Which college has the highest acceptance rate?:"\n"A:Covenant College"\n"B:University of Kansas"\n"C:University of Pikeville"\n"D:Houghton College ')
    if answer.lower()=='c':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 5: What was the best selling game system worldwide?"\n"A:Playstation 2"\n"B:Nintendo 3ds"\n"C:Atari 2600"\n"D:Playstation Portable ')
    if answer.lower()=='a':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer')

if answer.lower()=='videogames':
    answer=input('Question 1: In the game monster hunter world, who is controlling the weird outburst of the monsters?"\n"A:The fifth fleet"\n" B:Shanra Ishvalda"\n"C:Kuve Tolroth"\n" D:The headmaster')
    if answer.lower()=='b':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 2: In call of duty, who do you play as the most in Modern Warfare 3 Campaign?"\n"A:Yuri"\n"B:Makarov"\n"C:Soap"\n"D:Price ')
    if answer.lower()=='c':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
    questionHaligtree.show()
    answer=input('Question 3: In Elden ring, what is this area on the map?"\n"A:Calied"\n"B:Royal Capital"\n"C:Haligtree"\n"D:Limgrave ')
    if answer.lower()=='c':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
    questionHighnoon.show()
    answer=input('Question 4: In overwatch, how does high noon work in time to kill?"\n"A:Based on Health value"\n"B:Same charge up time all around"\n"C:Based on class of character"\n"D:None of the above  ')
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 5: In destiny 2, what exotic weapon was banned from the vanguard?"\n"A:Crimson"\n" B:Bad juju"\n"C:Red death"\n"D:Anarchy ')
    if answer.lower()=='a':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer')

if answer.lower()=='history':
    questionAthens.show()
    answer=input('Question 1: Who was the philosopher that died in Athens for thinking too much?"\n"A:Socrates"\n"B:Calis"\n"C:Alexander"\n"D:Acastus ')
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 2: What year did WW1 start?"\n"A:1918"\n"B:1914"\n"C:1910"\n"D:1900, ')
    if answer.lower()=='b':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 3: When was the Declaration of Independence signed?"\n"A:1800"\n"B:1790"\n"C:1776"\n"D:1780 ')
    if answer.lower()=='c':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 4: Which Pharaoh led the construction of the pyramids of Giza?"\n"A:Djoser"\n"B:Ramesses"\n"C:Amenhotep"\n"D:Khufu  ')
    if answer.lower()=='d':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')
    questionDay.show()
    answer=input('Question 5: What does the D in D-Day stand for?"\n"A:Designation"\n"B:Day"\n"C:Dread"\n"D:None of the above')
    if answer.lower()=='b':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer')

if answer.lower()=='movies':
    answer=input('Question 1: What is the actual last name of the character Rey in the newest star war triology?"\n"A:Palpatine"\n"B:Windu"\n"C:Skywalker"\n"D:We do not know')
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 2: In the Matrix, does neo take the blue pill or the red pill? "\n"A:Red "\n"B:Blue ')
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 3: For what movie did Steven Spielberg win his first Oscar for Best Director?"\n"A:The BFG"\n"B:Ready Player One"\n"C:Lincoln"\n"D:Schindlers List ')
    if answer.lower()=='d':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 4: What is the highest-grossing R-rated movie of all time?"\n"A:American Sniper"\n"B:Joker"\n"C:Deadpool"\n"D:Logan  ')
    if answer.lower()=='b':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 5: In Apocalypse Now, Robert Duvall says I love the smell of (what) in the morning?"\n"A:Naplam"\n"B:Blood"\n"C:Air"\n"D:None of the above')
    if answer.lower()=='a':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer')

if answer.lower()=='music':
    questionMoonwalk.show()
    answer=input('Question 1: Michael Jackson debuted his trademark moonwalk during which song in 1983?"\n"A:Billie Jean"\n"B:Smooth Criminal"\n"C:Beat it"\n"D:Earth Song')
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 2: In what year of the 80s did Madness split, eventually reforming as The Madness?"\n"A:1973"\n"B:1977"\n"C:1980"\n"D:1987 ')
    if answer.lower()=='c':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 3: How long ago was music created in years?"\n"A:32,047"\n"B:27,000"\n"C:35,000"\n"D:37,589 ')
    if answer.lower()=='c':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 4: Who replaced Ozzy Osbourne as Black Sabbaths leader singer?"\n"A:Ronnie James Dio"\n"B:Judas Priest"\n"C:Dokken"\n"D:Whitesnake ')
    if answer.lower()=='a':
        score += 1
        print('correct')
    else:
        print('Wrong Answer')

    answer=input('Question 5: Which singer released the album Alf?"\n"A:Michael Joseph Jackson"\n"B:Aretha Louise Franklin"\n"C:Alison Moyet"\n"D:Christopher Maurice')
    if answer.lower()=='c':
        score += 1
        print('Correct')
    else:
        print('Wrong Answer')






print('Thank you for Playing this small multi-category trivia game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Your score:',mark)
print('Have a good summer!')
