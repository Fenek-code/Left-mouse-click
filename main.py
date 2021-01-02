import datetime
import time
import pyautogui
import os
import keyboard


def run(_time, stop, start, amount, status, start_time):
    for i in range(_time):

        # Set time to zero (only needed for display)
        temp = datetime.timedelta(seconds=0)
        if status:
            # Find out how much time has passed since launch
            temp = str(datetime.timedelta(seconds=int(time.time() - start_time)))
            # Counting
            amount += 1
        else:
            i = 0  # don't let the loop move until we start the process

        time.sleep(1)
        os.system('CLS')  # Screen cleaner, only works on Windows

        print(f"{'(work)' if status else '[resting]'}"
              f"\n\nleft to click: {_time - (i)}"
              f"\nfor stop  pinch: '{stop}'"
              f"\nfor start pinch: '{start}'"
              f"\namount: {amount}"
              f"\ntime at work: {temp}"
              )

        if keyboard.is_pressed(stop):
            status = False  # click through time - off

        if keyboard.is_pressed(start):
            start_time = time.time()  # write the start time

            amount = 0  # cancel the account
            status = True  # click through time - on

    if status:
        pyautogui.click(button='right')  # press the right mouse button
    run(_time, stop, start, amount, status, start_time)  # do recursion


def main():
    run(
        int(input("Time between clicks in seconds: \t")),
        input("Stop key: \t"),
        input("Start key: \t"),
        0,
        False,
        time.time()
    )
    return


if __name__ == "__main__":
    main()
