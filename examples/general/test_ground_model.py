import sys
sys.path.append('../../pygeoson/general/')
import ground_model as gm

# Main =======================================================================
inputfile = './ground_model_input.xlsx'
outputfile = './ground_model_output.xlsx'
#
df_proj,df_loca,df_soil = gm.import_input(inputfile)
df_ground = gm.export_output(df_soil)
gm.convert_df_to_Excel(df_ground).to_excel(outputfile, index=False)
