# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:11:19 2023

@author: Edib
"""
import random 
import sys 
import main as inv


import ast

def run():    
    
    print("""
          Bu simülasyon aracı Envanter Yönetimi dersi için tasarlanmıştır.
          Bu aracı kullanarak farklı karakteristik özelliklere sahip problemleri
          optimal yöntemler veya  optimale yakın çözümler üreten algoritmalar ile 
          çözebilirsiniz.
          """)
          
    state = True
    
    print("""
          # ============================================================================
          #                                 AŞAMA 1 
          # ============================================================================
          """)
    
    while state == True: 
        
        
        ans1 = input("""
          Aşağıda yer alan problemlerden hangisi ile ilgileinyorsanız ilgili problemin
          kodunu konsola yazınız. 
          
          Kod                               İş
          ---   ------------------------------------------------------------ 
          1     Temel ekonomik sipariş miktarı modeli 
          2     Ekonomik sipariş miktarı modeli + Miktar indirimi durumu
          3     Ekonomik sipariş miktarı modeli + Gecikmeli teslim durumu 
          4     Ekonomik üretim miktarı modeli 
          5     Parti büyüklüğü problemi 
          6     Çıkış yapmak istiyorum.  
    
          """)
        
        
        
        if ans1 == "6" or ans1 not in ["1","2","3","4","5"]: 
            
            state = False

            print("""
          Çıkış yapılıyor. 
                  """)
            sys.exit()
        
           
        
        ans2 = input("""
          Probleminize ilişkin veri setini nasıl oluşturmak istersiniz? 
          Aşağıda yer alan işlerden yapmak istediğinizin kodunu konsola yazınız. 
          
          Kod                               İş
          ---   ------------------------------------------------------------ 
          1     Kullanacağım veri setini rassal olarak oluşturmak istiyorum. 
          2     Kullanacağım veri setini kendim oluşturmak istiyorum. 
          3     Çıkış yapmak istiyorum.  
    
          """)
        
        if ans1 == "1":
            
            state = False
            
            if ans2 == "1":
                
                D = random.randint(0,500)
                K = random.randint(50,2000)
                h = random.randint(1,5)
                c = random.randint(0,5)
                
                print("""
        =============================================================================     
        Oluşturulan problem verileri;
        Sab. Sip. Maliyeti ---> {},
        Bir. Sip. Maliyeti ---> {}, 
        Elde Bulundurma Maliyeti ---> {}, 
        Talep ---> {}.
        =============================================================================     
              """.format(K,c,h,D))
                
                data = inv.ESM(K, c, h, D)
                Qstar = data.optSipMikt()
              
                print("""
        =============================================================================     
        Ekonomik sipariş miktarı {} olarak belirlenmiştir. 
        Birim zamanda oluşan minimum toplam maliyet ise {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan optimal toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Sip. Maliyeti ---> {},
        Toplam Değişken Sip. Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Optimal döngü uzunluğu  ---> {} yıl.
        =============================================================================     
              """.format(Qstar,data.brZamanTopMal(Qstar),data.brZamanSabitMal(Qstar),data.brZamanDegMal(),data.brZamanElBulMal(Qstar),data.donguUzunl(Qstar)))
    
            elif ans2 == "2":
                
                  D_in = input("""
                Talep verisini giriniz.
              
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
                    
                  data = inv.ESM(K_in, c_in, h_in, D_in)
                  Qstar = data.optSipMikt()
            
                  print("""
        =============================================================================     
        Ekonomik sipariş miktarı {} olarak belirlenmiştir. 
        Birim zamanda oluşan minimum toplam maliyet ise {} olarak hesaplanmaktadır. 

        Birim zamanda oluşan optimal toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Sip. Maliyeti ---> {},
        Toplam Değişken Sip. Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
      
        Eğer birim zamanı yıl olarak kabul edersek;
        Optimal döngü uzunluğu  ---> {} yıl.
        =============================================================================     
                """.format(Qstar,data.brZamanTopMal(Qstar),data.brZamanSabitMal(Qstar),data.brZamanDegMal(),data.brZamanElBulMal(Qstar),data.donguUzunl(Qstar)))   


            elif ans2 == "3": 
                
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


        if ans1 == "2":
            
            state = False
            
            if ans2 == "1":
                
                D = random.randint(250,750)
                K = random.randint(0,20)
                cs = cs = [(0,500,0.3),(500,1000,0.29),(1000,float('inf'),0.28)]
                alpha = 0.2 
                
                print("""
        =============================================================================     
        Oluşturulan problem verileri;
        Sab. Sip. Maliyeti ---> {},
        Bir. Sip. Maliyeti ---> 0.30, eğer 0 ile 500 arasında sipariş olursa, 
                                0.29, eğer 500 ile 1000 arasında sipariş olursa, 
                                0.28, eğer 1000 den fazla sipariş olursa,  
        Elde Bulundurma Maliyeti ---> birim sipariş maliyetinin 0.2 katı, 
        Talep ---> {}.
        =============================================================================     
              """.format(K,D))
                
                data = inv.ESM_MI(K, cs, alpha, D)
                TCstar,Qstar,cstar = data.TopMal()
                
                data_new = inv.ESM(K, cstar, cstar*alpha, D)
                
                print("""
        =============================================================================     
        Bu durumda en uygun karar {} adet sipariş vermektir. 
        Bu kararla birlitke birim zamanda oluşan toplam maliyet {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Sip. Maliyeti ---> {},
        Toplam Değişken Sip. Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Döngü uzunluğu  ---> {} yıl.
        =============================================================================     
              """.format(Qstar,TCstar,data_new.brZamanSabitMal(Qstar),data_new.brZamanDegMal(),
              data_new.brZamanElBulMal(Qstar),data_new.donguUzunl(Qstar)))
    
    
            elif ans2 == "2":
                
                  D_in = input("""
                Talep verisini giriniz.
              
                """)
                  
                  K_in = input("""
                Sabit sipariş maliyetini giriniz.
                        
                """)
               
                  alpha_in = input("""
                Elde bulundurma maliyetini hesaplamak için kullanılacak çarpanı giriniz.
                (Elde bul. mal. birim değ. maliyetin kaç katı olsun istiyorsunuz?)
                
                """)
               
                  c_in = ast.literal_eval(input("""
                Birim sipariş maliyetlerini ve iskonto aralıklarını aşağıda gösterildiği gibi giriniz.
                (örn; (0,500,0.5),(500,1000,0.4),(1000,2000,0.3))        
                
                """))
                  
                  
                  c_in = list(c_in)  
                  
                  

                  data = inv.ESM_MI(K_in, c_in, alpha_in, D_in)
                  TCstar,Qstar,cstar = data.TopMal()
                  
                  print(TCstar,Qstar,cstar)
                  data_new = inv.ESM(K_in, cstar, cstar*float(alpha_in), D_in)
                
                  print("""
        =============================================================================     
        Bu durumda en uygun karar {} adet sipariş vermektir. 
        Bu kararla birlitke birim zamanda oluşan toplam maliyet {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Sip. Maliyeti ---> {},
        Toplam Değişken Sip. Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Döngü uzunluğu  ---> {} yıl.
        =============================================================================     
              """.format(Qstar,TCstar,data_new.brZamanSabitMal(Qstar),data_new.brZamanDegMal(),
                  data_new.brZamanElBulMal(Qstar),data_new.donguUzunl(Qstar)))

                                          
            elif ans2 == "3": 
                
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
                                          
                                          
    
        if ans1 == "3":
            
            state = False

            if ans2 == "1":
                
                D = random.randint(0,500)
                K = random.randint(50,2000)
                h = random.randint(1,5)
                c = random.randint(0,5)
                pi = h + random.randint(2,6)
                
                print("""
        =============================================================================     
        Oluşturulan problem verileri;
        Sab. Sip. Maliyeti ---> {},
        Bir. Sip. Maliyeti ---> {}, 
        Elde Bulundurma Maliyeti ---> {}, 
        Gecikmeli Teslim Maliyeti ---> {}, 
        Talep ---> {}.
        =============================================================================     
              """.format(K,c,h,pi,D))
                
                data = inv.ESM_GecTes(K, c, h, D, pi)
                Qstar = data.optSipMikt()
                Bstar = data.optGecTesMikt(Qstar)
                
                print("""
        =============================================================================     
        Ekonomik sipariş miktarı {} olarak belirlenmiştir. 
        Gecikmeli teslim (Karşılanamya talepn) miktarı {} olarak belirlenmiştir. 
        Birim zamanda oluşan minimum toplam maliyet ise {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan optimal toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Sip. Maliyeti ---> {},
        Toplam Değişken Sip. Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        Toplam Gecikmeli Teslim (Ceza) Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Optimal döngü içerisinde elde envanter bulundurulan süre ---> {} yıl,
        Optimal döngü içerisinde talebin karşılanmadığı süre ---> {} yıl,
        Optimal döngü uzunluğu ise  ---> {} yıl.
        =============================================================================     
              """.format(Qstar,Bstar,data.brZamanTopMal(Qstar,Bstar),data.brZamanSabitMal(Qstar),data.brZamanDegMal(),data.brZamanElBulMal(Qstar,Bstar),
              data.brZamanCezaMal(Qstar,Bstar),data.pozdonguUzunl(Qstar,Bstar),data.negdonguUzunl(Bstar),data.donguUzunl(Qstar)))

                

            elif ans2 == "2":
            
                  D_in = input("""
                Talep verisini giriniz.
              
                """)
                  
                  K_in = input("""
                Sabit sipariş maliyetini giriniz.
                        
                """)
               
                  h_in = input("""
                Elde bulundurma maliyetini giriniz.
               
                """)
                
                  pi_in = input("""
                Gecikmeli teslim (ceza) maliyetini giriniz.
               
                """)
                  c_in = input("""
                Birim sipariş maliyetini giriniz.
                        
                """)
            
                
                  data = inv.ESM_GecTes(K_in, c_in, h_in, D_in, pi_in)
                  Qstar = data.optSipMikt()
                  Bstar = data.optGecTesMikt(Qstar)
              
                  print("""
        =============================================================================     
        Ekonomik sipariş miktarı {} olarak belirlenmiştir. 
        Gecikmeli teslim (Karşılanamya talepn) miktarı {} olarak belirlenmiştir. 
        Birim zamanda oluşan minimum toplam maliyet ise {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan optimal toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Sip. Maliyeti ---> {},
        Toplam Değişken Sip. Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        Toplam Gecikmeli Teslim (Ceza) Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Optimal döngü içerisinde elde envanter bulundurulan süre ---> {} yıl,
        Optimal döngü içerisinde talebin karşılanmadığı süre ---> {} yıl,
        Optimal döngü uzunluğu ise  ---> {} yıl.
        =============================================================================     
            """.format(Qstar,Bstar,data.brZamanTopMal(Qstar,Bstar),data.brZamanSabitMal(Qstar),data.brZamanDegMal(),data.brZamanElBulMal(Qstar,Bstar),
            data.brZamanCezaMal(Qstar,Bstar),data.pozdonguUzunl(Qstar,Bstar),data.negdonguUzunl(Bstar),data.donguUzunl(Qstar)))        
            
            
            
            
            elif ans2 == "3": 
                
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



        if ans1 == "4":
            
            state = False
            
            if ans2 == "1":
                
                D = random.randint(0,500)
                K = random.randint(50,2000)
                h = random.randint(1,5)
                c = random.randint(0,5)
                P = random.randint(1000,2000)
                
                
                print("""
        =============================================================================     
        Oluşturulan problem verileri;
        Sab. Üret. Maliyeti ---> {},
        Bir. Üret. Maliyeti ---> {}, 
        Elde Bulundurma Maliyeti ---> {}, 
        Talep ---> {},
        Üretim ---> {}.
        =============================================================================     
              """.format(K,c,h,D,P))
                
                data = inv.EUM(K, c, h, D, P)
                Qstar = data.optSipMikt()
              
                print("""
        =============================================================================     
        Ekonomik üretim miktarı {} olarak belirlenmiştir.
        Bu durumda envanter seviyesinin ulaşabileceği en yüksek değer {} olarak hesaplanır.
        Birim zamanda oluşan minimum toplam maliyet ise {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan optimal toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Üretim Maliyeti ---> {},
        Toplam Değişken Üretim Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Optimal döngü içerisinde üretimin gerçekleştirildiği süre ---> {} yıl,
        Optimal döngü uzunluğu  ---> {} yıl.
        =============================================================================     
              """.format(Qstar,data.maxEnvSev(Qstar),data.brZamanTopMal(Qstar),data.brZamanSabitMal(Qstar),
              data.brZamanDegMal(),data.brZamanElBulMal(Qstar),data.uretdongUzunl(Qstar),data.donguUzunl(Qstar)))
    
            elif ans2 == "2":
                
                  D_in = input("""
                Talep verisini giriniz.
              
                """)
                
                  P_in = input("""
                Üretim verisini giriniz.
              
                """)               
                  
                  K_in = input("""
                Sabit üretim maliyetini giriniz.
                        
                """)
               
                  h_in = input("""
                Elde bulundurma maliyetini giriniz.
               
                """)
               
                  c_in = input("""
                Birim üretim maliyetini giriniz.
                        
                """)
                    
                  data = inv.EUM(K_in, c_in, h_in, D_in, P_in)
                  Qstar = data.optSipMikt()
            
                  print("""
        =============================================================================     
        Ekonomik üretim miktarı {} olarak belirlenmiştir.
        Bu durumda envanter seviyesinin ulaşabileceği en yüksek değer {} olarak hesaplanır.
        Birim zamanda oluşan minimum toplam maliyet ise {} olarak hesaplanmaktadır. 
        
        Birim zamanda oluşan optimal toplam maliyet bileşenleri ise aşağıda verilmektedir; 
        Toplam Sabit Üretim Maliyeti ---> {},
        Toplam Değişken Üretim Maliyeti ---> {}, 
        Toplam Elde Bulundurma Maliyeti ---> {}, 
        
        Eğer birim zamanı yıl olarak kabul edersek;
        Optimal döngü içerisinde üretimin gerçekleştirildiği süre ---> {} yıl,
        Optimal döngü uzunluğu  ---> {} yıl.
        =============================================================================     
              """.format(Qstar,data.maxEnvSev(Qstar),data.brZamanTopMal(Qstar),data.brZamanSabitMal(Qstar),
              data.brZamanDegMal(),data.brZamanElBulMal(Qstar),data.uretdongUzunl(Qstar),data.donguUzunl(Qstar)))  
                
           
            elif ans2 == "3": 
                
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
                
    
        if ans1 == "5":
        
            if ans2 == "1": 
                
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
                  
                  
                  
            elif ans2 == "2":
                
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
    
    
            elif ans2 == "3": 
                
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
            
                dic =  {1: "WW",
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