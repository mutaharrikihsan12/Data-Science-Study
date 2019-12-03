
print('Name     :   Muhammad Ihsan Mutaharrik')
print('Class    :   JC Data Science')
print('Exam 1_Python Fundamental_Answer')

print('\n')
#Jawaban no 2
def countVowel(word):
    word = word.lower()
    word = list(word)
    vocal_list = []
    for item in word:
        if item in 'aiueo':
            vocal_list.append(item)
    hasil = len(vocal_list)
    return hasil

print('Jawaban Nomor 2 :')   
print(countVowel('budi pergi ke pasar'))
print(countVowel('purwadhika'))
print('\n')

#Jawaban no 4
def countWords(sentence):
    sen_dict = {}
    sentence = sentence.split(' ')
    for item in sentence: 
        if (item in sen_dict):
            sen_dict[item] += 1
        else:
            sen_dict[item] = 1
    keys_list = []
    value_list = []

    for elemen in sen_dict:
        keys_list.append(elemen)


    for item in sen_dict.values():
        value_list.append(item)


    out = ''
    for x in range(len(keys_list)):
        out += 'Jumlah Kata ' + '\'' + keys_list[x].capitalize() + '\'' + ' ada sebanyak ' + str(value_list[x]) + '\n'
    return out

print('Jawaban Nomor 4 : ')
print(countWords('jangan jangan kamu adalah aku'))
print('\n')

#Jawaban no 3 
def given(mylist):
    newlist = []
    for first_list_index in range(len(mylist)):
        for second_list_index in range(len(mylist[first_list_index])):
            newlist.append(mylist[first_list_index][second_list_index])
            newlist.sort()
    return newlist

print('Jawaban Nomor 3 : ')
print(given([[3,2,1],[4,6,5],[],[9,7,8]]))
print(given([[3,4,2,1],[1,2,3],[5,4,3,1]]))
print('\n')


#Jawaban no 1
def remove_outlier(data):
    data2 = data.copy()
    data.sort()
    print('data asli = ' ,end = ' ')
    print(data2)
    print('data setelah di sort = ' ,end = ' ')
    print(data)
    print('setengah data pertama = ' ,end =' ')
    print(data[0:(len(data) // 2)])
    print('setengah data terakhir = ' ,end = ' ')
    print(data[(len(data) // 2)  : len(data)])

    q1_list = data[0:(len(data) // 2)]
    q3_list = data[(len(data) // 2) : len(data)]

    q1 = (q1_list[len(q1_list) // 2] +  q1_list[(len(q1_list) // 2) - 1]) / 2
    print('q1 adalah = ' ,end = ' ')
    print(q1)

    q3 = (q3_list[len(q3_list) // 2] +  q3_list[(len(q3_list) // 2) - 1]) / 2
    print('q3 adalah = ' ,end = ' ')
    print(q3)

    IQR = q3 - q1

    lower_limit = q1 - (1.5*IQR)
    upper_limit = q3 + (1.5*IQR)

    print('lower limit adalah = ' ,end =' ')
    print(lower_limit)
    print('upper limit adalah = ' ,end =' ')
    print(upper_limit)

    new_data = []
    for i in range(len(data2)):
        if(data2[i] > lower_limit and data2[i] < upper_limit):
            new_data.append(data2[i])

    print('data yang tidak outlier = ' ,end =' ')
    return new_data

print('Jawaban Nomor 1 : ')
print(remove_outlier([71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69]))
print('\n')
