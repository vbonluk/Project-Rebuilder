# coding:utf-8
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
    try:

        for fileObj in fileList:

            # 读取忽略规则
            if checkFileName(fileObj, "ignore_content.txt") == True:
                continue

            f = open(fileObj, 'r+', encoding='utf-8')
            all_the_lines = f.readlines()
            f.seek(0)
            f.truncate()
            print('内容编辑器：定位到文件：%s' % (fileObj))
            for line in all_the_lines:
                str1 = repalceStr
                str2 = newStr
                f.write(line.replace(str1, str2))
            f.close()
        print('修改 文件内容 执行完毕')
    except Exception as error:
        print(error)

def main(fileDir,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName):
    operation(fileDir,projectName_repalceStr,new_projectName)
    operation(fileDir, prefixName_repalceStr, new_prefixName)

if __name__ == '__main__':
    fileDir = "test"
    main(fileDir, 'test', 'demo')