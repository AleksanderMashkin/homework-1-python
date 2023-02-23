import model
import view
import datetime as dt

def start():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    print('Выберите операцию')
    choice = input('1. Add\n2. Subtract\n3. Multiply\n4. Divide\n')
    if choice == '1':
        result = model.sum()
        view.show(result)
    elif choice == '2':
        result = model.diff()
        view.show(result)
    elif choice == '3':
        result = model.multi()
        view.show(result)
    elif choice == '4':
        result = model.divis()
        view.show(result)
    else:
        print('Неккоректный выбор операции')
    time = dt.now().strftime('%H:%M')
    with open ('log.csv', 'a') as file:
        file.write('{value_a} - первое число, {value_b} - второе число, {result} - результат'.format(time))



    

