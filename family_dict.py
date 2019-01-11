# Define a dictionary that contains information about several members of your family. Use the following example as a template.

my_family = {
  "wife": {
    "name": "Sadie",
    "age": 26
  },
  "brother": {
    "name": "Brandon",
    "age": 26
  },
  "mother": {
    "name": "Susan",
    "age": 66
  },
  "father": {
    "name": "Mike",
    "age": 69
  }
}



family_list = {f'{member_info["name"]} is my {family_member} and is {str(member_info["age"])}' for (family_member, member_info) in my_family.items()
  }

# Using a dictionary comprehension, produce output 

print(family_list)


