import collections
print("TASK 1.1")
str=input("string; ")
tipl= list(str)
print(tipl)
print("TASK 1.2")
col = collections.Counter(str)
print(col)
print("TASK1.3")

list_vow = []
list_cons = []
list_symb = []

for char in col:
    if char in ['a','e','i','o','u']:
        list_vow.append(char)
    elif char.isalpha():
        list_cons.append(char)
    else:
        list_symb.append(char)

print("List of Vowels: ", list_vow)
print("List of Consonants: ", list_cons)
print("List of Symbols: ", list_symb)
# print("TASk1.4")
# list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]

# sorted_list = sorted(list_A)

# n = len(sorted_list)
# quartile_size = n // 4
# q1_size = quartile_size
# q2_size = quartile_size
# q3_size = quartile_size

# if n % 4 != 0:
#     q1_size += n % 4  

# q1 = sorted_list[:q1_size]
# q2 = sorted_list[q1_size:q1_size + q2_size]
# q3 = sorted_list[q1_size + q2_size:q1_size + q2_size + q3_size]
# q4 = sorted_list[q1_size + q2_size + q3_size:]

# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)

# print("TASK2.1")
# def create_student_dict(name, assignment_scores, lab_scores, test_scores):
#     student_dict = {}
#     student_dict['Name'] = name
#     student_dict['Assignment Scores'] = assignment_scores
#     student_dict['Lab Scores'] = lab_scores
#     student_dict['Test Scores'] = test_scores
#     return student_dict

# student1 = create_student_dict('Adam', [82, 56, 44, 30], [78, 77], [78.2, 77.2])
# print(student1)
# print("TASK2.2")
# def check_submission(student_dict):
#     submission_check = {}
#     for student in student_dict:
#         if len(student_dict[student]['Assignment Scores']) == 4 and len(student_dict[student]['Lab Scores']) == 2 and len(student_dict[student]['Test Scores']) == 2:
#             submission_check[student] = 6
#         else:
#             submission_check[student] = len(student_dict[student]['Assignment Scores']) + len(student_dict[student]['Lab Scores']) + len(student_dict[student]['Test Scores'])
#     return submission_check

# student_dict = {
#     'Adam': {'Name': 'Adam', 'Assignment Scores': [82, 56, 44, 30], 'Lab Scores': [78, 77], 'Test Scores': [78.2, 77.2]},
   
# }
# submission_check = check_submission(student_dict)
# print(submission_check)
# print("TASK2.3")
# def calculate_final_grade(student_dict):
#     final_grades = {}
#     for student in student_dict:
#         if len(student_dict[student]['assignment']) >= 4 and len(student_dict[student]['lab']) >= 2 and len(student_dict[student]['test']) >= 2:
#             assignment_average = sum(student_dict[student]['assignment']) / len(student_dict[student]['assignment'])
#             lab_average = sum(student_dict[student]['lab']) / len(student_dict[student]['lab'])
#             test_average = sum(student_dict[student]['test']) / len(student_dict[student]['test'])
#             final_grade = 0.3 * assignment_average + 0.5 * lab_average + 0.2 * test_average
#             final_grades[student] = final_grade
#         else:
#             final_grades[student] = 0
#     return final_grades

# student_dict = {
#     'Adam': {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'lab': [78.2, 77.2], 'test': [78, 77]}
# }
# final_grades = calculate_final_grade(student_dict)
# student_dict['Adam']['final_grade'] = final_grades['Adam']
# print(student_dict)
# print("TASK2.4")
# def create_nested_dict(student_dict):
#     nested_dict = {}
#     for student in student_dict:
#         if 'final_grade' in student_dict[student]:
#             nested_dict[student_dict[student]['name']] = {'Assignment Scores': student_dict[student]['assignment'], 'Lab Scores': student_dict[student]['lab'], 'Test Scores': student_dict[student]['test'], 'Final Grade': student_dict[student]['final_grade']}
#     return nested_dict

# student_dict = {
#     'Adam': {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'lab': [78.2, 77.2], 'test': [78, 77], 'final_grade': 70.25},
#     'Kevin': {'name': 'Kevin', 'assignment': [82, 30], 'lab': [78.2], 'test': [], 'final_grade': 0}
# }
# nested_dict = create_nested_dict(student_dict)
# print(nested_dict)
print("task3.1")
def threeone():
    transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2),(1001, 1)]

    stats = {}

    for user_id, transaction_type in transactions:
        if user_id not in stats:
            stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}

        if transaction_type in [1, 2, 3]:
            stats[user_id][transaction_type] += 1


    for user_id, user_data in stats.items():
        transaction_counts = [(t, user_data[t]) for t in [1, 2, 3]]
        transaction_counts.sort(key=lambda x: -x[1])
        most_frequent = transaction_counts[0][0]
        least_frequent = transaction_counts[-1][0]
        stats[user_id]['mft'] = most_frequent
        stats[user_id]['lft'] = least_frequent

    print(stats)



a={
    "name":"Nazzere",
    "hskhck":"jkdjesl",
    "labs": [2,3,5]
}
print(a["labs"][2])

