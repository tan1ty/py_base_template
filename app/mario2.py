def make_mario_pyramid():
    height = 0

    while True:
        try:
            height = int(input("Height: "))
            if height >= 1 and height <= 8:
                break
            else:
                print("Type height from 1 till 8")
        except ValueError:
            print("Type only integer")
                

    for i in range(height):
        spaces = " " * (height - i - 1)
        hashes = "#" * (i + 1)
        pyramid = spaces + hashes + "  " + hashes
        print(pyramid)

make_mario_pyramid()
