adjective = input("Enter an adjective:\n")
noun = []
noun.append(input("Enter a noun:\n"))
verb = input("Enter a verb:\n")
noun.append(input("Enter a noun:\n"))

text = "The "
text += adjective
text += " panda walked to the "
text += noun[0] 
text += " and then " 
text += verb 
text += ". A nearby " 
text += noun[1] 
text += " was unaffected by these events.\n"

print(text)

file_name = "mad_libs.txt"
with open(file_name, 'w') as OpenFile:
    OpenFile.write(text)