## Django Assignment  
### Scenario:  
- A school has Teachers, Students, Classroom, Subjects as it’s entities  
- Teachers details include name, DOJ, subjects he/she teaches, salary  
- Students details include name, DOJ, standard, roll no, ranking, point of contact (Relatives name, number and relation: could be more than 1), 
- Classroom details include seating capacity, web lecture support, shape (oval, rectangular, canopy, elevated), 
- Subjects: Chapters, total durations, per class duration(can range between 30 mins to 120 mins), 
  
### Suggestions and Assumptions:   
- Teachers : 
  - Turing: DOJ: 22 Aug 2017 | Subjects: Math, English | Salary: 18 LPA in hand | Also takes Web lectures. 
  - Dinho: DOJ: 1 Jan 2016 | Subjects: Sports, Health Science | Salary: 25 LPA in hand 
  - Adele: DOJ: 1 Mar 2015 | Subjects: English | Salary: 10 LPA in hand 
  - Freddie: DOJ: 1 Aug 2017 | Subjects: Music, English | Salary: 20 LPA in hand | Also takes Web lectures. 
  - Dalton: DOJ: 1 Mar 2017 | Subjects: Botany, Zoology | Salary: 9 LPA in hand | Also takes Web lectures. 
  - Harish: DOJ: 1 Feb 2017 | Subjects: Math, Science | Salary: 18 LPA in hand 
  - Trump: DOJ: 1 Aug 2017 | Subjects: Political Science, Business Administration, Foreign Affairs | Salary: 8 LPA in hand 
  - Swaraj: DOJ: 1 Sept 2019 | Subjects: Foreign Affairs, Negotiations | Salary: 28 LPA in hand | Also takes Web lectures. 
  - Socrates: DOJ: 1 June 2015 | Subjects: Philosophy, Moral Science | Salary: 11.5 LPA in hand | Also takes Web lectures. 
- Assume students as per your will. A class will have at least 15 students. A student can take more than 1 class 
- Ensure Model architecture isn’t redundant. 
- Ensure the number of model queries for each problem statements is not more than 1. 
- I may entries to entities in the live scenario. 
  
### Problem statement: 
- Tabular preview of the classroom, subjects being taught in those classrooms, teachers using the same. 
- Search option to show a list of students attending a teacher’s class (teacher can be searched by name) 
- No of students taught by teachers earning more than 1 Lac per month and the sum of their salaries. 
- No of students, No of teachers, and total hours required for subjects that are taught by more than 1 teacher. 
  
### Must: 
- Use both CBV and FBV. 
- Ensure no extra params are entertained in get/post data. 
- Validate data based on type, length, uniqueness before injecting in the DB. 
- Make the best use of ORM. 
- Indicate the concept of relational DB through Django relation. 
  
### You can: 
- Use Django Templates or React/Angular or any other Frontend Framework for UI 
- host the solution in Heroku or any cloud server 
- share the code either via mail or Online code repository 
  
