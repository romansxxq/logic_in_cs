
def run_machine(input_text, max_steps=20):
    tape = list(input_text) or ["_"]
    head = 0
    state = "START"

    for step in range(max_steps):
        if state == "HALT":
            print(f"Машина зупинилася за {step} кроків.")
            print("Стрічка:", "".join(tape))
            return

        if head < 0:
            tape.insert(0, "_")
            head = 0

        if head >= len(tape):
            tape.append("_")

        symbol = tape[head]

        # Якщо символ 1, то рухаємося праворуч.
        if symbol == "1":
            head += 1

        # Якщо символ 0, тозупиняємося.
        elif symbol == "0":
            state = "HALT"

        # Порожня клітинка викликає нескінченний рух.
        else:
            head += 1

        print(
            f"Крок {step + 1}: "
            f"стан={state}, позиція={head}, "
            f"стрічка={''.join(tape)}"
        )

    print(f"Машина не зупинилася за {max_steps} кроків.")
    print("Це не доводить, що вона ніколи не зупиниться.")


data = input("Введіть стрічку: ")
run_machine(data)
