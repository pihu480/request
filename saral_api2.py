import requests
import json
def saral():
    saral_api = " http://saral.navgurukul.org/api/courses"     
    saral_url = requests.get(saral_api)                        

    data = saral_url.json()
    with open ("courses.json","w") as saral_data:
        json.dump(data,saral_data,indent =4)

    print("")
    print("** Welcome to navgurukul and Learn basic programming launguage **")
    print("")
    def availableCourses():
        serial_no = 0
        for i in data["availableCourses"]:
            print(serial_no+1 ,i["name"], i["id"])
            serial_no=serial_no+1
        print("")
    availableCourses()
    
    available_Courses =int(input("Enter your courses number that you want to learn:- "))
    parent_id=data["availableCourses"][available_Courses-1]["id"]
    print(data["availableCourses"][available_Courses-1]["name"])

    # print("")
    # print("** Welcome to navgurukul and Learn basic programming launguage **")
    # print("")

    user_input_1=input("if you want next or previous n/p: ")
    if user_input_1=="p":
        availableCourses()
        # i=0
        # while i<len(data["availableCourses"]):
        #     Courses = (data["availableCourses"][i]["name"])
        #     print(i+1," ",Courses,data["availableCourses"][i]["id"])
        #     i=i+1
        available_Courses = int(input("Enter your courses number that you want to learn:-"))
        print(data["availableCourses"][available_Courses-1]["name"])

    parent_api = "http://saral.navgurukul.org/api/courses/"+str(data["availableCourses"][available_Courses-1]["id"])+"/exercises"
    parent_url = requests.get(parent_api)

    data_1 = parent_url.json()

    with open ("parentes.json","w") as child_data:
        json.dump(data_1,child_data,indent=4)
    def parentes_data():
        serial_no_1=0
        for i in data_1["data"]:
            print("      ",serial_no_1+1,".",i["name"])
            if len(i["childExercises"])>0:
                s= 0
                for j in i['childExercises']:
                    s = s+ 1
                    print( "               ",s,j['name'])
            else:
                print("                1",i["slug"])
            serial_no_1+=1
    parentes_data()
    print("")
    topic_no = int(input("Enter topic number that's you want to learn:- "))
    serial_no_3= 0
    my_list=[]
    for l in data_1['data']:
        serial_no_3+=1
        if topic_no == serial_no_3:
            user_input_3=input("Enter topic number that's you want to learn previous or next:- ")
            if user_input_3=="p":
                serial_no_1=0
                for i in data_1["data"]:
                    print("      ",serial_no_1+1,".",i["name"])
                    if len(i["childExercises"])>0:
                        s= 0
                        for j in i['childExercises']:
                            s = s+ 1
                            print( "               ",s,j['name'])
                    else:
                        print("                1",i["slug"])
                    serial_no_1+=1
                    topic_no = int(input("Enter topic number that's you want to learn:- "))
    m = 0
    while m < len(data_1["data"][topic_no-1]["childExercises"]):
        print("     ", m+1 ,data_1["data"][topic_no-1]["childExercises"][m]["name"])
        slug = (data_1["data"][topic_no-1]["childExercises"][m]["slug"])

        child_exercises_url = ("http://saral.navgurukul.org/api/courses/" +  str(parent_id) +"/exercise/getBySlug?slug=" + slug )
        Data_3 = requests.get(child_exercises_url)

        
        convert_data = Data_3.json()
        with open("Topic.json","w") as convert_1:
            json.dump(convert_data,convert_1,indent=4)
        my_list.append(convert_data["content"])
        m = m + 1
    def questions_data():
        questions_no = int(input("choose the specific questions no :- "))
        question=questions_no-1
        print(my_list[question])
        while questions_no > 0 :
            next_question = input("do you ne t question or previous question n/p :- ")
            if questions_no == len(my_list):
                print("next page")
            if next_question == "p" :
                if questions_no == 1:
                    print("no more questions")
                    break
                elif questions_no > 0:
                    questions_no = questions_no - 2
                    print(my_list[questions_no])
            elif next_question == "n":
                if questions_no < len(my_list):
                    index = questions_no + 1
                    print(my_list[index-1])
                    question = question + 1
                    questions_no = questions_no + 1 
                    if question == (len(my_list)-1) :
                        print("next page")
                        break
    questions_data()
saral()