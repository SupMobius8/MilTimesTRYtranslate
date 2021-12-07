def loe_failist(f)->list:
    """Loeme failist read ja lisame järjendisee
    """
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas
rus_list=loe_failist("rus.txt")
eng_list=loe_failist("eng.txt")
print(rus_list)
print(eng_list)
def translate():
    """Loeme failist sõnad ja tõlkime neid kõrval
    """
    v1=int(input("1 - Rus to ENG\n2 - Eng to RUS: "))
    if v1==1:
        g=str(input("what word u want to translate?  "))
        loe_failist("rus.txt")
        if g not in rus_list:
            print("There is now word like this!")
        else:
            a=rus_list.index(g)
            print(rus_list[a]," - ",eng_list[a],"\n")
    elif v1==2:
        x=str(input("what word u want to translate?  "))
        loe_failist("eng.txt")
        if x not in eng_list:
            print("There is now word like this!")
        else:
            b=eng_list.index(x)
            print(eng_list[b]," - ",rus_list[b],"\n")
    return
def new_word():
    """Lisame sõnad to rus.txt and eng.txt
    """
    p=int(input("1 - Rus and ENG\n2 - Eng and RUS: "))
    if p==1:
        n1=str(input("What word would u like to add?  "))
        with open("rus.txt", "a",encoding="utf-8-sig") as f1:
            f1.write(f"\n{n1}")
        n2=str(input("What the translation of this word?  "))
        with open("eng.txt", "a") as f2:
            f2.write(f"\n{n2}")
        rus_list=loe_failist("rus.txt")
        eng_list=loe_failist("eng.txt")
        print(rus_list)
        print(eng_list)
    elif p==2:
        n2=str(input("What word would u like to add?  "))
        with open("eng.txt", "a") as f2:
            f2.write(f"\n{n2}")
        n1=str(input("What the translation of this word?  "))
        with open("rus.txt", "a",encoding="utf-8-sig") as f1:
            f1.write(f"\n{n1}")
        rus_list=loe_failist("rus.txt")
        eng_list=loe_failist("eng.txt")
        print(rus_list)
        print(eng_list)
def correct():
    print("\nYES ?!?!? Thats not cool, we need to change them!!!")
    k=int(input("1 - Rus word\n2 - Eng word\n3 - BOTH ?:  "))
    if k==1:
        word1=str(input("what word u want to change?  "))  
        word2=str(input("how u want to change? "))
        loe_failist("rus.txt")
        if word1 not in rus_list:
            print("There is now word like this!")
        else:
            with open ('rus.txt', 'r', encoding="utf-8-sig") as frus:
                old_data = frus.read()
            new_data1 = old_data.replace(f'{word1}',"{word2}")
            with open ('rus.txt', 'w', encoding="utf-8-sig") as frus:
                frus.write(new_data1)
    elif k==2:
        eword1=str(input("what word u want to change?  "))
        eword2=str(input("how u want to change? "))
        loe_failist("eng.txt")
        if eword1 not in eng_list:
            print("There is now word like this!")
        else:
            with open ('eng.txt', 'r') as feng:
                old_data = feng.read()
            new_data2 = old_data.replace(f'{eword1}','{eword2}')
            with open ('eng.txt', 'w') as feng:
                feng.write(new_data2)
    elif k==3:
        rusword1=str(input("what rus word u want to change?  "))
        rusword2=str(input("how u want to change? "))
        loe_failist("rus.txt")
        if rusword1 not in rus_list:
            print("There is now word like this!")
        else:
            with open ('rus.txt', 'r', encoding="utf-8-sig") as frus1:
                old_data = frus1.read()
            new_data3 = old_data.replace(f'{rusword1}', '{rusword2}')
            with open ('rus.txt', 'w', encoding="utf-8-sig") as frus1:
                frus1.write(new_data3)
        engword1=str(input("what eng word u want to change?  "))
        engword2=str(input("how u want to change? "))
        loe_failist("eng.txt")
        if engword1 not in eng_list:
            print("There is now word like this!")
        else:
            with open ('eng.txt', 'r') as feng1:
                old_data = feng1.read()
            new_data4 = old_data.replace(f'{engword1}', '{engword2}')
            with open ('eng.txt', 'w') as feng1:
                feng1.write(new_data4)

