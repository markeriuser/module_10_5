import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Выход из цикла при пустой строке
                break
            all_data.append(line.strip())
    # Для демонстрации, можно вывести количество строк, считанных из файла
    print(f"Считано {len(all_data)} строк из {name}")

if __name__ == '__main__':
    
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейный вызов: {linear_duration:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multiprocessing_duration = time.time() - start_time
    print(f"Многопроцессный вызов: {multiprocessing_duration:.6f} секунд")
