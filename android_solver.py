# This program allows the sudoku_solver.py script to interact with an android emulator running the app
# 'Sudoku - The Clean One'.

import pyautogui
import time
import sudoku_solver

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

startx, starty = pyautogui.locateCenterOnScreen('./numbers/back.png')
startx = startx - 20
starty = starty + 73

def board_scanner():
    # Scan for Number 1s
    pyautogui.click(startx + 60, starty + 512)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x*52), int(starty + y*52), (168, 181, 189), tolerance=10):
                board[y][x] = 1

    # Scan for Number 2s
    pyautogui.click(startx + 141, starty + 512)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x*52), int(starty + y*52), (168, 181, 189), tolerance=10):
                board[y][x] = 2

    # Scan for Number 3s
    pyautogui.click(startx + 220, starty + 512)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x*52), int(starty + y*52), (168, 181, 189), tolerance=10):
                board[y][x] = 3

    # Scan for Number 4s
    pyautogui.click(startx + 301, starty + 512)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x * 52), int(starty + y * 52), (168, 181, 189), tolerance=10):
                board[y][x] = 4

    # Scan for Number 5s
    pyautogui.click(startx + 376, starty + 512)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x * 52), int(starty + y * 52), (168, 181, 189), tolerance=10):
                board[y][x] = 5

    # Scan for Number 6s
    pyautogui.click(startx + 60, starty + 597)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x * 52), int(starty + y * 52), (168, 181, 189), tolerance=10):
                board[y][x] = 6

    # Scan for Number 7s
    pyautogui.click(startx + 141, starty + 597)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x * 52), int(starty + y * 52), (168, 181, 189), tolerance=10):
                board[y][x] = 7

    # Scan for Number 8s
    pyautogui.click(startx + 220, starty + 597)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x * 52), int(starty + y * 52), (168, 181, 189), tolerance=10):
                board[y][x] = 8

    # Scan for Number 9s
    pyautogui.click(startx + 301, starty + 597)
    time.sleep(.25)
    for y in range(9):
        for x in range(9):
            if pyautogui.pixelMatchesColor(int(startx + x * 52), int(starty + y * 52), (168, 181, 189), tolerance=10):
                board[y][x] = 9


def fill_in():
    # Place Number 1s
    pyautogui.click(startx + 60, starty + 512)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 1:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 2s
    pyautogui.click(startx + 141, starty + 512)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 2:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 3s
    pyautogui.click(startx + 220, starty + 512)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 3:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 4s
    pyautogui.click(startx + 301, starty + 512)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 4:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 5s
    pyautogui.click(startx + 376, starty + 512)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 5:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 6s
    pyautogui.click(startx + 60, starty + 597)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 6:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 7s
    pyautogui.click(startx + 141, starty + 597)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 7:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 8s
    pyautogui.click(startx + 220, starty + 597)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 8:
                pyautogui.click(int(startx + x*52), int(starty + y*52))

    # Place Number 9s
    pyautogui.click(startx + 301, starty + 597)
    time.sleep(.25)
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 9:
                pyautogui.click(int(startx + x*52), int(starty + y*52))


print('\n\nEmpty Board:')
sudoku_solver.printb(board)
board_scanner()
print('\n\nScanned Board:')
sudoku_solver.printb(board)
sudoku_solver.solve(board)
print('\n\n\nSolved Board:')
sudoku_solver.printb(board)
print('\n\n')
print(board)
fill_in()
