import random 

deleted_word = 'абв'
words = ['абв', 'авб', 'бав', 'бва', 'ваб', 'вба', 'абв', 'авб', 'бав', 'бва', 'ваб', 'вба', 'абв', 'авб', 'бав', 'бва', 'ваб', 'вба']
word = []

count_words = int(input('Введите количество элементов: '))
word = random.sample(words, count_words)
print(word)


new_list = list(filter(lambda x: x != deleted_word, word))
print(new_list)

