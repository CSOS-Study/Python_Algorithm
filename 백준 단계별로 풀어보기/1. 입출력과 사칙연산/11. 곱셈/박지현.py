A = input()
B = input()

p3 = int(A) * int(B[2])
p4 = int(A) * int(B[1])
p5 = int(A) * int(B[0])
p6 = p3 + (p4 * 10) + (p5 * 100)  # 또는 p6=int(A)*int(B)

print(p3, p4, p5, p6, sep='\n')

