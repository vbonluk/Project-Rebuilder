import os
from checkFileName import checkFileName

def listFiles(dirPath):
    fileList = []
    for root, dirs, files in os.walk(dirPath):
        for fileObj in files:
            fileList.append(os.path.join(root, fileObj))
    return fileList

def operation(fileDir,repalceStr,newStr):
    fileList = listFiles(fileDir)
    for file in fileList:
        Olddir = os.path.join(fileDir, file)
        if os.path.isdir(Olddir):  # 如果是文件夹则跳过
            continue;
        if not os.path.isfile(file):
            continue

        # 读取忽略规则
        if checkFileName(file, "ignore_file.txt") == True:
            continue

        name = file
        str1 = repalceStr
        str2 = newStr
        try:
            print('文件名编辑器：定位到文件：%s' % (file))
            if str1 in name:
                new_name = name.replace(str1, str2)
                os.rename(file, new_name)
        except Exception as error:
            print(error)
    print('修改 文件名 执行完毕')

def main(fileDir,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName):
    operation(fileDir,projectName_repalceStr,new_projectName)
    operation(fileDir, prefixName_repalceStr, new_prefixName)


if __name__ == '__main__':
    fileDir = "test"
    main(fileDir, 'test', 'demo')