import random

notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

NUM_NOTES = len(notes)
EXERCISE_5_TIMES = 10
EXERCISE_6_TIMES = 6


def main():
    if get_iteration() < EXERCISE_5_TIMES:
        print('Exercise 5,', get_iteration() + 1, 'out of', EXERCISE_5_TIMES)
        exercise5()
    else:
        print('Exercise 6,', get_iteration() + 1 - EXERCISE_5_TIMES, 'out of',
              EXERCISE_6_TIMES)
        exercise6()
    update_iteration()

def randomnotes(num):
    if num > NUM_NOTES:
        return
    notes_left = notes.copy()
    note_order = ""
    for idx in range(num):
        next_note = notes_left[random.randint(0, NUM_NOTES - idx - 1)]
        note_order += next_note
        note_order += " "
        notes_left.remove(next_note)
    return note_order
    
def exercise5():
    print(randomnotes(2))

def exercise6():
    print(randomnotes(7))

def get_iteration():
    file = open('Desktop/python/iteration.txt', 'r')
    return int(file.read())

def update_iteration():
    iteration = (get_iteration() + 1)%(EXERCISE_5_TIMES + EXERCISE_6_TIMES)
    file = open('Desktop/python/iteration.txt', 'w')
    file.write(str(iteration))

main()
