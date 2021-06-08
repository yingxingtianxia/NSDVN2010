import time
import xlrd
from xlutils import copy as xlcopy
import xlutils


# 获取所有签到学员名单
def get_sign_stus():
    sign_stus = []
    today = time.strftime('%Y%m%d',time.localtime())
    sign_file = '%s.txt' % today
    with open(sign_file,'r',encoding='UTF-8') as fobj:
        data = fobj.readlines()
        for i in data:
            name = i.split('-')[0]
            sign_stus.append(name)

    return sign_stus


#获取表格学员名单
def get_stus(file):
    c_data = []

    rdata = xlrd.open_workbook(file, 'r')
    tables = rdata.sheets()

    talbe = tables[0]
    talbe_name = talbe.name
    talbe_rows = talbe.nrows
    talbe_cols = talbe.ncols

    table_row_values = talbe.row_values
    table_col_values = talbe.col_values
    
    # print(table_col_values(1))
    stus = table_col_values(1)

    return stus

# 组装签到列表
def create_sign_list(stus,sign_stus):
    sign_dic = {
        0: '缺勤',
        1: '出勤'
    }

    year = time.strftime('%Y',time.localtime())
    month = time.strftime('%m',time.localtime())
    day = time.strftime('%d',time.localtime())

    date = '%s年%s月%s日' % (year,month,day)
    sign_list = [date]
    for i in range(len(stus)-1):
        sign_list.append(0)

    for i in sign_stus:
        try:
            ind = stus.index(i)
        except ValueError:
            continue
        sign_list[ind] = 1

    # print(sign_list)
    for i in range(1,len(sign_list)):
        sign_list[i] = sign_dic[sign_list[i]]

    return sign_list


#回写数据
def write_back(sign_list, file):
    wdata = xlrd.open_workbook(file)
    table = wdata.sheets()[0]

    old_cols = table.ncols

    new_data = xlcopy.copy(wdata)
    new_table = new_data.get_sheet(0)

    for i in range(len(sign_list)):
        new_col = old_cols
        new_table.write(i,new_col,sign_list[i])

    new_data.save(file)


if __name__ == '__main__':
    file='tem.xls'
    sign_stus = get_sign_stus()
    stus = get_stus(file)
    sign_list = create_sign_list(stus,sign_stus)
    write_back(sign_list,file)