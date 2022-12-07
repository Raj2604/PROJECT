print("Given Elements List : ")
List ={1,2,3}
print(List)
print("Relation is : ")
relation = {(1,3),(3,2),(1,2),(1,1),(2,2),(3,3)}
print(relation)
flag = True
for element in List:
    reflexive_tuple = tuple((element,element))
    if reflexive_tuple not in relation:
        flag = False
        break;
if flag == True:
    for tup in relation :
        if len(set(tup)) != 1:
            anti_symmetric = (tup[1], tup[0])
            #print("anti_symmetric",anti_symmetric)
            if anti_symmetric in relation:
                flag = False
                break;
            else:
                ele1 = tup[0]
                ele2 = tup[1]
                data_start_with_ele2 = [rec for rec in relation if rec[0] == ele2]
                for temp in data_start_with_ele2:
                    transitive_tuple = tuple((ele1,temp[1]))
                    if transitive_tuple not in relation:
                        flag = False
                        break;                    
if flag == True:
    print("Result : Is a POSET (Partially Ordered Set)")
else:
    print("Result : Is not a POSET (Partially Ordered Set)")
            
        


        