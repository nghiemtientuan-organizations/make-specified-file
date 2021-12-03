# Create file text
#
# @input string filename
# @input number size (byte)
#
# @return null
def create_file(filename, size=0):
    f = open('results/' + filename, 'w')

    text = ''
    i = 0
    line = str(i)
    while len(text + line) <= size:
        text += line
        i += 1
        line = '\r\n' + str(i)

    f.write(text)
    f.close()
