# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:11:30 2023

@author: Edib
"""

import numpy as np
import matplotlib.pyplot as plt

class MRP:
    """
    This class includes exact and heuristic algorithms 
    for lot-sizing problem with time varying demand   
    """
    def __init__(self,K,c,h,D):
        """
        Parameters
        ----------
        K : float
            The fixed ordering cost.
        c : float
            The unit ordering cost.
        h : float
            The unit holding cost.
        D : list
            Demand data.
        """
    
        self.K,self.c,self.h = float(K),float(c),float(h)
        self.D = {i+1: D[i] for i in range(len(D))}
        self.T = len(D)

    def Cstar(self,n,a):
        
        cost = self.K
        for i in range(n,n+a):
            cost += (i-n)*self.h*self.D[i] + self.c*self.D[i]
        
        return cost
    
    def Tdemand(self,n,a):
        return sum(self.D[i] for i in range(n,n+a))
    
    def WW(self):
        
        RepSchedule = np.zeros(self.T)
        cost_array = np.zeros(self.T+1)
        brecursion = self.T
        
        while brecursion > 0: 
            
            temp = []
            max_a = self.T+1 - brecursion 
            
            for a in range(1,max_a+1):
                temp += [self.Cstar(brecursion,a) + cost_array[brecursion+a-1]]
            
            cost_array[brecursion-1] = np.min(temp)
            RepSchedule[brecursion-1] = np.argmin(temp) + 1 
            brecursion -= 1 
        
        n = 1 
        for i in range(len(RepSchedule)):
            if n != i+1: 
                RepSchedule[i] = 0.
            else:
                temp = int(RepSchedule[i])
                RepSchedule[i] = self.Tdemand(n,int(RepSchedule[i]))
                n += temp
            
        return cost_array[0], RepSchedule
            
     
    def SM(self):
        
        n = 1
        cost = 0. 
        RepSchedule = np.zeros(self.T)
        
        
        while n < self.T+1:
            
            max_a = self.T+1 - n
            a,bestcost = 1, np.Infinity
            
            while a < max_a+1:
                
                spcost = self.Cstar(n,a)/a
                
                if spcost <= bestcost:
                    bestcost = spcost  
                    RepSchedule[n-1] = self.Tdemand(n,a)
                else: 
                    break
                
                temp_cost =  spcost * a  
                a += 1                 
            
            
            n += a - 1
            cost += temp_cost 
        
        
        return cost, RepSchedule
                
                
    def LUC(self):            
        
        n = 1
        cost = 0. 
        RepSchedule = np.zeros(self.T)
        
        while n < self.T+1:
            
            max_a = self.T+1 - n
            a,bestcost = 1, np.Infinity
            
            while a < max_a+1:
                
                spcost = self.Cstar(n,a)/self.Tdemand(n,a)

                if spcost <= bestcost:
                    bestcost = spcost
                    RepSchedule[n-1] = self.Tdemand(n,a)
                else: 
                    break
                
                temp_cost =  spcost * self.Tdemand(n,a)  
                a += 1                 
            
            n += a - 1
            cost += temp_cost 
        
        return cost, RepSchedule    
    
    
    def LFL(self):
        RepSchedule = np.array([self.D[i] for i in range(1,self.T+1)])
        cost = self.K * self.T + self.c * sum(RepSchedule)
        return cost, RepSchedule  
    
    def PPB(self):
        pass 
        
    def PlotGraph(self,algorithm="WW"):
               
        plt.ioff()
        
        if algorithm == "WW":
            Cost,RepSchedule = self.WW()
        elif algorithm == "SM":
            Cost,RepSchedule = self.SM()
        elif algorithm == "LUC":
            Cost,RepSchedule = self.LUC()
        elif algorithm == "LFL":
            Cost,RepSchedule = self.LFL()
        elif algorithm == "PPB":
            Cost,RepSchedule = self.PPB()
            
        PostReplenishmentLevel = np.zeros(self.T+1)
        PreReplenishmentLevel = np.zeros(self.T+1)
        InitialInventoryLevel = 0
        periods = []

        for i in range(self.T):
            if i == 0:
                PreReplenishmentLevel[i] = InitialInventoryLevel
                periods += [i+1]
            else: 
                PreReplenishmentLevel[i] = PostReplenishmentLevel[i-1] - self.D[i]
                periods += [i+1]
            
            PostReplenishmentLevel[i] = PreReplenishmentLevel[i] + RepSchedule[i]
            periods += [i+1]
                        
        yaxis = [j for i in zip(PreReplenishmentLevel,PostReplenishmentLevel) for j in i]        
        periods += [self.T+1]
        periods += [self.T+1]
        
        fig = plt.figure(figsize=(12,4))
        #Adding cost as a text
        plt.text(0.85, 0.85, f'Cost: {Cost}', transform=plt.gca().transAxes,
                 fontsize = 11, style='italic')
        
        #Adding inventory levels on markers
        for i in range(len(periods)):
            plt.text(periods[i]+.1, yaxis[i], "%d" %yaxis[i])

        plt.plot(periods,yaxis, color='black', linestyle='dashed',marker='o', markerfacecolor='red')
        plt.xticks(range(1,self.T+2))
        plt.xlabel("Periods")
        plt.ylabel("Inventory Level")
        plt.title(f'{algorithm} Algorithm Inventory Level Graph')
        plt.grid()
        plt.show()
        
        return fig
    

class ESM:
    
    def __init__(self,K,c,h,D):
        """
        Parameters
        ----------
        K : float
            The fixed ordering cost.
        c : float
            The unit ordering cost.
        h : float
            The unit holding cost.
        D : float
            Demand data.
        """
    
        self.K,self.c,self.h,self.D = float(K),float(c),float(h),float(D)
            
    def brZamanSabitMal(self,Q):
        return (self.K*self.D)/Q
    
    def brZamanDegMal(self):
        return self.D*self.c
    
    def brZamanElBulMal(self,Q):
        return self.h*Q/2.
    
    def brZamanTopMal(self,Q):
        return self.brZamanSabitMal(Q)+self.brZamanDegMal()+self.brZamanElBulMal(Q)
    
    def donguUzunl(self,Q):
        return Q/self.D
    
    def optSipMikt(self):
        return (2*self.K*self.D/self.h)**.5


class ESM_GecTes:
    
    def __init__(self,K,c,h,D,pi):
        """
        Parameters
        ----------
        K : float
            The fixed ordering cost.
        c : float
            The unit ordering cost.
        h : float
            The unit holding cost.
        D : float
            Demand data.
        """
    
        self.K,self.c,self.h,self.pi,self.D = float(K),float(c),float(h),float(pi),float(D)
            
    def brZamanSabitMal(self,Q):
        return (self.K*self.D)/Q
    
    def brZamanDegMal(self):
        return self.D*self.c
    
    def brZamanElBulMal(self,Q,B):
        return self.h*(Q-B)**2/(2*Q)

    def brZamanCezaMal(self,Q,B):
        return self.pi*(B)**2/(2*Q)
    
    def brZamanTopMal(self,Q,B):
        return self.brZamanSabitMal(Q)+self.brZamanDegMal()+self.brZamanElBulMal(Q,B)+self.brZamanCezaMal(Q,B)
    
    def donguUzunl(self,Q):
        return Q/self.D
    
    def pozdonguUzunl(self,Q,B):
        return (Q-B)/self.D
    
    def negdonguUzunl(self,B):
        return (B)/self.D
    
    def optSipMikt(self):
        return (2*self.K*self.D*(self.h+self.pi)/(self.h*self.pi))**.5
    
    def optGecTesMikt(self,Q):
        return Q*self.h/(self.h+self.pi) 


class EUM:
    
    def __init__(self,K,c,h,D,P):
        """
        Parameters
        ----------
        K : float
            The fixed ordering cost.
        c : float
            The unit ordering cost.
        h : float
            The unit holding cost.
        D : float
            Demand data.
        """
    
        self.K,self.c,self.h,self.D,self.P = float(K),float(c),float(h),float(D),float(P)
            
    def brZamanSabitMal(self,Q):
        return (self.K*self.D)/Q
    
    def brZamanDegMal(self):
        return self.D*self.c
    
    def brZamanElBulMal(self,Q):
        return (self.h*Q*(1-self.D/self.P))/2.
    
    def brZamanTopMal(self,Q):
        return self.brZamanSabitMal(Q)+self.brZamanDegMal()+self.brZamanElBulMal(Q)
    
    def donguUzunl(self,Q):
        return Q/self.D
    
    def optSipMikt(self):
        return (2*self.K*self.D/(self.h*(1-self.D/self.P)))**.5
    
    def uretdongUzunl(self,Q):
        return Q/self.P
    
    def maxEnvSev(self,Q):
        return Q * (1-self.D/self.P)



class ESM_MI:
    
    def __init__(self,K,cs,alpha,D):
    
        self.K,self.cs,self.alpha,self.D = float(K),cs,float(alpha),float(D)
    
    
    def hesaplaQ(self,a,b,c):
        instance = ESM(self.K, c, c*self.alpha, self.D)
        if instance.optSipMikt() > b: 
            return (b,c)
        elif instance.optSipMikt() < a:
            return (a,c)
        else: 
            return (instance.optSipMikt(),c)
        
    def TopMal(self):
        
        best_Obj, best_Q, best_c = (float('inf'),float('inf'),float('inf'))

        for (a,b,c) in self.cs:
            Q,c = self.hesaplaQ(a, b, c)
            instance = ESM(self.K, c, c*self.alpha, self.D)
            TC = instance.brZamanTopMal(Q)
            if TC <= best_Obj:
                best_Obj, best_Q, best_c  = TC, Q, c
        
        return (best_Obj,best_Q, best_c)


    
if __name__ == "__main__":
    
    c = MRP(267,4,4,[169, 185, 212, 190, 101, 241, 72, 32, 220, 105, 246, 244])
    print(c.WW())
    print(c.SM())
    print(c.LUC())
    print(c.LFL())
    c.PlotGraph()
