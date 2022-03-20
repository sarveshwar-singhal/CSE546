import numpy as np
def main():
    arr =  [1, 2, 5, 3]
    pieces = [[5], [1, 2], [3]]
    cp_pieces = pieces.copy()
    cp_arr = arr.copy()
    for pie in cp_pieces:
        for ele in pie:
            if ele in cp_arr:
                cp_arr.remove(ele)
            else:
                return False
    print("first loop is executed")
    if cp_arr != []:
        return False
    print("secondd loop is executed")
    np_arr = np.array(arr)
    print(np_arr)
    print(pieces)
    for pie in pieces:
        np_pie = np.array(pie)
        # np_pie = pie
        print(np_pie)
        if np_pie not in np_arr:
            return False
    return True


if __name__ == '__main__':
    val = main()
    print(val)