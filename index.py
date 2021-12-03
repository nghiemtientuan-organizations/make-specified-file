FILE_TYPES = {
    # text
    'txt': 'txt',

    # shel run
    'exe': 'exe',

    # image
    'jpg': 'jpg',
    'png': 'png',
    'jpeg': 'jpeg',

    # excel
    'xls': 'xls',
    'xlsx': 'xlsx',

    # word
    'doc': 'doc',
    'docx': 'docx',

    # pdf
    'pdf': 'pdf',

    # PowerPoint
    'ppt': 'ppt',
    'pptx': 'pptx',
}

# Create file text
#
# @input string filename
# @input number size (byte)
#
# @return null
def create_file(filename, type='txt', size=0):
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

create_file_numbers('tuntun.txt', 1000)