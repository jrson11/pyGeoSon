# Name: ground_model.py
# Purpose: To generate discretized ground model based on soil strata
# Authour: Jungrak Son
# Version: 01/03/2023

import numpy as np
import pandas as pd

def generate_template():
    df_proj = pd.DataFrame()
    df_loca = pd.DataFrame()
    df_soil = pd.DataFrame()
    #
    df_proj.loc[0,'Project'] = 'test1'
    df_proj.loc[0,'Project_Name'] = 'test1-example'
    df_proj.loc[0,'Project_No'] = '20230103'
    df_proj.loc[0,'Project_Location'] = 'Texas'
    df_proj.loc[0,'Project_Engineer'] = 'JS'
    #
    df_loca.loc[0,'Data_No'] = '[-]'
    df_loca.loc[0,'Location_ID'] = '[-]'
    df_loca.loc[0,'North'] = '[m]'
    df_loca.loc[0,'East'] = '[m]'
    df_loca.loc[0,'Max_Depth'] = '[ft]'
    df_loca.loc[0,'Ground_Elevation'] = '[ft]'
    df_loca.loc[0,'Water_Depth'] = '[ft]'
    #
    df_soil.loc[0,'Layer_No'] = '[-]'
    df_soil.loc[0,'Soil_Unit'] = '[-]'
    df_soil.loc[0,'Top_Elevation'] = '[ft]'
    df_soil.loc[0,'Base_Elevation'] = '[ft]'
    df_soil.loc[0,'Thickness'] = '[ft]'
    df_soil.loc[0,'Eff_Unit_Weight'] = '[pcf]'
    df_soil.loc[0,'Shear_Strength'] = '[psf]'
    df_soil.loc[0,'Friction_Angle'] = '[deg]'
    
    return df_proj

def import_df_from_Excel(FILE,SHEET):
    test = pd.read_excel(FILE,sheet_name=SHEET,nrows=1)
    test_col = list(test.columns)
    test_unit = list(test.loc[0,:])
    test_head = list()
    for i in range(len(test_col)):
        test_head.append(test_col[i]+test_unit[i])
    df_test = pd.read_excel(FILE,sheet_name=SHEET,skiprows=1)
    df_test.columns = test_head
    return df_test

def import_input(FILE):
    df_proj = pd.read_excel(FILE, sheet_name='PROJECT')
    df_loca = import_df_from_Excel(FILE,'LOCATION')
    df_soil = import_df_from_Excel(FILE,'SOIL')

    return df_proj, df_loca, df_soil

def export_output(df_SOIL):
    df_soil = df_SOIL
    #
    # Depth
    zmax = max(df_soil['Top_Elevation[ft]'])
    zmin = min(df_soil['Base_Elevation[ft]'])
    dz = 1 #[ft]
    zz = np.arange(zmax,zmin-dz,-dz)
    nz = len(zz)
    #
    # Ground Modeling
    df_ground = pd.DataFrame()
    df_ground['Elevation[ft]'] = zz
    df_ground['Soil_Unit[-]'] = np.nan
    df_ground['Eff_Unit_Weight[pcf]'] = np.nan
    df_ground['Shear_Strength[psf]'] = np.nan
    df_ground['Friction_Angle[deg]'] = np.nan
    df_ground['Soil_Type[N/NC]'] = np.nan
    #
    # Ground Modeling
    idx = 0
    for i in range(nz):
        z = df_ground.loc[i,'Elevation[ft]']
        base_z = df_soil.loc[idx,'Base_Elevation[ft]']
        if z <= base_z:
            if i == nz-1:
                pass # To prevent the last value to exceed the limit
            else:
                idx = idx + 1
        # 
        df_ground.loc[i,'Soil_Unit[-]'] = df_soil.loc[idx,'Soil_Unit[-]']
        df_ground.loc[i,'Eff_Unit_Weight[pcf]'] = df_soil.loc[idx,'Eff_Unit_Weight[pcf]']
        df_ground.loc[i,'Shear_Strength[psf]'] = df_soil.loc[idx,'Shear_Strength[psf]']
        df_ground.loc[i,'Friction_Angle[deg]'] = df_soil.loc[idx,'Friction_Angle[deg]']
        #
        if df_ground.loc[i,'Friction_Angle[deg]'] == 0:
            df_ground.loc[i,'Soil_Type[N/NC]'] = 'C'
        else:
            df_ground.loc[i,'Soil_Type[N/NC]'] = 'NC'
    #
    # Calculation
    df_ground['Depth[ft]'] = zmax - df_ground['Elevation[ft]']
    df_ground['del_σv_eff[psf]'] = df_ground['Eff_Unit_Weight[pcf]']*dz
    df_ground.loc[0,'del_σv_eff[psf]'] = 0
    df_ground['σv_eff[psf]'] = np.cumsum(df_ground['del_σv_eff[psf]'])
    
    return df_ground

def convert_df_to_Excel(df_ground):
    cols = pd.DataFrame(df_ground.columns)
    df_head = cols[0].str.split('[',expand=True)
    df_head[2] = '['+df_head[1]
    df_head.drop(columns=[1], inplace=True)
    df_head.columns = ['head','unit']
    #
    ground = df_ground.copy()
    ground.columns = list(df_head['head'])
    for i in range(len(cols)):
        ground.loc[-1,df_head.loc[i,'head']] = df_head.loc[i,'unit']
    ground.sort_index(ascending=True, inplace=True)
    
    return ground

# Main =======================================================================
'''
inputfile = './ground_model_input.xlsx'
outputfile = './ground_model_output.xlsx'
#
df_proj,df_loca,df_soil = import_input(inputfile)
df_ground = export_output(df_soil)
convert_df_to_Excel(df_ground).to_excel(outputfile, index=False)
'''
