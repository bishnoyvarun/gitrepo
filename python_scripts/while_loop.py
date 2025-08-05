list=[1,4,9,16,25,36,49,64,81,100]
x = int(input("enter the number: "))

idx = 0
while idx < len(list):
    if (list[idx]==x):
        print("found at idx", idx)
        break;
    else:

        print("finding")     
    idx += 1
print("loop ended")
