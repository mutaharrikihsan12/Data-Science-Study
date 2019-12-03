data = [71, 70, 73, 70, 70, 69, 70, 72, 71, 300, 71, 69]
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
print(new_data)
        