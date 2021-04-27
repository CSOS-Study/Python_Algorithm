s, ans = str(input()).upper(), {}
for i in s:
    ans.setdefault(i, 0)
    ans[i] += 1
if list(ans.values()).count(max(ans.values())) > 1: print('?')
else: print(sorted(ans.items(), key=lambda x:x[1], reverse=True)[0][0])
