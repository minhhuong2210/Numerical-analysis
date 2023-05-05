from numpy . random import rand
a = 10**6 # 1 000 000 VNĐ
b = 10**8 # 100 000 000 VNĐ
n = 50000 # 50000 tài khoản
rate = 5 # 5% 
target = 10**9 # tỷ phú

def hacker_bank(a,b,n,target,rate):
    count = 0
    t = 0
    tai_khoans = a + (b-a)*rand(n,1)
    while t<target:
        for tai_khoan in tai_khoans:
            # Tính lãi KH ngày hôm đó
            lai = tai_khoan[0]*rate/365/100
            # cập nhật tai khoản KH
            tai_khoan[0]+= (lai // 1000)*1000
            # lãi hacker lấy được
            p = lai - (lai // 1000)*1000
            print("Đang hack được:",p,"VNĐ")
            t+=p
        # cập nhật lãi TK hacker
        t += t*rate/365/100
        # update ngày
        count += 1
    print()
    return count,t

res = hacker_bank(a,b,n,target,rate)
money = str(round(res[1]))
print("Hacker cần", res[0], "ngày để trở thành tỷ phú, với tổng số tiền:", money[0]+"."+money[1:4]+"."+money[4:7]+"."+money[7:10],"VNĐ.")     
print()