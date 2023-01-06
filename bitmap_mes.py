def get_init_bitmap():
    with open('bitmap.txt','r') as bitmap_file:
        bitmap = bitmap_file.readlines()
    return bitmap


def get_input():
    return input('Enter the message to display with the bitmap.\n >')


def create_bitmap_message(bitmap,word):
    for i in range(len(bitmap)):
        curr_ind = 0
        for z in range(len(bitmap[i])):
            bitmap_list = list(bitmap[i])
            if bitmap_list[z] == '*' or bitmap_list[z] == '.':
                bitmap_list[z] = word[curr_ind]
            curr_ind = curr_ind+1
            if curr_ind == len(word):
                curr_ind = 0
            bitmap[i] = ''.join(bitmap_list) 
    print(''.join(bitmap))


def do_bitmap():
    bitmap = get_init_bitmap()
    word = get_input()
    create_bitmap_message(bitmap,word)


if __name__ == '__main__':
    do_bitmap()