
import io 
import os
#import upload_video as v

#import split_video as sv

#import classify as sst
direct= "R207642E-R204433P"
fpath = os.path.join(direct, "upload_video.py")
v = open(fpath)


fpat = os.path.join(direct, "split_video.py")
sv = open(fpat)
fpa = os.path.join(direct, "upload_video.py")
sst = open(fpa)




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







