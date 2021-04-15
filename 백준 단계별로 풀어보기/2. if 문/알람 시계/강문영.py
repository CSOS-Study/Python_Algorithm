hour,miniute = map(int,input().split())

is_minus = miniute-45<0

new_hour = (hour-int(is_minus))%24
new_miniute = miniute-45

if(is_minus):
    new_miniute = 15 + miniute

print(new_hour,new_miniute,sep=' ')



