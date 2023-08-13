import streamlit as st
import pandas as pd
import time
st.title('Funding Dashboard')
st.header('I am learning Streamlit')
st.subheader('This is a subheader utility function')

## write
st.write("This is used for writing something")
## markdown
st.markdown("""
My fav movies
- Lord of the rings
- Harry Potter
""")


### we can write code
st.code("""
def foo(input):
    return input**2
x = foo(2)
""")
## usage of latex
st.latex('x^2 + y^2 =1')

df = pd.DataFrame({
    'name':['Nitish','Saima'],
    'marks':[50,60],
    'package':[20,17.75]
})
st.dataframe(df)

### creating metrics
st.metric('Revenue','Rs 3L','-3%')

#showing JSON objects
st.json({
    'name':['Nitish','Saima'],
    'marks':[50,60],
    'package':[20,17.75]
})
## adding images
st.image('lena15.jpg')
# adding videos
# st.video('file_name')

#side bar\
st.sidebar.title('Sidebar ka title')
st.sidebar.image('lena15.jpg')

#placing image side by side
cols1, cols2 = st.columns(2)
with cols1:
    st.image('lena15.jpg')
with cols2:
    st.image('lena15.jpg')

###Status message
st.error('login failed')
st.success('login successfull')
st.info('login')
st.warning('warning message')


### progress of the bar
# bar = st.progress(0)
# for i in range(1,100):
#     time.sleep(0.1)
#     bar.progress(i)


### Taking user input
#text input
email = st.text_input('Enter email')
number = st.number_input('enter number')
st.date_input('enter data')

#Buttons
import pandas as pd
file = st.file_uploader('Upload a CSV file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())