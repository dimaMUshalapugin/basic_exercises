# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])



# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len([j for j in ''.join(word) if j.lower() == 'а']))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len([j for j in ''.join(word) if j.lower() not in ['а', 'е', 'у', 'ы', 'о', 'э', 'я', 'и', 'ю']]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for i in ''.join(sentence).split():
    print(i[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
q = []
for i in sentence.split():
    q.append(len(i))
print(int(sum(q)/len(sentence.split())))