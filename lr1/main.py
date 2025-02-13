import subprocess
import os
import time

file_path = "taylor.py"
print("Введіть A: ")
A = input()
print("Введіть B: ")
B = input()
print("Введіть крок: ")
steps = input()

id_terminal = {}

while True:
    print("1 - створити потоки")
    print("2 - видалити потік")
    print("3 - змінити пріоритет потоку")
    print("0 - вийти")
    print("Введіть команду: ")
    i = input()

    if i == "1":
        print("Введіть кількість потоків(до 8):")
        ii = input()

        for j in range(int(ii)):
            terminal_name = f"Terminal{j+1}"
            start_time = time.time()  

            process = subprocess.Popen(["xterm", "-hold", "-T", terminal_name, "-e", "python3", "taylor.py", A, B, steps])

            id_terminal[terminal_name] = {"pid": process.pid, "start_time": start_time}

            print(f"Термінал {terminal_name} створено з PID: {process.pid}")

    elif i == "2":
        print("Введіть ім'я потоку, який потрібно видалити:")
        terminal_name = input()

        if terminal_name in id_terminal:
            pid = id_terminal[terminal_name]["pid"]
            subprocess.Popen(["kill", str(pid)])
            elapsed_time = time.time() - id_terminal[terminal_name]["start_time"]
            print(f"Термінал {terminal_name} з PID {pid} був видалений. Час роботи: {elapsed_time:.2f} секунд.")
            del id_terminal[terminal_name]
        else:
            print(f"Термінал з ім'ям {terminal_name} не знайдений в словнику.")

    elif i == "3":
        print("Введіть ім'я потоку для зміни пріоритету:")
        terminal_name = input()

        if terminal_name in id_terminal:
            print("Введіть новий пріоритет:")
            new_priority = input()
            subprocess.Popen(["renice", new_priority, str(id_terminal[terminal_name]["pid"])])
            print(f"Пріоритет термінала {terminal_name} змінено.")
        else:
            print(f"Термінал з ім'ям {terminal_name} не знайдений в словнику.")

    elif i == "0":
        break

# sudo gnome-system-monitor

