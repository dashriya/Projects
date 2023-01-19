name = input("Input student's name: ")
stud_score = int(input("Input student's score: "))

if stud_score >= 90:
    print("Student recieves a A grade.")
elif stud_score >= 80:
    print("Student recieves a B grade.")
elif stud_score >= 70: 
    print("Student recieves a C grade.")
elif stud_score >= 60:
    print("Student recieves a D grade.")
#else: (nest if else statements)
    #if stud_score >= 80:
       # print("Student recieves a B grade.")
   # else: 
       # if stud_score >= 70:
           # print("Student recieves a C grade.")
      #  else:
          #  if stud_score >= 60:
           #     print("Student recieves a D grade.")