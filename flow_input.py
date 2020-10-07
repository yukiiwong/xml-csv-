import xml.dom.minidom
import read_csv as rc

#在内存中创建一个空的文档

lenid = int(input("输入id数量\n"))
road_inf = rc.rc("road_inf.csv")
doc=xml.dom.minidom.Document()
#创建一个根节点对象
root=doc.createElement('routes')
#print('添加的xml标签为：',root.tagName)

#给根节点添加属性
root.setAttribute('xmlns:xsi','http://www.w3.org/2001/XMLSchema-instance')
root.setAttribute('xsi:noNamespaceSchemaLocation','http://sumo.dlr.de/xsd/routes_file.xsd')
#将根节点添加到文档对象中
doc.appendChild(root)


for i in range(lenid):

    print('第%d个flow的信息为' %i)
    flow = doc.createElement('flow')
    flow.setAttribute('id', '%d' % i)


    f_from = input("第%d个的起点位置from\n" %i)
    f_from = road_inf[f_from]
    flow.setAttribute('from', '%s' % f_from)

    f_to = input("第%d个的终点位置to\n" %i)
    f_to = road_inf[f_to]
    flow.setAttribute('to', '%s' % f_to)

    number = int(input("第%d个的流量number\n" %i))
    flow.setAttribute('number', '%d' %number )

    root.appendChild(flow)
#给根节点添加一个叶子节点
#company=doc.createElement('gloryroad')
#叶子节点下再嵌套叶子节点
#name=doc.createElement('name')
#给节点添加文本节点
#name.appendChild(doc.createTextNode('光荣之路'))

#ceo=doc.createElement('CEO')
#ceo.appendChild(doc.createTextNode('吴老师'))
#将各叶子节点添加到父节点company中
#company.appendChild(name)
#company.appendChild(ceo)
#将company节点添加到根节点companys中
#root.appendChild(company)

#此处需要用codecs.open可以指定编码方式
fp=open("car.flow.xml",'w', encoding = 'utf-8')
#将内存中的xml写入到文件
doc.writexml(fp,indent='',addindent='\t',newl='\n',encoding='utf-8')
fp.close()