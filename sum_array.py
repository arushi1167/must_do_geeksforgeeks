# Algorithm
# 1. if sum=12 return
# 2. if sum > 12 remove initial numbers form sequence
# 3. if sum < 12 add numbers 

def subarr_sum(sums,arr):
	count=start=end=0
	while(count != sums and end<len(arr)):
		if (count > 12):
			count-=arr[start]
			start+=1
		else:
			count+=arr[end]
			end+=1
		print(count,end)
	print(start)
	print(end-1)
	return

arr= [1,2,3,4,5,6,7,8,9,10]
n=15

subarr_sum(n,arr)
