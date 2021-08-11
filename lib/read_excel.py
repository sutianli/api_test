import xlrd
'''
wb=xlrd.open_workbook("test_youfen_data.xlsx")#打开excel
sh=wb.sheet_by_name("Test_contrast")#按工作簿名定位工作表
print((sh.nrows))#有效数据行数
print(sh.ncols)#有效数据列表
print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
print(sh.row_values(0))  # 输出第1行的所有值（列表格式）

# 将数据和标题组装成字典，使数据更清晰
print(dict(zip(sh.row_values(0), sh.row_values(1))))

# 遍历excel,打印所有的数据
for i in range(sh.nrows):
    print(sh.row_values(i))
'''

#使用函数封装,读取文件sheet名为xxx的数据
def excel_to_list(data_file, sheet):
    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典

#根据列名获取该列的数据
def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:  # 如果字典数据中case_name与参数一致
            return case_data
            # 如果查询不到会返回None

if __name__ == '__main__':   # 测试一下自己的代码
    data_list = excel_to_list("../data/test_youfen_data.xlsx", "Test_contrast")  # 读取excel，TestUserLogin工作簿的所有数据
    case_data = get_test_data(data_list, 'test_contrast_normal')  # 查找用例'test_user_login_normal'的数据
    print(case_data)