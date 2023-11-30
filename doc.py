class documentair:
    count = 0
    def __init__(self,titre,date_sortie):
        self.titre = titre
        self.date_sortie = date_sortie
        documentair.count+=1    
        self.code=documentair.count              
       

    def get_titre(self):
      return self.titre
    
    def set_titre(self,value):
        self.titre = value
       
    def get_date_sortie(self):
      return self.date_sortie
    
    def set_date_sort(self,value):
       self.date_sortie = value

    def ToString(self):
        return f"""titre:{self.titre}
        date de sortie:{self.date_sortie}"""
    
    def equal(self,doc2):
       if self.code ==doc2.code:
          return True
       else:
          return False
       
class exemplaire(documentair):
   def __init__(self,titre,date_sortie,numero,date_achat):
      super().__init__(titre,date_sortie)
      self.numero = numero
      self.date_achat = date_achat

   def get_numero(self):
      return self.numero
   
   def set_numero(self,value):
      self.numero = value

   def get_date_achat(self):
      return self.date_achat
   
   def ToString(self):
      return f"{super().ToString()}numero:{self.numero}date_achat:{self.date_achat}"
   
   def Equal(self,doc2):
       if self.numero ==doc2.numero:
          return True
       else:
          return False
   
   
   
   
doc1 = documentair("hourri","1/1/2024")
doc2 = documentair("neymar","5/3/2019")
doc3 = exemplaire("zidan in paris","19/5/2015","5","22/5/2015")
doc4 = exemplaire("zidan in paris","19/5/2015","6","22/5/2015")
print(doc3.ToString())
print(doc3.Equal(doc4))

  

  
             
    
    
    

      
    
      

        
