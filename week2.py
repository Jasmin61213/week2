#要求一
def calculate(min, max, step):
    sum=0
    while min<=max:
        sum+=min
        min+=step
    print(sum)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

#要求二
def avg(data):
    sum=0
    i=0
    for employees in data["employees"]:
        if employees["manager"]==False:
            sum+=employees["salary"]
            i+=1
    print (sum/i)
avg({
    "employees":[ 
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob", 
            "salary":60000, 
            "manager":True
        }, 
        {
            "name":"Jenny", 
            "salary":50000, 
            "manager":False
        }, 
        {
            "name":"Tony", 
            "salary":40000, 
            "manager":False
        }, 
        ]
    }) # 呼叫 avg 函式

#要求三
def func(a):
    def _func(b,c):
        print(a+(b*c))
    return _func
func(2)(3, 4)# 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#要求四
def maxProduct(nums):
    list=[]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            list.append(nums[i]*nums[j])
    print(max(list))
maxProduct([5, 20, 2, 6]) # 得到 120 
maxProduct([10, -20, 0, 3]) # 得到 30 
maxProduct([10, -20, 0, -3]) # 得到 60 
maxProduct([-1, 2]) # 得到 -2 
maxProduct([-1, 0, 2]) # 得到 0 
maxProduct([5,-1, -2, 0]) # 得到 2 
maxProduct([-5, -2]) # 得到 10

#要求五
def twoSum(nums, target):
    hashtable={} #建立字典
    for i in range(len(nums)):
        hashtable[nums[i]]=i #建立 [數值：第幾個]
    for i in range(len(nums)):
        if target-nums[i] in hashtable: #如果target-nums有在字典裡
            if hashtable[target-nums[i]] != i: 
                return [i, hashtable[target-nums[i]]] #不是的話就存起來之後使用
    return []
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9