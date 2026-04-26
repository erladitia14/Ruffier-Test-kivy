''' Module for calculating the results of the Ruffier tests.
 
The sum of the three attempts at heart rate readings (before exertion, right after exertion, and after a short break)
ideally, there should be no more than 200 beats per minute.
We suggest that the children measure their heart rate for 15 seconds,
and we get the result of beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result is from the ideal 200 beats, the worse it is.
Traditionally, tables are given for the values divided by 10.
 
Ruffier index  
   RI = (S - 200) / 10
is evaluated according to age according to the table:
       7–8             9–10                11–12               13–14               15+ (only for adolescents!)
perfect    6.4 and below   4.9 and below       3.4 and below         1.9 and below               0.4 and below
good    6.5–11.9     5–10.4          3.5–8.9           2–7.4                   0.5–5.9
satisfactory  12–16.9      10.5–15.4       9–13.9            7.5–12.4                6–10.9
weak  17–20.9      15.5–19.4       14–17.9           12.5–16.4               11–14.9
unsatisfactory   21 and above     19.5 and above      18 and above          16.5 and above             15 and above
 
the result “unsatisfactory” is 4 away from the result “weak” for all ages,
“weak” is 5 away from “satisfactory,” and “good” is 5.5 away from “satisfactory,”
 
so we will write a function ruffier_result(r_index, level) which will produce
the calculated Ruffier index and “unsatisfactory” level for the tested age, and produce a result
 
'''
# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart performance: "
txt_nodata = '''
there is no data for that age'''
txt_res = []
txt_res.append('''low.
Go see your doctor ASAP!''')
txt_res.append('''satisfactory.
Go see your doctor!''')
txt_res.append('''average.
It might be worth doing additional tests at the doctor.''')
txt_res.append('''
higher than average''')
txt_res.append('''
high''')
 
def ruffier_index(P1, P2, P3):
   ''' it returns the index value according to the three pulse calculations for comparison with the table'''
   S = 4 * (P1 + P2 + P3)
   return (S - 200) / 10

def neud_level(age):
   ''' the options with an age of less than 7 and with adults have to be processed separately,
   here we select the level "unsatisfactory" only within the table:
   for the age of 7, "unsatisfactory" is an index of 21, then onwards every 2 years it decreases by 1.5 until the level of 15 at age 15-16 '''
   if age < 7:
       return None
   if age <= 8:
       return 21
   if age <= 10:
       return 19.5
   if age <= 12:
       return 18
   if age <= 14:
       return 16.5
   return 15

def ruffier_result(r_index, level):
   ''' the function obtains a Ruffier index and interprets it,
   we return the readiness level: a number from 0 to 4
   (the higher the readiness level, the better).  '''
   if r_index >= level:
       return 0  # low / unsatisfactory
   if r_index >= level - 4:
       return 1  # satisfactory / weak
   if r_index >= level - 9:
       return 2  # average / satisfactory
   if r_index >= level - 14.5:
       return 3  # higher than average / good
   return 4  # high / perfect

def test(P1, P2, P3, age):
   ''' this function can be used from outside the module for calculating the Ruffier index.
   We return the ready texts that just need to be written in the necessary place
   We use the constants used at the beginning of this module for texts. '''
   level = neud_level(age)
   if level is None:
       return txt_nodata
   r_index = ruffier_index(P1, P2, P3)
   result = ruffier_result(r_index, level)
   return txt_index + str(round(r_index, 1)) + "\n" + txt_workheart + txt_res[result]
