  
class Quotes:
  def quote(self):# reads from quotes file containing 100 quotes and picks one randomly. 
        import random
        f=open('Quotes.txt','r')
        content=f.read()
        content=content.split('\n')
        return random.choice(content)
      

