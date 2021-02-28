"""
Question for linyun Mo

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30. D is the variable
whose values should be input to your program in a comma-separated sequence.
Example:
Let us assume the following comma separated input sequence is given to the program: 100,150,180
The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be rounded off to its nearest value
(for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input.

谷歌中文翻译：
编写一个程序，根据给定的公式计算并打印该值：Q = [（2 * C * D）/ H]的平方根
以下是C和H的固定值：C为50。H为30 。D是变量，其值应以逗号分隔的顺序输入到程序中。
示例：假定给程序提供了以下逗号分隔的输入序列：100,150,180程序的输出应为：18,22,24

提示：如果接收到的输出为十进制形式，则应四舍五入至最接近的值（例如，如果接收到的输出为26.0，则应将其打印为26）。应假定为控制台输入。
"""

import math

c = 50
h = 30
list1 = []
list2 = input().split(',')
for d in list2:
    outcome = math.sqrt(2 * c * float(d) / h)
    come = str(int(outcome))
    list1.append(come)
print(','.join(list1))
