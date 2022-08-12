from audioop import lin2adpcm
import streamlit as st
from PIL import Image



st.sidebar.title('Sidebar')
side_button = st.sidebar.button('Press Me')
if side_button:
    st.write('Button was pressed')

#Header
st.image('Images/penguins.jpg', use_column_width='always')
st.title('Streamlit Demo With Penguin')
st.header('This is a header')
col11, col12 = st.columns(2)
col11.subheader('Column 1')
col12.subheader('Column 2')
col21, col22, col23 = st.columns([3,2,1])
col21.write('widest column, place filler etc. text will wrap around the column if theres is enough')
col22.write('medium column hfhe bfbfh bwfhb hfbeb fhb')
col23.write('small column kf jwfhwj fnfjwn fwjn fnf')
st.markdown('Markdown **syntax** *works*')
'Markdown'
'## Magic'
st.write('<h2 style="text-align:center">Text Aligned with Html</h2', unsafe_allow_html=True)

st.header('Widget Functionality')

button1 = st.button('This is a button')
if button1:
    st.write('You clicked button')
check = st.checkbox('Please check this box')
button2 = st.button('Is box checked')
if button2:
    if check:
        st.write('The box was checked')
    else:
        st.write('The box was not check')

st.subheader('Radio Button')
animal_options = ['Cats', 'Dogs', 'Pigs']
fav_animal = st.radio('Which animal is your favorite?', animal_options)
button3 = st.button('Submit animal')
if button3:
    st.write(f'You selected {fav_animal} as your favorite animal')
    if fav_animal == 'Cats':
        st.write('MEOW')
    elif fav_animal == 'Dogs':
        st.write('WHOOF')
    else:
        st.write('OINK')

st.subheader('Selectbox')
fav_animal2 = st.selectbox('Which animal is your favorite?', animal_options)
st.write(f'Your favorite animal is {fav_animal2}')

like_animals = st.multiselect('Which animals do you like?', animal_options)
st.write(like_animals)
st.write(f'The animal you liked first was {like_animals[0]}')


num_pets = st.slider('How many pets is to many?', 2, 20, 2, 2)

pet_name = st.text_input('What is your pets name?', value='I do not have a pet')
st.write("Pet's name:", pet_name)

