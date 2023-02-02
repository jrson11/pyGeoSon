import streamlit as st
from copy import deepcopy

#def streamlitPCPT():
from groundhog.siteinvestigation.insitutests.pcpt_processing import PCPTProcessing, DEFAULT_CONE_PROPERTIES
from groundhog.general.soilprofile import SoilProfile, profile_from_dataframe
