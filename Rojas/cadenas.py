#1. INDEXACION++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                   1         2         3         4         5
#         012345678901234567890123456789012345678901234567890132
mensaje=("No todos aquellos que viajan sin rumbo están perdidos")

# 1.Acceder el inidice 36 -> b
print(mensaje[36])
# 2.Acceder el inidice 44 -> r
print(mensaje[47])
# 3.Acceder el inidice 34 -> u
print(mensaje[34])
# 4.Acceder el inidice 03 -> t
print(mensaje[3])
# 5.Acceder el inidice 24 -> a
print(mensaje[24])
# 6.Acceder el inidice 13 -> l
print(mensaje[13])
# 7.Acceder el inidice 07 -> s
print(mensaje[7])
# 8.Acceder el inidice 41 -> t
print(mensaje[41])
# 9.Acceder el inidice 26 -> a
print(mensaje[26])
# 10.Acceder el inidice 33 -> r
print(mensaje[33])
# 11.Acceder el inidice 03 -> t
print(mensaje[3])
# 12.Acceder el inidice 03 -> p
print(mensaje[45])
# 13.Acceder el inidice 03 -> l
print(mensaje[14])
# 14.Acceder el inidice 03 -> a
print(mensaje[26])
# 15.Acceder el inidice 03 -> N
print(mensaje[0])


#2. LONGITUD++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1.Imprimir la longitud de la palabra "hello" la cual es:5
salut="hello"
print(len(salut))

# 2.Imprimir la longitud de la palabra "magneta" la cual es:7
color="magneta"
print(len(color))

# 3.Imprimir la longitud de la palabra "pelota" la cual es:6
objeto="pelota"
print(len(objeto))

#4.Imprimir la longitud de la palabra "apio" la cual es:4
verd="apio"
print(len(verd))

# 5.Imprimir la longitud de la palabra "uva" la cual es:3
frut="uva"
print(len(frut))

# 6.Imprimir la longitud de la palabra "correr" la cual es:6
acc="correr"
print(len(acc))

# 7.Imprimir la longitud de la palabra "programacion" la cual es:12
curso="programacion"
print(len(curso))

# 8.Imprimir la longitud de la palabra "UNPRG" la cual es:5
uni="UNPRG"
print(len(uni))

# 9.Imprimir la longitud de la palabra "pedro" la cual es:5
name="pedro"
print(len(name))

# 10.Imprimir la longitud de la palabra "help" la cual es:4
alp="help"
print(len(alp))

# 11.Imprimir la longitud de la palabra "code" la cual es:4
bet="code"
print(len(bet))

# 12.Imprimir la longitud de la palabra "edit" la cual es:4
cin="edit"
print(len(cin))

# 13.Imprimir la longitud de la palabra "plugin" la cual es:6
dud="plugin"
print(len(dud))

# 14.Imprimir la longitud de la palabra "python" la cual es:6
eps="python"
print(len(eps))

# 15.Imprimir la longitud de la palabra "tetminal" la cual es:8
fix="terminal"
print(len(fix))


#3. COMPARACION+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1.Comparar si las dos cadenas son iguales
xat="hola"
yet="como estas"
print(xat == yet)

# 2.Comparar si las dos cadenas son diferentes
frut="uva"
verd="apio"
print(verd != frut)

# 3.Comparar si las dos cadenas son iguales
acc="correr"
curso="programacion"
print(acc == curso)

# 4.Comparar si las dos cadenas son diferentes
name="pedro"
uni="UNPRG"
print(name != uni)

# 5.Comparar si las dos cadenas son iguales
color="magneta"
farge="magneta"
print(color == farge)

# 6.Comparar si una de las cademas es mayor que la otra
eps="python"
bet="code"
print(eps > bet)

# 7.Comparar si una de las cademas es mayor que la otra
cin="edit"
dud="plugin"
print(cin < dud)

# 8.Comparar si una de las cademas es mayor que la otra
fix="terminal"
salut="hello"
print(salut < fix)

# 9.Comparar si una de las cademas es mayor que la otra
one="mente"
zes="entorno"
print(one > zes)

# 10.Comparar si una de las cademas es mayor o igual que la otra
two="lugar"
vijf="vida"
print(two >= vijf)

# 11.Comparar si una de las cademas es mayor o igual que la otra
three="cielo"
vier="frenesi"
print(three <= vier)

# 12.Comparar si una de las cademas es mayor o igual que la otra
four="limite"
drie="sombra"
print(four >= drie)

# 13.Comparar si una de las cademas es mayor o igual que la otra
five="mundo"
twee="ilusion"
print(five >= twee)

# 14.Comparar si una de las cademas es mayor o igual que la otra
six="futuro"
een="naturaleza"
print(een >= six)

# 15.Comparar si una de las cademas es mayor que la otra
sette="cultura"
minder="cultura"
print(sette < minder)


#4. CONCATENACION+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1.Mostrar el mensaje:"futuro entorno"
zes="entorno"
six="futuro"
print(six+" "+zes)

# 2.Mostrar el mensaje:" la cultura frenesi"
vier="frenesi"
sette="cultura"
print("la"+" "+sette+" "+vier)

# 3.Mostrar el mensaje: "mundolimite"
five="mundo"
four="limite"
print(five+four)

# 4.Mostrar el mensaje: "la sombra de la vida"
drie="sombra"
vijf="vida"
print("la"+" "+drie+" "+"de"+" "+"la"+" "+vijf)

# 5.Mostrar el mensaje: "lo escencial es invisible a los ojos"
mede=" escencial "
osem=" invisible "
tiri=" ojos"
print("lo"+mede+"es"+osem+"a"+" "+"los"+tiri)

# 6.Mostrar el mensaje: "
tiri=" ojos"
umi="puerta"
eka="alma"
print("los"+tiri+" "+"son"+" "+"la"+" "+umi+" "+"del"+" "+eka)

# 7.Mostrar el mensaje: "ultrasuperahorro"
eli="ultra"
ner="super"
iwa="ahorro"
print(eli+ner+iwa)

# 8.Mostrar el mensaje:
bet="code"
cin="edit"
print("I"+" "+cin+" "+"your"+" "+bet)

# 9.Mostrar el mensaje:
acc="correr"
dud="plugin"
print(acc+" "+dud)

# 10.Mostrar el mensaje:"hola pedro"
print(xat+" "+name)

# 11.Mostrar el mensaje:"mente frenesi"
print(one+" "+vier)

# 12.Mostrar el mensaje: "pelota magneta"
print(objeto+" "+color)

# 13.Mostrar el mensaje: "programacion python"
print(curso+" "+eps)

# 14.Mostrar el mensaje:"ilusion terminal"
print(twee+" "+fix)

# 15.Mostrar el mensaje:"lugar de cultura"
print(two+" "+"de"+" "+minder)


#5. CORTADO DE CADENAS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#                   1         2         3         4         5         6         7         8         9         0         1
#         01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901324567890123456789012
beskjed=("La mayoría de los hombres son como hojas que caen y revolotean indecisas mientras que otras son como los astros: " \
#                2         3         4         5         6         7         8         9         0         1       
#         34567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890   
         "siguen una ruta fija,ningún viento los alcanza y llevan en su interior su propia ley y trayectoria")
print(len(beskjed))

# 1.Del mensaje anterior imprimir: "hojas"
print(beskjed[35:40])

# 2.Del mensaje anterior imprimir: "interior"
print(beskjed[175:183])

# 3.Del mensaje anterior imprimir: "viento"
print(beskjed[141:147])

# 4.Del mensaje anterior imprimir: "trayectoria"
print(beskjed[200:211])

# 5.Del mensaje anterior imprimir: "astros"
print(beskjed[105:111])

# 6.Del mensaje anterior imprimir: "hombres"
print(beskjed[18:25])

# 7.Del mensaje anterior imprimir: "ruta"
print(beskjed[124:128])

# 8.Del mensaje anterior imprimir: "ningún viento los alcanza"
print(beskjed[134:159])

# 9.Del mensaje anterior imprimir: "los hombres son como hojas"
print(beskjed[14:40])

# 10.Del mensaje anterior imprimir: "en su interior su propia ley "
print(beskjed[169:197])

# 11.Del mensaje anterior imprimir: "siguen una ruta fija"
print(beskjed[113:133])

# 12.Del mensaje anterior imprimir: "son como los astros"
print(beskjed[92:111])

# 13.Del mensaje anterior imprimir: "la hoja cae"
print(beskjed[0:2]+beskjed[34:39]+beskjed[44:48])

# 14.Del mensaje anterior imprimir: "un hombre lleva su ley fija"
print(beskjed[120:122]+beskjed[17:24]+beskjed[161:167]+beskjed[183:186]+beskjed[193:197]+beskjed[128:133])

# 15.Del mensaje anterior imprimir: "p e r ú"
print(beskjed[187:188]+beskjed[12:13]+beskjed[52:53]+beskjed[138:139])


#6. ITERACION+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#1.Imprimir la palabra
nam="mejor"
for letra in nam:
    print(letra)

#2.Imprimir la palabra
nem="ser"
for letra in nem:
    print(letra)

#3.Imprimir la palabra
pen="temido"
for letra in pen:
    print(letra)

#4.Imprimir la palabra
lin="que"
for letra in lin:
    print(letra)

#5.Imprimir la palabra
zan="amado"
for letra in zan:
    print(letra)

#6.Imprimir la palabra
dro="---"
for letra in dro:
    print(letra)

#7.Imprimir la palabra
its="El"
for letra in its:
    print(letra)

#8.Imprimir la palabra
il="FIN"
for letra in il:
    print(letra)

#9.Imprimir la palabra
fit="JUSTIFICA"
for letra in fit:
    print(letra)

#10.Imprimir la palabra
sub="LOS"
for letra in sub:
    print(letra)

#11.Imprimir la palabra
med="MEDIOS"
for letra in med:
    print(letra)

#12.Imprimir la palabra
uni="UNPRG"
for letra in uni:
    print(letra)

#13.Imprimir la palabra
esc="EPIE"
for letra in esc:
    print(letra)

#14.Imprimir la palabra
fim="FACFYM"
for letra in fim:
    print(letra)

#15.Imprimir la palabra
thm="python"
for letra in thm:
    print(letra)


#7. BUSQUEDA++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#1. Encontrar la "a" en la cadena "sombra"(5)
drie="sombra"
print(drie.find("a"))

#2. Encontrar la "d" en la cadena "vida" (0)
vijf="vida"
print(vijf.find("v"))

#3. Encontrar la "m" en la cadena "programacion" (6)
curso="programacion"
print(curso.find("m"))

#4. Encontrar la "l" en la cadena "alma" (1)
eka="alma"
print(eka.find("l"))

#5. Encontrar la "r" en la cadena "puerta" (3)
umi="puerta"
print(umi.find("r"))

#6. Encontrar la "u" en la cadena "cultura" (1)
sette="cultura"
print(sette.index("u"))

#7. Encontrar la "e" en la cadena "frenesi" (2)
vier="frenesi"
print(vier.index("e"))

#8. Encontrar la "s" en la cadena "sombra" (0)
drie="sombra"
print(drie.index("s"))

#9. Encontrar la "o" en la cadena "como estas" (1)
yet="como estas"
print(yet.index("o"))

#10. Encontrar la "n" en la cadena "mundo" (2)
five="mundo"
print(five.index("n"))

#11. Encontrar la "i" en la cadena "limite" (1)
four="limite"
print(four.index("i"))

#12. Encontrar la "a" en la cadena "hola" (3)
xat="hola"
print(xat.index("a"))

#13. Encontrar la palabra "cielo" en la cadena "el cielo azul"
clo="el cielo azul"
print(clo.find("cielo"))

#14. Encontrar la palabra "brillante" en la cadena "la cadena brillante"
rpr="la cadena brillante"
print(rpr.index("brillante"))

#15. Encontrar la palabra "nuevo" en la cadena "el celular nuevo"
kgr="el celular nuevo"
print(kgr.find("nuevo"))


#8. OPERACIONES EMBEBIDAS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#1.Contar todas las "o" en el siguiente texto
text="Vemos las cosas, no como son, sino como somos nosotros"
print(text.count("o"))
#2.Convertir la cadena a minusculas
fit="JUSTIFICA"
print(fit.lower())
#3.converitir la cadena a mayusculas
clo="el cielo azul"
print(clo.upper())
#4.Reemplazar "verdad" por la palabra "falsedad"
str="Debo encontrar una verdad que sea verdad para mí"
print(str.replace("verdad","falsedad"))
#5.Devolver la cadena sin espacios en blanco
cad="             Hi everyone"
print(cad.strip())
#6.dividir la cadena por $
tring="Hace$falta$una$vida$para$aprender$a$vivir"
print(tring.split("$"))
#7.comprobar si la cadena esta compuesta por numeros
dgi="123456"
print(dgi.isdigit())
#8.comprobar si la cadena es alfanumerica
alf="16546ads"
print(alf.isalnum())
#9.comprobar si la cadena tiene caracteres del alfabeto
fbet="65463541s"
print(fbet.isalpha())
#10.devolver la cadena en mayusculas
vijf="vida"
print(vijf.upper())
#11.rempplazar la palabra "hombre" por "ser humano"
edtt="El hombre no está hecho para la derrota. Un hombre puede ser destruido, pero no derrotado"
print(edtt.replace("hombre","ser humano"))
#12.hacer en matusculas
fra="Lo mucho se vuelve poco con desear otro poco más"
print(fra.upper())
#13.convertir a minusculas
uni="UNPRG"
print(uni.lower())
#14.comprobar si la cadena es de numeros
cji="sdf64565"
print(cji.isdigit())
#15.comprobar si la cadean tiene elemntos ASCII
gru="656345635sd@"
print(gru.isascii())



