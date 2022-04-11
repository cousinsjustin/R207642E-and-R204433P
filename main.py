
import io 

import upload_video.py as v

import split_video.py as sv

import classify as sst
pip install opencv-python

import cv2 as cv

import tempfile
import streamlit as st



uploaded_file = st.file_uploader("Choose a video...", type=["mp4"])

v.upload_video(uploaded_file)

classifications = sst.classifyImages()

#function to search in frames
def searchInFrames(object_):
    
    indeces = []
    
    if object_ in classifications:
        st.write(" object has been found")
  
    else:
        st.write("object is not in the frames!")
        
  #input is our varible to store our input      
input = st.text_input("object to search: ")

if st.button('Search'): 
    
    frames =[]
    
    detected_paths = []
    
    searchInFrames(input)
    
    st.write("")


#imports
# import io 

# import cv2 as cv

# import tempfile
# import streamlit as st







