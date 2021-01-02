import time
import pyautogui as auto
import os
import keyboard

amount = 0


def run(_time, stop):
    global amount

    for i in range(_time):
        time.sleep(1)
        os.system('CLS')
        print(f"time: {_time - i} |\t for stop pinch:'{stop}'\t |\tamount:{amount}")

        if keyboard.is_pressed(stop):
            return

    auto.click(button='right')
    amount += 1
    run(_time, stop)


def main():
    run(
        int(input("Время между кликами в секундах: \t")),
        input("Клавиша останова: \t")
    )
    return


if __name__ == "__main__":
    main()
