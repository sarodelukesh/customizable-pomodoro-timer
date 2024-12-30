import time
import os
import sys
import select

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_timer(minutes, seconds):
    clear_terminal()
    big_digits = {
        '0': ["  0000  ", " 00  00 ", "00    00", "00    00", "00    00", " 00  00 ", "  0000  "],
        '1': ["   11   ", "  111   ", "   11   ", "   11   ", "   11   ", "   11   ", "  1111  "],
        '2': ["  2222  ", " 22  22 ", "     22 ", "   222  ", "  22    ", " 22     ", " 222222 "],
        '3': ["  3333  ", "33    33", "     33 ", "   333  ", "     33 ", "33    33", "  3333  "],
        '4': ["   444  ", "  4444  ", " 44 44  ", "44  44  ", "44444444", "    44  ", "    44  "],
        '5': [" 555555 ", " 55     ", " 55555  ", "     55 ", "     55 ", "55   55 ", " 55555  "],
        '6': ["  6666  ", " 66     ", "66      ", "666666  ", "66    66", "66    66", " 66666  "],
        '7': ["77777777", "     77 ", "    77  ", "   77   ", "  77    ", " 77     ", "77      "],
        '8': ["  8888  ", "88    88", "88    88", "  8888  ", "88    88", "88    88", "  8888  "],
        '9': ["  9999  ", "99    99", "99    99", "  999999", "      99", "     99 ", "  9999  "],
        ':': ["        ", "   ::   ", "   ::   ", "        ", "   ::   ", "   ::   ", "        "]
    }

    time_str = f"{minutes:02}:{seconds:02}"
    lines = [""] * 7
    for char in time_str:
        for i in range(7):
            lines[i] += big_digits[char][i] + "  "

    for line in lines:
        print(line.center(os.get_terminal_size().columns))

def pomodoro_timer(work_minutes, break_minutes):
    total_seconds = work_minutes * 60

    while total_seconds:
        minutes, seconds = divmod(total_seconds, 60)
        display_timer(minutes, seconds)
        time.sleep(1)
        total_seconds -= 1

        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            command = sys.stdin.readline().strip()
            if command.lower() == 'stop':
                print("Timer stopped.")
                return
            elif command.lower() == 'reset':
                print("Timer reset.")
                return pomodoro_timer(work_minutes, break_minutes)

    print("Time's up! Take a break.")
    total_seconds = break_minutes * 60
    while total_seconds:
        minutes, seconds = divmod(total_seconds, 60)
        display_timer(minutes, seconds)
        time.sleep(1)
        total_seconds -= 1

    print("Break's over! Back to work.")

if __name__ == "__main__":
    work_minutes = int(input("Enter work session duration (in minutes): "))
    break_minutes = int(input("Enter break duration (in minutes): "))
    print("Enter 'stop' to stop the timer or 'reset' to reset it.")
    pomodoro_timer(work_minutes, break_minutes)

