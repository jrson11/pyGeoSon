
import sys
sys.path.append('../../pygeoson/general/')
import ground_model as gm
sys.path.append('../../pygeoson/deep_foundation/')
import axial_capacity as ac

# Main =======================================================================
inputfile = './ground_model_input.xlsx'
outputfile = './axial_capacity_output.xlsx'
#

## Ground Model
df_proj,df_loca,df_soil = gm.import_input(inputfile)
df_ground = gm.export_output(df_soil)
#gm.convert_df_to_Excel(df_ground).to_excel(outputfile, index=False)

## FHWA
df_new1 = ac.FHWA.NcNqNg(df_ground)
df_new2 = ac.FHWA.skin_friction(df_new1)
