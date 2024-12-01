import streamlit as st 
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import base64
import time

st.set_page_config(layout="wide") #landsacpe view

#adding pic  (not done need to see this!!!)
# Use your image path and converting the image to base64

# Function to convert image to base64

###
#def get_base64_of_image(image_path):
#    with open(image_path, "rb") as image_file:
#        return base64.b64encode(image_file.read()).decode()
#    
#img_path = "houses.png"
#img_base64 = get_base64_of_bin_file(img_path)

#st.markdown(
#    f"""
#    <style>
#    .stApp {{
#        background-image: url("data:image/jpg;base64,{img_base64}");
#        background-size: cover;
#        background-position: center;
#    }}
#    </style>
#    """,
#    unsafe_allow_html=True
#)




with open("../pickles/classifier.pkl", "rb") as file:
    classifier = pickle.load(file) 

st.title("Welcome to the Roadway to your Dream House!")
st.header("This classifier tells your requirements available on a Main road or not!")

df0 = pd.read_csv("../notebooks/Housing.csv")

#categorical variables
#mainroad = list(df0['mainroad'].unique())
guestroom = list(df0['guestroom'].unique())
basement = list(df0['basement'].unique())
hotwaterheating = list(df0['hotwaterheating'].unique())
airconditioning = list(df0['airconditioning'].unique())
prefarea = list(df0['prefarea'].unique())
furnishingstatus = list(df0['furnishingstatus'].unique())

#other features
bedrooms = list(df0['bedrooms'].unique())
bathrooms = list(df0['bathrooms'].unique())
stories = list(df0['stories'].unique())
parking = list(df0['parking'].unique())

#metric_list = list(df['metric'].unique())
with st.sidebar:
    #adding color
    st.markdown(
        """
        <style>
        .stApp
        [data-testid="stSidebar"]{
            background-color: #00008B; /* Dark Blue background color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.subheader("Please choose the following generic features in your Dream House.")
   # mainroad = st.selectbox(label = "On Mainroad", options = mainroad)
    guestroom = st.selectbox(label = "Having Guestroom", options = guestroom)
    basement = st.selectbox(label = "Having Basement", options = basement)
    hotwaterheating = st.selectbox(label = "Having Hot water heating", options = hotwaterheating)
    airconditioning = st.selectbox(label = "Having airconditioning", options = airconditioning)
    prefarea = st.selectbox(label = "Your preferred area priority enabling", options = prefarea)
    furnishingstatus = st.selectbox(label = "Furnishing status", options = furnishingstatus)


#label_encoding
# Convert categorical value to numerical value using Label Encoding
#mainroad_map = {"yes": 1, "no": 0}
#mainroad_encoded = mainroad_map[mainroad]

guestroom_map = {"yes": 1, "no": 0}
guestroom_encoded = guestroom_map[guestroom]

basement_map = {"yes": 1, "no": 0}
basement_encoded = basement_map[basement]

hotwaterheating_map = {"yes": 1, "no": 0}
hotwaterheating_encoded = hotwaterheating_map[hotwaterheating]

airconditioning_map = {"yes": 1, "no": 0}
airconditioning_encoded = airconditioning_map[airconditioning]

prefarea_map = {"yes": 1, "no": 0}
prefarea_encoded = prefarea_map[prefarea]

furnishingstatus_map = {"semi-furnished": 1, "furnished": 0, "unfurnished": 2}
furnishingstatus_encoded = furnishingstatus_map[furnishingstatus]
# Input widgets in the sidebar
#with st.sidebar:
#	continent = st.selectbox(label = "Choose a continent", options = continent_list)
	# input widget 2
#	...

#with st.sidebar:
with st.form("user_input"):
    st.subheader("Please Choose/Enter the following details:")
    price = st.number_input("Budget in USD", min_value=0, max_value=1000000000)
    area_requirement = st.number_input("Area Requirement", min_value=0, max_value=10000)
    bedrooms = st.selectbox(label = "No. of Bedrooms", options = bedrooms)
    bathrooms = st.selectbox(label = "No. of Bathrooms", options = bathrooms)
    stories = st.selectbox(label = "No.of Stories", options = stories)
    parking = st.selectbox(label = "No. of Parking spots", options = parking)
    
    
    #bedrooms = st.number_input("bedrooms", min_value=0, max_value=10, value= 3)
    #bathrooms = st.number_input("bathrooms", min_value=0, max_value=8, value= 2)
    #stories = st.number_input("stories", min_value=0, max_value=6, value= 2)
    #mainroad = st.number_input("mainroad (Type 1 if required, 0 if not)", min_value=0, max_value=8, value= 1)
    #guestroom = st.number_input("guestroom (Type 1 if required, 0 if not)", min_value=0, max_value=8, value= 1)
    #basement = st.number_input("basement (Type 1 if required, 0 if not)", min_value=0, max_value=8, value= 1)
    #hotwaterheating = st.number_input("hotwaterheating (Type 1 if required, 0 if not)", min_value=0, max_value=8, value= 0)
    #airconditioning = st.number_input("airconditioning (Type 1 if required, 0 if not)", min_value=0, max_value=8, value= 1)
    #parking = st.number_input("parking", min_value=0, max_value=6, value= 2)
    #prefarea = st.number_input("prefarea (Type 1 if required, 0 if not)", min_value=0, max_value=8, value= 0)
    #furnishingstatus = st.number_input("furnishingstatus (Type 1 if semi-furnished, Type 2 if unfurnished and Type 0 if fully furnished is required)", min_value=0, max_value=5, value= 1)
    button = st.form_submit_button()

if button:
    st.write("Submitted!")
    # Add a time delay of 2 seconds
    st.write("Your Data is being processed, Please Wait ... ")
    time.sleep(3)

    
   
        
    df_pred = pd.DataFrame({
        "price": price,
        "area": area_requirement,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "guestroom": guestroom_encoded,
        "basement": basement_encoded,
        "hotwaterheating": hotwaterheating_encoded,
        "airconditioning": airconditioning_encoded,
        "parking": parking,
        "prefarea": prefarea_encoded,
        "furnishingstatus": furnishingstatus_encoded  
        }
    , index=["user"])
    
   

    y_pred = classifier.predict(df_pred)  #if normalization done, values will be different!!!
     #encoding for display
    #y_pred_new = {0 : "Mainroad", 1 : "Streetroad"}  
    #mainroad_encoded = mainroad_map[mainroad]
    
    if y_pred == 1:
        st.subheader("The House will be on Mainroad!")
    else:
        st.subheader("The House will NOT be on Mainroad!")

    #text = f'The House will be on {y_pred[0]} !'
    
    #st.subheader(text)