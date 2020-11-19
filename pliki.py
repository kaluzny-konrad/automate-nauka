bacon_file_name = 'bacon.txt'

baconFile = open(bacon_file_name,'w')
baconFile.write('Hello, world!\n')
baconFile.close()

baconFile = open(bacon_file_name,'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open(bacon_file_name,'r')
content = baconFile.read()
baconFile.close()

print('\n\nv1 - read and close\n')
print(content)

text = ['Hello, world!\n']
text2 = ['Bacon is not a vegetable.']


with open(bacon_file_name, 'w') as baconFile:
    baconFile.writelines(text)

with open(bacon_file_name, 'a') as baconFile:
    baconFile.writelines(text2)

print('\n\nv2 - with readlines for\n')
with open(bacon_file_name) as baconFile:
    content = baconFile.readlines()
    for line in content:
        print(line)

print('\n\nv3 - with while if not break\n')
with open(bacon_file_name) as baconFile:
    while True:
        line = baconFile.readline()
        if not line:
            break
        print(line)



#BEST 1: gdy potrzebne wszystko razem
print('\n\nv4 - with read\n')
with open(bacon_file_name) as baconFile:
    content = baconFile.read()
    print(content)

#BEST 2: gdy każda linia osobno
print('\n\nv5 - with for\n')
with open(bacon_file_name) as baconFile:
    for line in baconFile:
        print(line)


# zapisywanie wyniku zmiennych i odczytywanie spowrotem
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie','Pooka','Bulbik']
print(cats)
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
cats2 = shelfFile['cats']
print(cats2)
shelfFile.close()
print('\n')

with shelve.open('mydata') as shelfFile:
    print(list(shelfFile.keys()))
    print(list(shelfFile.values()))