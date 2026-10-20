import subprocess
import sys
import time

def check_program(filepath):
    start_time = time.time()

    try:
        result = subprocess.run([sys.executable, filepath], 
            capture_output=True, 
            text=True, 
            timeout=10
        )

        elapsed_time = time.time() - start_time

        print("Програма завершиался")
        print(f"Час виконання: {elapsed_time:.2f} секунд")

        if result.returncode != 0:
            print("Програма завершилася з помилкою:")

        if result.stdout:
            print("Вивід програми:")
            print(result.stdout)

        if result.stderr:
            print("Помилки програми:")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("Програма перевищила ліміт часу виконання (10 секунд) і була зупинена.")

    except FileNotFoundError:
        print(f"Файл '{filepath}' не знайдено. Перевірте шлях до файлу.")

    except Exception as err:
        print(f"Сталася помилка при виконанні програми: {err}")

flepath = input("Введіть шлях до файлу програми: ")
check_program(flepath)
