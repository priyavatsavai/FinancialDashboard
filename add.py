import streamlit as st
st.write("Welcome to My First Streamlit App!")

st.header("This is a header")
# Create a button
if st.button("Click Me"):
    st.write('Button Clicked')

favourite_fruits = ["Äpple","Banana","Cherry"]

st.write("This is My Favourite Fruits List!  Check it Out")
st.write(favourite_fruits)
image_url = "https://thumbs.dreamstime.com/b/apple-cherry-banana-strawberry-isolated-white-background-fresh-apple-cherry-banana-strawberry-isolated-white-250773356.jpg"
st.image(image_url, "This is an image from a URL",use_column_width = True)
