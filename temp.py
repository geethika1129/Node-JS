""" def python_func(name , key=3):
    while key>0:
        print(name[:2 :-3],end="")
        key=key-1
print(python_func("TanaNisha")) """
 
""" sq={i:i*i for i in range(2,6)}
print(sq) """

""" def ex(val):
    val=val+'4'
    val=val*2
    return val
print(ex("jump")) """

""" car={'Audi','bmw','scorpio'}
print(car&set('Mycar'))
 """

""" text="CCC Training"
a=0
while a<len(text):
 print(text[a],end=" ")
 a-=1 """

""" check=bytearray(2)
print(check,len(check)) """

""" word="positive"
print(word[:2]) """

""" try:
  num1=10.25
  num2=20+10j
  print(num1^num2)

except ValueError:
 print("values")
except TypeError:
 print("datatypes") """

""" def student():
    name="niki"
    age=20
    return name and age
print(student()) """

""" alph ={'A':65,'B':66,'C':67,'D':68}
tot=0
for i in alph.values():
    tot+=i
print(tot) """

""" days={'Monday', 'Tuesday','Wednessday'}
leave_days={'Saturday','Sunday'}
days.update(leave_days)
print(days&leave_days) """

""" num=10
if False :
 num-= 100
else:
  num+=50
print(num) """

""" user = str
end = "0"
hours = round(40,2)
print("One Stop Shop Payroll Calculator")
hours = (float(input("Please enter hours worked: ", )))
payrate =(float(input("Please enter your payrate: $", )))
if hours < 40:
 print("Employee's name: ", user)
 print("Overtime hours: 0")
 print("Overtime Pay: $0.00")
 regularpay = round(hours * payrate, 2)
 print("Gross Pay: $", regularpay)
elif hours > 40:
 overtimehours = round(hours - 40.00,2)
 print("Overtime hours: ", overtimehours)
 print("Employee's name: ", user)
 regularpay = round(hours * payrate,2)
 overtimerate = round(payrate * 1.5, 2)
 overtimepay = round(overtimehours * overtimerate)
 grosspay = round(regularpay+overtimepay,2)
 print("Regular Pay: $", regularpay)
 print("Overtime Pay: $",overtimepay)
 print("Gross Pay: $", grosspay)
while user != end:
 print()
 user = input("Please enter your name or type '0' to quit: ")
if user == end:
 print("End of Report") """

 #2+22+222..........
""" terms=5
sum=0
for i in range(terms+1):
    sum+=i """

""" def unique(l):
  x=[]
  for i in l:
      if x not in l:
          x.append(i)
          return x
list=[1,2,3,4,1,2]
k=unique(list)
print(k) """

""" def make_bold(fn):
 def wrapped():
  return "<b>" + fn() + "</b>"
 return wrapped
def make_italic(fn):
 def wrapped():
   return "<i>" + fn() + "</i>"
 return wrapped
def make_underline(fn):
 def wrapped():
   return "<u>" + fn() + "</u>"
 return wrapped
@make_bold
@make_italic
@make_underline
def hello():
 return "hello world"
print(hello()) """

""" 
n=5
for i in range(1,n+1):
    print('cube of:'+str(i )+'is :'+str(i*i*i))  """

""" import random
def Rand(start, end, num):
  res = []
  for j in range(num):
    res.append(random.randint(start, end))
  return res
# Driver Code
num = 10
start = 20
end = 40
print(type(Rand))
print(Rand(start, end, num)) """

""" n=5
sum=0
for i in range(n+1):
    sum+=i
print(sum) """

# import required packages
import sqlite3
# Create a connection anf cursor
con = sqlite3.connect(&#39;file4.db&#39;)
c = con.cursor()
# create a function to print the whole table:
def printall():
global c
for row in c.execute(&quot;SELECT * FROM datatable&quot;):
print(row)

# Create a sample table and insert data into it:
c.execute(&quot;CREATE TABLE datatable(ID INTEGER,Name TEXT);&quot;)
# INSERT
namelist = [(1,&#39;Aman&#39;),(2,&#39;Aviraj&#39;),(3,&#39;Venkat&#39;)]
c.executemany(&quot;INSERT INTO datatable VALUES(?,?)&quot;,namelist)
con.commit()
print(&quot;\nInitial table: &quot;)
printall()
# DELETE
print(&quot;\nDeleting an enrty : (3,Venkat)&quot;)
c.execute(&quot;DELETE FROM datatable WHERE Name = &#39;Venkat&#39;;&quot;)
print(&quot;\nTable is now: &quot;)
printall()
# UPDATE
print(&quot;\nUpdating a name to full name:&quot;)
print(&quot;\nTable is now: &quot;)
c.execute(&quot;UPDATE datatable SET Name=&#39;AMAN BHAI PATEL&#39; WHERE ID=1;&quot;)
printall()


  