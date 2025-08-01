import streamlit as st
import langchain_helper

# App layout and title
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍴", layout="centered")
st.markdown(
    """
    <style>
        .main {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
        }
        .title {
            font-family: Arial, Helvetica, sans-serif;
            font-size: 3em;
            color: #d35400;
        }
        .header {
            font-family: 'Courier New', Courier, monospace;
            color: #2980b9;
            font-weight: bold;
        }
        .menu-item {
            font-size: 1.1em;
            color: #34495e;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title'>🍽️ Restaurant Name Generator</h1>", unsafe_allow_html=True)

# Sidebar for cuisine selection
st.sidebar.header("Cuisine Selection")
cuisine = st.sidebar.selectbox(
    "Select your desired cuisine",
    ["Indian", "Italian", "Chinese", "Mexican", "American", "Japanese", "Arabic", "Thai", "French", "Spanish"],
)

custom_cuisine = st.sidebar.text_input("Or type a custom cuisine:")

# Combine selection and custom cuisine
final_cuisine = custom_cuisine if custom_cuisine.strip() else cuisine

# Generate and display restaurant details
if st.sidebar.button("Generate Restaurant"):
    response = langchain_helper.generate_restaurant_name_and_items(final_cuisine)
    st.markdown(f"<h2 class='header'>{response['restaurant_name'].strip()}</h2>", unsafe_allow_html=True)
    st.markdown("**Menu Items:**")
    menu_items = response["menu_items"].strip().split(",")
    for item in menu_items:
        st.markdown(f"- <span class='menu-item'>{item.strip()}</span>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
