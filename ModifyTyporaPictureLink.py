import os
import re

# 给文件重命名
# 由于无法直接读取 .md 文件的内容，因此先要强制进行转换
def renameFileSuffix(cwd,srcSuffix,dstSuffix):
    files = os.listdir(cwd)        #得到文件夹下面的所有名称
    #print(files)

    # 如果是文件夹，则需要进行迭代
    for file in files:
        if os.path.isdir(cwd+'/'+file):                         #如果是文件夹，则继续执行
            #print('是文件夹')
            renameFileSuffix(cwd+"/"+file,srcSuffix,dstSuffix)           #迭代，调用自己

        # 如果不是文件夹，直接读取数据
        else:
            src = os.path.join(cwd, cwd+'/'+file)                    #源路径,例如 C:/test/test.md
            dst = os.path.join(cwd, cwd+'/'+file.replace(srcSuffix,dstSuffix))                    #目的路径,例如 C:/test/test.txt
            os.rename(src, dst)


# 读取文件夹下文件的内容
def modifyFileContent(path,regexStr,newStr):
    files = os.listdir(path)                            #得到文件夹下面的所有名称
    #print(files)

    # 如果是文件夹，则需要进行迭代
    for file in files:
        if os.path.isdir(path+'/'+file):                          #如果是文件夹，则继续执行
            #print('是文件夹')
            modifyFileContent(path+"/"+file,regexStr,newStr)                      #迭代，调用自己

        # 如果不是文件夹，直接读取数据
        else:
            with open(path+"/"+file,encoding='UTF-8',errors='ignore') as f:        # 如果是文件夹，则获得此路径
                s = f.read()
                if re.search(regexStr,s):
                    s.replace(regexStr,newStr)
                #print(str.replace(regexStr,newStr))
                f.close()
            with open(path+"/"+file,'w',encoding='UTF-8',errors='ignore') as f2:       # 忽略某些报错，因为在运行的过程中，会有很多乱码(不可见字符)导致程序中断
                #print('文件写入')
                f2.write(s.replace(regexStr,newStr))
                f.close()


if __name__ == "__main__":

    srcSuffix = '.md'
    dstSuffix = '.txt'

    regexstr = 'E:\\desktop\\file'                        #原始内容
    newstr = 'C:\\Users\\XieZhendong\\Documents'          #更改后的内容
    cwd = 'C:/Users/XieZhendong/Desktop/桌面/笔记'          #要更改的当前目录

    renameFileSuffix(cwd);                               #将md文件改为txt文件
    modifyFileContent(cwd, regexstr, newstr)

