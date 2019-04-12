def digit_sum(num):
    num=str(num)
    sum=0
    for i in range(len(num)):
        sum+=int(num[i])
    return sum

def is_harshad(int):
        sum=digit_sum(int)
        if int%sum==0:
            return True
        else:
            return False
            
            
    
def main():
    for i in range(1,200):
        if is_harshad(i):
            print(i)
            
                


main()
