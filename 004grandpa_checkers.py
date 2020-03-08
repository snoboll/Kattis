def run():
    dim = int(input())
    board = []
    for line in range(dim):
        board.append(list(input()))

    for row in board:
        bcount = 0
        wcount = 0
        white = 0
        black = 0
        for pos in row:
            if pos == "B":
                black += 1
                bcount += 1
                wcount = 0
            elif pos == "W":
                white += 1
                wcount += 1
                bcount = 0
            if(bcount >= 3 or wcount >= 3):
                print("0")
                return
        if(black != white):
            print("0")
            return

    board = list(map(list, zip(*board)))
    for col in board:
        bcount = 0
        wcount = 0
        white = 0
        black = 0
        for pos in col:
            if pos == "B":
                black += 1
                bcount += 1
                wcount = 0
            elif pos == "W":
                white += 1
                wcount += 1
                bcount = 0

            if(bcount >= 3 or wcount >= 3):
                print("0")
                return
        if(black != white):
            print("0")
            return

    print("1")
if __name__ == "__main__":
    run()
