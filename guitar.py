import random

guitar_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
legato_exercises = list(range(39, 58))
alt_picking_exercises = list(range(62, 79))
econ_picking_exercises = list(range(82, 88))
sweeping_exercises = list(range(93, 111))
combined_exercises = list(range(114, 125))
skipping_exercises = list(range(128, 137))

EXERCISE_4_TIMES = 10
EXERCISE_5_TIMES = 6

def shuffled_notes():
    new_notes = guitar_notes.copy()
    random.shuffle(new_notes)
    return new_notes

def get_iteration(num):
    if num == 4:
        file = open('Desktop/python/guitar/iteration4.txt', 'r')
    else:
        file = open('Desktop/python/guitar/iteration5.txt', 'r')
    return int(file.read())

def update_iteration(num):
    iteration = get_iteration(num) + 1
    if num == 4:
        iteration %= EXERCISE_4_TIMES
        file = open('Desktop/python/guitar/iteration4.txt', 'w')
    else:
        iteration %= EXERCISE_5_TIMES
        file = open('Desktop/python/guitar/iteration5.txt', 'w')
    file.write(str(iteration))

def has_sharp(note):
    return note in ['A', 'C', 'D', 'F', 'G']

def has_flat(note):
    return note in ['A', 'B', 'D', 'E', 'G']

def exercise2():
    notes = shuffled_notes()
    print('Exercise 2')
    for note in notes:
        print(note)

def exercise3():
    sharp_notes = guitar_notes.copy()
    sharp_notes = [note for note in sharp_notes if has_sharp(note)]
    sharp_notes = [note + ' sharp' for note in sharp_notes]
    flat_notes = guitar_notes.copy()
    flat_notes = [note for note in flat_notes if has_flat(note)]
    flat_notes = [note + ' flat' for note in flat_notes]
    notes = sharp_notes + flat_notes
    random.shuffle(notes)
    print('Exercise 3')
    for note in notes:
        print(note)
    
def exercise4():
    notes = shuffled_notes()
    print('Exercise 4,', get_iteration(4) + 1, 'out of', EXERCISE_4_TIMES)
    print(notes[0], notes[1])
    update_iteration(4)

def exercise5():
    notes = shuffled_notes()
    print('Exercise 5,', get_iteration(5) + 1, 'out of', EXERCISE_5_TIMES)
    print(notes[0], notes[1], notes[2], notes[3], notes[4], notes[5], notes[6])
    update_iteration(5)

def legato():
    exercises = legato_exercises.copy()
    return random.choice(exercises)

def picking():
    exercises = alt_picking_exercises.copy()
    exercises.extend((econ_picking_exercises.copy()))
    return random.choice(exercises)

def sweeping():
    exercises = sweeping_exercises.copy()
    return random.choice(exercises)

def misc_exercise():
    exercises = combined_exercises.copy()
    exercises.extend(skipping_exercises.copy())
    return random.choice(exercises)
