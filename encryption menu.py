import math
Symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
def ceaser(text,key):
    c = input('to encrpyt the message type \'E\', to decrypt the message type \'D\' :')
    global etext
    etext = ''
    for m in text :
        if m in Symbols:
            index = Symbols.find(m)
            if c == 'E':
                new_index = index + key
            elif c == 'D':
                new_index = index - key
            if new_index >= len(Symbols):
                new_index -= len(Symbols)
            elif new_index< 0 :
                new_index += len(Symbols)


            etext += Symbols[new_index]

    print (etext)

def sub(text):
    
    key = input('Enter the key for substitution cipher : ')
    while len(key)< 26 :
        key = input('The key needs to be at least 26 characters long ')
    global etext
    etext = ''
    for m in text :
        index = text.find(m)
        etext += key[index]
    print(etext)
        


def ceaser_bd (text):
    for x in range(len(Symbols)):
        global etext
        etext = ''
        for m in text :
            if m in Symbols:
                index = Symbols.find(m)
                new_index = index - (x+1)
                if new_index <0 :
                    new_index += len(Symbols)
                etext += Symbols[new_index]
        print('try number #',x+1,':',etext)

def transpositione(text,key):
    c = input('to encrpyt the message type \'E\', to decrypt the message type \'D\' :')
    if c == 'E':
        global etext
        etext = ['']*key
        for x in range(key):
            index = x
            while index<len(text):
                etext[x]+= text[index]
                index += key
        print(''.join(etext))
    elif c == 'D':
        columns = math.ceil(len(text)/float(key))
        rows = key
        etext = ['']*columns
        shadedboxes = (columns*rows) - len(text)
        co = 0
        ro= 0
        for x in text:
            etext[co]+= x
            co += 1
            if co == columns or (co == columns-1 and ro >=rows - shadedboxes):
                co = 0
                ro+=1
        print(''.join(etext))

def jump(text,key):
    global etext
    etext = ''
    c =input('To encrypt press \'E\' and to Decrypt press \'D\'')
    if c == 'E':
        for x in (text):
            if x in Symbols :
                index = Symbols.find(x)
                new_index = index*key
                if new_index > len(Symbols ):
                    new_index -= len(Symbols)
                etext += Symbols[new_index]
    else :
        for x in (text):
            if x in Symbols:
                index = Symbols.find(x)
                new_index = index/key
                if new_index > len(Symbols ):
                    new_index -= len(Symbols)
                etext += Symbols[new_index]

    print (etext)

def jumpbf(text):
    global etext
    etext = ''
    for x in range(50):
        for y in text:
            if y in Symbols:
                index = Symbols.find(y)
                new_index = index/ (x+1)
                etext += Symbols[new_index]
                print ('PRESS CONTROL C TO END THE LOOP IF YOU FOUND THE TEXT')
        
        

def tranbd(text):
    global etext
    for y in range(math.ceil(len(text)/2)):
        key = y+1
        columns = math.ceil(len(text)/float(key))
        rows = key
        etext = ['']*columns
        shadedboxes = (columns*rows) - len(text)
        co = 0
        ro= 0
        for x in text:
            etext[co]+= x
            co += 1
            if co == columns or (co == columns-1 and ro >=rows - shadedboxes):
                co = 0
                ro+=1
        print('attempt# ',y+1,':',''.join(etext))




def main():
    print ('menu for encryption and decryption :\n 1)Ceaser \n 2)Transposition \n 3) Jump \n 4) Substitution ')
    content = input('Do you want to use a file or a text (F/T):')
    if content == 'T':
        t = input ('Kindly input the text :')
    elif content == 'F':
        name = input ('Enter the file name with extension')
        file = open(name)
        t = file.read()
        file.close()
    menu = int(input('choose from the menu :'))
    if menu == 1 :
        k = input('Do you have the key ?(Y/N) :')
        if k == 'Y':
            ke = int(input('What is the encryption or decryption key ?: '))
            ceaser(t,ke)
        else :
            ceaser_bd(t)
    if menu == 2:
        k = input('Do you have the key ?(Y/N) :')
        if k == 'Y':
            ke = int(input('What is the encryption or decryption key ?: '))
            transpositione(t,ke)
        else :
            tranbd(t)
    if menu == 3:
        k = input('Do you have the key (Y/N)?')
        if k == 'Y':
            ke = int(input('What is the encryption or decryption key'))
            jump (t,ke)
        elif k == 'N':
            jumpbf(text)
    if menu == 4:
        k = input('Do you have the key (Y/N)?')
        if k == 'Y':
            
            sub (t)
        elif k == 'N':
            jumpbf(text)
            

    cho = input('Do you want to store this data into a text file ?(Y/N)')
    if cho == 'Y':
        naam = input('Enter the name of the file to be created')
        file = open(naam+'txt','w')
        file.write (''.join(etext))
main()
di = 0

while di == 0:
    i = input('Do you want to run it again (Y/N)?')
    
    if i == 'Y':
        di = 0
        main()
    else :
        di = 1







def gcd(a,b):
    while a!= 0 :
        a,b = b%a,a
    return b


def modinverse(a,m):
    if gcd(a,m)!=1:
        return none
    u1,u2,u3 = 1,0,a
    v1,v2,v3 =0,1,m
    while v3 !=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m



    
    
            
            
    
    
    
            
    
   
        




                

                    
            
    
    

    
