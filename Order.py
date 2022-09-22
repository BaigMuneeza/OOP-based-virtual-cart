from Account import Account
from ShoppingCart import ShoppingCart

class Order:
    while True:# system to create or login to an account.
            Account_info=Account()
            log=input('*Enter option number: ')
            if log!='1' and log!='2' :
                print('Invalid!\nTry Again!')
                continue
                
                
            if log=='1':
                 password=Account_info.Login()
                 if password=='None':
                    print('Account doesnot exist! Try again or Create Account\n')
                    continue
                 else:   
                   break

            if log=='2':   
                 password=Account_info.CreateAccount()
                 if password=='None':
                     print('This username or password is already taken,Try again\n')
                     continue
                 else:
                     break

        

    currentCart=ShoppingCart('Shoppingcart.txt') #instantiates an emptylist
 
    StorageList=ShoppingCart('ProductDatabase.txt')#instantiates an emptylist
    StorageList.LoadList()#loads the product Database file in the list


    def disp_products(self):#displays product menu
        print()
        Order.StorageList.ViewCart()
        
    def Shop(self):#shopping system
        print()
        print('#Please enter the ID of the Books you would like to purchase.\n#Enter E in place of ID to exit Shop mode.\n#######################################')
        Order.currentCart.order(Order.StorageList)
                         
    def View(self): #Displays contents of cart            
                 Order.currentCart.ViewCart()
                 
    def QuantityAdjust(self): #Adjust Quantity
        for i in range(1,1000):
            try:
                print()
                PId=input('*Enter ID of product: ')
                if PId in 'Ee':
                    print()
                    break
                    return
                else:                    
                    Quant=int(input('*Enter Quantity: '))
                    for i in Order.currentCart.cart:
                        if str(i[0])==PId:
                            initialQ=i[3]
                            i[3]=Quant
                            Order.currentCart.saveCart()
                            for m in Order.StorageList.cart:
                                  if str(m[0])==PId:
                                      if initialQ>=i[3]:
                                          s=initialQ-i[3]
                                          m[3]=m[3]+s
                                          Order.StorageList.saveCart()
                                      else:#initialQ<=i[3]:
                                          s=i[3]-initialQ
                                          m[3]=m[3]-s
                                          Order.StorageList.saveCart()
                                  else:
                                      pass
                        else:
                            pass
            except:
                print('Invalid Entry!!Try Again')
                continue

                        
                        

                 
    def removeP(self):# removes element from cart
            while True:
                        a=Order.currentCart.remove_item()
                        if a=='e':
                            break
                            return
                        else:                                    
                                Order.currentCart.saveCart()
                                Q=a[0]
                                Id=a[1]
                                for m in Order.StorageList.cart:
                                     if str(m[0])==str(Id):
                                         m[3]=m[3]+a[0]
                                         Order.StorageList.saveCart()
                        
                        

    def ShoppingHistory(self):#displays shopping history of User 
            history=ShoppingCart('Shoppinghistory.txt')##[] instanties an empty list
            history.LoadList()#loads shopping history of all users 
            for i in history.cart:#seearches for history of current user
                  if Order.log=='1':#if account exists
                      if str(i[0])==Order.password:
                            print('*************************************************************************')
                            i.extend(Order.currentCart.cart)
                            history.saveCart()
                            history.printHistory(i)
                            break
                      else:
                            pass

                  
                  elif Order.log=='2':#if its a new user
     
                                transfer=ShoppingCart('Shoppinghistory.txt')
                                transfer.LoadList()

                               
                                l=[Order.password]
                                l.extend(Order.currentCart.cart)
                                transfer.cart.append(l)               
                                transfer.saveCart()
                                Order.currentCart.ViewCart()
                                break



