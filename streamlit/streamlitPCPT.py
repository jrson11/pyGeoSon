import streamlit as st
import numpy as np
import pandas as pd
import altair as alt


from groundhog.general.soilprofile import SoilProfile, profile_from_dataframe

st.set_page_config(page_title="Groundhog PCPT processing",layout='wide')
cols = st.beta_columns([1, 3])
