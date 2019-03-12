  # import pdb; pdb.set_trace()
file_write = open('palindromes.txt', "w")
file_read = open('input.txt', "r")

def read_file(file_read, file_write):
    data = file_read.read().lower().split()
    my_pal(data, file_write)


def my_pal(data, file_write):
    for word in data:
        rev = word[::-1]
        if word == rev:
          file_write.write(word + '\n')
    file_write.close()
    print('Palindromes complete. Please check your output file.')


read_file(file_read, file_write)


