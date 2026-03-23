student = {
    "name":"Alice",
      "age":"21", 
      "subjects": ["maths", "physics", "programming"], 
      "scores": {
          "Maths": 18,
          "Physics": 16,
          "Programming": 19 }
          }
print(student["subjects"][1])
print(student["scores"]["Programming"])
student["subjects"].append("Chemistry")
student["scores"]["Chemistry"] =17
print(student)
