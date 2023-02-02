import streamlit as st
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot, download_plotlyjs


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
from groundhog.general import soilprofile as sp
