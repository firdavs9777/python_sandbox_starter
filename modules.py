# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core Modules 
import datetime 
from datetime import date
import time
from time import time
import camelcase # type: ignore
# import validator
from validator import validate_email
# today = datetime.date.today()

today = date.today()
# timestamp =  time.time()
timestamp =  time()
print(timestamp)
print(today)

c = camelcase.CamelCase()
text = "hello world from python"
camel_text = c.hump(text)
print(camel_text) 


email = 'test@gmail.com'
if(validate_email(email)):
  print('Valid')
else:
  print('Not valid')