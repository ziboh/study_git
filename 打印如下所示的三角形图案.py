# 打印如下所示的三角形图案。
"""
*
**
***
****
*****
"""
"""
    *
   **
  ***
 ****
*****
"""
"""
    *
   ***
  *****
 *******
*********
"""
# 这是一个废话

row = int(input('请输入需要打印的行数：'))
for x in range(1,row+1):
    for y in range(1,x+1):
        print("*",end="")
    print()


for x in range(1,row+1):
    print("*"*x)


for x in range(1,row+1):
    print(" "*(row-x)+"*"*x)


for x in range(1,row+1):
    print(" "*(row-x)+"*"*(2*x-1))