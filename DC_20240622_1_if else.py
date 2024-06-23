# age = int(input('Please enter age:'))
# file_types = {
#     ".txt": "Text File",
#     ".pdf": "PDF Document",
#     ".jpg": "JPEG Image"}
# print(file_types)
# marks = [70,80,85,99,91,88,40]
# i = 1
# for i in range(0, len(marks), 1):
#     if marks[i] >= 90:
#         print('Master class:', marks[i])
#     elif marks[i] >= 80:
#         print('Expert class', marks[i])
#     elif marks[i] >= 70:
#         print('Experienced class', marks[i])
#     else:
#         print('Need to focus on subject', marks[i])
l =[1,2,3,4,5]
print(l)
i=1
l1 = []
l2 = []
for i in range(0,len(l), 1):
    l1.append(l[i]+1)

for i in l:
    l2.append(i+1)
print(l1)
print('l2', l2)

##
strl1 =[]
num1 = []
strl =[12,23,'skills', 'masters', 'trained', 'course',12.10, 25.00]
for i in strl:
    if type(i) == str:
        strl1.append(i)
    elif type(i) == int or type(i) == float:
        num1.append(i)
print(strl1)
print(num1)


