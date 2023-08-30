import math

x1 = float(input('insira um numero para x1\n'));
y1 = float(input('insira um numero para y1\n'));
x2 = float(input('insira um numero para x2\n'));
y2 = float(input('insira um numero para y2\n'));
p1=(x2-x1)**2;
p2=(y2-y1)**2;
d=math.sqrt(p1+p2);
print('O resultado é:',d);