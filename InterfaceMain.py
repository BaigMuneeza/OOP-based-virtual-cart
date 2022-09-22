from Menu  import Menu
from Order import Order
from Quote import Quotes

class UserInterface:
    def __init__(self):
            while True:
                m=Menu()#displays menu
                o=Order()
                print('*You can proceed to shop\n\n**********************Displaying Available Books****************************: ')
                o.disp_products()#displays products
                o.Shop()#shop system
                while True:
                    while True:
                        try:
                            UserInterface.subMenu() #sub menu
                            print('*To select an option enter corresponding number\npress E to exit menu*\n')
                            n=input('*Enter number corresponding to the editing option for your cart: ')
                            print()
                            if n in 'Ee':
                                  print()
                                  break
                            elif n=='1' or n=='2' or n=='3' or n=='4' :
                                
                                if n=='1':
                                           print('#Viewing Cart\n************')
                                           q=Quotes()
                                           print('Quote!!!:',q.quote())
                                           print()
                                           o.View()
                                           
                                elif n =='2':
                                      print('#Removing Book\n****************')
                                      print('*Enter ID to remove or press E to exit')
                                      o.removeP()

                                elif n=='3':
                                      print('#Quantity Adjusment\n****************')
                                      print('*Enter ID and new Quantity\n Enter E inplace of ID to exit')
                                      o.QuantityAdjust()
                                elif n=='4':
                                      print('#Checking Out\n******************')
                                      print()
                                      a=input('Would you like to view your Shopping History?Enter Y/N: ')
                                      if a in 'Yy':
                                          o.ShoppingHistory()
                                          print()
                                          break
                                      else:
                                          break
                            else:
                                print('Invalid\nPlease try again!!!\n')
                        except:
                            print('Invalid\nPlease try again!!!\n')
                            exit=input('\n*Press Y if you still want to edit your cart.\n*Press E to exit App\n*Press anyother key to return to Main Menu: ')
                            print('*'*50)
                            print()
                            if exit=='y' or exit=='Y':
                                    continue
                            else:
                                    break
                    exit=input('\n*Press Y if you still want to edit your cart.\n*Press E to exit App\n*Press anyother key to return to Main Menu: ')
                    print('*'*50)
                    print()
                    if exit=='y' or exit=='Y':
                            continue
                    else:
                            break

            
                if exit in 'Ee':
                               print('Thanks For Shoping Here!\nHappy Reading!!')
                               print('Exiting App')
                               break 

                                   

    def subMenu():
        print('\n^^^^^^^^^^^^^^^^^^')
        print('####Cart Editing Menu####')
        print()
        print('#1. View Cart')
        print('#2. Remove Book')
        print('#3. Adjust Quantity')
        print('#4. CheckOut')
        print()


