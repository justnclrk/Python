# Write a program that prints a 'checkerboard' pattern to the console.
# Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alternate stars and spaces. The goal is to repeat a process several times. This should make you think of looping.
print('Range Counter')
for count in range(0, 4):
    print("* * * * ")
    print(" * * * *")

print('Checkerboard Function')


def checkerboard():
    for i in range(8):
        if i % 2 == 0:
            print("* " * 4)
        else:
            print(" *" * 4)


checkerboard()
