#基本使用方式
#[a:b:c] a表示取（a,b]区间的切片数据，a为开区间，b为闭区间，c表示步长（为负数是表示反向）
l = [x for x in range(10)]
l1 = l[::-1] #倒叙排列
l2 = l[2:] #从下标2开始（去掉0,1）
l3 = l[:5]#从头开始，到结束
l4 = l[:6:-2]#倒序开始，步长为2，取到l4[6]
print(l4)
print(l[::-2])
#使用slice对象，使得切片更可读
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                     $17.50    3    $52.50
1489  6mm Tactile Switch x20                $4.95     2    $9.90
1510  Panavise Jr. - PV-201                 $28.00    1    $28.00
1601  PiTFT Mini Kit 320x240                $34.95    1    $34.95"""
SKU = slice(0,6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split("\n")[2:]
for item in line_items:
    print(item[DESCRIPTION] + ": PRICE IS : "+item[UNIT_PRICE])
