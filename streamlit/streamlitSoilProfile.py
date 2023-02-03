import streamlit as st
import numpy as np
#
from groundhog.general import soilprofile as sp
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px


# Front-End =============================================
#  - Purpose: to develop user friendly GUI of engineering web app
#  - Author: J.Chang (000@gmail.com)
#  - Last update:
st.markdown('## Subsurface Soil Profile')

st.sidebar.markdown('## Sidebar')

st.sidebar.markdown('### Inputs')
option_input = st.sidebar.selectbox('Which data to use?',('Previous Example', 'Upload New Data'))
option_output = st.sidebar.button('Download the example')

st.sidebar.markdown('### Outputs')
option_output = st.sidebar.button('Download the result')

st.sidebar.markdown('### Interpretation')
option_depth = st.sidebar.slider('Depth to draw a guideline in plots', 0, 10, 2)  # min, max, default





# Back-End =============================================
# - Purpose: to deploy geo engineering skills
#  - Author: J.Son (jon.jungrak.son@gmail.com)
#  - Last update: 2/2/2023

## Initialization
df = sp.SoilProfile({
    'Depth from [m]': [0, 1, 3, 4],
    'Depth to [m]': [1, 3, 4, 10],
    'Soil type': ['SAND', 'CLAY', 'SILT', 'SAND'],
    'Relative density': ['Loose', None, 'Medium dense', 'Dense'],
    'qt [MPa]': [3.5, 1.25, 6, 45],
    'Total unit weight [kN/m3]': [19, 18, 19, 20]
})

## Dataframe
st.write('### Previous Example Data')
st.dataframe(df)

## Plotting
st.write('### Plots')
fig = make_subplots(rows=1, cols=3, subplot_titles=('Log','UW','CPT'))
#
for i in range(len(df)):
    fig.add_trace(go.Scatter(x=[1,2],y=[df.loc[i,'Depth from [m]'],df.loc[i,'Depth to [m]']]), row=1,col=1)
#
fig.add_trace(go.Scatter(x=df['Total unit weight [kN/m3]'], y=df['Depth from [m]'],
                         mode='lines+markers', line_shape='vh', name='from', showlegend=False), row=1,col=2)
fig.add_trace(go.Scatter(x=df['Total unit weight [kN/m3]'], y=df['Depth to [m]'],
                         mode='lines+markers', line_shape='hv', name='to', showlegend=False), row=1,col=2)
#
fig.add_trace(go.Scatter(x=df['qt [MPa]'], y=df['Depth to [m]'],
                         mode='lines+markers', name='qt'), row=1,col=3)
#
fig.update_yaxes(autorange="reversed")
fig['layout']['yaxis']['title']='Depth [m]'
fig['layout']['xaxis']['title']=' '
fig['layout']['xaxis2']['title']='[KN/m3]'
fig['layout']['xaxis3']['title']='[MPa]'
fig.update_layout(height=600, width=800, title_text="")
#
st.plotly_chart(fig)

