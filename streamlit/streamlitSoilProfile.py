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

## Dataframe
df = sp.SoilProfile({
    'Depth from [m]': [0, 1, 3, 4],
    'Depth to [m]': [1, 3, 4, 10],
    'Soil type': ['SAND', 'CLAY', 'SILT', 'SAND'],
    'Relative density': ['Loose', None, 'Medium dense', 'Dense'],
    'qt [MPa]': [3.5, 1.25, 6, 45],
    'Total unit weight [kN/m3]': [19, 18, 19, 20]
})

zmin = df.min_depth
zmax = df.max_depth

st.write('### Previous Example Data')
st.write('min depth = '+str(zmin)+' / max depth = '+str(zmax))
st.dataframe(df)

## Processing - Groundhog is Not working for now
df2 = df.calculate_overburden()
st.dataframe(df2)

#grid = df2.map_soilprofile()
#st.dataframe(grid)

## Plotting


st.write('### Plots')
fig = make_subplots(rows=1, cols=3, subplot_titles=('Log','Unit Weight','Logging'))
#
#fig.add_trace(go.Scatter(x=[0,1],y=[1,1], text=['un','fill'], mode='text'), row=1,col=1)
for i in range(len(df)):
    if df.loc[i,'Soil type'] == 'SAND':
        c = 'LightYellow'
    elif df.loc[i,'Soil type'] == 'CLAY':
        c = 'Brown'
    elif df.loc[i,'Soil type'] == 'SILT':
        c = 'Green'
    else:
        c = 'Black'
    #

    fig.add_shape(type='rect',x0=0,y0=df.loc[i,'Depth from [m]'],x1=2,y1=df.loc[i,'Depth to [m]'],
                  line=dict(color='Black',width=2), fillcolor=c, opacity=0.5, row=1,col=1)
    fig.add_trace(go.Scatter(x=[1],y=[df.loc[i,'Depth from [m]']/2+df.loc[i,'Depth to [m]']/2],
                             text=df.loc[i,'Soil type'], mode='text'), row=1,col=1)
fig.add_trace(go.Scatter(x=[0,2], y=[option_depth,option_depth],
                         mode='lines', line=dict(color='Red',dash='dash')), row=1,col=1)
#
fig.add_trace(go.Scatter(x=df['Total unit weight [kN/m3]'], y=df['Depth from [m]'],
                         mode='lines+markers', line_shape='vh', line=dict(color='RoyalBlue'),
                         name='from', showlegend=False), row=1,col=2)
fig.add_trace(go.Scatter(x=df['Total unit weight [kN/m3]'], y=df['Depth to [m]'],
                         mode='lines+markers', line_shape='hv', line=dict(color='RoyalBlue'),
                         name='to', showlegend=False), row=1,col=2)
fig.add_trace(go.Scatter(x=[18,20], y=[option_depth,option_depth],
                         mode='lines', line=dict(color='Red',dash='dash')), row=1,col=2)
#
fig.add_trace(go.Scatter(x=df['qt [MPa]'], y=df['Depth to [m]'],
                         mode='lines+markers', name='qt'), row=1,col=3)
fig.add_trace(go.Scatter(x=[0,40], y=[option_depth,option_depth],
                         mode='lines', line=dict(color='Red',dash='dash')), row=1,col=3)
#
#fig.update_yaxes(autorange="reversed")
fig.update_yaxes(range=[zmax,zmin])
fig['layout']['yaxis']['title']='Depth [m]'
fig['layout']['xaxis']['title']=' '
fig['layout']['xaxis2']['title']='$\gamma [KN/m3]'
fig['layout']['xaxis3']['title']='CPT qt [MPa]'
fig.update_layout(height=600, width=800, title_text="")
fig.update_layout(showlegend=False)
#
st.plotly_chart(fig)

