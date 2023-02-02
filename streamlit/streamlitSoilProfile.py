import streamlit as st
import numpy as np
#
from groundhog.general import soilprofile as sp
from plotly.offline import plot
import plotly.graph_objs as go
from plotly.subplots import make_subplots


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
'''
fig = profile_2.plot_profile(
    parameters=(('Total unit weight [kN/m3]',), ('qc [MPa]', 'qt [MPa]')),
    showlegends=((False,), (True, True)),
    xtitles=(r'$ \gamma \ \text{[kN/m} ^3 \text{]} $', r'$ q_c, \ q_t \ \text{[MPa]} $'),
    ztitle=r'$ z \ \text{[m]} $',
    xranges=((15, 22), (0, 60)),
    zrange=(10, 0),
    fillcolordict={'SAND': 'yellow', 'CLAY': 'brown', 'SILT': 'green'})
'''

'''
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 1])

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, name="linear",
                    line_shape='linear'))
fig.add_trace(go.Scatter(x=x, y=y + 5, name="spline",
                    text=["tweak line smoothness<br>with 'smoothing' in line object"],
                    hoverinfo='text+name',
                    line_shape='spline'))
fig.add_trace(go.Scatter(x=x, y=y + 10, name="vhv",
                    line_shape='vhv'))
fig.add_trace(go.Scatter(x=x, y=y + 15, name="hvh",
                    line_shape='hvh'))
fig.add_trace(go.Scatter(x=x, y=y + 20, name="vh",
                    line_shape='vh'))
fig.add_trace(go.Scatter(x=x, y=y + 25, name="hv",
                    line_shape='hv'))

fig.update_traces(hoverinfo='text+name', mode='lines+markers')
fig.update_layout(legend=dict(y=0.5, traceorder='reversed', font_size=16))

fig = go.Figure()
fig.add_trace(go.Scatter(x=profile_2['Total unit weight [kN/m3]'], y=profile_2['Depth to [m]'], line_shape='hv', name='hv'))
fig.add_trace(go.Scatter(x=profile_2['Total unit weight [kN/m3]'], y=profile_2['Depth to [m]'], line_shape='vh', name='vh'))
fig.add_trace(go.Scatter(x=profile_2['Total unit weight [kN/m3]'], y=profile_2['Depth from [m]'], line_shape='hv', name='hv2'))
fig.add_trace(go.Scatter(x=profile_2['Total unit weight [kN/m3]'], y=profile_2['Depth from [m]'], line_shape='vh', name='vh2'))
fig.update_yaxes(autorange="reversed")
fig.update_layout(autosize=False,width=400,height=700)
'''

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(x=profile_2['Total unit weight [kN/m3]'], y=profile_2['Depth from [m]'], line_shape='vh', name='UW'), row=1,col=1)
fig.add_trace(go.Scatter(x=profile_2['qc from [MPa]'], y=profile_2['Depth from [m]'], line_shape='linear', name='qc'), row=1,col=2)
fig.update_yaxes(autorange="reversed")
fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")


st.plotly_chart(fig)
