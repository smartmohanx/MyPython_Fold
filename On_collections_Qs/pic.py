
#pickling example
lis = [1,2,3,0,4,9,5,6,8,7]
import pickle
file = open("employee_info.txt","wb")
pickle.dump(lis,file)
file.close()
print("Data Written to File")

##unpickling example;
# import pickle
# file = open("employee_info.txt","rb")
# lis = pickle.load(file)
# print(lis)
# file.close()