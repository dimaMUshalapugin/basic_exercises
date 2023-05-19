# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])



# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'е', 'у', 'ы', 'о', 'э', 'я', 'и', 'ю']
print(len([letter for letter in word if letter.lower() not in vowels]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
spisok = []
for letter in sentence.split():
    spisok.append(len(letter))
print(int(sum(spisok)/len(sentence.split())))