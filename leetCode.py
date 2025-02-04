# mencari int yang hanya muncul satu kali
nums = list(map(int, input("Masukan Array: ").split()))
for num in nums:
    if nums.count(num) == 1:
        print(num)
        break
