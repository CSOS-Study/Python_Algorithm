def self_number(num):
    result = num + sum(map(int,str(num)))
    return result

full_set = set(range(1,10001))
has_self_number = set()

for i in full_set:
    has_self_number.add(self_number(i))

for i in sorted(full_set-has_self_number):
    print(i)