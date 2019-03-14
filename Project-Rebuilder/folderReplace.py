import os
from checkFileName import checkFileName

def listFiles(dirPath,repalceStr,newStr):
    try:
        # 重命名子文件夹
        for root, dirs, files in os.walk(dirPath):
            new_path = tree_son_folder(dirs,root,repalceStr,newStr)
            if not new_path == '':
                listFiles(new_path, repalceStr, newStr)


    except Exception as error:
        print(error)

def tree_son_folder(dirs_p,root_path,repalceStr,newStr):

    deepest_folder_name = root_path.split('/')[-1]
    if repalceStr in deepest_folder_name:
        fileObj = root_path
        # 读取忽略规则
        if checkFileName(fileObj,"ignore_folder.txt") == True:
            return ''
        if os.path.isdir(root_path):
            new_path = replace(root_path,repalceStr,newStr)
            return new_path
    return ''

def replace(path,repalceStr,newStr):
    if os.path.isdir(path):  # 如果是文件夹则跳过
        str1 = repalceStr
        str2 = newStr
        try:
            current_folder_name = path.split('/')[-1]
            path_without_folder = ''
            cout = 0
            path_list = path.split('/')
            for path_str in path_list:
                if not path_str == '' and cout < len(path_list) - 1:
                    path_without_folder = path_without_folder + '/' + path_str
                cout = cout + 1
            if str1 in current_folder_name:
                new_name = current_folder_name.replace(str1, str2)
                new_path = path_without_folder + '/' + new_name
                os.rename(path, new_path)
                print('文件夹重命名：%s --> %s' % (path,new_path))
                return new_path
        except Exception as error:
            print(error)

def main(fileDir,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName):
    listFiles(fileDir,projectName_repalceStr,new_projectName)
    listFiles(fileDir, prefixName_repalceStr, new_prefixName)
    print('修改 文件夹名 执行完毕')


if __name__ == '__main__':
    fileDir = "test"
    main(fileDir, 'test', 'demo')