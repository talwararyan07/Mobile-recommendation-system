import pandas as pd
import pickle
import streamlit as st


# Set the page background image
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('bg.png');
}

[data-testid="stSidebar"] {
    background-image: url('https://www.freepik.com/premium-photo/pink-bokeh-glitter-sweet-background-graphic-design-illustration_127467140.htm');
    background-size: cover;
    color: white;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the model and dataset
with open('mobile_recommender.pkl', 'rb') as model_file:
    similarity = pickle.load(model_file)

data = pd.read_csv('mobiles_dataset.csv')

# Function to get recommendations
def get_recommendations(product_index, num_recommendations=5):
    sim_scores = list(enumerate(similarity[product_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]  # Exclude the product itself
    recommended_indices = [i[0] for i in sim_scores]
    return data.iloc[recommended_indices]

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Recommendation"])

# Main Page
if app_mode == "Home":
    st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 80px; 
            border-radius: 10px;
        ">
            <h1 style="color: black;">Mobile Recommendation System</h1>
            <h3 style="color: black;">"Best place to find your dream mobile"</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Display mobile images in columns with background styling
    st.markdown(
         """
         <div style="display: flex; justify-content: space-around; 
                     background-color: rgba(0, 0, 0, 0); padding: 20px; border-radius: 10px; 
                     margin-top: 20px;">
         """, unsafe_allow_html=True
     )
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image('phone1.png')
    with col2:
        st.image('phone2.png')
    with col3:
        st.image('phone3.png')
    with col4:
        st.image('phone4.png')
    with col5:
        st.image('phone5.png')

    st.markdown("</div>", unsafe_allow_html=True)

elif app_mode == "About":
    st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 30px; 
            border-radius: 10px;
        ">
            <h1 style="color: black;">About</h1>
            <p style="color: black;">In today's fast-paced digital world,
            selecting the right mobile device can be overwhelming due to the plethora of options available.
            A mobile recommendation system powered by machine learning can significantly enhance user experience by providing tailored recommendations
            based on user preferences and device features. This system leverages content-based collaborative filtering, 
            which combines the strengths of content-based filtering and collaborative filtering techniques.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
         """
         <div style="display: flex; justify-content: space-around; 
                     background-color: rgba(0, 0, 0, 0); padding: 10px; border-radius: 10px; 
                     margin-top: 10px;">
         """, unsafe_allow_html=True
     )
    st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 30px; 
            border-radius: 10px;
        ">
            <h1 style="color: black;">Objectives</h1>
            <h3 style="color: black;">The primary objectives of the mobile recommendation system include:</h>
            <p style="color: black;"></p>
            <p style="color: black;">1.Personalized Recommendations: Provide users with mobile device suggestions that align with their preferences and needs.</p>
            <p style="color: black;">2.User Engagement: Increase user interaction with the platform by offering relevant recommendations.</p>
            <p style="color: black;">3.Market Insights: Gather data on user preferences to analyze trends in mobile device choices.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
         """
         <div style="display: flex; justify-content: space-around; 
                     background-color: rgba(0, 0, 0, 0); padding: 10px; border-radius: 10px; 
                     margin-top: 10px;">
         """, unsafe_allow_html=True
     )
   
    st.markdown(
         """
         <div style="display: flex; justify-content: space-around; 
                     background-color: rgba(0, 0, 0, 0); padding: 10px; border-radius: 10px; 
                     margin-top: 10px;">
         """, unsafe_allow_html=True
     )
    st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 30px; 
            border-radius: 10px;
        ">
            <h1 style="color: black;">Made By</h1>
            <h3 style="color: black;">Name: Apoorv Bagga</h3>
            <h3 style="color: black;">Subject: Statistical Machine Learning [CSET211]</h3>
            <h3 style="color: black;">Enrollment No.: E23CSEU1120</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

elif app_mode == "Recommendation":
    st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 20px; 
            border-radius: 10px;
        ">
            <h1 style="color: black;">Mobile Recommender</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    <style>
    .selectbox-label {
        color: black; /* Set text color to black */
        font-weight: bold; /* Make text bold */
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="selectbox-label">Select a product:</p>', unsafe_allow_html=True)
    # Select a product to recommend from
    product_names = data['Name'].tolist()
    selected_product = st.selectbox("", product_names)

    if st.button('Show Similar Phones'):
        product_index = data[data['Name'] == selected_product].index[0]
        recommended_products = get_recommendations(product_index)

        # Display recommended products with clickable links
        st.markdown(
        """
        <div style="
            background-color: rgba(255, 255, 255, 0.9); 
            padding: 5px; 
            border-radius: 10px;
        ">
            <h4 style="color: black;">Recommended Products</h4>
        </div>
        """,
        unsafe_allow_html=True
    )
        st.markdown(
         """
         <div style="display: flex; justify-content: space-around; 
                     background-color: rgba(0, 0, 0, 0); padding: 10px; border-radius: 10px; 
                     margin-top: 10px;">
         """, unsafe_allow_html=True
     )
        for index, row in recommended_products.iterrows():
            product_div = f"""
            <div style="
                background-color: rgba(125, 133, 129, 0.9); 
                border-radius: 20px;
                padding: 5px;
                margin: 20px;
            ">
                <h3 style="margin: 0;">{row['Name']}</h3>
                <p><strong>Price:</strong> {row['Price']}</p>
                <p><strong>Stars:</strong> {row['stars']}</p>
                <p><strong>Description:</strong> {row['description']}</p>
                <p><a href="{row['url']}" style="text-decoration: none; color: blue;">View Product</a></p>
            </div>
            """
    
            # Display the product div in Streamlit
            st.markdown(product_div, unsafe_allow_html=True)
            #st.image("phone1.png", width=300)#Demo image