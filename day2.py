filename = 'input/2.txt'

test = False

test_ranges = ('11-22,95-115,998-1012,1188511880-1188511890,222220-222224,'
               '1698522-1698528,446443-446449,38593856-38593862,565653-565659,'
               '824824821-824824827,2121212118-2121212124')

repeat_IDs = []
numbers_max = []
add_sum = False
summation = 0

def main(ranges):
    global add_sum
    global summation
    ranges_split = ranges.split(',')
    for rangeOfID in ranges_split:
        lower, upper = rangeOfID.split('-')
        numbers_max.append(int(lower))
        numbers_max.append(int(upper))
        for num in range(int(lower), int(upper)+1):
            num_s = str(num)
            length = int(len(num_s))
            if (length % 2) == 0:
                length_12 = int(length / 2)
                if num_s[:length_12] == num_s[length_12:]:
                    add_to_sum(num)
                    continue
            if (length % 3) == 0:
                length_13 = int(length / 3)
                if num_s[:length_13] == num_s[length_13:length_13*2] == num_s[length_13*2:]:
                    add_to_sum(num)
                    continue
            if (length % 4) == 0:
                length_14 = int(length / 4)
                if num_s[:length_14] == num_s[length_14:length_14*2] == num_s[length_14*2:length_14*3] == num_s[length_14*3:]:
                    add_to_sum(num)
                    continue
            if (length % 5) == 0:
                length_15 = int(length / 5)
                if num_s[:length_15] == num_s[length_15:length_15*2] == num_s[length_15*2:length_15*3] == num_s[length_15*3:length_15*4] == num_s[length_15*4:]:
                    add_to_sum(num)
                    continue
            if (length % 6) == 0:
                length_16 = int(length / 6)
                if num_s[:length_16] == num_s[length_16:length_16*2] == num_s[length_16*2:length_16*3] == num_s[length_16*3:length_16*4] == num_s[length_16*4:length_16*5] == num_s[length_16*5:]:
                    add_to_sum(num)
                    continue
            if (length % 7) == 0:
                length_17 = int(length / 7)
                if num_s[:length_17] == num_s[length_17:length_17*2] == num_s[length_17*2:length_17*3] == num_s[length_17*3:length_17*4] == num_s[length_17*4:length_17*5] == num_s[length_17*5:length_17*6] == num_s[length_17*6:]:
                    add_to_sum(num)
                    continue
            if (length % 8) == 0:
                length_18 = int(length / 8)
                if num_s[:length_18] == num_s[length_18:length_18*2] == num_s[length_18*2:length_18*3] == num_s[length_18*3:length_18*4] == num_s[length_18*4:length_18*5] == num_s[length_18*5:length_18*6] == num_s[length_18*6:length_18*7] == num_s[length_18*7:]:
                    add_to_sum(num)
                    continue
            if (length % 9) == 0:
                length_19 = int(length / 9)
                if num_s[:length_19] == num_s[length_19:length_19*2] == num_s[length_19*2:length_19*3] == num_s[length_19*3:length_19*4] == num_s[length_19*4:length_19*5] == num_s[length_19*5:length_19*6] == num_s[length_19*6:length_19*7] == num_s[length_19*7:length_19*8] == num_s[length_19*8:]:
                    add_to_sum(num)
                    continue
            if (length % 10) == 0:
                length_110 = int(length / 10)
                if num_s[:length_110] == num_s[length_110:length_110*2] == num_s[length_110*2:length_110*3] == num_s[length_110*3:length_110*4] == num_s[length_110*4:length_110*5] == num_s[length_110*5:length_110*6] == num_s[length_110*6:length_110*7] == num_s[length_110*7:length_110*8] == num_s[length_110*8:length_110*9] == num_s[length_110*9:]:
                    add_to_sum(num)
                    continue
    print(summation)


def add_to_sum(num):
    global summation
    global add_sum
    repeat_IDs.append(num)
    summation += num


if __name__ == '__main__':
    if test:
        ranges = test_ranges
    else:
        with open(filename, encoding='UTF=8') as file:
            ranges = file.read()

    print(f'Done')