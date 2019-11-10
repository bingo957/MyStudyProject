class FileProject:
    """给文件对象包装确认删除对象时文件流关闭"""
    def __init__(self, filename='sample.txt'):
        self.new_file = open(filename, 'r+')

    def __del__(self):
        self.new_file.close()
        del self.new_file
