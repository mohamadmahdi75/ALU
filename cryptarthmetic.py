import re
import itertools
from itertools import permutations

word="ODD + ODD == EVEN"


def a(word):  #ایمپورت ها انجام شود

    a=["{}*{}".format(10**i,d)    for (i,d) in enumerate(word[::-1]) ]
    if re.findall(r"[A-Z]+",word):   #اگر حروف بزرگ پیدا کردی
        return  "(" + "+".join(a) + ")"  #فقط در آن حروف ایندکس حرف را در خود حرف ضرب کن 
    else:
        return word #اگر نه پس خود علامت را برگردان



print(list(map(a,re.split(r"([A-Z]+)",word))))



ali=list(map(a,re.split(r"[\s]",word)))
akbar="".join(ali)
print("akbar=",akbar)

F="lambda {}:{}".format(''.join(set(re.findall(r"[A-Z]",word))), akbar  )


def faster_solve(formula):
    params=', '.join(set(re.findall(r"[A-Z]",word)))
    
    ali=list(map(a,re.split(r"[\s]",word)))
    akbar="".join(ali)



    F=eval("lambda {}:{}".format(params, akbar))
    
    letter=''.join(set(re.findall(r"[A-Z]",word)))


    for digit in itertools.permutations((1,2,3,4,5,6,7,8,9,0),len(letter)):
        try:
            if F(*digit) is True:
                table=str.maketrans(letter,''.join(map(str,digit)))

                return  formula.translate(table)

        except ArithmeticError:
            pass 


print("faster solve is=>",faster_solve(word))