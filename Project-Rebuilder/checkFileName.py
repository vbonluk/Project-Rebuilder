import os

def checkFileName(fileObj,ignore_file_name):
    # 读取忽略规则
    ignore_file_path = os.path.join(os.getcwd(), ignore_file_name)
    f4 = open(ignore_file_path, 'r', encoding='utf-8')
    line_ignore_all_str = f4.readlines()
    is_ignore = False
    for line_ignore in line_ignore_all_str:
        # 去掉\n
        line_ignore = line_ignore.strip()
        if line_ignore in fileObj:
            # 检查是否含有 例外 文件
            is_had_exception_file = False
            f5 = open(ignore_file_path, 'r', encoding='utf-8')
            line_ignore_exception_all_str = f5.readlines()
            for line_ignore_exception in line_ignore_exception_all_str:
                # 去掉\n
                line_ignore_exception = line_ignore_exception.strip()
                if '[+exception+]' in line_ignore_exception:
                    exception_str = line_ignore_exception.replace('[+exception+]','')
                    if exception_str in fileObj:
                        is_had_exception_file = True
            if is_had_exception_file == False:
                is_ignore = True
                continue


    f4.close()

    return is_ignore

if __name__ == '__main__':
    pass