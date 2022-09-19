num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))


# num2是大的值
if num1 > num2:
    num1, num2 = num2, num1

for x in range(num1, 0, -1):
    if num1 % x == 0 and num2 % x == 0:
        maximum_convention = x
        break

least_common_multiple = int(num1 * num2 / x)
print("最大公约数为：%d" % (x))
print(f"最小公倍数为：{least_common_multiple}")
print("最小公倍数为：{}".format(least_common_multiple))
