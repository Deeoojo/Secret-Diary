from replit import db
import datetime, os, time

def add():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f'Diary entry for {timestamp}')
  print()
  Convo = input("Talk to me: >")
  db[timestamp] = Convo

def view():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f'''{key} {db[key]}''')
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0] =='e'):
      break
password = input("Password: ")
if password != "Danny1":
  print("Imposter")
  exit()
while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    add()
  else:
    view()
