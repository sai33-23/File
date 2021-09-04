banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("exercise.txt")
i=0
while i<len(banks_list):
    file.write(banks_list[i])
    file.write("\n")
    i=i+1
print(banks_list)

