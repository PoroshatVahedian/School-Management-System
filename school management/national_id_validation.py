national_id_check  = False

def national_id_validation_function(nums):
    global national_id_check
    if len(nums)==10:
        l=[]
        s=1
        for i in nums:
            l.append(int(i))
        ragham_control=l.pop()
        reverse=l[::-1]
        my_list=[]
        for i in reverse:
            s+=1
            i*=s
            my_list.append(i)
        k=0
        for i in my_list:
            k+=i
        remainder=k%11
        if remainder>=2:
            check_control=11-remainder
            if check_control==ragham_control:
                national_id_check = True
                return national_id_check
        elif remainder<2:
            if remainder==ragham_control:
                national_id_check = True
                return national_id_check
            else:
                national_id_check = False
                return national_id_check
    else:
        national_id_check = False
        return national_id_check


