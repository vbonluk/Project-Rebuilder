# encoding:UTF-8
import folderReplace
import fileNameReplace
import contentReplace
import commentReplace
import shutil,os

# projectName is your project name
# prefixName is your project prefix word
# if your projectName and prefixName is same , just set same word
def main(fileDir,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName,website):
    try:
        # 去掉最后一个'/'或者'\'
        lastStr = fileDir[len(fileDir) - 1]
        fileDir_true = ''
        if '/' == lastStr or '\\' == lastStr:
            fileDir_true = fileDir[0 : len(fileDir)-1]
        else:
            fileDir_true = fileDir
        # 获取上层目录
        path = os.path.abspath(os.path.dirname(fileDir_true))
        # 获取目标文件夹名
        target_folder_name = fileDir_true.split('/')[-1]
        factory_path = path + '/VB-factory/'
        new_folder_path = factory_path + target_folder_name
        if not os.path.exists(factory_path):
            # 创建工厂文件夹
            os.makedirs(factory_path)
        else:
            # 删除工厂文件夹内的文件
            shutil.rmtree(factory_path)
            # 创建工厂文件夹
            os.makedirs(factory_path)

        # 拷贝目标文件夹
        shutil.copytree(fileDir_true, new_folder_path)

        folderReplace.main(new_folder_path,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName)

        new_edit_path = new_folder_path.replace(projectName_repalceStr,new_projectName)
        fileNameReplace.main(new_edit_path,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName)
        contentReplace.main(new_edit_path,projectName_repalceStr,prefixName_repalceStr,new_projectName,new_prefixName)
        commentReplace.main(new_edit_path,copyright_str=projectName_repalceStr,website=website)

        # 检查是否有podfile
        podfile_path = new_edit_path + '/Podfile'
        if os.path.exists(podfile_path):
            print('发现Podfile文件！开始执行pod install')
            cmd_1 = 'cd ' + '"' + new_edit_path + '"'
            # os.system(cmd_1)
            # 设置读取编码为UTF-8
            cmd_2 = 'export LC_ALL="en_US.UTF-8"'
            # os.system(cmd_2)
            cmd_3 = 'pod install'
            # os.system(cmd_3)
            cmd = cmd_1 + '&&' + cmd_2 + '&&' + cmd_3
            os.system(cmd)

        print('==================')
        print('====程序执行完毕====')
        print('=Mission Complete=')
        print('==================')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    fileDir = "/path/to/your/project/"
    main(fileDir,projectName_repalceStr='testProject',prefixName_repalceStr='tp',new_projectName='demoProject',new_prefixName='demo',website='www.demo.com')