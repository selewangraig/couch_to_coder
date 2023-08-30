employees = [
 {
 "first_name":"Jose",
 "last_name":"Lopez",
 "email":"joselopez0944@example.com",
 "age":25,
 "job_title":"Project Manager",
 "years_of_experience":1,
 "salary":8500,
 "department":"Product"
 },
 {
 "first_name":"Diane",
 "last_name":"Carter",
 "email":"dianecarter1228@example.com",
 "age":26,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":2,
 "salary":7000,
 "department":"Product"
 },
 {
 "first_name":"Shawn",
 "last_name":"Foster",
 "email": None,
 "age":37,
 "job_title":"Customer Service Rep",
 "years_of_experience":14,
 "salary":17000,
 "department":"Business"
 },
 {
 "first_name":"Brenda",
 "last_name":"Fisher",
 "email":"brendafisher3185@example.com",
 "age":31,
 "job_title":"Web Developer",
 "years_of_experience":8,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Sean",
 "last_name":"Hunter",
 "email": None,
 "age":35,
 "job_title":"Project Manager",
 "years_of_experience":11,
 "salary":14500,
 "department":"Product"
 },
 {
 "first_name":"Joshua",
 "last_name":"Jacobs",
 "email":"joshuajacobs5904@example.com",
 "age":28,
 "job_title":"Project Manager",
 "years_of_experience":3,
 "salary":10500,
 "department":"Business"
 },
 {
 "first_name":"Brianna",
 "last_name":"Marshall",
 "email":None,
 "age":33,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":10,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"John",
 "last_name":"Tate",
 "email":"johntate7881@example.com",
 "age":33,
 "job_title":"Mobile Developer",
 "years_of_experience":10,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"Jillian",
 "last_name":"Byrd",
 "email":None,
 "age":34,
 "job_title":"Business Analyst",
 "years_of_experience":10,
 "salary":11000,
 "department":"Business"
 },
 {
 "first_name":"Melanie",
 "last_name":"Sharp",
 "email":"melaniesharp9256@example.com",
 "age":41,
 "job_title":"Web Developer",
 "years_of_experience":15,
 "salary":14500,
 "department":"Product"
 },
 {
 "first_name":"Brandy",
 "last_name":"Mckee",
 "email":None,
 "age":37,
 "job_title":"Marketing Manager",
 "years_of_experience":14,
 "salary":14000,
 "department":"Business"
 },
 {
 "first_name":"Robert",
 "last_name":"Simpson",
 "email":"robertsimpson11778@example.com",
 "age":36,
 "job_title":"Marketing Manager",
 "years_of_experience":12,
 "salary":15000,
 "department":"Business"
 },
 {
 "first_name":"George",
 "last_name":"Mckenzie",
 "email":"georgemckenzie12384@example.com",
 "age":28,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":4,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Joseph",
 "last_name":"Smith",
 "email":None,
 "age":40,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":14,
 "salary":14000,
 "department":"Product"
 },
 {
 "first_name":"Dana",
 "last_name":"Crawford",
 "email":"danacrawford14310@example.com",
 "age":32,
 "job_title":"Project Manager",
 "years_of_experience":8,
 "salary":12000,
 "department":"Product"
 },
 {
 "first_name":"Christopher",
 "last_name":"Benson",
 "email":None,
 "age":29,
 "job_title":"Web Developer",
 "years_of_experience":5,
 "salary":7500,
 "department":"Product"
 },
 {
 "first_name":"Nicole",
 "last_name":"Smith",
 "email":"nicolesmith16360@example.com",
 "age":26,
 "job_title":"Designer",
 "years_of_experience":4,
 "salary":10000,
 "department":"Product"
 },
 {
 "first_name":"Peter",
 "last_name":"Jimenez",
 "email":"peterjimenez17791@example.com",
 "age":28,
 "job_title":"UX Designer",
 "years_of_experience":3,
 "salary":6500,
 "department":"Business"
 },
 {
 "first_name":"Sergio",
 "last_name":"Boyle",
 "email":"sergioboyle18425@example.com",
 "age":31,
 "job_title":"Tester",
 "years_of_experience":6,
 "salary":9000,
 "department":"Product"
 },
 {
 "first_name":"Brianna",
 "last_name":"Moss",
 "email":None,
 "age":31,
 "job_title":"Designer",
 "years_of_experience":5,
 "salary":10500,
 "department":"Product"
 },
 {
 "first_name":"Taylor",
 "last_name":"Garner",
 "email":"taylorgarner20196@example.com",
 "age":32,
 "job_title":"Machine Learning Engineer",
 "years_of_experience":6,
 "salary":11000,
 "department":"Product"
 },
 {
 "first_name":"Michael",
 "last_name":"Padilla",
 "email":"michaelpadilla21381@example.com",
 "age":29,
 "job_title":"Customer Service Rep",
 "years_of_experience":5,
 "salary":9500,
 "department":"Business"
 },
 {
 "first_name":"Yvette",
 "last_name":"Walker",
 "email":None,
 "age":26,
 "job_title":"Designer",
 "years_of_experience":2,
 "salary":7000,
 "department":"Product"
 },
 {
 "first_name":"Kristina",
 "last_name":"Pena",
 "email":"kristinapena23750@example.com",
 "age":34,
 "job_title":"Business Analyst",
 "years_of_experience":11,
 "salary":12500,
 "department":"Business"
 }
]

#print the name of the person who has the highest salary
highest_salary = 0
highest_salary_name = ""
for i in range(len(employees)):
    if employees[i]["salary"] > highest_salary:
        highest_salary = employees[i]["salary"]
        highest_salary_name = employees[i]["first_name"] + " " + employees[i]["last_name"]
        

print("The employee with the highest salary is ", highest_salary_name)

#print the combined years of experience of all employees at the company
total_years = 0
for i in range(len(employees)):
    total_years += employees[i]["years_of_experience"]

print("\nThe total years of experience is ", total_years)

#Some people don't have an email address - collect their details into a new list!
no_email = []
for i in range(len(employees)):
    if employees[i]["email"] == None:
        no_email.append(employees[i])

print("\nPeople with no email address: ", no_email)

#Which one costs more for the company - Product department salaries or Business department salaries?
product_salaries = 0
business_salaries = 0
for i in range(len(employees)):
    if employees[i]["department"] == "Product":
        product_salaries += employees[i]["salary"]
    else:
        business_salaries += employees[i]["salary"]

if product_salaries > business_salaries:
    print("\nProduct department salaries cost more than business department salaries.")
else:
    print("\nBusiness department salaries cost more than product department salaries.")

#What is the average salary for people over 30 years of age?
over_30_salaries = 0
over_30_count = 0
for i in range(len(employees)):
    if employees[i]["age"] > 30:
        over_30_salaries += employees[i]["salary"]
        over_30_count += 1
        
average_over_30 = round((over_30_salaries / (float)(over_30_count)),2 )
print("\nThe average salary for people over 30 is ", average_over_30)

#Create a new dict and calculate how many people are working with certain job titles.
job_titles = {}
for i in range(len(employees)):
    if employees[i]["job_title"] in job_titles:
        job_titles[employees[i]["job_title"]] += 1
    else:
        job_titles[employees[i]["job_title"]] = 1

print("\nNumber of people with each job title: ", job_titles)