import streamlit
import pandas
import requests

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here, so that customers can pick the fruits they want to include
fruits_selected = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#Display the table on page
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruityvice Fruit Advice!')

#Display Fruity Vice API response
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#Take the json version of the response and normalize it
fruityvice_normalize = pandas.json_normalize(fruityvice_response.json())
#Output it on the screen as a table
streamlit.dataframe(fruityvice_normalize)

