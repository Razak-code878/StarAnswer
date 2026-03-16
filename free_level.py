simp_cyc1_1 = """for i in range(7):
    fill_cell()
    move_right()
    move_right()
fill_cell()
"""

simp_cyc1_2 = """for i in range(14):
    move_right()
fill_cell()
for i in range(6):
    move_down()
for i in range(14):
    move_left()
fill_cell()
for i in range(14):
    move_right()"""

simp_cyc1_3 = """fill_cell()
for i in range(14):
    move_right()
    fill_cell()
for i in range(6):
    move_down()
    fill_cell()"""

simp_cyc1_4 = """for i in range(6):
    move_down()
fill_cell()
for i in range(13):
    move_right()
    fill_cell()
move_up()
move_right()
fill_cell()
for i in range(5):
    move_up()
    fill_cell()
for i in range(6):
    move_down()
fill_cell()"""

simp_cyc1_5 = """for i in range(14):
    move_right()
for i in range(14):
    fill_cell()
    move_down()
    move_left()
    fill_cell()
while free_from_right():
    move_right()"""

# -- SIMP_CYC2 --

simp_cyc2_1 = """for i in range(14):
    fill_cell()
    move_right()
    fill_cell()"""

simp_cyc2_2 = """for i in range(14):
    move_right()
fill_cell()
for i in range(6):
    move_down()"""

simp_cyc2_3 = """for i in range(14):
    fill_cell()
    move_right()
    fill_cell()
for i in range(6):
    move_down()"""

simp_cyc2_4 = """for i in range(14):
    fill_cell()
    move_down()
    move_right()
    fill_cell()"""


















