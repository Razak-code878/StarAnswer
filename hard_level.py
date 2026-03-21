
# СР цикл While

hard_while1_1 = """while not cell_is_filled():
    move_right()"""

hard_while1_2 = """while cell_is_filled():
    move_up()"""

hard_while1_3 = """if not free_from_right():
    while free_from_left():
        move_left()
else:
    total = 0
    while not cell_is_filled():
        move_right()
        total += 1
    if total == 2:
        for i in range(5):
            move_left()"""

hard_while1_4 = """move_down()
if not free_from_down():
    for _ in range(7):
        move_up()
else:
    if cell_is_filled():
        while free_from_down():
            move_down()
    else:
        move_down()
        if cell_is_filled():
            pass
        else:
            while free_from_up():
                move_up()"""

hard_while1_5 = """if free_from_down():
    if not cell_is_filled():
        for _ in range(3):
            move_right()
else:
    if cell_is_filled():
        while free_from_right():
            move_right()
    else:
        while free_from_right():
            move_right()
        move_left()"""

hard_while1_6 = """if free_from_right():
    if cell_is_clean():
        while free_from_down():
            move_down()
        move_up()
    else:
        while free_from_down():
            move_down()
        if not cell_is_filled():
            while free_from_up():
                move_up()
else:
    for _ in range(4):
        move_down()"""

hard_while1_7 = """while free_from_right():
    fill_cell()
    move_right()
fill_cell()
if free_from_up():
    while free_from_up():
        move_up()
    while free_from_left():
        fill_cell()
        move_left()
    fill_cell()"""

hard_while1_8 = """if free_from_left():
    move_left()
    if free_from_left():
        move_left()
        move_left()
        move_down()
        while free_from_up():
            fill_cell()
            move_up()
        fill_cell()
        while free_from_right():
            move_right()
        while free_from_down():
            fill_cell()
            move_down()
        fill_cell()
    else:
        fill_cell()
        while free_from_right():
            move_right()
        fill_cell() 
        if free_from_down():
            move_down()
            fill_cell()
            move_left()
            fill_cell()
else:
    while free_from_down():
        fill_cell()
        move_down()
    while free_from_up():
        fill_cell()
        move_up()
    fill_cell()"""

hard_while1_9 = """while free_from_left():
    move_left()
fill_cell()
while free_from_right():
    move_right()
fill_cell()"""

hard_while1_10 = """while free_from_down():
    move_down()
while free_from_right():
    move_right()
fill_cell()
while free_from_up():
    move_up()
fill_cell()
while free_from_left():
    move_left()
fill_cell()
while free_from_down():
    move_down()
fill_cell()"""

hard_while1_11 = """while free_from_right():
    move_right()
    fill_cell()
while not free_from_down():
    move_left()
while free_from_down():
    move_down()
    fill_cell()
while free_from_up():
    move_up()
while not free_from_left():
    fill_cell()
    move_down()
while free_from_left():
    move_left()
    fill_cell()
while not free_from_down():
    move_right()"""


# Задание на оценку «Цикл FOR»

hard_for1_1 = """if cell_is_filled():
    move_down()
    fill_cell()
    move_right()
    move_up()
    if cell_is_filled():
        move_down()
        fill_cell()
        while free_from_right():
            move_right()
            fill_cell()
    else:
        move_down()
        while free_from_right():
            move_right()
        fill_cell()
else:
    move_down()
    while free_from_right():
        move_right()
        move_up()
        if cell_is_filled():
            move_down()
            fill_cell()
        else:
            move_down()"""

hard_for1_2 = """while free_from_up():
    if cell_is_filled():
        move_right()
        fill_cell()
        move_left()
        move_up()
    else:
        move_right()
        if cell_is_filled():
            move_left()
            fill_cell()
            move_up()
        else:
            move_left()
            move_up()
       
if cell_is_filled(): # 3,5,7
    move_right()
    fill_cell()
else:
    move_right()
    if cell_is_filled(): #1,4,6,8
        move_left()
        fill_cell()
        move_right()
    else:
        pass
"""

hard_for1_3 = """fill_cell()
move_up()
if free_from_left():
    move_left()
    fill_cell()#1,3,5,6
    try:
        while free_from_left():
            for _ in range(2):
                move_left()
            move_up()
            move_right()
            fill_cell()
            for _ in range(2):
                move_up()
            move_left()
            move_down()
            fill_cell()
    except Exception:
        move_left()
        fill_cell()

else: #2,4
    move_up()
    move_left()
    move_down()
    fill_cell()
    try:
        for _ in range(8):
            move_left()
            move_up()
            fill_cell()
    except Exception:
        try:
            while free_from_left():
                move_left()
                move_up()
                move_right()
                fill_cell()
                move_up()
                move_up()
                move_left()
                move_down()
                fill_cell()
                move_left()
        except Exception:
            move_down()
            move_left()
            move_up()
            fill_cell()"""

hard_for1_4 = """while free_from_right():
    move_right()
    if not free_from_right():
        if free_from_down():
            move_down()
        else:
            move_up()
if free_from_down():
    move_down()
while free_from_right():
    move_right()
    if not free_from_right():
        if free_from_down():
            move_down()
        else:
            move_up()
if free_from_up():
    move_up()"""

hard_for1_5 = """while free_from_right():
    move_right()
while free_from_down():
    fill_cell()
    move_down()
    move_left()
fill_cell()
while free_from_up():
    move_up()
while free_from_down():
    fill_cell()
    move_down()
    move_right()
fill_cell()"""
