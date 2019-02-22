
turno = str(input('Digite seu turno: M-matutino ou V-Vespertino ou N- Noturno: '))

if turno == 'M':    #o usuario estuda de manha?
    print( 'Bom Dia !!')        
elif turno == 'V':  #o usuario estuda a tarde? 
    print ('Boa Tarde!!' )       
elif turno == 'N':  #o usuario estuda de noite?
    print ('Boa Noite!!')        
else:    
    print ('Intrada invalida')
