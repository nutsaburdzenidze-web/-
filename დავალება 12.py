# დავალება 1
# import json, os, sys

# def create_json_file(path, file):
#     file_path = f"{path}/{file}.json"
#     os.makedirs(path, exist_ok=True)
#     try:
#         with open(file_path, mode='x', encoding='utf-8') as f:
#             ...
#     except FileExistsError:
#         print("file already exists")
#     return file_path

# file_path = create_json_file('files', 'data')




# დავალება 2


# import json, os
# from pprint import pp

# def read_json_file(path):
#     try:
#         with open(path, mode='r', encoding='utf-8') as f:
#             return json.loads(f.read())
#     except FileNotFoundError:
#         print("File not found.")

# file_path = "files/data.json"

# file_content = read_json_file(file_path)
# pp(file_content)
# დავალება 3
# import json, os
# chess_players = [
#   {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
#   {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
#   {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
#   {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
#   {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
#   {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
#   {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
#   {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
#   {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
# ]

# new_students = [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]
# def write_json_file(path, json_data):
#   with open(path, mode='w', encoding='utf-8') as f:
#     f.write(json.dumps(json_data, indent=2))
# def read_json_file(path):
#     try:
#         with open(path, 'r', encoding='utf-8') as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []

# def write_json_file(path, json_data):
#   with open(path, mode='w', encoding='utf-8') as f:
#     f.write(json.dumps(json_data, indent=2))
   

# def update_file(path, new_students):
#  data = read_json_file(path)
 
#  for new_student in new_students:
#     for st in data:  
#             if st['id'] == new_student['id']:
#                 print("student with id already exists")
#                 break
#     else:
#         data.append(new_student)

#  write_json_file(path, data)
#  return data
    



# file_path = "files/data.json"
# write_json_file(file_path, chess_players)
# data = update_file(file_path, new_students)
# print(data)

# დავალება 4
# import json, os

# def update_file(path, new_data):
#     try:
#         with open(path, mode='r', encoding='utf-8') as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         data =[]
#     for item in new_data:
#         data.append(item)
#     with open(path, mode='w', encoding='utf-8') as f:
#         json.dump(data, f, indent=2)
#     return data