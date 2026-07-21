#My code with Time complexity of 0(n**2)
arr=[1,3,6]
k=5
if k in arr:
    print(arr.index(k))
else:
    arr.append(k)
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr.index(k))

#modified version using chatgpt for Time complexity of 0(n)
arr_1=[2,4,8,9]
k=6
for i in range(len(arr_1)):
    if arr_1[i]==k:
        print(i)
else:
    arr_1.append(k)
    i=len(arr)-1
    while i>0 and arr_1[i]<arr_1[i-1]:
        arr_1[i],arr_1[i-1]=arr_1[i-1],arr_1[i]
        i-=1
    print(i)
