# coding=utf-8
import codecs

import xlwt
# 创建 xls 文件对象
wb = xlwt.Workbook()
# 新增一个表单
sh = wb.add_sheet('A Test Sheet')
# 按位置添加数据
sh.write(0, 0, 1234.56)
sh.write(1, 0, 8888)
sh.write(2, 0, u'张中俊')
sh.write(2, 1, u'爱中国')
# 保存文件
wb.save('f:\\example.xls')