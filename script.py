import getpass
import irancell2
my_list=["Air1","Air2","Warrior"]
number=[1,2,3,4]
print("you can select one of the below types!")
num=1
for type in my_list:
    print(f"{num}.{type}")
    num+=1

select_type=8
while select_type>4 or select_type<1:
    select_type=int(input("please select your type: "))
    if select_type >4 or select_type<1:  
        print("your select isnt correct")
    else:
        selected_item=my_list[select_type-1]
        print(f"you choose -> {selected_item}")

else:
    print("i got it!")


tasknumber=input("please enter your task number: ")
instances=irancell2.Pass_credit(tsknumb=tasknumber)

if select_type ==1 :
    result=instances.Air1(username="masoud", password="123456789", serveraddress="192.168.21.161",keyword=selected_item)
    print(f"Here you are{result}")
else:
    result=instances.Air2(username="masoud", password="123456789", serveraddress="192.168.21.161",keyword=selected_item)
    print(f"Here you are{result}")

print("Thanks to use my script bye!")