number = int(input())

while number:
    H, W, N = map(int, input().split())

    floor = N%H
    room = N/H+1

    if floor == 0:
        floor = H
        room -= 1

    print("%d%02d"%(floor,room))

    number -= 1