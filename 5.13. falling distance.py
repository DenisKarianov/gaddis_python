# show falling distance
def falling_distance(seconds):
    distance = (9.8 * seconds ** 2) / 2
    return distance


def main():
    # make cycle to show falling distance for time from 1 to 10 seconds
    for i in range(1, 11):
        print(f'{falling_distance(i)}')


main()
