# Introduction-Python training
# Lecture 2: Data Types
# Assignment: Task1
# Created by Undral, Aug, 2022

"""
Question 1.Текст болон тооноос бүрдсэн list үүсгэн, list-н дээрх үйлдлүүдийг гүйцэтгэ
"""
s_grade=['Math', 60, 'Data Science', 73, 'Economy', 80]
type(s_grade)
# list operators
    s_grade[0] 
    s_grade[0-3]
    s_grade[0:3]
    s_grade[:1]
    s_grade[1:]
    s_grade[-1]
    s_grade[-3:-1]
    s_grade[-2:]
    s_grade[-1:]
    s_grade
# join
    s_grade_add=['English', 70]
    print(s_grade+s_grade_add)

# append
    s_subjects=['Math', 'Data Science', 'Economy']
    s_grades=[60, 73, 80]
    s_subjects.append(s_grades)
    print(s_subjects)

#insert into list
    s_grade.insert(-1,'English')
    print(s_grade)
 #extend 
    s_grades.extend(s_subjects)   
    print(s_subjects)

# remove by index
    s_grade.pop()
    s_grade.pop(-2)

#remove the value
    s_grade.remove('Math')
    s_grade

"""
Question 2.Өөрийн нэг найзын төрсөн огноог текстээс datatime-руу, datatime-аас текст рүү хөрвүүл
"""
import datetime
# text-->date
    birthdate_str1 = "20 June, 1988"
    print("birthdate_string =", birthdate_str1)
    birthdate_d1 = datetime.datetime.strptime(birthdate_str1, "%d %B, %Y")
    print("birthdate_date =", birthdate_d1)
    #
    birthdate_str2 = '2016/03/21' 
    birthdate_str2 = birthdate_str2.replace('/','-')
    birthdate_str2 = datetime.datetime.strptime(birthdate_str2, "%Y/%m/%d")
    print("birthdate_date =", birthdate_str2)

# date-->text
    birthdate=datetime.date(day=20,year=1988, month=6)
    birthdate_str = birthdate.strftime("%m/%d/%Y")
    print("birthday:", birthdate_str)

"""
Question 3. Сонгосон жижиг хүснэгтэн өгөгдлийг dictionary болгох жишээ үзүүл
"""

'''
Exmaple table: Student's grade
-------------------------------------------------------------------------------------
                                      Subject name  
-------------------------------------------------------------------------------------
                     Math                   Data Science         Economy                 
-------------------------------------------------------------------------------------
            Percentage Letter grade  Percentage Letter grade Percentage Letter grade 
-------------------------------------------------------------------------------------
Student1    60      D-               73          C-           70        C-           
Student2    70      C-               83          B-           89        B-           
Student3    90      A-               90          A-           95        A+           
-------------------------------------------------------------------------------------
'''
### Create Dictionary
student1={'Math_PG': 60, 'Math_LG': 'D-', 'DS_PG': 73, 'DS_LG': 'C-', 'Eco_PG': 70, 'Eco_LG': 'C-'}
student2={'Math_PG': 70, 'Math_LG': 'C-', 'DS_PG': 83, 'DS_LG': 'B-', 'Eco_PG': 89, 'Eco_LG': 'B-'}
student3={'Math_PG': 90, 'Math_LG': 'A-', 'DS_PG': 90, 'DS_LG': 'A-', 'Eco_PG': 95, 'Eco_LG': 'A+'}

# Estimate Overall grade
    import statistics
    student1['Tot_PG']=statistics.mean([student1['Math_PG'], student1['DS_PG'], student1['Eco_PG']])
    student2['Tot_PG']=statistics.mean([student2['Math_PG'], student2['DS_PG'], student2['Eco_PG']])
    student3['Tot_PG']=statistics.mean([student3['Math_PG'], student3['DS_PG'], student3['Eco_PG']])

    if((student1['Tot_PG']>=60) & (student1['Tot_PG']<65)):
        student1['Tot_LP']='D-'
    elif((student1['Tot_PG']>=65) & (student1['Tot_PG']<70)):
        student1['Tot_LP']='D+'
    elif((student1['Tot_PG']>=70) & (student1['Tot_PG']<75)):
        student1['Tot_LP']='C-'
    elif((student1['Tot_PG']>=75) & (student1['Tot_PG']<80)):
        student1['Tot_LP']='C+' 
    elif((student1['Tot_PG']>=80) & (student1['Tot_PG']<85)):
        student1['Tot_LP']='B-' 
    elif((student1['Tot_PG']>=85) & (student1['Tot_PG']<90)):
        student1['Tot_LP']='B+'
    elif((student1['Tot_PG']>=90) & (student1['Tot_PG']<95)):
        student1['Tot_LP']='A-'    
    elif(student1['Tot_PG']>=95):
        student1['Tot_LP']='A+'
    else:
        student1['Tot_LP']='F'

    if((student2['Tot_PG']>=60) & (student2['Tot_PG']<65)):
        student2['Tot_LP']='D-'
    elif((student2['Tot_PG']>=65) & (student2['Tot_PG']<70)):
        student2['Tot_LP']='D+'
    elif((student2['Tot_PG']>=70) & (student2['Tot_PG']<75)):
        student2['Tot_LP']='C-'
    elif((student2['Tot_PG']>=75) & (student2['Tot_PG']<80)):
        student2['Tot_LP']='C+' 
    elif((student2['Tot_PG']>=80) & (student2['Tot_PG']<85)):
        student2['Tot_LP']='B-' 
    elif((student2['Tot_PG']>=85) & (student2['Tot_PG']<90)):
        student2['Tot_LP']='B+'
    elif((student2['Tot_PG']>=90) & (student2['Tot_PG']<95)):
        student2['Tot_LP']='A-'    
    elif(student2['Tot_PG']>=95):
        student2['Tot_LP']='A+'
    else:
        student2['Tot_LP']='F'

    if((student3['Tot_PG']>=60) & (student3['Tot_PG']<65)):
        student3['Tot_LP']='D-'
    elif((student3['Tot_PG']>=65) & (student3['Tot_PG']<70)):
        student3['Tot_LP']='D+'
    elif((student3['Tot_PG']>=70) & (student3['Tot_PG']<75)):
        student3['Tot_LP']='C-'
    elif((student3['Tot_PG']>=75) & (student3['Tot_PG']<80)):
        student3['Tot_LP']='C+' 
    elif((student3['Tot_PG']>=80) & (student3['Tot_PG']<85)):
        student3['Tot_LP']='B-' 
    elif((student3['Tot_PG']>=85) & (student3['Tot_PG']<90)):
        student3['Tot_LP']='B+'
    elif((student3['Tot_PG']>=90) & (student3['Tot_PG']<95)):
        student3['Tot_LP']='A-'    
    elif(student3['Tot_PG']>=95):
        student3['Tot_LP']='A+'
    else:
        student3['Tot_LP']='F'

print(student1)
print(student2)
print(student3)

big_dict = {"Not bad": student1, "Good": student2, 'Very good': student3}
big_dict
''' RESULT
------------------------------------------------------------------------------------------------------------
                                                    Subject name  
------------------------------------------------------------------------------------------------------------
                     Math                   Data Science         Economy                  Overall
------------------------------------------------------------------------------------------------------------
            Percentage Letter grade  Percentage Letter grade Percentage Letter grade Percentage Letter grade
------------------------------------------------------------------------------------------------------------
Student1    60      D-               73          C-           70        C-           67.7       D+
Student2    70      C-               83          B-           89        B-           80.7       B-
Student3    90      A-               90          A-           95        A+           91.7       A-
------------------------------------------------------------------------------------------------------------
'''
