from graphy import drawNetworkGraph

__author__ = 'user'

from xlsx_processer import *

basicdata = CBasicXlsData({"a":1,"b":1},"FIELDWITHDATA")
basicdata1 = CBasicXlsData(["d","dd","ddd"],"FIELDNAME")


basicdata.updateByData([1,2])
basicdata1.updateByDict({"a":3,"c":5,"d":6})

xlsdata = basicdata.getData()
xlsdata1 = basicdata1.getData()


#print(id(xlsdata))
#print(id(xlsdata1))

#print(xlsdata)
#print(xlsdata1)


xlssheet = CBasicXlsSheet("./data/mv.xlsx")
xlssheet.getHeader()
x = xlssheet.getData(2)
drawNetworkGraph(x)
# print(x.__len__())
# print(x[0].getData())
# print(x[1].getData())