import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, download_plotlyjs
from groundhog.general import soilprofile as sp


# Front-End =============================================
#  - Purpose: to develop user friendly GUI of engineering web app
#  - Author: J.Chang (000@gmail.com)
#  - Last update:
st.markdown('## Soil Profile')


# Back-End =============================================
# - Purpose: to deploy geo engineering skills
#  - Author: J.Son (jon.jungrak.son@gmail.com)
#  - Last update: 2/2/2023

## Initialization
profile_2 = sp.SoilProfile({
    'Depth from [m]': [0, 1, 3, 4],
    'Depth to [m]': [1, 3, 4, 10],
    'Soil type': ['SAND', 'CLAY', 'SILT', 'SAND'],
    'Relative density': ['Loose', None, 'Medium dense', 'Dense'],
    'qc from [MPa]': [3, 1, 4, 40],
    'qc to [MPa]': [4, 1.5, 8, 50],
    'qt [MPa]': [3.5, 1.25, 6, 45],
    'Total unit weight [kN/m3]': [19, 18, 19, 20]
})
    
fig = profile_2.plot_profile(
    parameters=(('Total unit weight [kN/m3]',), ('qc [MPa]', 'qt [MPa]')),
    showlegends=((False,), (True, True)),
    xtitles=(r'$ \gamma \ \text{[kN/m} ^3 \text{]} $', r'$ q_c, \ q_t \ \text{[MPa]} $'),
    ztitle=r'$ z \ \text{[m]} $',
    xranges=((15, 22), (0, 60)),
    zrange=(10, 0),
    fillcolordict={'SAND': 'yellow', 'CLAY': 'brown', 'SILT': 'green'})

    
    
st.plotly_chart(fig, use_container_width=True)

