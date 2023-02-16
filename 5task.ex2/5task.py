f2 = open("text_words.txt", 'w+')
f1 = open('text_code_words.txt', 'w+')
text_rle = str(input('Введите текст: '))
a = f2.write(text_rle)
f2.close()
f2 = open('text_words.txt', 'r')

file_text = f2.readlines()
file_text = list(''. join (file_text))
print(file_text)



def rle_count(string):
    count = 0
    new_string = ''
    element = string[0]
    for i in range(1, len(string)):
        if string[i] == element:
            count += 1
        else:
            new_string = new_string + str(count) + element
            element = string[i+1]
            count = 1
    return new_string




a2 = f1.write(rle_count(file_text))

