my_dict = {
  "students": [
    {"id": 20, "name": "Giorgi", "age": 25},
    {"id": 25, "name": "Giorgi", "age": 23},
    {"id": 56, "name": "Nika", "age": 25},
    {"id": 100, "name": "Nika", "age": 22},
    {"id": 1232, "name": "Dato", "age": 22},
    {"id": 846723, "name": "Archili", "age": 32}
  ],
  "subjects": [
    {"id": 1, "name": "Math", "grades": {"20": "B", "25": "A", "56": "B", "100": "A", "1232": "C", "846723": "A"}},
    {"id": 2, "name": "Physics", "grades": {"20": "A", "25": "B", "56": "B", "100": "A", "1232": "C", "846723": "B"}},
    {"id": 3, "name": "English", "grades": {"20": "A", "25": "A", "56": "A", "100": "A", "1232": "B", "846723": "A"}},
    {"id": 4, "name": "Chemistry", "grades": {"20": "B", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
    {"id": 5, "name": "History", "grades": {"20": "C", "25": "B", "56": "B", "100": "A", "1232": "A", "846723": "A"}},
  ]
}
st_id = int(input("studentebis ID: 20, 25, 56, 100, 1232, 846723. airchiet studentis ID: "))

for students in my_dict["students"]:
 if st_id == students["id"]:
  st_name = students['name']
  st_age = students['age']
    
print("student information")
print(f"ID: {st_id}, Name: {st_name}, age: {st_age} ")

for subjects in my_dict.get('subjects'):
      st_subject = subjects.get('name')
      for grades in subjects.get('grades'):
        if str(st_id) in grades:
           st_grade = subjects['grades'].get(str(st_id))
           print(f"subject: {st_subject}, grade: {st_grade}")
