import remove_duplicates
import missing_number
from fileparser import *
import retry_decorator

print("Task_1: remove_duplicates")
print(remove_duplicates.remove_duplicates("I like like the course"))
print(remove_duplicates.remove_duplicates("The text is a corrupted version version of the original"))

print("Task_2: missing_number")
case_1 = missing_number.MissingNumber()
print(case_1.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
case_2 = missing_number.MissingNumber()
print(case_2.missing_number([3, 0, 1]))

print("Task_3: retry_decorator")
retry_decorator.foo()

print("Task_4: file_parser")
file_parser1 = FileParser(file_path="file.json")
print(file_parser1.parse())
file_parser2 = FileParser(file_path="file.txt")
print(file_parser2.parse())
file_parser3 = FileParser(file_path="file.csv")
print(file_parser3.parse())
