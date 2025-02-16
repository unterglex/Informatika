from random import seed, randint
seed(213)
x=randint(1,9)
print('Рандом:',x)
'''На основании результатов соревнований по прыжкам в длину (фамилии и результаты трёх попыток) составить итоговый протокол соревнований, 
считая, что в зачёт идёт лучший результат.'''
def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as file: #без утф-8 у меня китайские иероглифы
        lines = file.readlines()
    data = []
    for line in lines:
        parts = line.split()  # Разделение строки на фамилию и результаты
        if len(parts) < 2:  # Если нет результатов попыток, пропускаем строку
            continue
        surname = parts[0]
        attempts = list(map(float, parts[1:]))
        data.append((surname, attempts))
    return data
def best_attempt(attempts):
    if not attempts:  # Если список пуст
        return 0
    return max(attempts)
def write_results(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for surname, best in data:
            file.write(f"{surname} {best}\n")
def main():
    input_filename = 'ggwp.txt'  # Файл с исходными данными
    output_filename = 'lala.txt'  # Файл для записи результатов
    data = read_data(input_filename)
    best_results = [(surname, best_attempt(attempts)) for surname, attempts in data]
    best_results.sort(key=lambda x: x[1], reverse=True)
    write_results(output_filename, best_results)
if __name__ == "__main__":
    main()
