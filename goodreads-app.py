import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

#main page settings
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
data_analysis = st.beta_container()

#load images
firstpix = Image.open('/Users/olatunde/Desktop/goodreads/book-header.jpeg')
#ravecla = Image.open('/Users/olatunde/Desktop/goodreads/data/ravenclaw.gif')

#datasets
df = pd.read_csv('/Users/olatunde/Desktop/goodreads/Books_universe.csv')

#sidebar settings
st.sidebar.header('Team Ravenclaw')
st.sidebar.markdown("![Alt Text](https://media4.giphy.com/media/lKYMj63WqlBcc/giphy.gif?cid=ecf05e470d15qsjwvus5fhfgb3l2hpf5js7gqr26lshesrpe&rid=giphy.gif&ct=g)")
st.sidebar.markdown('Who we are:')
st.sidebar.markdown("""⬇️ This Project was created by 4 ***[Strive School](https://strive.school/)*** Students.⬇️""")
st.sidebar.markdown(""" > • Sven Skyth Henriksen: [GitHub ](https://github.com/Sven-Skyth-Henriksen)&[ LinkedIn](https://www.linkedin.com/in/sven-skyth-henriksen-4857bb1a2/)
	> 
	> • Paramveer Singh: [GitHub ](https://github.com/paramveer)&[ LinkedIn](https://www.linkedin.com/in/paramveer-singh07/)
	>
	> • Madina Zhenisbek: [GitHub ](https://github.com/madinach)&[ LinkedIn](https://www.linkedin.com/in/madina-zhenisbek/)
	>
	> • Olatunde Salami: [GitHub ](https://github.com/salamituns)&[ LinkedIn](https://www.linkedin.com/in/olatunde-salami/)
	""")
#sidebar= st.sidebar.selectbox

with header:
    st.title('Books everyone should read atleast once')
    st.image(firstpix)
    st.text('')
    st.write("""Books generally serves as a medium of recording information wether in the form of writing or in form of images, 
     and the importance of books cannot be overemphasised. Estimates have shown that about a total of 2,700 books are published daily, 
     which means so many books but so little time to read them all.""") 
    st.write("""In this project, we navigate through [GoodReads](https://www.goodreads.com/list/show/264.Books_That_Everyone_Should_Read_At_Least_Once)
     to scrape data of the best books that everyone should read at least once in their life time. From the scraped data, 
     we got some interesting insights that you might be curious to know and stored the answers in a readable format for your convinience.""")
    st.text('')
    #st.markdown('''## 🔥 Best books you really have to read atleast once 🔥
    	#Please select a page:''')

with dataset:
    df = pd.read_csv('/Users/olatunde/Desktop/goodreads/Books_universe.csv')
    df = df.drop(columns=['Unnamed: 0'])
    df.rename(columns={'publish_year':'pub_year', 'num_pages': 'num_pages'}, inplace=True)
    st.markdown("![Data](https://media4.giphy.com/media/xT9C25UNTwfZuk85WP/200.webp?cid=ecf05e47844brv5239cczg9hqo5ernebyirvx4xaua7k2dk8&rid=200.webp&ct=g)")
    if st.checkbox('Toggle-on to see the list of books'):
    	st.write(df)

with features:
    st.subheader('Diving deep into the best books collection :mag:')
    st.text('')
    st.text('Here you can browse through some of our exploratory analysis.')
    columns_to_show = st.multiselect("Some of the interesting features includes:", df.columns)
	#st.dataframe(df[columns_to_show])


with data_analysis:
    st.subheader('Analysis of people, book and life')
    st.text('Here you get to choose different plots and see how people, books and life are inter-related with each other.')


with st.beta_expander('• In what year was most of the outstanding books released?'):
    st.text('Books released')
    pub = pd.DataFrame(df['original_publish_year'].value_counts()).head(50)
    pub = pub[1::]
    st.bar_chart(pub)
    st.markdown(''' • We can infers that most books got published in 2003.  ''')

with st.beta_expander('• Which authors have the highest outstanding books'):
    st.subheader('Authors and how many Books they wrote:')
    author = pd.DataFrame(df['author'].value_counts()).head(50)
    st.area_chart(author)
    st.markdown(''' • Here we can see clearly that **Stephen King** and **William Shakespeare**
    published the most books
      ''')

with st.beta_expander('• Were the most outstanding books release as single or in series)'):
    st.subheader('Series:')
    rating_count = pd.DataFrame(df['series'].value_counts()).head(50)
    st.bar_chart(rating_count)
    st.markdown('Here we can see that there are much more **single released** books then those released in series.')


