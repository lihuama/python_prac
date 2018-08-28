file_name = input("File name:\n> ")
print(f"\nCreating your file \'{file_name}\'....\n")
txt = open(file_name,'w+')

line1 = 'I am a superman.'
line2 = 'No blood, no revolution.'
line3 = 'He, the one who changed the world.'

def wline(a,n):
    a.write(eval('line'+str(n))+'  length='+str(len(eval('line'+str(n)))))
    a.write("\n")

for i in range(1,4):
    wline(txt,i)

txt.seek(0)

print(f"{file_name}:")
print(txt.read())