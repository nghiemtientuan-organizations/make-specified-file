import os


mb_size = 1024 * 1024


def output_path(name, extention):
    return 'results/{}.{}'.format(name, extention)


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        return os.stat(file_path).st_size

    return 0
