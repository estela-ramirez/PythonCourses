class A:
    sample_list = []
    sample_int  = 0

A_1 = A()
A_2 = A()

A_1.sample_int = 5
A_2.sample_int = 10
print(A_1.sample_int, "\n", A_2.sample_int, "\n",  sep = "")

#make sure lists are empty
print(A_1.sample_list, "\n", A_2.sample_list, "\n",  sep = "")

A_1.sample_list.append(5)
A_2.sample_list.append(15)

print(A_1.sample_list, "\n", A_2.sample_list, "\n",  sep = "")

A_3 = A()# new objects have sae shared list values
print(A_3.sample_list, "\n")

A_1.sample_list = [] #make separate lists
print(A_1.sample_list, "\n", A_2.sample_list, "\n", A_3.sample_list, "\n", sep = "")

A_1.sample_list = []#all lists have been emptied
A_2.sample_list = []
A_3.sample_list = []
print(A_1.sample_list, "\n", A_2.sample_list, "\n", A_3.sample_list, "\n",  sep = "")

A_4 = A()#new list still has old data
print(A_4.sample_list, "\n")

A_4.sample_list.clear()
print(A_4.sample_list, "\n")

A_5 = A()
print(A_5.sample_list, "\n")#now new elements start with empty shared list



class B:
    sample_int = 0
    
class C: #prevents accidental sharing
    sample_B = None

class D:#allows accidental sharing
    d_sample_B = B()

D_1 = D()
print(D_1.d_sample_B.sample_int, "\n")


D_1.d_sample_B.sample_int = 5
D_2 = D()
print(D_1.d_sample_B.sample_int, "\n", D_2.d_sample_B.sample_int, "\n", sep = "")





