# app/main.py

import sys
from app import router
from app import memory_module

def main():
    print("Добро пожаловать в My AI Assistant!")
    memory = memory_module.Memory()

    while True:
        try:
            user_input = input("Введите ваш запрос (или 'выход' для завершения): ")
            if user_input.lower() in ['выход', 'exit']:
                print("Завершение работы. До свидания!")
                break

            response = router.route_request(user_input, memory)
            print(f"Ответ: {response}")

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            sys.exit(0)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
