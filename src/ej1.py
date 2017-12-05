if __name__ == '__main__':
    with open('input1.txt') as input_file:
        rows = [row.strip().lower() for row in input_file.readlines()]
        cols = [''.join(row) for row in zip(*rows)]
        rev_rows = [row[::-1] for row in rows]
        rev_cols = [col[::-1] for col in cols]
    count = 0
    for direction in [rows, cols, rev_rows, rev_cols]:
        for strip in direction:
            count += strip.count('hola')
    print(f'The soup contains the word "hola" {count} times.')
