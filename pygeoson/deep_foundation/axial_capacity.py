# Name: axial_capacity.py
# Purpose: To calculate pile bearing capacity
# Authour: Jungrak Son
# Version: 01/03/2023

import numpy as np
import pandas as pd

class FHWA():
    
    def NcNqNg(df_ground):
        ϕ = df_ground['ϕ[deg]']

        # Surcharge Term
        Nq = np.exp(np.pi*np.tan(ϕ*np.pi/180))*(np.tan((45+ϕ/2)*np.pi/180))**2
        df_ground['Nq'] = Nq
    
        # Cohesion Term
        ii = ϕ == 0
        Nc = Nq*0
        Nc[ii] = 5.14
        Nc[~ii] = (Nq[~ii]-1)/np.tan(ϕ[~ii]*np.pi/180)    
        df_ground['Nc'] = Nc
    
        # Footing Term
        Ng = 2*(Nq+1)*np.tan(ϕ*np.pi/180)
        df_ground['Ng'] = Ng
    
        return df_ground
    
    def Nq_DrivenPiles(phi):
        dic_Nq = {15:4.8, 17.5:6.2, 20:8.2, 22.5:12, 25:15,27.5:21,
                  30:30, 32.5:43, 35:64, 37.5:98, 40:160, 42.5:265, 45:475}
        Nq = dic_Nq[phi]
        
        return Nq
    
    def alpha_method():
        # This is not correct. This should be updated
        alpha = 0.4
        
        return alpha

    def skin_friction(df_ground):
        # Main equation: fs = c + sh*tan(del) = c + K*sv*tan(del)
        
        
        # Total Stress Analysis (alpha method) for CLAY
        # --> fs = c = alpha * su, where alpha by (Tomlinson,1980)
        Su = df_ground['Su[psf]']
        fs = FHWA.alpha_method()*Su
        df_ground['fs[ksf]'] = fs
        
        
        # Effective Stress Analysis (beta method)
        # --> fs = K*s'v*tan(del)
        ii = df_ground['Soil_Type[C/NC]'] == 'NC'
        
        
        return df_ground
    
    def end_bearing(df_ground):
        # Main equation: qp = cNc + qNq + 0.5 gBNg
        
        # Total Stress Analysis for CLAY
        # --> Nq = 1, Ng = 0, Nc = 9 typically used
        # Thus, Qp = Ap*Su*Nc
        Su = df_ground['Su[psf]']
        qp = 9*Su
        df_ground['qp[ksf]'] = qp
        
        # Effective Stress Analysis (DrivenPile, Thurman,1964)
        # --> Qp = Ap*q*alpha*Nq'
        # But, following the limiting value from (Meyerhof,1976)
        
        
        
        return df_ground
