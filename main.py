import time

COMM_TXTFILE = 'weighted-scores-calculator.txt'

def check_errors(file):
    """Checks for errors in the file and returns an error statement."""
    error = None
    if len(lines) < 2:
        error = "Error: Parameters missing. See Documentation for details."
    else:
        for i in range(1,len(lines)):
            line_arr = lines[i].split(',')
            if len(line_arr) != 3:
                error = "Error: Priority category is missing data."
            elif not line_arr[1].strip().isnumeric() or not line_arr[2].strip().isnumeric():
                error = "Error: Priority category weight or score is not a number"
    return error

def build_2d_arr(received_data):
    """Builds 2d array"""
    sum_w = 0
    arr = []
    headers = []
    data_row = []
    for i in range(len(lines)+1):
        if i == 0:
            headers.append('Item ID')
            data_row.append(lines[i].strip()) # append item identifier
        elif i == len(lines):
            headers.append('Total Weighted Score')
            data_row.append(sum_w)
        else:
            line = lines[i].split(',')
            headers.append(line[0] + ' (' + line[1] + ')')  # add priority category and weight in paranthesis in header
            data_row.append(line[2].strip()) # append unweighted score

            sum_w += int(line[1]) * int(line[2])
    arr.append(headers)
    arr.append(data_row)
    return arr

def sort_arr(arr):
    """Sorts array in non-ascending order with item identifier as first element"""
    new_arr = [arr[0]]
    for i in range(1, len(arr)):
        line = arr[i].split(',')
        if i == 1 or int(line[1]) < int(first_new_arr_line[1]):
            new_arr.append(arr[i])
        else:
            new_arr.insert(1, arr[i])
        first_new_arr_line = new_arr[1].split(',')
    return new_arr

def is_sorted(arr):
    """Checks if categories are sorted in non-ascending order"""
    for i in range(1, len(arr)):
        line = arr[i].split(',')
        line_weight_int = int(line[1])
        if i > 1 and line_weight_int > prev_line_weight_int:
            return False
        prev_line_weight_int = line_weight_int
    return True

if __name__ == '__main__':
    while True:
        time.sleep(5)
        with open(COMM_TXTFILE, 'r', newline='\n') as f:
            lines = f.readlines()
            if lines == []:
                continue

            error = check_errors(f)

        if error:
            with open(COMM_TXTFILE, 'w', newline='') as f:
                f.write(error)
            continue

        if not is_sorted(lines):
            lines = sort_arr(lines)

        arr = build_2d_arr(lines)

        with open(COMM_TXTFILE, 'w', newline='') as f:
            f.write(str(arr))

        time.sleep(20)
