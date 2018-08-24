## Models

Model_Name            | Description
----------------------|------------------------------------------------------------------------------------------------------
Subject               | Used to store *subject_name* and its corresponding *paper_id*.
Teacher               | Used to store *teacher_name* and their *department*.
TeacherSubjectMapping | Used to store the realationship between Subject and Teacher model. Eg. X teacher teach Y subject.
Section               | It store the seciton, branch, year, shift and Teacher -----> Subject record of a particular class.
Feedback	      | Used to store feedback of every teacher on the basis of the subject he/she teach.
