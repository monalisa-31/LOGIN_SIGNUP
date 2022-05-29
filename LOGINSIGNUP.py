import json
import os
main_dict={}
list=[]
dic_out={}
user_info={}
print("Welcome to the Login Signup Page")
if os.path.exists("userdetails.json"):
    pass
else:
    create=open("userdetails.json","w+")
    create.close()
choose = int(input(("\n \n1. For Sign_up\n2. For Log_in \n........")))
if choose == 1:
    name=input("enter the name : ")
    print(name)
    pas=input("enter your password : " )
    u,d,s=0,0,0
    for check in pas:
        if (check.islower()):
            u+=1
        if(check=='@'or check=='#'):
            s+=1
        if (check.isdigit()):
            d+=1
    try:
        with open("userdetails.json","r") as output:
            user_data=json.load(output)
            for info in user_data["user"]:
                pass
    except:
        pass
    if (u>=1 and s>=1 and d>=1 and s+u+d==len(pas)):
        pas1=input("\n \U0001F61B enter your password again : ")
        if pas==pas1: 
            if  os.stat("userdetails.json").st_size==0:
                print("Congracts",name,"You are Sign_up Succesfully")
                description=input("Enter your Description : ")
                birth_date=input("Enter Your Date Of Birth : ")
                Gender=input("Enter your Gender \n1.female\n2.male\n: ")
                hobbies=input("Enter Your hobby : ")
                try:
                    user_info["description"]=description
                    user_info["d_o_b"]=birth_date
                    user_info["Gender"]=Gender
                    user_info["Hobbies"]=hobbies
                    dic_out["Username"]=name
                    dic_out["Password"]=pas
                    dic_out["Profile"]=user_info
                    list.append(dic_out)
                    main_dict["user"]=list
                    with open("userdetails.json","r+") as file:
                        read_file= file.read()
                        userdata=json.loads(read_file)
                        for i in userdata:
                            if i =="user":
                                x=userdata[i]
                                x.append(dic_out.copy())
                                main_dict["user"]=x
                                json.dumps(main_dict,file)
                                file.close()
                except:
                    with open("userdetails.json","w") as f:
                        f.write(json.dumps(main_dict, indent=4))
            else:
                if info["Username"]!= name  or info["Password"]!= pas:
                    print("Congracts",name,"You are Log_in Succesfully")
                    description=input("Enter your Description=")
                    birth_date=input("Enter Your Date Of Birth : ")
                    Gender=input("Enter your Gender : \n1.female\n2.male\n")
                    hobbies=input("Enter Your hobby : ")
                    try:
                        user_info["description"]=description
                        user_info["d_o_b"]=birth_date
                        user_info["Gender"]=Gender
                        user_info["Hobbies"]=hobbies
                        dic_out["Username"]=name
                        dic_out["Password"]=pas
                        dic_out["Profile"]=user_info
                        list.append(dic_out)
                        main_dict["user"]=list
                        with open("userdetails.json","r+") as file:
                            read_file= file.read()
                            userdata=json.loads(read_file)
                            for i in userdata:
                                if i =="user":
                                    x=userdata[i]
                                    x.append(dic_out.copy())
                                    main_dict["user"]=x
                                    json.dumps(main_dict,file)
                                    file.close()
                    except:
                        with open("userdetails.json","w") as f:
                            f.write(json.dumps(main_dict, indent=4))
                else:
                    print("Your account is already Exsist!")
        else:
            print("both password are not same")
    else:
        print("At least password should contain one Specail number or one digit")
elif choose==2:
    user_name=input("enter your username=")
    log_in_password=input("enter your Log in Password=")
    with open("userdetails.json","r") as log_in_file:
        log_in_info=json.load(log_in_file)
        for output_data in log_in_info["user"]:
            if output_data["Username"] == user_name and output_data["Password"]==log_in_password:
                print(user_name+ "You Logged In Succesfully")