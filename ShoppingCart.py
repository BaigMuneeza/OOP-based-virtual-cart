from ListManager import ListManager

class ShoppingCart:## intantites an empty list and takes a filename as a parameter to be utilized loading the file to the list or saving the list to the file
    def __init__(self,filename):
        self.f=filename
        self.cart=[]
    def addtoCart(self,x):#adds product in the cart list
        self.cart.append(x)
        
    def saveCart(self):#saves the cart list in file
        c=ListManager(self.cart)
        c.saveToFile(self.f)
        
    def LoadList(self):#loads file in the list
        h=ListManager(self.cart)
        h.readFromFile(self.f)

    def order(self,x):#takes order asks the ID no and quantity adds it in the cart and adjusts the quantity in product stockdatabase
        while True:
                try:
                    print()
                    PId=input('*Enter ID number of Book : ')
                    PId=str(PId)
                    if  PId not in 'eE':
                          Quant=int(input('*Enter quantity: '))  
                          for m in x.cart:
                              if str(m[0])==PId:
                                    print('*********************************************************')
                                    Book=list(m)
                                    Book[3]=Quant
                                    self.addtoCart(Book)
                                    self.saveCart()
                                    m[3]=m[3]-Quant
                                    x.saveCart()
                    else: #PId in 'eE':
                            print('###Exiting Shop mode###')
                            break
                except:
                    print('Invalid\nPlease try again!!!\n')
                    continue
                    
 

   
        
    def remove_item(self):#removes product from cart list and adjusts quantity back in product stock database
        while True:
            try:
                print()
                ID=input('*Enter Product ID to be removed:')
                if ID in 'Ee':
                    print()
                    return('e')
                    break
                
                if int(ID)>10 or int(ID)<=0:
                    print('Invalid Entry!!Try Again')
                    continue
                    
                else:
                        for i in self.cart:
                            if int(ID)== i[0]:
                                 self.cart.remove(i)
                                 return (i[3],int(ID))
                                 break
            except:
                print('Invalid Entry!!Try Again')
                continue
                
                
    def ViewCart(self): ##Displays the contents of cart
        d=ListManager(self.cart)
        
        for i in d.general_list:
            print()
            print('#Book ID : ',i[0])
            print('#Name Of Book: ',i[1])
            print('#Price : Rs.',i[2])
            print('#Quantity : ',i[3])
            print()
        print('*********************************************************')
        print()
        
    def printHistory(self,j): #utilized to print history of the user where j is the list for shopping history
         print('##Displaying Shopping History!##')
         for i in j:
             if isinstance(i,str):                 
                 pass
             else:
                print()
                print('#ID :',i[0])
                print('#Name Of Product: ',i[1])
                print('#Price : Rs.',i[2])
                print('#Quantity Bought :',i[3])
            



