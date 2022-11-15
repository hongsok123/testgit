a_list=[2,3,4,5]
b_list=[3,5,6,7]

def dot(a_list, b_list):
    if len(a_list) != len(b_list):
        raise ValueError
    else:
        temp_arr=[]
        for i in range(len(a_list)):
            temp_arr.append(a_list[i] * b_list[i])      
    
        resultvalue= sum(temp_arr)
        return resultvalue
 
print(dot(a_list, b_list))
    