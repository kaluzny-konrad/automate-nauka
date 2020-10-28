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

print('\n\nv1 - read\n')
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

print('\n\nv4 - with for\n')
with open(bacon_file_name) as baconFile:
    for line in baconFile:
        print(line)

print('\n\nv5 - with read\n')
with open(bacon_file_name) as baconFile:
    content = baconFile.read()
    print(content)