
import requests
import json

saral_url="http://saral.navgurukul.org/api/courses"
saral_api=requests.get(saral_url)
data=saral_api.json()

with open("childern_data.json","w") as f:
    json.dump(data,f,indent=4)  


print("")
print("*Well Come to navgurukul larning programing course**")
print("")

serial_no=0
for i in data["availableCourses"]:
    print(serial_no+1,i["name"],i["id"])
    serial_no=serial_no+1
print("")
cources_name=int(input("select a corcese number :-"))
cource_1=data["availableCourses"][cources_name-1]["name"]
parents_id=data["availableCourses"][cources_name-1]["id"]
print(cource_1)

print(" ")
print("********wlecome to navgurukul and learn basis programming*******")
print("")
user_input_1=input("if you want next or p  n/p")
if user_input_1=="p":
    i=0
    while i<len(data["availableCourses"]):
        courses=(data["availableCourses"][i]["name"])
        print(i+1,"  ",courses,data["availableCourses"][i]["id"])
        i=i+1
    user_input=int(input("enter the courses number that you want to l" ))
    print(data["availableCourses"][user_input-1]["name"])

parentes_api= "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][cources_name-1]["id"])+"/exercises"
parentes_url=requests.get(parentes_api)
data1=parentes_url.json()
with open("parentes_data.json","w") as file:
    json.dump(data1,file,indent=4)

j=0
for i in data1["data"]:
    print("   ",j+1,".",i["name"])
    if data1["data"][j]["childExercises"]==[]:
        slug=(data1["data"][j]["slug"])
        print("        1.",slug)
    else:
        l=0
        while l<len(data1["data"][j]["childExercises"]):
            child=data1["data"][j]["childExercises"][l]["name"]
            print("            ",l+1,".",child)
            l=l+1
    j=j+1
print(" ")

topic_no=int(input("enter the topic number"))
serial_no_3=0
my_list=[]
for l in data1["data"]:
    serial_no_3=+1
    if topic_no==serial_no_3:
        user_input_3=input("Enter topic number that's you want to learn previous or next:- ")
        if user_input_3=="p":
            j=0
            for i in data1["data"]:
                print("   ",j+1,".",i["name"])
                if data1["data"][j]["childExercises"]==[]:
                    slug=(data1["data"][j]["slug"])
                    print("        1.",slug)
                else:
                    l=0
                    while l<len(data1["data"][j]["childExercises"]):
                        child=data1["data"][j]["childExercises"][l]["name"]
                        print("            ",l+1,".",child)
                        l=l+1
                    j=j+1
                topic_no = int(input("Enter topic number that's you want to learn:- "))
m=0
while m<len(data1["data"][topic_no-1]["childExercises"]):
    print("      ",m+1,data1["data"][topic_no-1]["childExercises"][m]["name"])
    slug=(data1["data"][topic_no-1]["childExercises"][m]["slug"])
    mogli=(' http://saral.navgurukul.org/api/courses/'+str(parents_id)+'/exercise/getBySlug?slug='+slug)
    mogli_url=requests.get(mogli)

    datak=mogli_url.json()
    with open("topic.json","w") as fi:
        json.dump(datak,fi,indent=4)
        my_list.append(datak["content"])
    m=m+1

content1=int(input('enter the topic no'))
question=content1-1
print(my_list[question])
while content1>0:
    next=input("enter the next p/n")
    if content1==len(my_list):
        print("next page")
    if next=="p":
        if content1==1:
            print("no more question")
            break
        elif content1>0:
            content1=content1-2
            print(my_list[content1])
    elif next=="n":
        if content1<len(my_list):
            index=content1+1
            print(my_list[index-1])
            question=question+1
            content1+=1
            if question==(len(my_list))-1:
                print("next page")
                break

            
        

