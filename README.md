# CollegeProject
This is a feedback system project. Through this project, we are digitalizing the feedbacks given by the students for their teachers and making them anonymous as well as abstract from the teachers.
There are many drawbacks of the traditional system. Such as, some of the teachers were able to figure out which feedback is given by whom. The evaluation scores had to be fed into the database, which led to wastage of manpower, time and paper. At times it is difficult to understand the writing of the student which makes it troublesome for understanding the suggestion given by the student. 
So, this project is designed to tackle all these problems efficiently and only admin will be able to see the outcome of the feedback given by students for the respective teachers in a convenient manner.
But there is also another problem, some students are not regular in colleges but give the feedback due to which it may harm the profile of a good teacher. So, we will also develop our project in such a way that, the feedbacks of such students will not affect the feedback of a teacher.
Initially we are only focussing on the student's section in our project.So details are as follows-:
Models in our project
----------------------
1)StudentInfo -:This model contains the student's Name, Enrollment Number, Section and Password.
2)TeacherSection -:This model contains Section as a list and teachers as list element's.
3)Feedback-:This model contain's all the review results that was given by student's.
Forms in our project
--------------------
1)StudentLogin -:Contain only Username and Password 
2)StudentRegister-:Contains all as StudentInfo model and also a password confirmation field. 
3)Rating -:This form will contain all info related to Feedback modeland also to TeacherSection model.

