phrase = input('Винни, спой пожалуйста: ').split()

glasnye = ['у', 'е', 'ё', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю']

list_1 = []
for i in range (len(phrase)):
    clicker = 0
    for j in range (len(phrase[i])):
        if phrase[i][j] in glasnye:
            clicker += 1
    list_1.append(clicker)

counter = 0
for i in range (1, len(list_1)):
    if list_1[i] != list_1[i-1]:
        counter +=1

if counter == 0:
    print('С ритмом все в порядке')
else:
    print('Над ритмом стоит поработать еще')
