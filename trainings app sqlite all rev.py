import sqlite3

db = sqlite3.connect(r"C:\Users\zizo\Documents\python1\app.db") 



cr =db.cursor()

uid = 1

def commit_and_close():
    #save and close 
    db.commit()
    
    db.close()
    print("connection is closed")



input_msg = """
what do you want to do ?
"s" => Show Skills
"a" => Add skill
"d" => Delwete
"u" => Update skill
"q" => Quit App 
choose Option: 
"""
user_input = input(input_msg).strip().lower()



def show_skills():
    cr.execute(f"select * from skills where user_id='{uid}'")

    results = cr.fetchall()
    

    print(f"you have {len(results)} skills ")

    if len(results) > 0:

        print("shoing skills with progress:")
    for row in results:
        print(f"Skill is {row[0]}," ,end=" ") 
        print(f"progress is {row[1]}")    
    commit_and_close()    

def add_skills():
    
    sk_name = input("write Skill Name").strip().capitalize()
    
    
    cr.execute(f"select name from skills where  name = '{sk_name}' and user_id='{uid}'")
    results = cr.fetchone()

    if results == None:
        prog = input("Write Skill progress").strip()

        cr.execute(f"insert into skills(name, progress, user_id) values('{sk_name}','{prog}','{uid}')")
    else:
        #print(" you cannot add it , exists")
        
        # Task  from elzero lesson 126 sloved by me :) Abdelrahman bassel and i added my iedas more 
        y_n = input(" you cannot add it , exists . do you want to update it Y/N ?").strip()
        if y_n == "y":
            prog = input("Write Skill progress").strip()
            cr.execute(f"update skills set progress='{prog}' where name ='{sk_name}' and user_id = '{uid}'")
        else:
            print("closed didnt add")

    commit_and_close()

    

def delete_skills():
    sk_name = input("write Skill Name").strip().capitalize()
    

    
    cr.execute(f"delete from skills where name='{sk_name}' and user_id='{uid}'")
    commit_and_close()

def update_skills():
    
    sk_name = input("write Skill Name").strip().capitalize()
   
    
    #my code add beacause if not found skill name = not continue
    cr.execute(f"select name from skills where name='{sk_name}' and user_id='{uid}'")
    result = cr.fetchone()
    if result != None:
        prog = input("write your new progress skill").strip()
        cr.execute(f"update skills set progress='{prog}' where name ='{sk_name}' and user_id = '{uid}'")
    else:
        print(f"not found skill name as {sk_name}")
       
       # my idea to check if you want add new skill if not exists in update
        y_no = input("not exisst , do you want add new skill. Y/N")
        
        if y_no=="y":
            sk_name = input("write new skill to adding")
            prog = input("write progres")
            cr.execute(f"insert into skills(name, progress, user_id) values('{sk_name}','{prog}','{uid}')")
        else:
            print("closed db thank you")
    commit_and_close()

commands_list = ["s","a","d","u","q"]

if user_input in commands_list:
    #print(f"your choice is exixst its right and is {user_input}")

    if user_input == "s":
        show_skills()
    elif user_input == "a":
        add_skills()
    elif user_input == "d":
        delete_skills()
    elif user_input == "u":
        update_skills()
    else:
        print("App closed")            

else:
    print("is not found command")





