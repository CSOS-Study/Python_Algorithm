x = int(input())
y = int(input())

is_y_upper = y>0
is_x_upper = x>0

if(is_x_upper and is_y_upper):
    print(1)
if(is_x_upper and not is_y_upper):
    print(4)
if(not is_x_upper and is_y_upper):
    print(2)
if(not is_x_upper and not is_y_upper):
    print(3)

