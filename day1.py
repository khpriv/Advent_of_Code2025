test_moves = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

moves = []


def main(moves):
    print('- The dial starts by pointing at 50.')
    currentPoint = 50
    setOnZeroCounter = 0
    for move in moves:
        if move[:1] == 'L':
            currentPoint = currentPoint - (int(move[1:]) % 100)
        if move[:1] == 'R':
            currentPoint = currentPoint + (int(move[1:]) % 100)
        if currentPoint < 0:
            currentPoint = 100 + currentPoint
        if currentPoint > 99:
            currentPoint = currentPoint - 100
        if currentPoint == 100:
            currentPoint = 0
        if currentPoint == 0:
            setOnZeroCounter += 1
        print(f'- The dial is rotated {move.rstrip('\n')} to point at {currentPoint}.')
    print('Password is ' + str(setOnZeroCounter))


if __name__ == '__main__':
    with open('input/1.txt', encoding='UTF=8') as file:
        moves = file.readlines()
    main(moves)
    print(f'Done')

