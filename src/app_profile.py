import os
import sys
import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report 


SIZE_FILE_LIMIT=50
st.set_page_config(page_title='Data profiler', layout='wide')

def get_filesize(file):
    size_bytes = sys.getsizeof(file)
    size_mb = size_bytes / (1024*1024)
    return size_mb

def validate_file(file):
    filename = file.name
    name, ext = os.path.splitext(filename)
    if ext  in ('.csv', '.xlsx', '.xls'):
        return ext
    else:
        return False

with st.sidebar:
    uploaded_file = st.file_uploader(f"Upload .csv, .xlsx files not to exceed {SIZE_FILE_LIMIT} MB")
    if uploaded_file is not None:
        st.write('Modes of Operations')
        detailed = st.checkbox('Do you want Detailed Report ?',True)
        display_mode =st.radio('Display Mode:',
                                  options=('Primary', 'Dark', 'Orange'))
        if display_mode == 'Dark':
            dark_mode = True
            orange_mode = False
        elif display_mode == 'Orange':
            dark_mode = False
            orange_mode = True
        else:
            dark_mode = False
            orange_mode = False


if uploaded_file is not None:
    df = None
    ext = validate_file(uploaded_file)
    if ext:
        filesize = get_filesize(uploaded_file)
        if filesize <= SIZE_FILE_LIMIT:
            if ext == '.csv':
                df = pd.read_csv(uploaded_file)
            else:
                xl_file = pd.ExcelFile(uploaded_file)
                sheet_tuple = tuple(xl_file.sheet_names)
                sheet_name = st.sidebar.selectbox('Select the sheet',sheet_tuple)
                df = xl_file.parse(sheet_name)

            with st.spinner('Generating Report'):
                pr = ProfileReport(df, 
                                minimal= not detailed, 
                                dark_mode=dark_mode, 
                                orange_mode=orange_mode
                                )

            st_profile_report(pr)
        else:
            st.error(f'Maximum allowed filesize is {SIZE_FILE_LIMIT} But reeived {filesize} MB')
    else:
        st.error('Invalid File type. Valid file types are .csv, .xlsx, .xls')
else:
    st.title('Data Profiler')
    st.info('Upload your data in the left sidebar to generate profiling')