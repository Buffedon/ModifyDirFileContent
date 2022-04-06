# ModifyDirFileContent
修改文件夹下所有文件的指定内容

## 背景
由于换了一台新电脑，Typora上的笔记需要进行迁移，但是迁移过后发现图片链接的位置对应不上。在此，作者就像用所学知识，编写一个脚本，更改文件夹下 .md 文件中所有图片的链接

## 说明
1.由于无法直接读取 md 文件内容，因此要先将 md 文件转化为 txt 文件
2.然后读取文件内容，匹配原始要修改的内容，进行replace 替换，最后再写入文本


## 函数说明
renameFileSuffix        #改变文件后缀名
modifyFileContent       #改变文件中的指定内容


## 变量说明
srcSuffix = '.md'                                     #原文件后缀名
dstSuffix = '.txt'                                    #修改后的后缀名
regexstr = 'E:\\desktop\\file'                        #原始内容
newstr = 'C:\\Users\\XieZhendong\\Documents'          #更改后的内容
cwd = 'C:/Users/XieZhendong/Desktop/桌面/笔记'          #要更改的当前目录

