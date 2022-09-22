from ListManager import ListManager
## Accounts creates or logs into an account
class Account:
     info=ListManager()
     info.readFromFile('Accountinfo.txt')
     def Login(self):## Login system,searches the accounts file for password and username match,if account doesnot exist shall return None which will trigger a respose telling the user that account doesnot exist.
                  password='None'
                  x=input('\n*Enter User Name: ')
                  x1=input('*Enter Password: ')
                  for i in Account.info.general_list:
                      if i[0]==x and i[1]==x1:
                          print()
                          print('*Login was Successful!!!')
                          password=x1
                          break
                      else:
                          pass
                  return password 
                  
         
     def CreateAccount(self):##Creates a new account and stores info in account file, if username or password already exists,triggers a respose telling the user that username or password already exists.
        
        x=input('\n*Enter User Name: ')
        x1=input('*Enter Password: ')
        x2=input('*Enter Full Name: ')
        x3=input('*Enter Adress: ')
        password='None'
        for i in Account.info.general_list:
             if i[0]==x or i[1]==x1:
                  return password
             else:
                  pass
              
     
        Account.info.general_list.append([x,x1,x2,x3])
        Account.info.saveToFile('Accountinfo.txt')
        print()
        print('*Account Created Successesfully!!!!')
        return x1





                    
        
