from core.const import mb_size, output_path


def create_file_text(filename, size):
    """
        Create file text extension

        Parameters:
        filename (string): file name
        size     (number): file size by MB

        Returns:
        bool: status create file
    """

    try:
        filename = output_path(filename, 'txt')
        byte_size = size * mb_size

        with open(filename, 'wb') as f:
            f.seek(byte_size)
            f.write(' '.encode("utf-8"))
            f.close()

        return True
    except Exception as e:
        print('[Notify][CREATE FILE][txt] error: {}'.format(str(e)))

        return False
