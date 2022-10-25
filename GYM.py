#Get Age input
while True:
  Age = input("What's your age group?: ")
  try:
    Age = int(Age)
    if Age in range(14, 100):
      print("Accepted")
      break
    else:
      print("Error")
  except:
    print("Error, Please input a valid number")

#Get Weight input
while True:
  Weight = input("Weight Range in Kgs: ")
  try:
    Weight = int(Weight)
    if Weight in range(30, 250):
      print("Accepted")
      break
    else:
      print("Error")
  except:
    print("Error, Please input a valid number")
      
#Get Height input
while True:
  Height = input("Height range cms: ")
  try:
    Height = int(Height)
    if Height in range(120, 210):
      print("Accepted")
      break
    else:
      print("Error")
  except:
    print("Error, Please input a valid number")

#Get Gender input
while True:
  Gender = input("Gender Male or Female: ")
  try:
    Gender = str(Gender)
    if Gender == "Male":
      print("Accepted")
      break
    elif Gender == "Female":
      print("Accepted")
      break
    else:
      print("Error")
  except:
    print("Error, Please input a valid number")
      
#Calculate BMR
while True:
  try:
    if Gender == "Male":
      print("Accepted")
      BMR = 66.47 + (13.75*Weight) + (5.003*Height) - (6.755*Age)
      break
    elif Gender == "Female":
      print("Accepted")
      BMR = 655.1 + (9.563*Weight) + (1.85*Height) - (4.676*Age)
      break
    else:
      print("Error")
  except:
    print("Error, Please input a valid number")  

#Calculate BMI
while True:
  print("1: Little to no exercise")
  print("2: Little exercise")
  print("3: Light exercise")
  print("4: Moderate exercise")
  print("5: Heavy exercise")
  print("6: Very heavy exercise ")
  gym = input("Individual's level of exercise: ")
  try:
    if gym == "1":
      print("Accepted")
      kilcalorie = BMR * 1.2
      break
    elif gym == "2":
      print("Accepted")
      kilocalorie = BMR * 1.375
      break
    elif gym == "3":
      print("Accepted")
      kilocalorie = BMR * 1.55
      break
    elif gym == "4":
      print("Accepted")
      kilocalorie = BMR * 1.725
      break
    elif gym == "5":
      print("Accepted")
      kilocalorie = BMR * 1.9
      break
    else:
      print("Error")
  except:
    print("Error, Please input a valid number")  

#Calculate BMR and catogaries
m = Height / 100
BMI = Weight / ((m)*(m))

if 1<= BMI <= 18.5:
  categories = "Underweight"
elif 18.5<= BMI <=24.9:
  categories = "Normal Weight"
elif 25<= BMI <=29.9:
  categories = "Overweight"
elif 30<= BMI <=250:
  categories = "Obesity"
else:
  print("Error")

#Output 
BR = round(BMR, 2)
BI = round(BMI, 1)
KL = round(kilcalorie)

print("---------------GYM MEMBER DETAIL---------------")
print("Age :", Age)
print("Weight : ", Weight)
print("Gender : ", Gender)
print("Height : ", Height)
print("------------------------------")
print("BMR: ", BR)
print("BMI: ", BI)
print("BMI: ", "BMI=22(Normal Weight)")
print("Standard BMI categorie : ", categories)
print("Daily Intake to maintain current weight: ", KL)
print("-------------------------------")
