#配列
arr = ["Python", "PHP", "Ruby"]

print(arr[0]) #Python
print(arr[1]) #PHP
print(arr[2]) #Ruby

for lang in arr:
  print(lang) #Pytho PHP Ruby
  print(f"{lang}講座")
  
for lang in arr:
  if lang == "PHP":
    continue
  print(lang) #Python Ruby

#連想配列
arr = {"key1": "Python", "key2": "PHP"}

print(arr["key1"]) #Python

for key in arr:
  print(key) #key1 key2
  print(arr[key]) #Python PHP
  
for key, val in arr.items():
  print(f"{key}は{val}です")
