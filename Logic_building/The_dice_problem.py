
#You are given a cubic dice with 6 faces. All the individual faces have a number printed on them.
# The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of the cube, 
# your task is to guess the number on the opposite face of the cube.

def cube_dice(n):
    if n > 6 or n < 1:
        return "Invalid input"
    else:
        return 7 - n
    
if __name__ == "__main__":
    print(cube_dice(6))
    print(cube_dice(5))