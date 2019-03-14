# coding:utf-8

# 修改头部注释

import os
from datetime import datetime, timezone ,timedelta
import getpass
from checkFileName import checkFileName


def listFiles(dirPath):
    fileList = []
    for root, dirs, files in os.walk(dirPath):
        for fileObj in files:
            fileList.append(os.path.join(root, fileObj))
    return fileList


def main(fileDir,copyright_str,website):
    searchMaxLineNum = 50 # 检索内容的最大行数，超过这个数值的后面的行内容不再检索
    fileList = listFiles(fileDir)
    try:
        for fileObj in fileList:
            # 读取忽略规则
            if checkFileName(fileObj,"ignore_comment.txt") == True:
                continue
            f = open(fileObj, 'r', encoding='utf-8')
            all_the_lines = f.readlines()
            # f.seek(0)
            # f.truncate()
            print('注释编辑器：定位到文件：%s' % (fileObj))
            lineNum = 0
            tezheng_start = '/*'
            tezheng_end = '*/'
            tezheng_start_num = 0
            tezheng_end_num = 0
            is_found_start_num = False
            is_found_end_num = False
            for line in all_the_lines:
                if lineNum < searchMaxLineNum:
                    if tezheng_start in line and is_found_start_num == False:
                        tezheng_start_num = lineNum
                        is_found_start_num = True
                    if tezheng_end in line and is_found_end_num == False:
                        tezheng_end_num = lineNum
                        is_found_end_num = True
                    lineNum = lineNum + 1

            f.close()
            print('检索到注释行数：%d到%d' % (tezheng_start_num + 1, tezheng_end_num + 1))

            print('开始删除原有注释')
            # 删除原有注释
            f2 = open(fileObj, 'r+', encoding='utf-8')
            all_the_lines = f2.readlines()
            f2.seek(0)
            f2.truncate()
            lineNum_delete = 0
            for line in all_the_lines:
                if lineNum_delete < searchMaxLineNum:
                    if lineNum_delete >= tezheng_start_num and lineNum_delete <= tezheng_end_num:
                        lineNum_delete = lineNum_delete + 1
                        continue
                f2.write(line)
                lineNum_delete = lineNum_delete + 1
            f2.close()

            print('开始写入新注释')
            # 写入新注释
            f3 = open(fileObj, 'r+', encoding='utf-8')
            all_the_lines = f3.readlines()
            f3.seek(0)
            f3.truncate()
            lineNum_add = 0
            for line in all_the_lines:
                if lineNum_add == tezheng_start_num:
                    # 读取注释文本
                    name = "comments.txt"
                    comments_file_path = os.path.join(os.getcwd(), name)
                    f4 = open(comments_file_path, 'r', encoding='utf-8')
                    line_comments = f4.readlines()
                    for line_comment in line_comments:
                        if '___DATE___' in line_comment:
                            # 设置日期
                            utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
                            # astimezone()将转换时区为北京时间:
                            bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
                            curr_time = bj_dt.strftime('%Y/%m/%d')
                            line_comment = line_comment.replace('___DATE___',curr_time)

                        if '___FILENAME___' in line_comment:
                            file_name = fileObj.split("/")[-1]
                            line_comment = line_comment.replace('___FILENAME___', file_name)

                        if '___FULLUSERNAME___' in line_comment:
                            Author = getpass.getuser()
                            line_comment = line_comment.replace('___FULLUSERNAME___', Author)

                        if '___COPYRIGHT___' in line_comment:
                            if not copyright_str == '':
                                # 设置日期
                                utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
                                # astimezone()将转换时区为北京时间:
                                bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
                                curr_time = bj_dt.strftime('%Y')
                                cr = 'Copyright © ' + curr_time + ' ' + copyright_str + '. All rights reserved.'
                                line_comment = line_comment.replace('___COPYRIGHT___', cr)

                        if '___WEBSITE___' in line_comment:
                            if not website == '':
                                line_comment = line_comment.replace('___WEBSITE___', website)

                        if '___PACKAGENAME___' in line_comment:
                            line_comment = line_comment.replace('___PACKAGENAME___', copyright_str)

                        f3.write(line_comment)

                    # 写入3行空白行
                    f3.write('\n')
                    f3.write('\n')
                    f3.write('\n')
                    f4.close()
                    print('写入新注释完毕')

                f3.write(line)
                lineNum_add = lineNum_add + 1
            f3.close()


        print('修改 文件 执行完毕')
    except Exception as error:
        print(error)

if __name__ == '__main__':
    fileDir = "test"
    main(fileDir,copyright_str='demo',website='www.test.com')