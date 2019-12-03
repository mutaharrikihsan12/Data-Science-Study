#jawaban no 1
def remove_outlier(data):
    dataSorted = sorted(data)
    mid = len(data) // 2
    data1 = dataSorted[0 : mid]
    data3 = dataSorted[-mid: ]
    if (len(data1) % 2 != 0):
        q1 = data1[len(data1)//2]
    else:
        q1 = (data1[len(data1)//2] + (data1[(len(data1)//2)-1])) / 2
    if (len(data3) % 2 != 0):
        q3 = data3[len(data3)//2]
    else:
        q3 = (data3[len(data3)//2] + (data3[(len(data3)//2)-1])) / 2
    IQR = q3 - q1
    lower_limit = q1 - (1.5*IQR)
    upper_limit = q3 + (1.5*IQR)
    newdata = []
    for item in data:
        if(item > lower_limit and item < upper_limit):
            newdata.append(item)
    print('data asli adalah {}'.format(data))
    print('data setelah di sort {}'.format(dataSorted))
    print('setengah data pertama {}'.format(data1))
    print('setengah data kedua {}'.format(data3))
    print('upper limit adalah {}'.format(upper_limit))
    print('lower limit adalah {}'.format(lower_limit))
    print('data yang tidak outlier adalah = {}'.format(newdata))

remove_outlier([71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69])


#jawaban no 2
def count_vowel(words):
    jumlah_vowel = 0
    vowel = 'aiueo'
    for item in words:
        if(item.lower() in vowel):
            jumlah_vowel += 1
    print(jumlah_vowel)

count_vowel('budi pergi ke pasar')

#jawaban no 3
def given(num_list):
    new_list = []
    for item in num_list:
        for element in item:
            new_list.append(element)
            new_list.sort()
    print(new_list)

given([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]])

#jawaban no 4
def countwords(words):
    wordlist = words.split(' ')
    count_dict = {}
    for item in wordlist:
        if(item in count_dict.keys()):
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    for key, value in count_dict.items():
        print("Jumlah kata '{}' ada sebanyak {}".format(key.capitalize() , value))

countwords('jangan jangan kamu adalah aku')