# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:11:19 2023

@author: Edib
"""
import random 
import sys 
import main as inv


def run():    
    
    print("""
          Bu simülasyon aracı Envanter Yönetimi dersi için tasarlanmıştır.
          Bu aracı kullanarak Dinamik Parti Büyüklüğü problemini optimal veya 
          optimale yakın çözümler üreten algoritmalar ile çözebilirsiniz.
          """)
          
    state = True
    
    print("""
          # ============================================================================
          #                                 AŞAMA 1 
          # ============================================================================
          """)
    
    while state == True: 
        
        ans = input("""
          Aşağıda yer alan işlerden yapmak istediğinizin kodunu konsola yazınız. 
          
          Kod                               İş
          ---   ------------------------------------------------------------ 
          1     Kullanacağım veri setini rassal olarak oluşturmak istiyorum. 
          2     Kullanacağım veri setini kendim oluşturmak istiyorum. 
          3     Çıkış yapmak istiyorum.  
    
          """)
        
        
        if ans == "1": 
            
            state = False
            
            T = int(input("""
          Kaç dönemlik talep verisi üretmek istiyorsunuz? 

          """))
                          
            D = [random.randint(0,250) for i in range(T)]
            K = random.randint(50,1000)
            h = random.randint(1,10)
            c = random.randint(1,5)
            
            print("""
          =============================================================================     
          Oluşturulan problem verileri;
          Sab. Sip. Maliyeti ---> {},
          Bir. Sip. Maliyeti ---> {}, 
          Elde Bulundurma Maliyeti ---> {}, 
          Talep ---> {}.
          =============================================================================     
          """.format(K,h,c,D))
              
              
              
        elif ans == "2":
            
            state = False

            
            D_in = input("""
         Lütfen gireceğiniz talep verisini aralarda virgül olacak şekilde giriniz.
         örn; 15,23,48,56,24
        
         """)
            
            K_in = input("""
         Sabit sipariş maliyetini giriniz.
                  
         """)
         
            h_in = input("""
         Elde bulundurma maliyetini giriniz.
         
         """)
         
            c_in = input("""
         Birim sipariş maliyetini giriniz.
                  
         """)
            
            D = [int(i) for i in D_in.split(",")]
            K = float(K_in)
            h = float(h_in)
            c = float(c_in)

            print("""
         =============================================================================     
         Girilen problem verileri;
         Sab. Sip. Maliyeti ---> {},
         Bir. Sip. Maliyeti ---> {}, 
         Elde Bulundurma Maliyeti ---> {}, 
         Talep ---> {}.
         =============================================================================     
          """.format(K,h,c,D))


        elif ans == "3": 
            
            state = False

            print("""
          Çıkış yapılıyor. 
                  """)
            sys.exit()
        
        else: 
            state = True 
            print("""
          Yanlış kod girdiniz!!! 
          """)

    
    data = inv.MRP(K, c, h, D)
    
    print("""
          # ============================================================================
          #                                 AŞAMA 2 
          # ============================================================================
          """)
    
    state = True
    
    while state == True: 
        
        dic = {1: "WW",
               2: "LFL",
               3: "SM",
               4: "LUC",
               5: "PPB"}
        
        algs = input("""
         Aşağıda yer alan algoritmalardan kullanmak istediğinizin kodunu konsola yazınız. 
            
         1. Wagner-Whitin Algoritması
         2. Lot-for-Lot Algoritması 
         3. Silver-Meal Algoritması
         4. En Küçük Birim Maliyet Yaklaşımı
         5. Parça Dönem Dengesi Yaklaşımı
            
         Eğer birden fazla algoritma ile sonuçları görmek istiyorsanız kodları aralarında
         virgül olacak şekilde giriniz. 
         örn; 1,3,5
      
         """)    
         
        print("""
        # ============================================================================
        #                                 AŞAMA 3 
        # ============================================================================
        """)
       
        alg = [int(i) for i in algs.split(",")] 
        if set(alg).issubset([1,2,3,4,5]):
            state = False
            for a in alg: 
                data.PlotGraph(algorithm=dic[a])
                print("\n")
        else: 
            print("""
        Yanlış kod girdiniz!!! 
        """) 