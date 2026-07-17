import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
import time 
st.set_page_config("👑 QUANTIQUE")
st.sidebar.title("🧭 Navigation")

page = st.sidebar.radio(
    "✨ Discover QUANTIQUE", 
    [
        "🏠 Dashboard",
        "📊 Analytics",
        "✨ StyleDNA",
        "💎 My Luxury Wardrobe",
        "🌍 Fashion Passport" ,
        "📸 Social Fashion Trends"
    ]
)
st.sidebar.divider()

st.sidebar.markdown("### ✨ Project Creator")
st.sidebar.write("**Simran Bhatti**")
st.sidebar.caption("B.Tech Data Science")
st.sidebar.caption(" of second year ")

if page ==  "🏠 Dashboard":
    st.title(" 👑 QUANTIQUE") #cd C:\Users\simar\Desktop\fashion
    st.subheader("Luxury Fashion Intelligence Platform")#streamlit run fashion.py
    st.caption("Discover the world's fashion heritage")              
    st.divider()

    # ================= STATISTICS =================
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👗 Dresses", "250+")

    with col2:
        st.metric("🤵 Men's Wear", "180+")

    with col3:
        st.metric("💎 Premium", "120+")

    with col4:
        st.metric("🌍 Seasons", "4")

    st.divider()

    # ================= SEARCH =================
    st.warning("Warning: Fits may steal hearts 💘")
    season = st.radio(
    "💖 Pick Your Season",
     ["🌞 Summer vibes", "🌷 Spring Bloom", "🍁 Autumn Muse", "❄️ Winter Luxe"],
    horizontal=True
)

    left, right = st.columns(2)
    with left:
       if season == "🌞 Summer vibes":
        st.subheader("🌞 Summer vibes")
        st.write("Lightweight, breathable styles for sunny adventures.")

        if st.button(" 🌞summer Explore collection"):
        
           st.markdown("---")
           st.markdown("# 🌞 Summer Collection")
             # ================= WOMEN =================

           st.markdown("## 👗 Women's summer Collection")
             # Row 1
           col1, col2, col3 = st.columns(3)

           with col1:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer collection.jpg", width=700)
            st.write("🌴 Coastal Breeze Dress")
            
           with col2:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer collection 2.jpg", width=700)
            st.write("🌊 Ocean Breeze Dress")

           with col3:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer collection6.jpg", width=700)
            st.write("✨ Capri Bloom Dress")

           col4, col5, col6 = st.columns(3)

           with col4:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer collection3.jpg", width=700)
            st.write("✨ Santorini Breeze Dress")

           with col5:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer collection 4.jpg", width=700)
            st.write("✨ Amalfi Summer Dress")

           with col6:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer collection5.jpg", width=700)
            st.write("✨ Santorini Breeze Dress")
             # ================= MEN ================= #
           st.markdown("---")
           st.markdown("## 🤵 Men's summer Collection")

           col7, col8, col9 = st.columns(3)

           with col7:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer men c1.jpg", width=700)
            st.write("✨ Santorini Breeze Dress")

           with col8:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer men 2.jpg", width=700)
            st.write("✨ Amalfi Summer Dress")

           with col9:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer c men3.jpg", width=700)
            st.write("✨ Santorini Breeze Dress")
           col10, col11, col12 = st.columns(3)

           with col10:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer c men 4.jpg", use_container_width=True)
            st.write("👔 QUANTIQUE Coastal Luxe")

           with col11:
            st.image("c:/Users/simar/Desktop/fashion/photos/summer c men 5.jpg",  use_container_width=True)
            st.write("👕 Riviera Linen Shirt")

           with col12:
            st.image("c:/Users/simar/Desktop/fashion/photos/sumen c men 3.jpg",  use_container_width=True)
            st.write("🌿 Ocean Breeze Shirt")
           # ================= PREMIUM COLLECTION =================

           st.markdown("---")
           st.markdown("## ✨ Premium Summer Collection")

           # Row 5
           col13, col14, col15 = st.columns(3)

           with col13:
             st.image("c:/Users/simar/Desktop/fashion/photos/summer both 2.jpg", use_container_width=True)
             st.markdown(" #☀️ Riviera Luxe Dress")

           with col14:
              st.image("c:/Users/simar/Desktop/fashion/photos/sumer both 1.jpg", use_container_width=True)
              st.markdown("#👔 QUANTIQUE Coastal Signature")

           with col15:
             st.image("c:/Users/simar/Desktop/fashion/photos/summmer both.jpg", use_container_width=True)
             st.markdown("#🌊 Ocean Breeze Couture")
           st.markdown("###☀️ Solstice Luxe Dress")
           st.warning("Lightweight luxury fabrics and vibrant summer colors designed for elegance, comfort, and effortless style.")

       elif season ==  "🌷 Spring Bloom":
        st.subheader("🌷 Spring Bloom")
        st.write("Fresh pastel styles inspired by blooming gardens.")
        if st.button("🌷 Explore Spring Collection"):

           with st.spinner("🌸 Curating your Spring Collection..."):
             time.sleep(2)

           st.success("🌷 Welcome to QUANTIQUE Spring Bloom!")

           st.markdown("# 🌸 🌼 🌺 🌷 🌸 🌼 🌺 🌷")

           # ================= WOMEN =================

           st.markdown("## 👗 Women's Spring Collection")

           # Row 1
           col1, col2, col3 = st.columns(3)

           with col1:
            st.image("c:/Users/simar/Desktop/fashion/photos/sprong girl 1.jpg", use_container_width=True)
            st.markdown("#🌸 Blossom Luxe Dress")

           with col2:
             st.image("c:/Users/simar/Desktop/fashion/photos/spring girl2.jpg", use_container_width=True)
             st.markdown("#🌷 Petal Grace Dress")

           with col3:
              st.image("c:/Users/simar/Desktop/fashion/photos/spring girl 3.jpg", use_container_width=True)
              st.markdown("#🌺 Garden Muse Dress")


           # Row 2
           col4, col5, col6 = st.columns(3)

           with col4:
             st.image("c:/Users/simar/Desktop/fashion/photos/spring girl 4.jpg", use_container_width=True)
             st.markdown("#🌼 Bloom Elegance Dress")

           with col5:
             st.image("c:/Users/simar/Desktop/fashion/photos/spring gilr 5 jpg", use_container_width=True)
             st.markdown("#🌹 Floral Symphony Dress")

           with col6:
              st.image("c:/Users/simar/Desktop/fashion/photos/spring girl 6.jpg", use_container_width=True)
              st.markdown("#🌿 Spring Whisper Dress")


           # ================= MEN =================

           st.markdown("---")
           st.markdown("## 🤵 Men's Spring Collection")

           # Row 3
           col7, col8, col9 = st.columns(3)

           with col7:
            st.image("c:/Users/simar/Desktop/fashion/photos/spring men 1.jpg", use_container_width=True)
            st.markdown("#👔 QUANTIQUE Spring Elite")

           with col8:
            st.image("c:/Users/simar/Desktop/fashion/photos/spring meen 2.jpg", use_container_width=True)
            st.markdown("#🌿 Riviera Linen Shirt")

           with col9:
            st.image("c:/Users/simar/Desktop/fashion/photos/spring men 3.jpg", use_container_width=True)
            st.markdown("#🌷 Spring Breeze Shirt")


           # Row 4
           col10, col11, col12 = st.columns(3)

           with col10:
            st.image("c:/Users/simar/Desktop/fashion/photos/spring men 4.jpg", use_container_width=True)
            st.markdown("#🌼 Coastal Cotton Shirt")

           with col11:
            st.image("c:/Users/simar/Desktop/fashion/photos/spting men 5.jpg", use_container_width=True)
            st.markdown("#🌺 Garden Classic Shirt")

           with col12:
             st.image("c:/Users/simar/Desktop/fashion/photos/spring men 6.jpg", use_container_width=True)
             st.markdown("#🌊 Ocean Breeze Shirt")


           # ================= PREMIUM COLLECTION =================

           st.markdown("---")
           st.markdown("## ✨ Premium Spring Collection")
            # Row 5
           col13, col14, col15 = st.columns(3)
 
           with col13:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum premim.jpg", use_container_width=True)
            st.markdown("#🌸 Blossom Royale Dress")

           with col14:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum premim 1.jpg", use_container_width=True)
            st.markdown("#👔 QUANTIQUE Heritage Signature")

           with col15:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum permium 3.jpg", use_container_width=True)
             st.markdown("#🌷 Floral Elegance Couture")

           st.markdown("### 🌷 Eternal Blossom Dress")
           st.success("Fresh floral tones and luxurious fabrics designed to celebrate the beauty of the spring season.")
           
           
       elif season == "🍁 Autumn Muse":
         st.subheader("🍁 Autumn Muse")
         if st.button("🍁 Explore Autumn Collection"):

           with st.spinner("🍂 🍁 Curating your Autumn Collection..."):
             time.sleep(2)

           st.success("🍁 Welcome to QUANTIQUE Autumn Muse!")

           st.markdown("# 🍂 🍁 🍂 🍁 🍂 🍁 🍂")


           # ================= WOMEN =================#

           st.markdown("## 👗 Women's Autumn Collection")

           # Row 1
           col1, col2, col3 = st.columns(3)

           with col1:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum girl speical 1.jpg", use_container_width=True)
            st.markdown("#🍂 Maple Elegance Dress")

           with col2:
             st.image("c:/Users/simar/Desktop/fashion/photos/autm girl special 2.jpg", use_container_width=True)
             st.markdown("#🤎 Cocoa Luxe Dress")

           with col3:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum speical 3 girl.jpg", use_container_width=True)
             st.markdown("#🍁 Autumn Whisper Dress")


           # Row 2
           col4, col5, col6 = st.columns(3)

           with col4:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum girl 1.jpg", use_container_width=True)
             st.markdown("#🌰 Chestnut Grace Dress")

           with col5:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum girl 2.jpg", use_container_width=True)
             st.markdown("#🧡 Amber Bloom Dress")

           with col6:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum girl 4.jpg", use_container_width=True)
             st.markdown("#🍷 Burgundy Muse Dress")


           # ================= MEN =================

           st.markdown("---")
           st.markdown("## 🤵 Men's Autumn Collection")

           # Row 3
           col7, col8, col9 = st.columns(3)

           with col7:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum boy 1.jpg", use_container_width=True)
             st.markdown("#👔 QUANTIQUE Autumn Elite")

           with col8:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum boy 2.jpg", use_container_width=True)
            st.markdown("#🧥 Heritage Suede Jacket")

           with col9:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum boy 3.jpg", use_container_width=True)
             st.markdown("#🍂 Rustic Linen Shirt")


            # Row 4
           col10, col11, col12 = st.columns(3)

           with col10:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum boy 4.jpg", use_container_width=True)
             st.markdown("#🤎 Woodland Classic Shirt")

           with col11:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum boy 5.jpg", use_container_width=True)
            st.markdown("#🌿 Olive Prestige Shirt")

           with col12:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum boy 6.jpg", use_container_width=True)
            st.markdown("#🍁 Harvest Luxe Jacket")


           # ================= PREMIUM COLLECTION =================

           st.markdown("---")
           st.markdown("## ✨ Premium Autumn Collection")

           # Row 5
           col13, col14, col15 = st.columns(3)
 
           with col13:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum premim.jpg", use_container_width=True)
            st.markdown("#🍂 Golden Maple Dress")

           with col14:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum premim 1.jpg", use_container_width=True)
            st.markdown("#👔 QUANTIQUE Heritage Signature")

           with col15:
             st.image("c:/Users/simar/Desktop/fashion/photos/autum permium 3.jpg", use_container_width=True)
             st.markdown("#🍁 Harvest Luxe Jacket")
           st.markdown("### 🍁 Royal Autumn Couture")
           st.error("Warm earthy tones with cozy layers for crisp autumn days.")
        
       elif season == "❄️ Winter Luxe":
        st.subheader("❄️ Winter Luxe")
        st.write("Luxury winter fashion with elegant coats and cozy essentials.")
        if st.button("❄️ Explore winter Collection"):
            # Winter animation
           st.snow()

            # Loading message
           with st.spinner("❄️ Preparing your Winter Collection..."):
                time.sleep(2)

           st.success("✨ Welcome to QUANTIQUE Winter Luxe Collection!")

           st.markdown("---")

          
           st.markdown("## ❄️ Winter Collection")

   

           # ================= WOMEN =================

           st.markdown("## 👗 Women swinter Collection")

           # Row 1
           col1, col2, col3 = st.columns(3)

           with col1:
            st.image("c:/Users/simar/Desktop/fashion/photos/winter sj.jpg", use_container_width=True)
            st.markdown("#❄️ Arctic Elegance Dress")

           with col2:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter girl 2.jpg", use_container_width=True)
             st.markdown("#🧥 Snow Queen Coat")

           with col3:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter girl 3.jpg", use_container_width=True)
             st.markdown("#🤍 Frost Pearl Dress")


           # Row 2
           col4, col5, col6 = st.columns(3)

           with col4:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter girl 4.jpg", use_container_width=True)
             st.markdown("#🌰 Chestnut Grace Dress")

           with col5:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter girl 5.png", use_container_width=True)
             st.markdown("#🧡 Amber Bloom Dress")

           with col6:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter girl 6.jpg", use_container_width=True)
             st.markdown("#🍷 Burgundy Muse Dress")


           # ================= MEN =================

           st.markdown("---")
           st.markdown("## 🤵 Men's winter Collection")

           # Row 3
           col7, col8, col9 = st.columns(3)

           with col7:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter boy 1.jpg", use_container_width=True)
             st.markdown("#👔 QUANTIQUE Autumn Elite")

           with col8:
            st.image("c:/Users/simar/Desktop/fashion/photos/winter boy 2.jpg", use_container_width=True)
            st.markdown("#🧥 Heritage Suede Jacket")

           with col9:
             st.image("c:/Users/simar/Desktop/fashion\photos/winter boy 3.jpg", use_container_width=True)
             st.markdown("#🍂 Rustic Linen Shirt")


           # Row 4
           col10, col11, col12 = st.columns(3)

           with col10:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter boy 4.jpg", use_container_width=True)
             st.markdown("#🤎 Woodland Classic Shirt")

           with col11:
            st.image("c:/Users/simar/Desktop/fashion/photos/autum boy special 1.jpg", use_container_width=True)
            st.markdown("#🌿 Olive Prestige Shirt")

           with col12:
            st.image("c:/Users/simar/Desktop/fashion/photos/winter boy 6.jpg", use_container_width=True)
            st.markdown("#❄️ Harvest Luxe Jacket")


         # ================= PREMIUM COLLECTION =================

           st.markdown("---")
           st.markdown("## ✨ Premium winter Collection")

           # Row 5
           col13, col14, col15 = st.columns(3)
 
           with col13:
            st.image("c:/Users/simar/Desktop/fashion/photos/winter premim.jpg", use_container_width=True)
            st.markdown("#🍂 Golden Maple Dress")

           with col14:
            st.image("c:/Users/simar/Desktop/fashion/photos/winter perimum.jpg", use_container_width=True)
            st.markdown("#👔 QUANTIQUE Heritage Signature")

           with col15:
             st.image("c:/Users/simar/Desktop/fashion/photos/winter perimum 2.jpg", use_container_width=True)


           st.markdown("### ❄️ Eternal Frost Dress")
           st.info("Luxurious winter layers with elegant textures designed to keep you warm in timeless style. " )
           
    with right:   
     if season == "🌞 Summer vibes":
      st.image("c:/Users/simar/Desktop/fashion/photos/fashion1.jpg",width=500)
     elif season == "🌷 Spring Bloom":
       st.image("c:/Users/simar/Desktop/fashion/photos/fashion 2.jpg",width=500)
     elif season == "🍁 Autumn Muse":
       st.image("c:/Users/simar/Desktop/fashion/photos/fashion 4.jpg", width=500)
     elif season == "❄️ Winter Luxe": 
       st.image("c:/Users/simar/Desktop/fashion/photos/fashion 8 .jpg",width=500)
       st.warning("Warm earthy tones with cozy layers for crisp winter days.")
    st.divider()

          # ================= WHY CHOOSE QUANTIQUE =================

    st.markdown("## ✨ Why Explore QUANTIQUE?")

    col1, col2, col3 = st.columns(3)

    with col1:
      st.markdown("""
### 🌍 Fashion Passport

Travel across the world and discover the history behind traditional fashion.
""")

    with col2:
      st.markdown("""
### 🎮 Interactive Challenges

Play fashion games, earn Passport XP, and unlock exclusive badges.
""")

    with col3:
     st.markdown("""
### 🤖 AI Fashion Guide

Get smart styling suggestions inspired by global fashion cultures.
""")  


elif page ==  "📊 Analytics":
    st.title( "📊 Analytics")
    st.write("Transform fashion data into intelligent insights with QUANTIQUE. ")
    df = pd.read_csv("purchase_data.csv")

    search = st.text_input("🔍 Search Store")
    if search:

        result = df[
          (df["UnitPrice"] == int(search)) |
          (df["UnitCost"] == int(search))
    

        ]
        st.dataframe(result)

    st.dataframe(df)
    df["Sales"] = df["UnitPrice"] * df["InboundInventory"]
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
          st.metric("💰 Total Sales", "₹24.8L", "+12%")

    with col2:
          st.metric("🛍️ Orders", "3,520", "+280")

    with col3:
           st.metric("👥 Customers", "8,910", "+15%")

    with col4:
            st.metric("👗 Products", "1,248", "+35")
    chart = st.selectbox(
        "📊 Choose a Chart",
        [
            "📈 Monthly Sales Trend",
            "📊 Sales Distribution by Region"
        ]
    )
    if chart == "📈 Monthly Sales Trend":
       
            
      st.subheader("📈 Monthly Sales Trend")
      df = pd.read_csv("c:/Users/simar/Desktop/fashion/purchase_data.csv")
      df["PurchaseDate"] = pd.to_datetime(df["PurchaseDate"])#This converts them into real date format.
      df["Month"] = df["PurchaseDate"].dt.strftime("%b")#It creates a new column called Month
      df["Sales"] = df["UnitPrice"] * df["InboundInventory"]#It creates another new column called Sales.
      monthly_sales = df.groupby("Month")["Sales"].sum()#It groups all the rows according to the month.
      fig, ax = plt.subplots(figsize=(10,5))#Creates an empty graph.

      ax.plot(
       monthly_sales.index,
       monthly_sales.values,
       marker="o",
       linewidth=3,#Makes the line thicker.
       markersize=6#Makes circles bigger.
       
    )#This draws the graph.

      ax.set_title("📈 Monthly Sales Trend", fontsize=10)#Adds graph title.

      ax.set_xlabel("Month")

      ax.set_ylabel("Sales (₹)")

      ax.grid(True)#Adds background grid lines

      st.pyplot(fig)#This is the line that shows your Monthly Sales Trend graph.

    elif chart == "📊 Sales Distribution by Region":    
      st.subheader("📊 Sales Distribution by Region")
      region_sales = df.groupby("Region")["Sales"].sum()
      df.groupby("Region") 
      fig, ax = plt.subplots(figsize=(4,4))
      ax.pie(
      region_sales.values,
      labels=region_sales.index,
      autopct="%1.1f%%",
        startangle=32

    )
      ax.axis("equal")

      st.pyplot(fig)
elif page == "✨ StyleDNA":

    st.title("✨ StyleDNA")

    st.write("Discover your unique fashion identity with AI.")        
    season = st.selectbox(
    "✨ Style for Which Season?",
    [
        "🌞 Summer Vibes",
        "🌸 Spring Bloom",
        "🍁 Autumn Muse",
        "❄️ Winter Luxe"
    ]
  )
    gender = st.selectbox(
      "💎 Find Your Signature Style",
    [
        "👗 Women's Luxe",
        "🤵 Men's Luxe"
    ]
  )
    style = st.selectbox(
    "🪄 Curate Your Perfect Look",
    [
        "🌿 Casual Chic",
        "💼 Office Elegance",
        "✨ Evening Glam",
        "👑 Luxury Couture"
    ]
  )
    budget = st.slider(
    "💰 Select Your Budget (₹)",
    10000,
    90000,
    5000,
    9000
  )
    if "show_recommendation" not in st.session_state:
     st.session_state.show_recommendation = False

    if st.button("✨ Get AI Recommendation"):
     st.session_state.show_recommendation = True

    if st.session_state.show_recommendation:


      st.subheader("🤖 Your AI Recommendation")

      st.write("Season:", season)
      st.write("Collection:", gender)
      st.write("Style:", style)
      st.write("Budget: ₹", budget)

      st.divider()

      if season == "❄️ Winter Luxe":

        st.markdown("## ❄️ Winter Luxe Recommendation")
        st.success("❄️ QUANTIQUE AI has selected a luxurious Winter outfit to keep you warm and stylish!")

        col1, col2, col3 = st.columns(3)
        if gender == "👗 Women's Luxe":
          with col1:
           st.image(
            "c:/Users/simar/Desktop/fashion/photos/winter girl 2.jpg",
            width=200,
            caption="❄️ Winter Women's Collection"
          )
          with col2:
           st.image(
            "c:/Users/simar/Desktop/fashion/photos/winter girl 6.jpg",
            width=200,
            caption="❄️ Winter Women's Collection"
          )
           with col3:

               st.markdown("### 👗 Outfit Details")
               st.write("🧥 Long Wool Coat")
               st.write("👢 Knee High Boots")
               st.write("👜 Luxury Handbag")
               st.write("🧣 Cashmere Scarf")
               st.write("🧤 Leather Gloves")
          st.markdown("### ⭐ Outfit Rating")

          st.write("9.8 / 10")
          st.markdown("### 🤖 Why QUANTIQUE Recommended This")

          st.write("✔ Perfect for cold winter weather")
          st.write("✔ Matches your selected style")
          st.write("✔ Fits your selected budget")
          st.write("✔ Trending in Winter 2026")

          st.markdown("### 🎨 Recommended Color Palette")

          st.write("⚫ Black")
          st.write("🤍 White")
          st.write("🩶 Grey")
          st.write("🍷 Burgundy")
          st.write("🤎 Chocolate Brown")

          st.markdown("### 👜 Perfect Accessories")

          st.write("⌚ Luxury Watch")
          st.write("🧤 Leather Gloves")
          st.write("🧣 Cashmere Scarf")
          st.write("🕶️ Polarized Sunglasses")
          st.write("👜 Designer Leather Bag")

          st.markdown("### 💰 Estimated Outfit Cost")

          st.write("🧥 Long Wool Coat : ₹18,000")
          st.write("👢 Knee High Boots : ₹12,000")
          st.write("👜 Luxury Handbag : ₹25,000")
          st.write("🧣 Cashmere Scarf : ₹5,000")
          st.write("🧤 Leather Gloves : ₹4,000")

          st.markdown("---")

          st.markdown("## 💳 Total Estimated Cost: ₹64,000")

          st.markdown("### 🧺 Care Instructions")

          st.write("🧼 Dry clean the wool coat for longer durability.")
          st.write("👢 Clean leather boots with leather polish.")
          st.write("🧣 Hand wash the cashmere scarf with cold water.")
          st.write("👜 Store the leather handbag in a dust bag.")
          
          st.markdown("---")

          st.markdown("## 🎉 QUANTIQUE AI Final Summary")

          st.write("✔ Season: Winter Luxe")
          st.write("✔ Collection: Luxury")
          st.write("✔ Personalized for your selected style")
          st.write("✔ Recommended based on your budget")
          st.write("✔ Luxury accessories included")
          st.write("✔ Winter color palette selected")

          st.success("✨ Your Winter Luxe outfit is ready. Enjoy your premium fashion experience with QUANTIQUE!")
          if st.button("❤️ Save to Wishlist"):
            st.success("Item saved to your Wishlist!") 
          if st.button("🛍️ Add to Cart"):
             st.success("Outfit added to your Cart!")

          if st.button("📥 Download Recommendation"):
           st.success("Recommendation is ready to download!")
          st.markdown("### ❄️ AI Winter Fashion Tips")
          

          with st.expander("💡 Click to View Winter AI Fashion Tips"):

             winter_tips = [
              "🧥 Layer your outfit with a premium wool coat.",
              "🧣 A cashmere scarf adds warmth and elegance.",
              "👢 Leather boots are perfect for winter fashion.",
              "🧤 Wear leather gloves to complete your luxury look.",
              "🤍 Neutral shades like black, grey, and camel are timeless."
          ]

             st.info(random.choice(winter_tips))
          st.write("Layer wool and cashmere pieces with leather boots for a timeless winter look.")
          st.success("✨ Pair a premium wool overcoat with a turtleneck, tailored trousers, and Chelsea boots for a refined winter luxury style.")
          st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
          with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended")
          occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
          st.write("📍 Occasion:", occasion) 
        
          st.markdown("### 🤖 AI Occasion Advice")

          if occasion == "💼 Office":
              st.warning("Choose clean tailoring and neutral colors for a professional appearance.")

          elif occasion == "🎉 Party":
             st.warning("Add bold ccessories and statement footwear to stand out.")

          elif occasion == "💍 Wedding":
             st.warning("Elegant fabrics and premium accessories create a refined wedding look.")

          elif occasion == "🛍️ Shopping":
              st.warning("Comfort comes first—choose breathable fabrics and comfortable footwear.")

          elif occasion == "☕ Casual Outing":
              st.warning("Keep your look relaxed yet stylish with simple luxury pieces.")

          elif occasion == "✈️ Travel":
              st.warning("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

          elif occasion == "❤️ Date Night":
              st.warning("Choose sophisticated colors and elegant accessories to make a lasting impression.")  
          st.markdown("### 📊 QUANTIQUE AI Fashion Score")

          col1, col2 = st.columns(2)

          with col1:
           st.metric("✨ Style Match", "98%")
           st.metric("👑 Luxury Level", "96%")

          with col2:
           st.metric("🌡️ Weather Match", "100%")
           st.metric("😊 Comfort", "98%")

          st.markdown("### 🔥 Trend Score")
          st.progress(96)
          st.markdown("### 🎨 AI Color Psychology")

          with st.expander("🎨 Color Psychology "):

           st.write("⚫ Black → Powerful and luxurious.")
           st.write("🤍 White → Clean and elegant.")
           st.write("🩶 Grey → Modern and professional.")
           st.write("🍷 Burgundy → Rich and premium.")
           st.write("🤎 Camel → Warm and timeless.")
          st.markdown("## 🛍️ Winter Women's Shopping Checklist")

          st.checkbox("🧥 Long Wool Coat")
          st.checkbox("🧶 Cashmere Sweater")
          st.checkbox("👖 Thermal Leggings")
          st.checkbox("👢 Knee High Boots")
          st.checkbox("🧣 Cashmere Scarf")
          st.checkbox("🧤 Leather Gloves")
          st.checkbox("👜 Designer Handbag")
          st.checkbox("💍 Minimal Jewelry") 
          st.markdown("## ⚖️ Compare Two Outfit Styles")
          compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

          compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
          if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
               

          if style == "🌿 Casual Chic":

            st.write("✨ Casual Styling")
            st.write("🤍 White Knit Sweater")
            st.write("👟 White Sneakers")
            if budget <= 8000:

             st.write("💰 Budget Collection")
             st.write("🛍️ Estimated Cost: ₹9,500")

            elif budget <= 10000:

             st.write("💎 Premium Collection")
             st.write("🛍️ Estimated Cost: ₹8,500")

            else:

              st.write("👑 Luxury Collection")
              st.write("🛍️ Estimated Cost: ₹16,500")


          elif style == "💼 Office Elegance":

            st.write("✨ Office Styling")
            st.write("🤍 Formal Blazer")
            st.write("👠 Classic Heels")
            if budget <= 7000:

             st.write("💰 Budget Collection")
             st.write("🛍️ Estimated Cost: ₹9,098")

            elif budget <= 20000:

              st.write("💎 Premium Collection")
              st.write("🛍️ Estimated Cost: ₹7,500")

            else:

             st.write("👑 Luxury Collection")
             st.write("🛍️ Estimated Cost: ₹90,500")

          elif style == "✨ Evening Glam":

            st.write("✨ Evening Styling")
            st.write("👗 Velvet Dress")
            st.write("💍 Diamond Earrings")

          elif style == "👑 Luxury Couture":

            st.write("✨ Luxury Styling")
            st.write("👑 Designer Gown")
            st.write("👜 Luxury Handbag")
            if budget <= 9000:

             st.write("💰 Budget Collection")
             st.write("🛍️ Estimated Cost: ₹4,500")

            elif budget <= 20000:

             st.write("💎 Premium Collection")
             st.write("🛍️ Estimated Cost: ₹8,500")

            else:

             st.write("👑 Luxury Collection")
             st.write("🛍️ Estimated Cost: ₹16,500")

        
        elif gender == "🤵 Men's Luxe":
           col1, col2 = st.columns(2)
           with col1:
              st.image(
             "c:/Users/simar/Desktop/fashion/photos/fashion10.jpg",
             width=250,
             caption="❄️ Winter Women's Collection"
          )
           with col2:
             st.write("🧥 Premium Wool Overcoat")
             st.write("👔 Black Turtleneck Sweater")
             st.write("👖 Tailored Wool Trousers")
             st.write("🥾 Chelsea Leather Boots")
             st.write("⌚ Luxury Chronograph Watch")
           st.markdown("### ⭐ Outfit Rating")
           st.write("9.9 / 10")

           st.markdown("### 🤖 Why QUANTIQUE Recommended This")

           st.write("✔ Elegant luxury winter look")
           st.write("✔ Warm and comfortable for cold weather")
           st.write("✔ Suitable for office and evening events")
           st.write("✔ Inspired by premium European fashion")

           st.markdown("### 🎨 Recommended Color Palette")

           st.write("⚫ Jet Black")
           st.write("🔵 Navy Blue")
           st.write("🩶 Charcoal Grey")
           st.write("🤎 Dark Brown")
           st.write("🤍 Ivory White")

           st.markdown("### 👔 Luxury Accessories")

           st.write("🧣 Cashmere Muffler")
           st.write("🧤 Leather Gloves")
           st.write("⌚ Luxury Watch")
           st.write("🎩 Wool Fedora Hat")
           st.write("💼 Leather Briefcase")

           st.markdown("### 💰 Estimated Outfit Cost")

           st.write("🧥 Premium Wool Overcoat : ₹24,000")
           st.write("👔 Black Turtleneck : ₹4,500")
           st.write("👖 Wool Trousers : ₹7,500")
           st.write("🥾 Chelsea Boots : ₹18,000")
           st.write("⌚ Luxury Watch : ₹28,000")

           st.markdown("---")

           st.markdown("## 💳 Total Estimated Cost : ₹82,000")

           st.markdown("### 🧺 Care Instructions")

           st.write("🧼 Dry clean the overcoat.")
           st.write("🥾 Polish leather boots regularly.")
           st.write("🧣 Hand wash the cashmere muffler.")
           st.write("⌚ Store the luxury watch in its case.")

           st.markdown("---")

           st.markdown("## 🎉 QUANTIQUE AI Final Summary")

           st.write("✔ Premium Men's Winter Collection")
           st.write("✔ Luxury Business & Evening Style")
           st.write("✔ Personalized AI Recommendation") 
           st.markdown("### 🎨 AI Color Psychology")

           with st.expander("🎨 Why These Colors?"):

            st.write("⚫ Black → Powerful and luxurious.")
            st.write("🤍 White → Clean and elegant.")
            st.write("🩶 Grey → Modern and professional.")
            st.write("🍷 Burgundy → Rich and premium.")
            st.write("🤎 Camel → Warm and timeless.")  
           st.markdown("---")

           st.markdown("## 💡 QUANTIQUE AI Fashion Tips")

           st.info("""
            ✔ Layer your outfit for a premium look.

            ✔ Keep accessories minimal and elegant.

            ✔ Match your shoes with your bag or belt.

            ✔ Choose neutral colors for a timeless luxury style.

            ✔ Confidence is the best fashion statement.
            """) 

           st.markdown("### ❄️ AI Winter Fashion Tips")

           with st.expander("💡 Click to View Winter AI Fashion Tips"):

             winter_men_tips = [
             "🧥 A wool overcoat is a winter wardrobe essential.",
             "🧣 Pair a turtleneck with a blazer for a premium look.",
             "🥾 Chelsea boots add elegance and warmth.",
             "⌚ A luxury watch enhances every winter outfit.",
             "🖤 Dark shades like black, navy, and charcoal create a sophisticated style."
          ]

             st.info(random.choice(winter_men_tips))

           st.write("Layer wool and cashmere pieces with leather boots for a timeless winter look.")
           st.markdown("### 📊 QUANTIQUE AI Fashion Score")

           col1, col2 = st.columns(2)

           with col1:
            st.metric("✨ Style Match", "98%")
            st.metric("👑 Luxury Level", "99%")

           with col2:
             st.metric("🌡️ Weather Match", "100%")
             st.metric("😊 Comfort", "96%")

           st.markdown("### 🔥 Trend Score")
           st.progress(97)
           st.success("❄️ Elevate your winter wardrobe with layered wool fabrics, leather boots, and timeless accessories for effortless elegance.")
           st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
           with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended")
           occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
           st.write("📍 Occasion:", occasion) 
        
           st.markdown("### 🤖 AI Occasion Advice")

           if occasion == "💼 Office":
              st.error("Choose clean tailoring and neutral colors for a professional appearance.")

           elif occasion == "🎉 Party":
             st.error("Add bold ccessories and statement footwear to stand out.")

           elif occasion == "💍 Wedding":
             st.error("Elegant fabrics and premium accessories create a refined wedding look.")

           elif occasion == "🛍️ Shopping":
              st.error("Comfort comes first—choose breathable fabrics and comfortable footwear.")

           elif occasion == "☕ Casual Outing":
              st.error("Keep your look relaxed yet stylish with simple luxury pieces.")

           elif occasion == "✈️ Travel":
              st.error("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

           elif occasion == "❤️ Date Night":
              st.error("Choose sophisticated colors and elegant accessories to make a lasting impression.")  
           st.markdown("## 🛍️ Winter Men's Shopping Checklist")

           st.checkbox("🧥 Wool Overcoat")
           st.checkbox("👕 Turtleneck Sweater")
           st.checkbox("👖 Wool Trousers")
           st.checkbox("👞 Chelsea Boots")
           st.checkbox("🧣 Wool Scarf")
           st.checkbox("⌚ Luxury Watch")
           st.checkbox("🧤 Leather Gloves")
           st.checkbox("🎒 Leather Backpack") 
           st.markdown("## ⭐ Customer Reviews")
           st.markdown("## ⚖️ Compare Two Outfit Styles")
           compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

           compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
           if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
               

           st.write("⭐⭐⭐⭐⭐  Emma: Loved the Winter Luxe recommendation!")
           st.write("⭐⭐⭐⭐⭐  James: Perfect outfit for office wear.")
           st.write("⭐⭐⭐⭐☆  Olivia: Beautiful color combinations.")
        
      elif season == "🌞 Summer Vibes":
        if gender ==  "👗 Women's Luxe":
          st.markdown("## 🌞 Summer Vibes Recommendation")
          st.success("🌞 QUANTIQUE AI has curated a fresh and breezy Summer look just for you!")
          col1, col2, col3 = st.columns(3)
          with col1:
           st.image("c:/Users/simar/Desktop/fashion/photos/fashion12.jpg", width=200)
         
          with col2:  
           st.image("c:/Users/simar/Desktop/fashion/photos/fahion12.6.jpg",width=200)
          with col3: 
           st.write("👗 Cotton Maxi Dress")
           st.write("👡 Comfortable Sandals")
           st.write("👜 Straw Handbag")
           st.write("🕶️ UV Protection Sunglasses")
           st.write("⌚ Minimal Watch")

          st.markdown("### ⭐ Outfit Rating")
          st.write("9.7 / 10")

          st.markdown("### 🤖 Why QUANTIQUE Recommended This")

          st.write("✔ Perfect for hot summer weather")
          st.write("✔ Lightweight and breathable fabrics")
          st.write("✔ Matches your selected style")
          st.write("✔ Comfortable for everyday wear")

          st.markdown("### 🎨 Recommended Color Palette")

          st.write("🤍 White")
          st.write("💙 Sky Blue")
          st.write("💛 Lemon Yellow")
          st.write("🌿 Mint Green")
          st.write("🩷 Peach")

          st.markdown("### 💰 Estimated Outfit Cost")

          st.write("👗 Cotton Dress : ₹6,000")
          st.write("👡 Sandals : ₹3,000")
          st.write("👜 Straw Handbag : ₹2,500")
          st.write("🕶️ Sunglasses : ₹2,000")
          st.write("⌚ Watch : ₹4,500")
          st.markdown("---")

          st.markdown("## 💳 Total Estimated Cost: ₹18,000")
          st.markdown("### 🎨 AI Color Psychology")

          with st.expander("🎨 Why These Colors?"):

           st.write("🤍 White → Keeps the outfit fresh and cool.")
           st.write("💙 Blue → Gives a relaxing summer vibe.")
           st.write("💛 Yellow → Bright and cheerful.")
           st.write("🩷 Peach → Soft and elegant.")
           st.write("🌿 Green → Natural and refreshing.")

          st.markdown("---")

          st.markdown("## 🎉 QUANTIQUE AI Final Summary")

          st.write("✔ Season: Summer Vibes")
          st.write("✔ Collection: Luxury")
          st.write("✔ Personalized for your selected style")
          st.write("✔ Recommended based on your budget")
          st.write("✔ Summer accessories included")
          st.write("✔ Fresh summer color palette selected")
         
          st.markdown("### 🌞 AI Summer Fashion Tips")

          with st.expander("💡 Click to View Summer AI Fashion Tips"):

             summer_tips = [
              "🌞 Choose breathable cotton and linen fabrics.",
              "👗 Wear light-colored outfits to stay cool.",
              "🕶️ Sunglasses protect your eyes and complete your look.",
              "👜 Carry a straw or canvas handbag for a fresh summer style.",
              "👡 Comfortable sandals are perfect for hot weather."
          ]

             st.info(random.choice(summer_tips))
          st.markdown("### 📊 QUANTIQUE AI Fashion Score")

          col1, col2 = st.columns(2)

          with col1:
            st.metric("✨ Style Match", "98%")
            st.metric("👑 Luxury Level", "96%")

          with col2:
            st.metric("🌡️ Weather Match", "100%")
            st.metric("😊 Comfort", "95%")

          st.markdown("### 🔥 Trend Score")
          st.progress(94)   
            

          st.success("🌴 Choose premium linen outfits, clean sneakers, and lightweight accessories to stay comfortable and effortlessly stylish this summer.")
          st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
          with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended")
          occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
          st.write("📍 Occasion:", occasion) 
        
          st.markdown("### 🤖 AI Occasion Advice")

          if occasion == "💼 Office":
              st.info("Choose clean tailoring and neutral colors for a professional appearance.")

          elif occasion == "🎉 Party":
             st.info("Add bold ccessories and statement footwear to stand out.")

          elif occasion == "💍 Wedding":
             st.info("Elegant fabrics and premium accessories create a refined wedding look.")

          elif occasion == "🛍️ Shopping":
              st.info("Comfort comes first—choose breathable fabrics and comfortable footwear.")

          elif occasion == "☕ Casual Outing":
              st.info("Keep your look relaxed yet stylish with simple luxury pieces.")

          elif occasion == "✈️ Travel":
              st.info("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

          elif occasion == "❤️ Date Night":
              st.info("Choose sophisticated colors and elegant accessories to make a lasting impression.")  
          st.markdown("## 🛍️ Summer Women's Shopping Checklist")

          st.checkbox("👗 Cotton Maxi Dress")
          st.checkbox("👡 Flat Sandals")
          st.checkbox("👜 Straw Handbag")
          st.checkbox("🕶️ UV Sunglasses")
          st.checkbox("🧴 Sunscreen")
          st.checkbox("⌚ Minimal Watch")
          st.checkbox("👒 Sun Hat")
          st.checkbox("💄 Lip Balm")  
          st.markdown("## ⚖️ Compare Two Outfit Styles")
          compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

          compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
          if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
          st.button("💳 Buy Now")         
               
         
        elif gender == "🤵 Men's Luxe":

          st.markdown("## 🌞 Summer Men's Luxe Recommendation")

          st.success("🌞 QUANTIQUE AI has selected a premium Summer outfit for a fresh and stylish look!")

          col1, col2, col3 = st.columns(3)

          with col1:
            st.image(
            "c:/Users/simar/Desktop/fashion/photos/fashion16.jpg",
            width=200,
            caption="🌞 Summer Men's Collection"
          )
          with col2:
            st.image(
            "c:/Users/simar/Desktop/fashion/photos/fashion16.1.jpg",
            width=200,
            caption="🌞 Summer Men's Collection"
          )
            

          with col3:

            st.markdown("### 🤵 Outfit Details")
 
            st.write("👕 Premium Linen Shirt")
            st.write("👖 Beige Chino Pants")
            st.write("👟 White Leather Sneakers")
            st.write("⌚ Smart Watch")
            st.write("🕶️ Polarized Sunglasses")

          st.markdown("### ⭐ Outfit Rating")
          st.write("9.8 / 10")

          st.markdown("### 🤖 Why QUANTIQUE Recommended This")

          st.write("✔ Lightweight premium fabrics")
          st.write("✔ Perfect for hot weather")
          st.write("✔ Comfortable luxury style")
          st.write("✔ Vacation & travel ready")

          st.markdown("### 🎨 Recommended Color Palette")

          st.write("🤍 White")
          st.write("💙 Sky Blue")
          st.write("🟤 Beige")
          st.write("🌿 Olive Green")
          st.write("⚪ Cream")
          
          st.markdown("### 🎨 AI Color Psychology")

          with st.expander("🎨 Why These Colors?"):

           st.write("🤍 White → Keeps the outfit fresh and cool.")
           st.write("💙 Blue → Gives a relaxing summer vibe.")
           st.write("💛 Yellow → Bright and cheerful.")
           st.write("🩷 Peach → Soft and elegant.")
           st.write("🌿 Green → Natural and refreshing.")


          st.markdown("### 👔 Luxury Accessories")

          st.write("⌚ Smart Watch")
          st.write("🧢 Premium Cap")
          st.write("🕶️ Sunglasses")
          st.write("🎒 Leather Backpack")
          st.write("👞 Loafers")

          st.markdown("### 💰 Estimated Outfit Cost")

          st.write("👕 Linen Shirt : ₹6,500")
          st.write("👖 Chino Pants : ₹5,500")
          st.write("👟 Sneakers : ₹9,000")
          st.write("⌚ Smart Watch : ₹18,000")
          st.write("🕶️ Sunglasses : ₹6,000")

          st.markdown("## 💳 Total Estimated Cost : ₹45,000")

          st.markdown("### 🧺 Care Instructions")

          st.write("🧼 Wash linen shirt gently.")
          st.write("👟 Clean sneakers with a soft brush.")
          st.write("🕶️ Store sunglasses in a protective case.")
          st.write("⌚ Avoid water exposure for the watch.")

          st.markdown("---")

          st.markdown("## 🎉 QUANTIQUE AI Final Summary")

          st.write("✔ Premium Summer Collection")
          st.write("✔ Men's Luxury Style")
          st.write("✔ Personalized AI Recommendation") 
          st.markdown("### 🌞 AI Summer Fashion Tips")

          with st.expander("💡 Click to View Summer AI Fashion Tips"):

             summer_men_tips = [
             "👕 Linen shirts keep you cool and stylish.",
             "👟 White sneakers match almost every summer outfit.",
             "🕶️ Wear polarized sunglasses for sunny days.",
             "⌚ Keep accessories simple with a premium watch.",
             "🌿 Light colors like white, beige, and sky blue work best in summer."
          ]

             st.info(random.choice(summer_men_tips))
          
          
          st.markdown("### 📊 QUANTIQUE AI Fashion Score")

          col1, col2 = st.columns(2)

          with col1:
            st.metric("✨ Style Match", "98%")
            st.metric("👑 Luxury Level", "99%")

          with col2:
            st.metric("🌡️ Weather Match", "100%")
            st.metric("😊 Comfort", "96%")

          st.markdown("### 🔥 Trend Score")
          st.progress(97)
          st.success("🌴 Choose premium linen outfits, clean sneakers, and lightweight accessories to stay comfortable and effortlessly stylish this summer.")
          st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
          with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended")
          occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
          st.write("📍 Occasion:", occasion) 
        
          st.markdown("### 🤖 AI Occasion Advice")

          if occasion == "💼 Office":
              st.warning("Choose clean tailoring and neutral colors for a professional appearance.")

          elif occasion == "🎉 Party":
             st.warning("Add bold ccessories and statement footwear to stand out.")

          elif occasion == "💍 Wedding":
             st.warning("Elegant fabrics and premium accessories create a refined wedding look.")

          elif occasion == "🛍️ Shopping":
              st.warning("Comfort comes first—choose breathable fabrics and comfortable footwear.")

          elif occasion == "☕ Casual Outing":
              st.warning("Keep your look relaxed yet stylish with simple luxury pieces.")

          elif occasion == "✈️ Travel":
              st.warning("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

          elif occasion == "❤️ Date Night":
              st.warning("Choose sophisticated colors and elegant accessories to make a lasting impression.")  

          st.markdown("## 🛍️ Summer Men's Shopping Checklist")

          st.checkbox("👕 Premium Linen Shirt")
          st.checkbox("🩳 Cotton Shorts")
          st.checkbox("👟 White Sneakers")
          st.checkbox("🕶️ Polarized Sunglasses")
          st.checkbox("⌚ Smart Watch")
          st.checkbox("🧢 Summer Cap")
          st.checkbox("🎒 Lightweight Backpack")
          st.checkbox("🧴 Sunscreen")
          st.markdown("## ⚖️ Compare Two Outfit Styles")
          compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

          compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
          if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
          st.button("👑 Own This Look")     

        

     

      elif season == "🌸 Spring Bloom":
        if gender == "👗 Women's Luxe":  
          st.markdown("## 🌸 Spring Bloom Recommendation")

          st.success("🌸 Soft pastel colors create a fresh and graceful spring look.")
          col1, col2, col3 = st.columns(3)
          with col1:
           st.image("c:/Users/simar/Desktop/fashion/photos/spring girl2.jpg", width=600)
          with col2:
           st.image("c:/Users/simar/Desktop/fashion/photos/spring girl.jpg", width=300)
          with col3:
             st.write("🌸 Floral Dress")
             st.write("👟 White Sneakers")
             st.write("👜 Crossbody Bag")
             st.write("🕶️ Sunglasses")

          st.markdown("### 🎨 Recommended Color Palette")

          st.write("🩷 Blush Pink" )
          st.write("💜 Lavender")
          st.write("🌿 Mint Green")    
          st.write("🤍 White")
          st.write("🌼 Soft Yell0w")

          st.markdown("### 👜 Perfect Accessories")

          st.write("👜 Crossbody Bag")
          st.write("⌚ Elegant Watch")
          st.write("🕶️ Sunglasses")
          st.write("🌸 Floral Hair Clip")
          st.write("👒 Sun Hat")
          st.markdown("### 💰 Estimated Outfit Cost")

          st.write("👗 Floral Dress : ₹5,500")
          st.write("👟 White Sneakers : ₹4,000")
          st.write("👜 Crossbody Bag : ₹3,500")
          st.write("🌼 Light Cardigan : ₹2,500")
          st.write("🕶️ Sunglasses : ₹2,000")

          st.markdown("---")

          st.markdown("## 💳 Total Estimated Cost: ₹17,500")
          st.markdown("### 🎨 AI Color Psychology")

          with st.expander("🎨 Why These Colors?"):

            st.write("🌸 Pink → Feminine and cheerful.")
            st.write("💙 Sky Blue → Calm and refreshing.")
            st.write("🌿 Mint Green → Fresh and youthful.")
            st.write("🤍 White → Pure and elegant.")
            st.write("💛 Yellow → Optimistic and energetic.")
          st.markdown("---")

          st.markdown("## 🎉 QUANTIQUE AI Final Summary")

          st.write("✔ Season: Spring Bloom")
          st.write("✔ Fresh pastel color combination")
          st.write("✔ Comfortable everyday outfit")
          st.write("✔ Personalized recommendation")
          st.write("✔ Accessories included")
          st.markdown("###🪻 AI Spring Lavender Fashion Tips")

          with st.expander("💡 Click to View Spring AI Fashion Tips"):

            spring_tips = [
              "🌸 Wear pastel shades like blush pink, lavender, and mint green.",
             "👗 Floral dresses are perfect for creating a fresh spring look.",
             "🧥 Carry a lightweight denim jacket for cool mornings.",
             "👟 White sneakers add comfort while keeping your outfit stylish.",
             "👜 Choose a soft-colored handbag to complete your spring outfit.",
             "🌿 Prefer breathable fabrics like cotton and linen.",
             "💎 Keep accessories minimal for an elegant luxury style.",
             "🌞 Add stylish sunglasses for sunny spring days.",
             "🎀 Delicate jewelry adds a graceful finishing touch.",
             "✨ Confidence is your best fashion accessory."
          ]

            st.info(random.choice(spring_tips))

      
           
          st.write("Pastel colors and floral prints create a fresh, elegant spring outfit.")
          st.success("🌸 Refresh your wardrobe with soft pastel tones, lightweight fabrics, and elegant accessories for a graceful spring appearance.")
          st.markdown("### 📊 QUANTIQUE AI Fashion Score")

          col1, col2 = st.columns(2)

          with col1:
            st.metric("✨ Style Match", "98%")
            st.metric("👑 Luxury Level", "99%")

          with col2:
            st.metric("🌡️ Weather Match", "100%")
            st.metric("😊 Comfort", "96%")

          st.markdown("### 🔥 Trend Score")
          st.progress(93)
          st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
          with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended")
          occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
          st.write("📍 Occasion:", occasion) 
        
          st.markdown("### 🤖 AI Occasion Advice")

          if occasion == "💼 Office":
              st.warning("Choose clean tailoring and neutral colors for a professional appearance.")

          elif occasion == "🎉 Party":
             st.warning("Add bold ccessories and statement footwear to stand out.")

          elif occasion == "💍 Wedding":
             st.warning("Elegant fabrics and premium accessories create a refined wedding look.")

          elif occasion == "🛍️ Shopping":
              st.warning("Comfort comes first—choose breathable fabrics and comfortable footwear.")

          elif occasion == "☕ Casual Outing":
              st.warning("Keep your look relaxed yet stylish with simple luxury pieces.")

          elif occasion == "✈️ Travel":
              st.warning("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

          elif occasion == "❤️ Date Night":
              st.warning("Choose sophisticated colors and elegant accessories to make a lasting impression.")  
          st.markdown("## 🛍️ Spring Shopping Checklist")

          st.checkbox("🌸 Floral Dress / Shirt")
          st.checkbox("👖 Light Denim Jeans")
          st.checkbox("👟 White Sneakers")
          st.checkbox("👜 Crossbody Bag")
          st.checkbox("🕶️ Sunglasses")
          st.checkbox("⌚ Minimal Watch")
          st.checkbox("🌼 Lightweight Cardigan")
          st.checkbox("🎀 Hair Accessories")  
          st.markdown("## ⚖️ Compare Two Outfit Styles")
          compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

          compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
          if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
          st.button("👑 Own This Look")     
         

        elif gender == "🤵 Men's Luxe":

          st.markdown("## 🌸 Spring Men's Luxe Recommendation")
          st.success("🌸 QUANTIQUE AI has selected a sophisticated Spring outfit for a fresh and modern look!")

          col1, col2, col3 = st.columns(3)

          with col1:
           st.image(
            "c:/Users/simar/Desktop/fashion/photos/spring men.jpg",
            width=200,
            caption="🌸 Spring Men's Collection"
            )
          with col2:
            st.image(
            "c:/Users/simar/Desktop/fashion/photos/springmen2.jpg",
            width=200,
            caption="🌸 Spring Men's Collection"
            )

          with col3:

           st.markdown("### 🤵 Outfit Details")

           st.write("👕 Premium Linen Shirt")
           st.write("👖 Tailored White Trousers")
           st.write("👟 White Leather Sneakers")
           st.write("⌚ Luxury Watch")
           st.write("🕶️ Classic Sunglasses")

          st.markdown("### ⭐ Outfit Rating")
          st.write("9.9 / 10")

          st.markdown("### 🤖 Why QUANTIQUE Recommended This")

          st.write("✔ Perfect for pleasant spring weather")
          st.write("✔ Lightweight premium fabrics")
          st.write("✔ Modern luxury styling")
          st.write("✔ Ideal for brunches, vacations, and casual outings")

          st.markdown("### 🎨 Recommended Color Palette")

          st.write("🌿 Sage Green")
          st.write("🤍 Ivory White")
          st.write("🩶 Light Grey")
          st.write("🌤️ Sky Blue")
          st.write("🤎 Beige")

          st.markdown("### 👔 Luxury Accessories")

          st.write("⌚ Premium Watch")
          st.write("🕶️ Designer Sunglasses")
          st.write("🎒 Leather Backpack")
          st.write("🧢 Linen Cap")
          st.write("👞 Loafers")

          st.markdown("### 💰 Estimated Outfit Cost")

          st.write("👕 Premium Linen Shirt : ₹6,500")
          st.write("👖 Tailored White Trousers : ₹7,500")
          st.write("👟 White Leather Sneakers : ₹8,500")
          st.write("⌚ Luxury Watch : ₹18,000")
          st.write("🕶️ Designer Sunglasses : ₹5,500")

          st.markdown("---")

          st.markdown("## 💳 Total Estimated Cost : ₹46,000")

          st.markdown("### 🧺 Care Instructions")

          st.write("🧼 Wash linen shirt in cold water.")
          st.write("👖 Dry clean tailored trousers for best results.")
          st.write("👟 Clean sneakers with a soft cloth.")
          st.write("🕶️ Keep sunglasses in a protective case.")
          st.markdown("### 🎨 AI Color Psychology")

          with st.expander("🎨 Why These Colors?"):

            st.write("🌸 Pink → Feminine and cheerful.")
            st.write("💙 Sky Blue → Calm and refreshing.")
            st.write("🌿 Mint Green → Fresh and youthful.")
            st.write("🤍 White → Pure and elegant.")
            st.write("💛 Yellow → Optimistic and energetic.")

          st.markdown("---")

          st.markdown("## 🎉 QUANTIQUE AI Final Summary")

          st.write("✔ Premium Spring Collection")
          st.write("✔ Men's Luxury Style")
          st.write("✔ Personalized AI Recommendation")
          st.write("✔ Fresh spring color palette")
          st.write("✔ Luxury accessories included")

          st.markdown("### 🌸 Enjoy Your Spring Look!")

          st.write("Step into spring with confidence, comfort, and timeless elegance.")
          st.markdown("### 🌿 AI Spring Fresh Fashion Tips")
          with st.expander("💡 Get AI Fashion Tip"):

            spring_tips = [
              "🌸 Wear pastel shades for a fresh spring look.",
              "🧥 A light denim jacket is perfect for cool mornings.",
              "👟 Comfortable sneakers are ideal for spring walks.",
              "👜 Choose soft-colored handbags for an elegant style.",
              "🌿 Floral prints always complement the spring season."
          ]
            st.info(random.choice(spring_tips))

          st.write("Choose breathable fabrics like linen and light cotton, and pair pastel colors with neutral accessories for a refined spring look.")  
          st.markdown("### 📊 QUANTIQUE AI Fashion Score")
          
          col1, col2 = st.columns(2)

          with col1:
            st.metric("✨ Style Match", "97%")
            st.metric("👑 Luxury Level", "98%")

          with col2:
            st.metric("🌡️ Weather Match", "100%")
            st.metric("😊 Comfort", "99%")

          st.markdown("### 🔥 Trend Score")
          st.progress(95)
          st.warning("🌿 Combine lightweight jackets, breathable shirts, and smart loafers for a fresh and sophisticated spring look.")
          
          st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
          with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended") 
          occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
          st.write("📍 Occasion:", occasion) 
        
          st.markdown("### 🤖 AI Occasion Advice")

          if occasion == "💼 Office":
              st.success("Choose clean tailoring and neutral colors for a professional appearance.")

          elif occasion == "🎉 Party":
             st.success("Add bold ccessories and statement footwear to stand out.")

          elif occasion == "💍 Wedding":
             st.success("Elegant fabrics and premium accessories create a refined wedding look.")

          elif occasion == "🛍️ Shopping":
              st.success("Comfort comes first—choose breathable fabrics and comfortable footwear.")

          elif occasion == "☕ Casual Outing":
              st.success("Keep your look relaxed yet stylish with simple luxury pieces.")

          elif occasion == "✈️ Travel":
              st.success("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

          elif occasion == "❤️ Date Night":
              st.success("Choose sophisticated colors and elegant accessories to make a lasting impression.")
           
          st.markdown("## 🛍️ Spring Shopping Checklist")

          st.checkbox("🌸 Floral Dress / Shirt")
          st.checkbox("👖 Light Denim Jeans")
          st.checkbox("👟 White Sneakers")
          st.checkbox("👜 Crossbody Bag")
          st.checkbox("🕶️ Sunglasses")
          st.checkbox("⌚ Minimal Watch")
          st.checkbox("🌼 Lightweight Cardigan")
          st.checkbox("🎀 Hair Accessories")    
          st.markdown("## ⚖️ Compare Two Outfit Styles")
          compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

          compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
          if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
          st.button("✨ Purchase Luxury Outfit")       
                

      elif season == "🍁 Autumn Muse":

        if gender == "👗 Women's Luxe":

         st.markdown("## 🍁 Autumn Muse Recommendation")

         st.success("🍁 QUANTIQUE AI has crafted a warm and sophisticated Autumn ensemble for you!")
         col1, col2, col3 = st.columns(3)

         with col1:
          st.image(
            "c:/Users/simar/Desktop/fashion/photos/autumgirl.jpg",
            width=200,
            caption="🍁 Autumn Women's Collection"
         )
         with col2:
            st.image(
            "c:/Users/simar/Desktop/fashion/photos/autumG2.jpg",
            width=200,
            caption="🍁 Autumn Women's Collection"
         )

         with col3:

          st.markdown("### 👗 Outfit Details")

          st.write("🧥 Camel Trench Coat")
          st.write("🤎 Beige Turtleneck Sweater")
          st.write("👖 Dark Brown Trousers")
          st.write("👢 Leather Ankle Boots")
          st.write("👜 Premium Leather Handbag")

         st.markdown("### ⭐ Outfit Rating")
         st.write("9.9 / 10")

         st.markdown("### 🤖 Why QUANTIQUE Recommended This")

         st.write("✔ Perfect for cool autumn weather")
         st.write("✔ Warm layered styling")
         st.write("✔ Elegant luxury appearance")
         st.write("✔ Inspired by European autumn fashion")

         st.markdown("### 🎨 Recommended Color Palette")

         st.write("🤎 Camel")
         st.write("🧡 Burnt Orange")
         st.write("🍂 Rust Brown")
         st.write("🟫 Chocolate Brown")
         st.write("🤍 Cream")

         st.markdown("### 👜 Luxury Accessories")

         st.write("👜 Leather Handbag")
         st.write("🧣 Wool Scarf")
         st.write("⌚ Gold Watch")
         st.write("🕶️ Sunglasses")
         st.write("🍁 Felt Hat")

         st.markdown("### 💰 Estimated Outfit Cost")

         st.write("🧥 Trench Coat : ₹16,000")
         st.write("🤎 Sweater : ₹5,000")
         st.write("👖 Trousers : ₹6,500")
         st.write("👢 Leather Boots : ₹12,000")
         st.write("👜 Leather Handbag : ₹18,000")

         st.markdown("---")

         st.markdown("## 💳 Total Estimated Cost : ₹57,500")

         st.markdown("### 🧺 Care Instructions")

         st.write("🧼 Dry clean the trench coat.")
         st.write("🧣 Hand wash the wool scarf.")
         st.write("👢 Polish leather boots regularly.")
         st.write("👜 Store the handbag in a dust bag.")
         st.markdown("### 🎨 AI Color Psychology")

         with st.expander("🎨 Why These Colors?"):

           st.write("🤎 Brown → Represents stability, warmth, and confidence.")
           st.write("🧡 Burnt Orange → Symbolizes energy and creativity.")
           st.write("🤍 Cream → Adds elegance and softness.")
           st.write("🌿 Olive Green → Reflects nature and sophistication.")
           st.write("🟫 Chocolate Brown → Creates a luxurious autumn appearance.")

         st.markdown("---")

         st.markdown("## 🎉 QUANTIQUE AI Final Summary")

         st.write("✔ Premium Autumn Collection")
         st.write("✔ Women's Luxury Style")
         st.write("✔ Personalized AI Recommendation")
         st.write("✔ Warm autumn color palette")
         st.write("✔ Luxury accessories included")

         st.markdown("### 🍁 Enjoy Your Autumn Look!")

         st.write("Stay elegant, warm, and fashionable throughout the autumn season.")
         with st.expander("💡 Get AI Fashion Tip"):

           tips = [
           "🍁 Layer light and heavy fabrics for perfect autumn comfort.",
           "👢 Leather boots pair beautifully with trench coats.",
           "🧣 A scarf can completely transform your outfit.",
           "🎨 Earthy colors create a timeless luxury look.",
           "👜 Choose neutral accessories to match every outfit.",
           "✨ Confidence is the best fashion accessory."
          ]

           st.info(random.choice(tips))
       
           st.write("Layer neutral shades with warm earthy colors to create a timeless autumn luxury look.")
         st.markdown("### 📊 QUANTIQUE AI Fashion Score")

         col1, col2 = st.columns(2)
         with col1:
            st.metric("✨ Style Match", "98%")
            st.metric("👑 Luxury Level", "99%")

         with col2:
            st.metric("🌡️ Weather Match", "100%")
            st.metric("😊 Comfort", "96%")

         st.markdown("### 🔥 Trend Score")
         st.progress(97)
         st.markdown("### 📈 AI Evaluation")

         st.write("🌡️ Weather Compatibility")
         st.progress(100)

         st.write("🎨 Color Harmony")
         st.progress(98)

         st.write("👔 Style Match")
         st.progress(97)

         st.write("😊 Comfort")
         st.progress(95)

         st.write("🔥 Fashion Trend")
         st.progress(96)
         st.warning("🍁 Layer warm earthy tones with elegant trench coats and leather accessories to create a timeless autumn luxury look.")
         st.markdown("### 🤖 QUANTIQUE AI Style Analysis")

         with st.expander("📋 View AI Analysis"):

          st.write("✔ Style Match : Excellent")
          st.write("✔ Comfort Level : High")
          st.write("✔ Luxury Rating : Premium")
          st.write("✔ Seasonal Match : Perfect")
          st.write("✔ Color Coordination : Excellent")
          st.write("✔ Trend Status : Trending in 2026")
          st.write("✔ Occasion Match : Highly Recommended") 
         occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
         st.write("📍 Occasion:", occasion) 
        
         st.markdown("### 🤖 AI Occasion Advice")

         if occasion == "💼 Office":
              st.info("Choose clean tailoring and neutral colors for a professional appearance.")

         elif occasion == "🎉 Party":
             st.info("Add bold ccessories and statement footwear to stand out.")

         elif occasion == "💍 Wedding":
             st.info("Elegant fabrics and premium accessories create a refined wedding look.")

         elif occasion == "🛍️ Shopping":
              st.info("Comfort comes first—choose breathable fabrics and comfortable footwear.")

         elif occasion == "☕ Casual Outing":
              st.info("Keep your look relaxed yet stylish with simple luxury pieces.")

         elif occasion == "✈️ Travel":
              st.info("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

         elif occasion == "❤️ Date Night":
              st.info("Choose sophisticated colors and elegant accessories to make a lasting impression.")
         st.markdown("## 🛍️ Shopping Checklist")

         st.markdown("## 🛍️ Autumn Women's Shopping Checklist")

         st.checkbox("🧥 Camel Trench Coat")
         st.checkbox("🤎 Turtleneck Sweater")
         st.checkbox("👖 Brown Trousers")
         st.checkbox("👢 Leather Ankle Boots")
         st.checkbox("👜 Luxury Handbag")
         st.checkbox("🧣 Wool Scarf")
         st.checkbox("⌚ Gold Watch")
         st.checkbox("🍂 Felt Hat")
         st.markdown("## ⚖️ Compare Two Outfit Styles")
         compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

         compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
         if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
         st.button("💳 Buy Now")
              
                     
           

        elif gender == "🤵 Men's Luxe":

           st.markdown("## 🍁 Autumn Men's Luxe Recommendation")

           st.success("🍁 QUANTIQUE AI has selected a premium Autumn outfit for a stylish and comfortable look!")

           col1, col2, col3 = st.columns(3)

           with col1:
            st.image(
            "c:/Users/simar/Desktop/fashion/photos/autumbo2.jpg",
            width=200,
            caption="🍁 Autumn Men's Collection"
           )
           with col2:
            st.image(
            "c:/Users/simar/Desktop/fashion/photos/autumboy.jpg",
            width=200,
            caption="🍁 Autumn Men's Collection"
           )
           with col3:

            st.markdown("### 🤵 Outfit Details")

            st.write("🧥 Premium Suede Jacket")
            st.write("👕 Beige Knit Sweater")
            st.write("👖 Dark Brown Chinos")
            st.write("👞 Leather Chelsea Boots")
            st.write("⌚ Luxury Leather Watch")

            st.markdown("### ⭐ Outfit Rating")
            st.write("9.8 / 10")

           st.markdown("### 🤖 Why QUANTIQUE Recommended This")

           st.write("✔ Perfect for cool autumn weather")
           st.write("✔ Premium earthy color combination")
           st.write("✔ Comfortable luxury styling")
           st.write("✔ Ideal for everyday and evening wear")

           st.markdown("### 🎨 Recommended Color Palette")

           st.write("🤎 Chocolate Brown")
           st.write("🟤 Camel")
           st.write("🧡 Rust Orange")
           st.write("🌿 Olive Green")
           st.write("🖤 Black")

           st.markdown("### 👔 Luxury Accessories")

           st.write("⌚ Leather Strap Watch")
           st.write("🧣 Wool Scarf")
           st.write("🎒 Leather Backpack")
           st.write("🕶️ Sunglasses")
           st.write("👞 Chelsea Boots")

           st.markdown("### 💰 Estimated Outfit Cost")
           st.write("🧥 Suede Jacket : ₹15,000")
           st.write("👕 Knit Sweater : ₹6,000")
           st.write("👖 Chinos : ₹5,000")
           st.write("👞 Chelsea Boots : ₹10,000")
           st.write("⌚ Leather Watch : ₹12,000")
           st.markdown("### 🎨 AI Color Psychology")
 
           with st.expander("🎨 Why These Colors?"):

             st.write("🤎 Brown → Represents stability, warmth, and confidence.")
             st.write("🧡 Burnt Orange → Symbolizes energy and creativity.")
             st.write("🤍 Cream → Adds elegance and softness.")
             st.write("🌿 Olive Green → Reflects nature and sophistication.")
             st.write("🟫 Chocolate Brown → Creates a luxurious autumn appearance.")

           st.markdown("---")

           st.markdown("## 💳 Total Estimated Cost : ₹48,000")

           st.markdown("### 🧺 Care Instructions")

           st.write("🧼 Brush the suede jacket regularly.")
           st.write("👕 Fold knitwear instead of hanging it.")
           st.write("👞 Polish leather boots frequently.")
           st.write("⌚ Keep your leather watch away from water.")

           st.markdown("---")

           st.markdown("## 🎉 QUANTIQUE AI Final Summary")

           st.write("✔ Season: Autumn Muse")
           st.write("✔ Collection: Men's Luxe")
           st.write("✔ Personalized AI Recommendation")
           st.write("✔ Luxury accessories included")
           st.write("✔ Earth-tone color palette selected")

           st.markdown("### 🍁 Enjoy Your Autumn Look!")

           st.write("Stay elegant, warm, and fashionable throughout the autumn season.")
           with st.expander("💡 Get AI Fashion Tip"):

             tips = [
             "🍁 Layer light and heavy fabrics for perfect autumn comfort.",
             "👢 Leather boots pair beautifully with trench coats.",
             "🧣 A scarf can completely transform your outfit.",
             "🎨 Earthy colors create a timeless luxury look.",
             "✨ Confidence is the best fashion accessory."
           ]

             st.info(random.choice(tips))
           st.write("Layer neutral shades with warm earthy colors to create a timeless autumn luxury look.")
       
           st.markdown("### 📊 QUANTIQUE AI Fashion Score")

           col1, col2 = st.columns(2)

           with col1:
            st.metric("✨ Style Match", "98%")
            st.metric("👑 Luxury Level", "99%")

           with col2:
            st.metric("🌡️ Weather Match", "100%")
            st.metric("😊 Comfort", "96%")

            st.markdown("### 🔥 Trend Score")
            st.progress(97)
           st.error("🍂 Elevate your autumn style with suede jackets, knitwear, and Chelsea boots for a modern and sophisticated appearance.")
           st.markdown("### 🤖 QUANTIQUE AI Style Analysis")
      

           with st.expander("📋 View AI Analysis"):

            st.write("✔ Style Match : Excellent")
            st.write("✔ Comfort Level : High")
            st.write("✔ Luxury Rating : Premium")
            st.write("✔ Seasonal Match : Perfect")
            st.write("✔ Color Coordination : Excellent")
            st.write("✔ Trend Status : Trending in 2026")
            st.write("✔ Occasion Match : Highly Recommended") 
           occasion = st.selectbox(
             "📍 Select Occasion",
             [
                "💼 Office",
                "🎉 Party",
                "💍 Wedding",
                "🛍️ Shopping",
               "☕ Casual Outing",
               "✈️ Travel",
               "❤️ Date Night"
              ]
            ) 
           st.write("📍 Occasion:", occasion) 
        
           st.markdown("### 🤖 AI Occasion Advice")

           if occasion == "💼 Office":
              st.warning("Choose clean tailoring and neutral colors for a professional appearance.")

           elif occasion == "🎉 Party":
             st.warning("Add bold ccessories and statement footwear to stand out.")

           elif occasion == "💍 Wedding":
             st.warning("Elegant fabrics and premium accessories create a refined wedding look.")

           elif occasion == "🛍️ Shopping":
              st.warning("Comfort comes first—choose breathable fabrics and comfortable footwear.")

           elif occasion == "☕ Casual Outing":
              st.warning("Keep your look relaxed yet stylish with simple luxury pieces.")

           elif occasion == "✈️ Travel":
              st.warning("Wear wrinkle-resistant fabrics and comfortable shoes for easy movement.")

           elif occasion == "❤️ Date Night":
              st.warning("Choose sophisticated colors and elegant accessories to make a lasting impression.")
           st.markdown("## 🛍️ Shopping Checklist")

           st.checkbox("🧥 Jacket / Coat")
           st.checkbox("👕 Sweater / Shirt")
           st.checkbox("👖 Pants")
           st.checkbox("👢 Shoes")
           st.checkbox("👜 Bag")
           st.checkbox("⌚ Watch")
           st.checkbox("🧣 Scarf") 
           st.markdown("## ⚖️ Compare Two Outfit Styles")
           compare1 = st.selectbox(
              "👗 Select First Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
               "👑 Luxury Couture"
              ],
               key="compare1"
           )

           compare2 = st.selectbox(
             "👗 Select Second Style",
              [
              "🌿 Casual Chic",
              "💼 Office Elegance",
              "✨ Evening Glam",
              "👑 Luxury Couture"
              ],
           key="compare2"
           )
           if st.button("⚖️ Compare Outfits"):
               st.markdown("## 📊 Outfit Comparison")

               col1, col2, = st.columns(2)

               with col1:
                st.subheader(compare1)
                st.metric("⭐ Luxury", "92%")
                st.metric("😊 Comfort", "95%")
                st.metric("💰 Budget", "₹45,000")

               with col2:
                 st.subheader(compare2)
                 st.metric("⭐ Luxury", "98%")
                 st.metric("😊 Comfort", "90%")
                 st.metric("💰 Budget", "₹65,000")
           st.button("👑 Own This Look")

elif page == "💎 My Luxury Wardrobe":

  st.title("💎 My Luxury Wardrobe")

  st.markdown("""
  ### ✨ Welcome Back, Simran!

  ## **Discover. Curate. Shine.**

  Your AI-powered fashion companion for timeless luxury.
  """)

  st.divider()      
    # ================= PREMIUM CARDS =================

  card1, card2, card3, card4 = st.columns(4)

  with card1:
     st.metric(
        label="👑 Wardrobe Score",
        value="94%",
        delta="Luxury Icon"
     )

  with card2:
      st.metric(
        label="❤️ Saved Looks",
        value="156",
        delta="In your wardrobe"
     )

  with card3:
      st.metric(
        label="⭐ Style Match",
        value="98%",
        delta="AI Accuracy"
    )
      

  with card4:
     st.metric(
        label="🧬 Style DNA",
        value="Elegant",
        delta="Luxury"
     )           
  st.divider()

  st.subheader("✨ Today's Signature Look")

  left, right = st.columns([1.2,1])

  with left:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/wardrob.jpg",
        use_container_width=True
    )

  with right:

    st.markdown("## summer lookbook")

    st.write("Elegant winter outfit with timeless essentials.")

    st.write("✔ Premium Fabric")

    st.write("✔ Luxury Finish")

    st.write("✔ AI Recommended")

    st.button("❤️ Save to Wardrobe")   
  st.divider()

  st.subheader("💎 Your Luxury Collection")

  col1, col2, col3, col4, col5, col6 = st.columns(6)

  with col1:
      st.image("c:/Users/simar/Desktop/fashion/photos/dresses.jpg", use_container_width=True)
      st.markdown("### 👗 Dresses")
      st.caption("Luxury gowns, cocktail dresses & timeless couture.")

      st.button("✨ Explore", key="dress")

  with col2:
      st.image("c:/Users/simar/Desktop/fashion/photos/heels 2.jpg", use_container_width=True)
      st.markdown("### 👠shoes")
      st.caption("Premium heels, sneakers & designer footwear.")

      st.button("✨ Explore", key="shoes")

  with col3:
      st.image("c:/Users/simar/Desktop/fashion/photos/beg3.jpg", use_container_width=True)
      st.markdown("### 👜 Bags")
      st.caption("Elegant handbags, totes & luxury clutches.")

      st.button("✨ Explore", key="bags")
      

  with col4:
      st.image("c:/Users/simar/Desktop/fashion/photos/watch.jpg", use_container_width=True)
      st.markdown("### ⌚ Watches")
      st.caption("Luxury watches for timeless elegance.")

      st.button("✨ Explore", key="watch") 
      
  with col5:
      st.image("c:/Users/simar/Desktop/fashion/photos/jewerly.jpg", use_container_width=True)
      st.markdown("### 💍 Jewellery")
      st.caption("Necklaces, earrings & premium accessories.")

      st.button("✨ Explore", key="jewellery")
      
  with col6:
      st.image("c:/Users/simar/Desktop/fashion/photos/permiun.jpg", use_container_width=True)
      st.markdown("### 💎 Premium")
      st.caption("Exclusive luxury collection for every season.")

      st.button("✨ Explore", key="premium")
      # ================= MY WISHLIST =================

  st.divider()

  st.subheader("❤️ My Luxury Wishlist")

# ---------- First Item ----------
  col1, col2 = st.columns([1,2])

  with col1:
    st.image(
        "c:/Users/simar/Desktop/fashion/photos/dresses.jpg",
        use_container_width=True
    )

  with col2:

    st.markdown("### 👗 Black Satin Dress")

    st.write("⭐⭐⭐⭐⭐  (4.9/5)")

    st.write("💰 ₹8,499")

    st.write("Luxury evening dress with premium satin fabric.")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("👀 View", key="wish1"):
            st.markdown("#### 👗 Product Details")

            st.write("**Brand:** QUANTIQUE")

            st.write("**Material:** Premium Satin")

            st.write("**Color:** Midnight Black")

            st.write("**Sizes:** XS • S • M • L • XL")

            st.write("**Occasion:** Evening Party")

            st.write("**Luxury Rating:** ⭐⭐⭐⭐⭐")

            st.image(
                "c:/Users/simar/Desktop/fashion/photos/midnight.jpg",
                width=300
            )


    with c2:
        if st.button("🛒 Buy Now", key="buy1"):
            st.success("🛍 Added to Cart!")

            st.balloons()

            st.markdown("### Checkout Summary")

            st.write("👗 Black Satin Dress")

            st.write("💰 Price : ₹8,499")

            st.write("🚚 Free Delivery")

            st.write("🎁 Premium Gift Packaging Included")

  st.divider()

# ---------- Second Item ----------
  col1, col2 = st.columns([1,2])

  with col1:
    st.image(
        "c:/Users/simar/Desktop/fashion/photos/beg3.jpg",
        use_container_width=True
    )

  with col2:

    st.markdown("### 👜 Designer Handbag")

    st.write("⭐⭐⭐⭐⭐  (5.0/5)")

    st.write("💰 ₹45,999")

    st.write("Italian leather handbag from the premium collection.")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("👀 View", key="wish2"):
            st.markdown("#### 👜 Product Details")

            st.write("**Brand:** QUANTIQUE")

            st.write("**Material:** Genuine Italian Leather")

            st.write("**Color:**midnight black")

            st.write("**Size:** Medium")

            st.write("**Collection:** Premium Luxury")

            st.write("**Luxury Rating:** ⭐⭐⭐⭐⭐")

            st.image(
                "c:/Users/simar/Desktop/fashion/photos/bag.jpg",
                width=300
            )

    with c2:
        if st.button("🛒 Buy Now", key="buy2"):
            st.success("🛍 Added to Cart!")

            st.balloons()

            st.markdown("### Checkout Summary")

            st.write("👜 Designer Handbag")

            st.write("💰 Price : ₹45,999")

            st.write("🚚 Free Delivery")

            st.write("🎁 Premium Gift Packaging Included")

  st.divider()

# ---------- Third Item ----------
  col1, col2 = st.columns([1,2])

  with col1:
    st.image(
        "c:/Users/simar/Desktop/fashion/photos/watch.jpg",
        use_container_width=True
    )

  with col2:

    st.markdown("### ⌚ Luxury Watch")

    st.write("⭐⭐⭐⭐⭐  (4.8/5)")

    st.write("💰 ₹32,500")

    st.write("Minimal Swiss luxury watch.")

    c1, c2 = st.columns(2)

    with c1:
        if st.button("👀 View", key="wish3"):
            st.markdown("#### ⌚ Product Details")

            st.write("**Brand:** QUANTIQUE")

            st.write("**Movement:** Swiss Automatic")

            st.write("**Glass:** Sapphire Crystal")

            st.write("**Warranty:** 5 Years")

            st.write("**Water Resistance:** 100M")

            st.write("**Luxury Rating:** ⭐⭐⭐⭐⭐")

            st.image(
                "c:/Users/simar/Desktop/fashion/photos/watch for buy.png",
                width=300
            )

    with c2:
        if st.button("🛒 Buy Now", key="buy3"):
            st.success("🛍 Added to Cart!")

            st.balloons()

            st.markdown("### Checkout Summary")

            st.write("⌚ Luxury Watch")

            st.write("💰 Price : ₹32,500")

            st.write("🚚 Free Delivery")

            st.write("🎁 Premium Gift Packaging Included")


    st.divider()

  st.subheader("📊 Wishlist Summary")

  m1, m2, m3, m4 = st.columns(4)

  with m1:
    st.metric("❤️ Items", "3")

  with m2:
    st.metric("💰 Total Value", "₹86,998")

  with m3:
    st.metric("⭐ Luxury Score", "99%")

  with m4:
    st.metric("🔥 Most Wanted", "Handbag")

# ============================================================
# AI SHOPPING ADVICE
# ============================================================

  st.divider()

  st.subheader("🤖 QUANTIQUE AI Shopping Advice")

  st.success("""
  ✨ AI Recommendation

  Your wardrobe is almost complete.

  To create the perfect Luxury Capsule Collection,
  QUANTIQUE recommends adding:

  ✔ White Satin Blazer

  ✔ Beige High Heels

  ✔ Gold Bracelet

  ✔ Black Leather Belt

  These pieces will increase your Style Match to 100%.
  """)

  st.info("""
  💎 Shopping Tip

  Buy timeless pieces before trendy items.

  Luxury fashion is built around quality,
  not quantity.
  """)
 

  st.divider()

  st.markdown("## 🪞 Luxury style QUANTIQUE Aura Mirror")

  st.write("Discover your luxury personality for today.")

  mood = st.selectbox(
    "✨ How are you feeling today?",
    [
        "😊 Confident",
        "🌸 Elegant",
        "🔥 Bold",
        "💼 Professional",
        "💖 Romantic",
        "🌿 Relaxed"
    ]
  )

  if st.button("✨ Reveal My Luxury Identity"):

    st.balloons()

    if mood == "😊 Confident":

        st.success("👑 You are today's **Power Queen**")

        st.markdown("""
  ### Today's Signature Look

  🤍 White Blazer

  🖤 Black Trousers

  👠 Nude Luxury Heels

  👜 Leather Tote Bag

  ⌚ Gold Watch
  """)

        st.info("""
  💎 AI Advice

  Your confidence deserves timeless elegance.

  Luxury Score : 98%
  """)

    elif mood == "🌸 Elegant":

        st.success("🌸 You are today's **Old Money Muse**")

        st.markdown("""
  ### Today's Signature Look

  🤍 Satin Dress

  👠 Beige Heels

  👜 Pearl Handbag

  💍 Diamond Earrings

  ⌚ Silver Watch
  """)

        st.info("""
  💎 AI Advice

  Keep accessories minimal.

  Luxury Score : 99%
  """)

    elif mood == "🔥 Bold":

        st.success("🔥 You are today's **Fashion Icon**")

        st.markdown("""
  ### Today's Signature Look

  🖤 Black Leather Jacket

  👖 Premium Jeans

  👢 Luxury Boots

  👜 Designer Bag

  🕶 Black Sunglasses
  """)

        st.info("""
  💎 AI Advice

  Own every room you walk into.

  Luxury Score : 97%
  """)

    elif mood == "💼 Professional":

        st.success("💼 You are today's **Executive Elite**")

        st.markdown("""
  ### Today's Signature Look

  🤍 White Shirt

  🖤 Tailored Pants

  ⌚ Swiss Watch

  👜 Office Tote

  👞 Premium Shoes
  """)

        st.info("""
  💎 AI Advice

  Professional never goes out of style.

  Luxury Score : 96%
  """)

    elif mood == "💖 Romantic":

        st.success("💖 You are today's **Luxury Dreamer**")

        st.markdown("""
  ### Today's Signature Look

  🌸 Pink Satin Dress

  🤍 White Heels

  👜 Mini Luxury Bag

  💍 Rose Gold Jewellery

 🌷 Floral Perfume
  """)

        st.info("""
  💎 AI Advice

  Soft luxury creates unforgettable elegance.

  Luxury Score : 98%
  """)

    else:

        st.success("🌿 You are today's **Quiet Luxury Soul**")

        st.markdown("""
  ### Today's Signature Look

  🤎 Beige Sweater

  🤍 White Pants

  👟 Luxury Sneakers

  Brown Leather Bag

  ⌚ Minimal Watch
  """)

        st.info("""
  💎 AI Advice

  Luxury is simplicity.

  Luxury Score : 99%
  """)
# ============================================================
# 👑 QUANTIQUE LUXURY FASHION VAULT
# ============================================================

 

  st.divider()

  st.markdown("# 👑 QUANTIQUE Luxury Fashion Vault")

  st.caption("Unlock exclusive collections reserved for luxury members.")

  vault1, vault2, vault3 = st.columns(3)

# ================= COLLECTION 1 =================

  with vault1:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/ROYAL.jpg",
        use_container_width=True
    )

    st.markdown("### 👑 Royal Collection")
  

    st.write("⭐ Luxury Level : 5/5")

    if st.button("🔓 Preview", key="royal"):

        st.success("Royal Collection Unlocked")

        with st.expander("👑 View Collection"):

            st.write("💎 Collection : Royal Collection")

            st.write("🌤 Best Season : Winter")

            st.write("🎉 Occasion : Gala Dinner")

            st.write("🎨 Colors : Black • Gold • Ivory")

            st.write("💰 Price Range : ₹80,000 - ₹2,50,000")

            st.write("🤖 AI Recommendation : Perfect for luxury evenings.")

# ================= COLLECTION 2 =================

  with vault2:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/PARIS.jpg",
        use_container_width=True
    )

    st.markdown("### ✨ Paris Couture")

    st.write("⭐ Luxury Level : 5/5")

    if st.button("🔓 Preview", key="paris"):

        st.success("Paris Couture Opened")

        with st.expander("✨ View Collection"):

            st.write("🗼 Collection : Paris Couture")

            st.write("🌸 Best Season : Spring")

            st.write("🎉 Occasion : Fashion Show")

            st.write("🎨 Colors : Beige • White • Rose")

            st.write("💰 Price Range : ₹60,000 - ₹1,80,000")

            st.write("🤖 AI Recommendation : Elegant minimalist fashion.")

# ================= COLLECTION 3 =================

  with vault3:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/midnight elite.jpg",
        use_container_width=True
    )

    st.markdown("### 🌙 Midnight Elite")

    st.write("⭐ Luxury Level : 5/5")

    if st.button("🔓 Preview", key="midnight"):

        st.success("Midnight Elite Opened")

        with st.expander("🌙 View Collection"):

            st.write("🌙 Collection : Midnight Elite")

            st.write("🌃 Best Season : Autumn")

            st.write("🎉 Occasion : Luxury Party")

            st.write("🎨 Colors : Black • Silver • Navy")

            st.write("💰 Price Range : ₹1,00,000+")

            st.write("🤖 AI Recommendation : Bold luxury statement.")

# ============================================================
# MEMBERSHIP PROGRESS
# ============================================================

  st.divider()

  st.subheader("💎 Vault Membership Progress")

  st.progress(0.72)

  st.info("""
  👑 Diamond Member

  ✔ Royal Collection Unlocked

  ✔ Paris Couture Unlocked

  🔒 3 Exclusive Collections Remaining

  Unlock more collections by exploring QUANTIQUE.
  """)
elif page == "🌍 Fashion Passport":

  st.title("🌍 QUANTIQUE Fashion Passport")

  st.markdown("""
     ### Explore Luxury Fashion Around The World

      Travel through different countries,
      discover iconic fashion,
      unlock passport stamps,
      and become a Global Luxury Stylist.
       """)

  st.divider()

# ==========================================================
# PASSPORT HEADER
# ==========================================================

  left, right = st.columns([2,1])

  with left:

    st.image(
        "c:/users/simar/Downloads/ChatGPT Image Jul 14, 2026, 11_41_24 PM.png",
        use_container_width=True
    )

  with right:

    st.markdown("## 🛂 Your Passport")

    st.metric(
        "Countries Explored",
        "3 / 20"
    )

    st.progress(0.15)

    st.metric(
        "Passport Points",
        "12,450"
    )

    st.metric(
        "Current Rank",
        "Luxury Explorer"
    )

    st.button("📖 View Passport")

    st.divider()

# ==========================================================
# DESTINATION
# ==========================================================

  st.subheader("✈️ Choose Your Destination")

  st.caption("Select a country to explore its luxury fashion heritage.")
  row1 = st.columns(4)
  with row1[0]:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/india.jpg",
        use_container_width=True
    )

    st.markdown("### 🇮🇳 India")
    st.caption("The Land of Timeless Textiles")

    if "india_open" not in st.session_state:
        st.session_state.india_open = False

    if st.button("🌍 Start Journey", key="india"):
        st.session_state.india_open = not st.session_state.india_open

  if st.session_state.india_open:

    st.success("🇮🇳 Welcome to India's Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Jewellery",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    with tab1:
       st.markdown("## 🇮🇳 The Story of Indian Fashion")

       st.warning("""
       India has one of the world's oldest fashion traditions, dating back more than **5,000 years** to the Indus Valley Civilization.

       Ancient Indians were among the first people to cultivate cotton and create beautifully woven fabrics. Archaeological discoveries reveal that people wore finely crafted garments long before many other civilizations.

       During the **Mauryan and Gupta Empires**, clothing became a symbol of social status, with rich fabrics and intricate ornaments worn by royalty.

       The **Mughal Empire (16th–18th century)** transformed Indian fashion forever. Persian influences introduced luxurious silk, velvet, brocade, and gold zari embroidery. Outfits such as the **Lehenga**, **Sherwani**, and **Anarkali** became symbols of royal elegance.

       Over the centuries, each region of India developed its own unique textiles, including Banarasi Silk, Kanchipuram Silk, Chanderi, and Pashmina.

       Today, Indian fashion is celebrated worldwide for its craftsmanship, vibrant colors, embroidery, and luxury bridal couture.
      """)

    with tab2:
        st.info("👗 Saree")
        st.info("👑 Lehenga")
        st.info("🤵 Sherwani")
        st.info("🌸 Anarkali")
        st.info("👕 Kurta")

    with tab3:
        st.error("Banarasi Silk")
        st.error("Pashmina")
        st.error("Khadi")

    with tab4:
        st.warning("Kundan")
        st.warning("Polki")
        st.warning("Temple Jewellery")

    with tab5:
        st.info("Sabyasachi")
        st.info("Manish Malhotra")
        st.info("Ritu Kumar")

    with tab6:
        st.info("AI styling recommendations will appear here.")

 

  with row1[1]:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/fr.jpg",
        use_container_width=True
    )

    st.markdown("### 🇫🇷 France")

    st.caption("The Home of Haute Couture")

    if "france_open" not in st.session_state:
        st.session_state.france_open = False

    if st.button("🌍 Start Journey", key="france"):
        st.session_state.france_open = not st.session_state.france_open

  if st.session_state.france_open:

    st.success("🇫🇷 Welcome to French Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Jewellery",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of French Fashion")

        st.warning("""
France has been the global capital of fashion for over **400 years**.

The journey began during the reign of **King Louis XIV**, often called the
"Sun King." He believed clothing represented power, elegance, and wealth.
His magnificent Palace of Versailles became Europe's fashion center, where
nobles competed through luxurious garments.

During the 19th century, Paris introduced the concept of
**Haute Couture**, meaning garments were handcrafted exclusively
for individual clients using the finest fabrics.

Legendary designers such as **Coco Chanel**, **Christian Dior**,
**Yves Saint Laurent**, and **Hubert de Givenchy**
revolutionized women's fashion and luxury worldwide.

Today Paris Fashion Week remains the most prestigious fashion event
on Earth, attracting luxury brands and designers from around the globe.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.markdown("### 👗 Haute Couture Gown")
        st.info("""
Handcrafted luxury gowns made exclusively for wealthy clients.
Every piece is unique and requires hundreds of hours to create.
        """)

        st.markdown("### 👗 Little Black Dress")
        st.warning("""
Introduced by Coco Chanel in 1926, this elegant dress became one
of the most iconic garments in fashion history.
        """)

        st.markdown("### 👗 Parisian Blazer")
        st.error("""
French tailoring is known for sophisticated blazers that combine
comfort with timeless elegance.
        """)

        st.markdown("### 👗 Evening Gowns")
        st.success("""
Luxury evening gowns worn at royal events, fashion shows,
and international red carpet ceremonies.
        """)

        st.markdown("### 👗 Trench Coat")
        st.info("""
A timeless French-inspired outerwear piece admired for its
minimal elegance.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury French Fabrics")

        st.write("🧵 French Silk")
        st.write("🧵 Satin")
        st.write("🧵 Velvet")
        st.write("🧵 Lace")
        st.write("🧵 Organza")
        st.write("🧵 Chiffon")
        st.write("🧵 Brocade")

        st.info("""
       French luxury houses carefully select premium fabrics
      known for softness, elegance, and exceptional craftsmanship.
        """)

    # ======================================================
    # JEWELLERY
    # ======================================================

    with tab4:

        st.subheader("💎 French Luxury Jewellery")

        st.write("💎 Cartier")
        st.write("💎 Van Cleef & Arpels")
        st.write("💎 Boucheron")
        st.write("💎 Chaumet")
        st.write("💎 Diamond Necklaces")
        st.write("💎 Pearl Jewellery")
        st.write("💎 Luxury Watches")

        st.success("""
       France is home to some of the world's most prestigious
       luxury jewellery houses.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Legendary French Designers")

        st.write("👑 Coco Chanel")
        st.write("👑 Christian Dior")
        st.write("👑 Yves Saint Laurent")
        st.write("👑 Hubert de Givenchy")
        st.write("👑 Jean Paul Gaultier")
        st.write("👑 Pierre Cardin")
        st.write("👑 Louis Vuitton")

        st.info("""
       These designers transformed luxury fashion and continue
       to inspire modern designers across the world.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI French Style Guide")

        st.error("""
      ✨ Recommended Luxury Outfit

      👗 White Satin Dress

      🧥 Beige Parisian Blazer

      👠 Black High Heels

      👜 Louis Vuitton Handbag

      💎 Diamond Earrings

      ⌚ Luxury Watch

     💄 Classic Red Lipstick

     Perfect For:
     • Paris Fashion Week
     • Luxury Dinner
     • Business Gala
     • Wedding Reception
     • Red Carpet Events
        """)

        st.info("""
           🇫🇷 AI Fashion Tip

          French fashion is built around the philosophy that
        'elegance comes from simplicity.'

         Invest in timeless pieces, neutral colors, high-quality
          fabrics, and confidence rather than chasing trends.
           """)


  with row1[2]:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/japan.jpg",
        use_container_width=True
    )

    st.markdown("### 🇯🇵 Japan")

 
    st.caption("Tradition Meets Modern Innovation")

    if "japan_open" not in st.session_state:
        st.session_state.japan_open = False

    if st.button("🌍 Start Journey", key="japan"):
        st.session_state.japan_open = not st.session_state.japan_open

  if st.session_state.japan_open:

    st.success("🇯🇵 Welcome to Japanese Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Accessories",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of Japanese Fashion")

        st.error("""
Japanese fashion dates back over **1,000 years** and reflects the country's
deep respect for tradition, craftsmanship, and nature.

The **Kimono** became Japan's national dress during the Edo Period (1603–1868)
and was worn by samurai, nobles, merchants, and common people.

Traditional Japanese garments often featured seasonal motifs such as cherry blossoms,
cranes, bamboo, waves, and mountains.

During the Meiji Era, Japan adopted Western clothing while preserving its
traditional fashion heritage.

Today Japan is admired for blending timeless traditions with futuristic fashion,
making Tokyo one of the world's most influential fashion capitals.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.subheader("👗 Famous Japanese Traditional Dresses")

        st.markdown("### 👘 Kimono")
        st.warning("""
Japan's most iconic traditional garment made from luxurious silk and worn
during ceremonies, weddings, and festivals.
        """)

        st.markdown("### 👘 Yukata")
        st.info("""
A lightweight cotton version of the Kimono worn during summer festivals.
        """)

        st.markdown("### 👘 Hakama")
        st.warning("""
Traditional pleated trousers worn by samurai and martial artists.
        """)

        st.markdown("### 👘 Furisode")
        st.success("""
An elegant long-sleeved Kimono worn by unmarried women during celebrations.
        """)

        st.markdown("### 👘 Tomesode")
        st.error("""
A formal Kimono worn by married women at important ceremonies.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury Japanese Fabrics")

        st.write("🧵 Nishijin Silk")
        st.write("🧵 Chirimen Silk")
        st.write("🧵 Cotton")
        st.write("🧵 Hemp")
        st.write("🧵 Satin Silk")
        st.write("🧵 Brocade")
        st.write("🧵 Indigo Dyed Fabric")

        st.info("""
Japanese textiles are admired worldwide for their precision,
beautiful weaving techniques, and exceptional craftsmanship.
        """)

    # ======================================================
    # ACCESSORIES
    # ======================================================

    with tab4:

        st.subheader("💎 Traditional Accessories")

        st.write("💎 Kanzashi Hairpins")
        st.write("💎 Obi Belt")
        st.write("💎 Folding Fan")
        st.write("💎 Geta Sandals")
        st.write("💎 Zori Sandals")
        st.write("💎 Silk Handbags")
        st.write("💎 Decorative Hair Combs")

        st.success("""
Japanese accessories focus on elegance, balance, and harmony,
perfectly complementing traditional clothing.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Famous Japanese Designers")

        st.write("👑 Issey Miyake")
        st.write("👑 Yohji Yamamoto")
        st.write("👑 Rei Kawakubo")
        st.write("👑 Kenzo Takada")
        st.write("👑 Junya Watanabe")
        st.write("👑 Nigo")
        st.write("👑 Tadashi Shoji")

        st.info("""
Japanese designers are globally recognized for combining
minimalism, innovation, and artistic creativity.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI Japanese Style Guide")

        st.warning("""
✨ Recommended Luxury Outfit

👘 Elegant Silk Kimono

🎀 Embroidered Obi Belt

👡 Traditional Zori Sandals

💎 Kanzashi Hairpins

👜 Minimal Leather Handbag

⌚ Elegant Luxury Watch

Perfect For:
• Tea Ceremony
• Wedding
• Cultural Events
• Luxury Photoshoot
• Traditional Celebrations
        """)

        st.info("""
🇯🇵 AI Fashion Tip

Japanese fashion is built on simplicity,
balance, and attention to detail.

Choose soft colors, premium fabrics,
minimal accessories, and graceful silhouettes
for an authentic luxury Japanese look.
        """)


  with row1[3]:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/korean.jpg",
        use_container_width=True
    )

    st.markdown("### 🇰🇷 Korea")
 
    st.caption("Tradition Meets K-Fashion")

    if "korea_open" not in st.session_state:
        st.session_state.korea_open = False

    if st.button("🌍 Start Journey", key="korea"):
        st.session_state.korea_open = not st.session_state.korea_open

  if st.session_state.korea_open:

    st.success("🇰🇷 Welcome to Korean Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Accessories",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of Korean Fashion")

        st.info("""
Korean fashion has a rich history spanning over **2,000 years**.

The traditional **Hanbok** developed during the Three Kingdoms Period
and symbolizes grace, simplicity, and harmony.

Throughout the Joseon Dynasty (1392–1910), clothing reflected
social status, Confucian values, and Korean identity.

Modern Korea transformed into one of the world's fashion capitals
through K-pop, K-dramas, and Seoul Fashion Week.

Today South Korea blends traditional elegance with modern street fashion,
making it one of the fastest-growing fashion industries worldwide.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.subheader("👗 Famous Korean Traditional Dresses")

        st.markdown("### 👘 Hanbok")
        st.success("""
The national dress of Korea featuring flowing lines,
bright colours and elegant proportions.
        """)

        st.markdown("### 👗 Dangui")
        st.info("""
A traditional upper garment worn by noble women.
        """)

        st.markdown("### 👑 Wonsam")
        st.warning("""
Royal ceremonial dress worn by queens and princesses.
        """)

        st.markdown("### 👘 Durumagi")
        st.error("""
Traditional overcoat worn during colder seasons.
        """)

        st.markdown("### 👔 Jeogori")
        st.success("""
The upper jacket that forms the main part of Hanbok.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury Korean Fabrics")

        st.write("🧵 Korean Silk")
        st.write("🧵 Ramie Fabric")
        st.write("🧵 Hemp")
        st.write("🧵 Satin")
        st.write("🧵 Cotton")
        st.write("🧵 Embroidered Silk")
        st.write("🧵 Traditional Brocade")

        st.info("""
Traditional Korean fabrics are known for their soft texture,
beautiful colours, and exceptional craftsmanship.
        """)

    # ======================================================
    # ACCESSORIES
    # ======================================================

    with tab4:

        st.subheader("💎 Traditional Accessories")

        st.write("💎 Binyeo Hair Pin")
        st.write("💎 Norigae Ornament")
        st.write("💎 Beoseon Socks")
        st.write("💎 Embroidered Shoes")
        st.write("💎 Silk Hair Ribbon")
        st.write("💎 Decorative Fans")
        st.write("💎 Royal Hair Accessories")

        st.success("""
Accessories complete the beauty of Hanbok and
represent elegance and prosperity.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Famous Korean Designers")

        st.write("👑 Lie Sang Bong")
        st.write("👑 Juun.J")
        st.write("👑 Kim Seo Ryong")
        st.write("👑 Steve J & Yoni P")
        st.write("👑 Minju Kim")
        st.write("👑 Beyond Closet")
        st.write("👑 KYE")

        st.info("""
Korean designers are famous for combining
traditional culture with modern luxury fashion.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI Korean Style Guide")

        st.warning("""
✨ Recommended Luxury Outfit

👘 Modern Hanbok

👠 Elegant Heels

👜 Premium Mini Handbag

💎 Norigae Ornament

⌚ Luxury Watch

💄 Soft Korean Makeup

Perfect For:

• Cultural Festival

• Wedding

• Luxury Photoshoot

• Traditional Ceremony

• Fashion Event
        """)

        st.info("""
🇰🇷 AI Fashion Tip

Korean fashion focuses on clean silhouettes,
soft pastel colours, premium fabrics,
and minimal accessories.

Mixing traditional Hanbok elements with modern fashion
creates a timeless luxury look.
        """)
   
  row2 = st.columns(4)

  with row2[0]:

     st.image(
        "c:/Users/simar/Desktop/fashion/photos/ital.jpg",
        use_container_width=True
     )

     st.markdown("### 🇮🇹 Italy")

     st.caption("The Kingdom of Luxury Fashion")

     if "italy_open" not in st.session_state:
      st.session_state.italy_open = False

     if st.button("🌍 Start Journey", key="italy"):
        st.session_state.italy_open = not st.session_state.italy_open

  if st.session_state.italy_open:

    st.success("🇮🇹 Welcome to Italian Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Accessories",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of Italian Fashion")

        st.error("""
Italy has been one of the world's greatest fashion capitals for over **700 years**.

During the Renaissance (14th–17th century), cities like Florence,
Venice, and Milan became famous for producing luxurious silk,
velvet, lace, and handmade garments.

Italian nobles wore beautifully tailored clothing decorated with
gold embroidery, pearls, and precious gemstones.

After World War II, Italy became the center of luxury fashion,
with Milan emerging as one of the world's most influential fashion cities.

Today Italy is home to globally famous luxury brands and is known
for exceptional tailoring, leather craftsmanship, and timeless elegance.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.subheader("👗 Famous Italian Fashion")

        st.markdown("### 👗 Renaissance Gown")
        st.info("""
Elegant royal gowns worn by Italian noblewomen during the Renaissance.
        """)

        st.markdown("### 👔 Italian Tailored Suit")
        st.warning("""
The world's finest handcrafted suits made with perfect tailoring.
        """)

        st.markdown("### 👠 Luxury Evening Dress")
        st.success("""
Italian evening gowns are admired for elegance and premium fabrics.
        """)

        st.markdown("### 👗 Cocktail Dress")
        st.info("""
Popular luxury fashion worn during formal events.
        """)

        st.markdown("### 👢 Italian Leather Jacket")
        st.warning("""
One of Italy's most iconic luxury fashion pieces.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury Italian Fabrics")

        st.write("🧵 Italian Silk")
        st.write("🧵 Velvet")
        st.write("🧵 Cashmere")
        st.write("🧵 Wool")
        st.write("🧵 Fine Cotton")
        st.write("🧵 Leather")
        st.write("🧵 Satin")

        st.info("""
Italian fabrics are known for luxury, durability,
comfort, and world-class craftsmanship.
        """)

    # ======================================================
    # ACCESSORIES
    # ======================================================

    with tab4:

        st.subheader("💎 Luxury Accessories")

        st.write("👜 Leather Handbags")
        st.write("👠 Italian Heels")
        st.write("⌚ Luxury Watches")
        st.write("🕶 Designer Sunglasses")
        st.write("💎 Gold Jewellery")
        st.write("👞 Handmade Leather Shoes")
        st.write("🧣 Silk Scarves")

        st.success("""
Italy is considered the world's leader in
luxury leather accessories and handcrafted shoes.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Famous Italian Designers")

        st.write("👑 Giorgio Armani")
        st.write("👑 Gianni Versace")
        st.write("👑 Guccio Gucci")
        st.write("👑 Valentino Garavani")
        st.write("👑 Domenico Dolce")
        st.write("👑 Stefano Gabbana")
        st.write("👑 Miuccia Prada")

        st.info("""
Italian designers have defined luxury fashion for decades,
combining elegance, innovation, and superior craftsmanship.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI Italian Style Guide")

        st.info("""
✨ Recommended Luxury Outfit

🤵 Italian Tailored Suit

👞 Handmade Leather Shoes

⌚ Luxury Watch

👜 Premium Leather Bag

🕶 Designer Sunglasses

🧣 Silk Scarf

Perfect For:

• Business Meeting

• Luxury Dinner

• Milan Fashion Week

• Wedding Reception

• Luxury Travel
        """)

        st.warning("""
🇮🇹 AI Fashion Tip

Italian fashion is based on timeless elegance.

Choose neutral colours, perfectly fitted clothing,
premium leather accessories, and quality over quantity.

A well-tailored outfit is the true definition of Italian luxury.
        """)


  with row2[1]:

     st.image(
        "c:/Users/simar/Desktop/fashion/photos/turkey.jpg",
        use_container_width=True
     )

     st.markdown("### 🇹🇷 Turkey")

 
     st.caption("The Elegance of the Ottoman Empire")

     if "turkey_open" not in st.session_state:
        st.session_state.turkey_open = False

     if st.button("🌍 Start Journey", key="turkey"):
        st.session_state.turkey_open = not st.session_state.turkey_open

  if st.session_state.turkey_open:

    st.success("🇹🇷 Welcome to Turkish Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Accessories",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of Turkish Fashion")

        st.warning("""
Turkey has a magnificent fashion history dating back over **1,000 years**.

During the **Ottoman Empire (1299–1922)**, clothing represented power,
wealth, and social status. Sultans, queens, and nobles wore luxurious
silk robes decorated with gold embroidery, precious stones, and intricate
patterns.

The famous **Kaftan** became a symbol of royalty and was worn by Ottoman
rulers during official ceremonies.

Traditional Turkish fashion combines influences from Central Asia,
Persia, the Middle East, and Europe.

Today, Turkey continues to preserve its cultural heritage while blending
traditional elegance with modern luxury fashion.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.subheader("👗 Famous Turkish Dresses")

        st.markdown("### 👑 Ottoman Kaftan")
        st.warning("""
The royal robe worn by Ottoman Sultans and members of the royal family.
        """)

        st.markdown("### 👗 Bindallı")
        st.warning("""
A richly embroidered velvet dress traditionally worn during weddings
and engagement ceremonies.
        """)

        st.markdown("### 👘 Şalvar")
        st.error("""
Traditional loose trousers worn by both men and women.
        """)

        st.markdown("### 👗 Entari")
        st.error("""
A long flowing gown worn during the Ottoman period.
        """)

        st.markdown("### 👒 Traditional Wedding Dress")
        st.success("""
Decorated with handmade embroidery and luxurious fabrics.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury Turkish Fabrics")

        st.write("🧵 Ottoman Silk")
        st.write("🧵 Velvet")
        st.write("🧵 Brocade")
        st.write("🧵 Satin")
        st.write("🧵 Linen")
        st.write("🧵 Cotton")
        st.write("🧵 Gold Embroidered Fabric")

        st.info("""
Turkish fabrics are admired for their durability,
luxurious texture, and beautiful handcrafted embroidery.
        """)

    # ======================================================
    # ACCESSORIES
    # ======================================================

    with tab4:

        st.subheader("💎 Traditional Accessories")

        st.write("💎 Ottoman Crown")
        st.write("💎 Gold Jewellery")
        st.write("💎 Handmade Belts")
        st.write("💎 Silk Scarves")
        st.write("💎 Embroidered Shoes")
        st.write("💎 Decorative Headpieces")
        st.write("💎 Traditional Handbags")

        st.success("""
Ottoman accessories reflected wealth and elegance,
often crafted using gold, silver, pearls, and gemstones.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Famous Turkish Designers")

        st.write("👑 Arzu Kaprol")
        st.write("👑 Dice Kayek")
        st.write("👑 Zeynep Tosun")
        st.write("👑 Hakan Akkaya")
        st.write("👑 Özlem Süer")
        st.write("👑 Cengiz Abazoğlu")
        st.write("👑 Bora Aksu")

        st.info("""
Modern Turkish designers combine Ottoman elegance
with contemporary international fashion.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI Turkish Style Guide")

        st.info("""
✨ Recommended Luxury Outfit

👑 Ottoman Kaftan

🧵 Gold Embroidered Belt

💎 Pearl Jewellery

🧣 Silk Scarf

👠 Embroidered Shoes

👜 Luxury Leather Bag

Perfect For:

• Cultural Events

• Weddings

• Luxury Photoshoots

• Heritage Festivals

• Royal-Themed Celebrations
        """)

        st.warning("""
🇹🇷 AI Fashion Tip

Turkish fashion celebrates rich embroidery,
flowing silhouettes, luxurious silk fabrics,
and elegant accessories.

Pair a Kaftan with gold jewellery and
embroidered shoes for an authentic Ottoman-inspired luxury look.
        """)


  with row2[2]:

     st.image(
        "c:/Users/simar/Desktop/fashion/photos/mmmm.jpg",
        use_container_width=True
     )

     st.markdown("### 🇲🇦 Morocco")
 
     st.caption("The Kingdom of Desert Royalty")

     if "morocco_open" not in st.session_state:
        st.session_state.morocco_open = False

     if st.button("🌍 Start Journey", key="morocco"):
        st.session_state.morocco_open = not st.session_state.morocco_open

  if st.session_state.morocco_open:

    st.success("🇲🇦 Welcome to Moroccan Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Accessories",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of Moroccan Fashion")

        st.warning("""
Moroccan fashion is a beautiful blend of **Arab, Berber, Andalusian,
and African cultures**, creating one of the richest clothing traditions
in the world.

For centuries, Morocco was an important trading center connecting Europe,
Africa, and the Middle East. This cultural exchange influenced its fabrics,
colors, embroidery, and jewellery.

The **Kaftan** became Morocco's most iconic garment and was traditionally
worn by royalty and noble families during important celebrations.

Handcrafted embroidery, luxurious silk, velvet, and fine brocade fabrics
became symbols of elegance and prestige.

Today, Moroccan fashion continues to inspire luxury designers with its
rich colours, detailed craftsmanship, and timeless beauty.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.subheader("👗 Famous Moroccan Dresses")

        st.markdown("### 👑 Moroccan Kaftan")
        st.error("""
A luxurious full-length robe decorated with elegant embroidery,
worn during weddings and royal ceremonies.
        """)

        st.markdown("### 👗 Takchita")
        st.warning("""
A beautifully layered ceremonial dress often worn by brides
and during grand celebrations.
        """)

        st.markdown("### 👘 Djellaba")
        st.info("""
A traditional hooded robe worn by both men and women for everyday
comfort and elegance.
        """)

        st.markdown("### 👗 Gandoura")
        st.success("""
A loose-fitting traditional garment popular in warmer regions.
        """)

        st.markdown("### 👰 Moroccan Bridal Dress")
        st.error("""
Known for luxurious embroidery, colourful fabrics, and handcrafted details.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury Moroccan Fabrics")

        st.write("🧵 Silk")
        st.write("🧵 Velvet")
        st.write("🧵 Brocade")
        st.write("🧵 Satin")
        st.write("🧵 Cotton")
        st.write("🧵 Linen")
        st.write("🧵 Handmade Embroidered Fabric")

        st.info("""
Moroccan fabrics are famous for their vibrant colours,
luxurious textures, and detailed hand embroidery.
        """)

    # ======================================================
    # ACCESSORIES
    # ======================================================

    with tab4:

        st.subheader("💎 Traditional Accessories")

        st.write("💎 Silver Jewellery")
        st.write("💎 Berber Necklaces")
        st.write("💎 Gemstone Bracelets")
        st.write("💎 Handcrafted Belts")
        st.write("💎 Embroidered Slippers (Babouche)")
        st.write("💎 Decorative Headpieces")
        st.write("💎 Luxury Handbags")

        st.success("""
Moroccan accessories are handcrafted using silver,
semi-precious stones, leather, and traditional artistry.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Famous Moroccan Designers")

        st.write("👑 Albert Oiknine")
        st.write("👑 Fadila El Gadi")
        st.write("👑 Karim Tassi")
        st.write("👑 Maison Artc")
        st.write("👑 Noureddine Amir")
        st.write("👑 Zineb Joundy")
        st.write("👑 Salima Abdel Wahab")

        st.info("""
Modern Moroccan designers beautifully combine
traditional craftsmanship with contemporary luxury fashion.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI Moroccan Style Guide")

        st.warning("""
✨ Recommended Luxury Outfit

👑 Royal Moroccan Kaftan

🧵 Gold Embroidered Belt

💎 Berber Silver Jewellery

👠 Traditional Babouche Slippers

👜 Luxury Leather Handbag

🧣 Silk Shawl

Perfect For:

• Royal Weddings

• Luxury Photoshoots

• Cultural Celebrations

• Fashion Shows

• Heritage Events
        """)

        st.error("""
🇲🇦 AI Fashion Tip

Moroccan fashion is known for rich colours,
flowing silhouettes, luxurious embroidery,
and handcrafted accessories.

Pair a Kaftan with silver jewellery,
a decorative belt, and traditional Babouche slippers
for a timeless Moroccan luxury look.
        """)
    


  with row2[3]:

     st.image(
        "c:/Users/simar/Desktop/fashion/photos/uk.jpg",
        use_container_width=True
     )

     st.markdown("### 🇬🇧 United Kingdom")

     st.caption("The Home of Royal Elegance")

     if "uk_open" not in st.session_state:
        st.session_state.uk_open = False

     if st.button("🌍 Start Journey", key="uk"):
        st.session_state.uk_open = not st.session_state.uk_open

  if st.session_state.uk_open:

    st.success("🇬🇧 Welcome to British Fashion Heritage")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📜 History",
        "👗 Dresses",
        "🧵 Fabrics",
        "💎 Accessories",
        "👑 Designers",
        "🤖 AI Guide"
    ])

    # ======================================================
    # HISTORY
    # ======================================================

    with tab1:

        st.subheader("📜 History of British Fashion")

        st.warning("""
British fashion has influenced the world for over **500 years**.

During the Tudor and Victorian eras, clothing symbolized wealth,
social class, and royal status. Kings and queens wore luxurious velvet,
lace, silk, and embroidered garments decorated with pearls and precious gems.

London became one of the world's leading fashion capitals, famous for
its bespoke tailoring on Savile Row and elegant royal fashion.

The British Royal Family has greatly influenced global fashion trends,
while London Fashion Week showcases both classic elegance and modern creativity.

Today, British fashion is celebrated for its timeless tailoring,
luxury craftsmanship, and innovative design.
        """)

    # ======================================================
    # DRESSES
    # ======================================================

    with tab2:

        st.subheader("👗 Famous British Fashion")

        st.markdown("### 👑 Royal Gown")
        st.error("""
Elegant gowns worn by members of the Royal Family during official ceremonies.
        """)

        st.markdown("### 🤵 Savile Row Suit")
        st.warning("""
The world's most famous handcrafted men's suit,
known for perfect tailoring and exceptional quality.
        """)

        st.markdown("### 👒 Victorian Dress")
        st.success("""
A beautifully detailed dress featuring lace, corsets,
and luxurious fabrics from the Victorian period.
        """)

        st.markdown("### 🧥 Trench Coat")
        st.error("""
Originally designed in Britain, now one of the world's
most iconic luxury fashion pieces.
        """)

        st.markdown("### 👗 Tea Dress")
        st.info("""
A timeless British classic known for elegance and simplicity.
        """)

    # ======================================================
    # FABRICS
    # ======================================================

    with tab3:

        st.subheader("🧵 Luxury British Fabrics")

        st.write("🧵 Tweed")
        st.write("🧵 Wool")
        st.write("🧵 Cashmere")
        st.write("🧵 Velvet")
        st.write("🧵 Silk")
        st.write("🧵 Linen")
        st.write("🧵 Fine Cotton")

        st.info("""
British textiles are famous for premium wool,
luxury tweed, and world-class tailoring materials.
        """)

    # ======================================================
    # ACCESSORIES
    # ======================================================

    with tab4:

        st.subheader("💎 Luxury Accessories")

        st.write("👒 Royal Hats")
        st.write("👜 Designer Handbags")
        st.write("⌚ Luxury Watches")
        st.write("💎 Diamond Jewellery")
        st.write("🧣 Cashmere Scarves")
        st.write("👞 Handmade Leather Shoes")
        st.write("🎩 Top Hats")

        st.success("""
British accessories combine classic elegance,
luxury craftsmanship, and timeless sophistication.
        """)

    # ======================================================
    # DESIGNERS
    # ======================================================

    with tab5:

        st.subheader("👑 Famous British Designers")

        st.write("👑 Alexander McQueen")
        st.write("👑 Vivienne Westwood")
        st.write("👑 Stella McCartney")
        st.write("👑 Paul Smith")
        st.write("👑 Burberry")
        st.write("👑 Victoria Beckham")
        st.write("👑 Mary Quant")

        st.info("""
British designers are renowned for blending
traditional tailoring with bold creativity,
making London one of the world's most influential
fashion capitals.
        """)

    # ======================================================
    # AI GUIDE
    # ======================================================

    with tab6:

        st.subheader("🤖 AI British Style Guide")

        st.info("""
✨ Recommended Luxury Outfit

🤵 Navy Tailored Suit

👞 Black Leather Oxford Shoes

⌚ Luxury Watch

🧥 Beige Trench Coat

🧣 Cashmere Scarf

👜 Premium Leather Briefcase

Perfect For:

• Business Meetings

• Royal Events

• Luxury Dinner

• London Fashion Week

• Formal Celebrations
        """)

        st.success("""
🇬🇧 AI Fashion Tip

British fashion is built on timeless tailoring,
neutral colours, premium fabrics,
and elegant accessories.

Invest in quality pieces like a tailored blazer,
cashmere scarf, and leather shoes for a sophisticated
British luxury look.
        """)
  
  # ==========================================================
# PASSPORT STAMPS
# ==========================================================

  st.divider()

  st.subheader("🛂 Passport Stamp Collection")

  c1, c2, c3, c4 = st.columns(4)

  with c1:
    st.success("🇮🇳 India ✓")

  with c2:
    st.success("🇫🇷 France ✓")

  with c3:
    st.warning("🇯🇵 Japan 🔒")

  with c4:
    st.warning("🇰🇷 Korea 🔒")
  # ==========================================================
# JOURNEY
# ==========================================================

  st.divider()

  st.subheader("🏆 Your Fashion Journey")

  m1, m2, m3, m4 = st.columns(4)

  with m1:
    st.metric("Countries", "3/20")

  with m2:
    st.metric("Passport XP", "12,450")

  with m3:
    st.metric("Luxury Rank", "Explorer")

  with m4:
    st.metric("Collections", "15")  
  # ==========================================================
# 🎮 DAILY FASHION CHALLENGE
# ==========================================================

  st.divider()

  st.subheader("🎮 Today's Fashion Challenge")

  left, right = st.columns([2,1])

  with left:

    st.image(
        "c:/Users/simar/Desktop/fashion/photos/royal wedding.jpg",
        use_container_width=True
    )

  with right:

    st.markdown("## 🇮🇳 India")

    st.write("### Royal Wedding Challenge")

    # ============================================
# START CHALLENGE
# ============================================

    if "india_challenge" not in st.session_state:
     st.session_state.india_challenge = False

    if st.button("🚀 Start Challenge", key="challenge1"):
     st.session_state.india_challenge = True

    if st.session_state.india_challenge:

     st.divider()

     st.title("👑 Royal Wedding Fashion Mission")

     st.info("""
🎯 Mission

The Princess of Jaipur is getting married tomorrow.

You are the Royal Fashion Stylist.

Choose the perfect outfit to impress the Royal Family.

Complete the challenge to earn:

🏆 +500 Passport XP

🥇 Royal Stylist Badge
""")

    st.subheader("Step 1 • Choose the Dress")

    dress = st.radio(
        "",
        [
            "👗 Banarasi Lehenga",
            "👗 Jeans",
            "👗 Shorts",
            "👗 T-Shirt"
        ],
        key="dress"
    )

    st.subheader("Step 2 • Choose Jewellery")

    jewellery = st.radio(
        "",
        [
            "💎 Kundan Set",
            "⌚ Sports Watch",
            "🧢 Baseball Cap",
            "🎧 Headphones"
        ],
        key="jewel"
    )

    st.subheader("Step 3 • Choose Footwear")

    shoes = st.radio(
        "",
        [
            "👠 Golden Heels",
            "👟 Running Shoes",
            "🩴 Slippers",
            "🥾 Boots"
        ],
        key="shoe"
    )

    st.subheader("Step 4 • Choose Handbag")

    bag = st.radio(
        "",
        [
            "👜 Embroidered Potli",
            "🎒 School Bag",
            "🛍 Plastic Bag",
            "💼 Laptop Bag"
        ],
        key="bag"
    )

    st.divider()
    st.button("🛍 Shop Now", key="wedding collection_shop")

    if st.button("✨ Submit Royal Look"):

        score = 0

        if dress == "👗 Banarasi Lehenga":
            score += 25

        if jewellery == "💎 Kundan Set":
            score += 25

        if shoes == "👠 Golden Heels":
            score += 25

        if bag == "👜 Embroidered Potli":
            score += 25

        if score == 100:

            st.balloons()

            st.success("👑 PERFECT!")

            st.markdown("## ⭐⭐⭐⭐⭐")

            st.metric("Fashion Score", "100 / 100")

            st.success("🏆 +500 Passport XP")

            st.success("🥇 Royal Stylist Badge Unlocked")

            st.write("You created the perfect Royal Wedding outfit!")

        elif score >= 75:

            st.success("⭐⭐⭐⭐ Great Styling")

            st.metric("Fashion Score", f"{score}/100")

            st.info("Almost Perfect! Keep improving.")

        elif score >= 50:

            st.warning("⭐⭐ Good Attempt")

            st.metric("Fashion Score", f"{score}/100")

            st.write("Some fashion choices didn't match the royal theme.")

        else:

            st.error("❌ Fashion Disaster!")

            st.metric("Fashion Score", f"{score}/100")

            st.write("Try choosing more traditional luxury items.")
  # ==========================================================
# AI MISSION
# ==========================================================

  st.divider()

  st.subheader("🤖 AI Fashion Mission")

  st.success("""

  QUANTIQUE AI Challenge

  Travel to India.

  Explore traditional luxury fashion.

  Complete the Royal Wedding Challenge.

  Unlock your INDIA Passport Stamp.

  Earn +500 XP.

  """)  
  # ==========================================================
# ACHIEVEMENT
# ==========================================================

  st.divider()

  st.subheader("🏅 Upcoming Achievement")

  st.info("""

  🏅 Cultural Explorer

  Visit 5 countries.

  Reward

  👑 Gold Passport Badge

  """)
  # ==========================================================
# LEADERBOARD
# ==========================================================

  st.divider()

  st.subheader("🌎 Global Fashion Explorer")

  rank1, rank2, rank3 = st.columns(3)

  with rank1:
    st.metric("🥇 Explorer", "Sophia", "28 Countries")

  with rank2:
    st.metric("🥈 Explorer", "Emma", "24 Countries")

  with rank3:
    st.metric("🥉 Explorer", "You", "3 Countries")
    
  # ==========================================================
# 🇮🇳 INDIA EXPERIENCE
# ==========================================================

  st.divider()

  st.title("🇮🇳 INDIA")

  st.caption("The Land of Timeless Luxury Fashion")

  st.image(
    "c:/Users/simar/Desktop/fashion/photos/rk.jpg",
    use_container_width=True
  )

  st.markdown("""
  ## ✨ Discover India's Fashion Heritage

  India is one of the oldest fashion civilizations in the world.

  From handwoven Banarasi silk to royal bridal couture,
  every outfit tells a story of culture, craftsmanship,
  and timeless elegance.

  Explore India's luxury fashion through QUANTIQUE.
  """)

  st.divider()

# ==========================================================
# QUICK INFO
# ==========================================================

  st.subheader("📍 Country Overview")

  m1, m2, m3, m4 = st.columns(4)

  with m1:
    st.metric("Capital", "New Delhi")

  with m2:
    st.metric("Luxury Score", "★★★★★")

  with m3:
    st.metric("Fashion Cities", "5")

  with m4:
    st.metric("Heritage", "5000+ Years")

  st.divider()
 

 # ============================================
# 👗 Traditional Fashion Challenge
# ============================================

  st.info("### 🎮 Guess The Traditional Dress")

  if "fashion_xp" not in st.session_state:
    st.session_state.fashion_xp = 0


  st.metric("🏆 Passport XP", st.session_state.fashion_xp)

  st.divider()

  dresses = [

  {
    "name":"Banarasi Saree",
    "emoji":"🧵✨👰📍",
    "hint":"Luxury silk from Varanasi",
    "image":"c:/Users/simar/Desktop/fashion/photos/banarsi.jpg",
    "history":"""
The Banarasi Saree originated in Varanasi over 500 years ago during the Mughal Empire.
It is famous for luxurious silk and gold zari work and remains India's most iconic bridal saree.
"""
    
  },

  {
    "name":"Royal Lehenga",
    "emoji":"👑💍✨👰",
    "hint":"Royal bridal outfit",
    "image":"c:/Users/simar/Desktop/fashion/photos/lehnga.jpg",
    "history":"""
The Lehenga became popular during the Mughal period.
It was worn by queens and noblewomen and is now India's most famous bridal dress.
"""
  },

  {
    "name":"Sherwani",
    "emoji":"🤵👑🎩",
    "hint":"Traditional royal menswear",
    "image":"c:/Users/simar/Desktop/fashion/photos/men wear.jpg",
    "history":"""
The Sherwani was introduced during the Mughal Empire.
Today it is the traditional groom's outfit for Indian weddings.
"""
  },

  {
    "name":"Anarkali",
    "emoji":"🌸💃👸",
    "hint":"Named after a Mughal court dancer",
    "image":"c:/Users/simar/Desktop/fashion/photos/Anarkali.jpg",
    "history":"""
The Anarkali suit is inspired by the legendary Mughal court dancer Anarkali.
It is admired for its graceful flowing silhouette.
"""
  }

  ]

  options = [
    "Banarasi Saree",
    "Royal Lehenga",
    "Sherwani",
    "Anarkali"
  ]

  for i, dress in enumerate(dresses):#gives two things:

    st.divider()

    st.markdown(f"## Level {i+1}")

    st.markdown(f"# {dress['emoji']}")

    st.caption("Guess the Traditional Dress")

    answer = st.radio(
        "Choose your answer",
        options,
        key=f"radio_{i}"
    )

    if st.button("✅ Submit", key=f"submit_{i}"):

        if answer == dress["name"]:

            st.success("🎉 Correct Answer!")

            st.session_state.fashion_xp += 50

            st.snow()

            st.image(
                dress["image"],
                width=350
            )

            st.markdown(f"## 👗 {dress['name']}")

            st.info(dress["history"])
           
            st.button("🛍 Shop Now", key="banarasi_shop")

              
               

        else:

            st.error("❌ Wrong Answer")

            st.warning(f"💡 Hint : {dress['hint']}")

  st.divider()

  if st.session_state.fashion_xp >= 200:

    st.success("🏆 Congratulations!")

    st.markdown("""
# 👑 Indian Traditional Fashion Master

🎖 Badge Unlocked

🏆 +200 Passport XP

You guessed all four traditional dresses correctly!
""")
    
elif page == "📸 Social Fashion Trends":
   st.title("🔥 Trending Fashion Now")

   st.caption("Discover what's trending across social platforms right now.")

   st.info("✨ Live Trends • Updated Daily • Curated for You")
   
   st.subheader("✨ Today's Top Picks")

   col1, col2, col3, = st.columns(3)

   with col1:
    with st.container(border=True):
      st.markdown("### ✨ Floral Edit")
      st.image("c:/Users/simar/Pictures/Screenshots/inst.jpeg",
            use_container_width=True)
      st.write("🔥 Trending")
      st.caption("👗 Floral Summer Outfit")
      st.caption("⭐ Rating: 4.9/5")
      st.caption("❤️ Loved by Fashion Creators")
      st.success("📸 Instagram Exclusive")
      st.link_button(
          "📸 view Instagram",
         "https://www.instagram.com/reel/DaK5dx0I3qY/?igsh=MW80ZnRibm53YW5hOQ==")
      st.button("🛍 Shop Now", key="shop_floral")
      

   with col2:
    with st.container(border=True):
      st.markdown("### 💜 Lavender Mood")
    
      st.image("c:/Users/simar/Pictures/Screenshots/snap.jpeg",use_container_width=True)
      st.write("🔥 Trending")
      st.caption("👗 Lavender Evening Dress")
      st.caption("⭐ Rating: 4.8/5")
      st.caption("💜 Viral This Week")
      st.success("👻 Snapchat Spotlight")
   
      st.link_button("👻 view Snapchat", "https://www.snapchat.com/@snapchat/spotlight/W7_EDlXWTBiXAEEniNoMPwAAYY3VsYXB0bG1pAZ9UCLsDAZ9UCHMTAAAAAQ")
      st.button("🛍 Shop Now", key="shop_lavender")

   with col3:
    with st.container(border=True):
    
     st.markdown("### 🤍 Casual Chic")

     st.image("c:/Users/simar/Downloads/p.jpg", use_container_width=True)
     st.write("🔥 Trending")
     st.caption("👗 Casual Street Style")
     st.caption("⭐ Rating: 4.9/5")
     st.caption("🤍 Pinterest Favorite")
     st.success("📌 Pinterest Favorite")
     st.link_button("📌 view Pinterest", "https://pin.it/634OgvfSL")
     st.button("🛍 Shop Now", key="shop_casual")
   st.warning("💡 Click any button above to explore the original fashion inspiration.")
   st.subheader("💖 Why Everyone Loves These Trends")

   col1, col2, col3 = st.columns(3)

   with col1:
    st.metric("🔥 Daily Views", "45M+")

   with col2:
    st.metric("👗 Trending Looks", "250+")

   with col3:
    st.metric("🌍 Countries", "80+")

   st.info(
    "✨ Fashion is not just about clothing — it's about confidence, creativity, and expressing yourself."
   )

   st.error(
    "💡 Tip: Save your favorite looks from Instagram, Snapchat, and Pinterest to build your own style inspiration."
   )   

  


   st.divider()

   st.subheader("🔥 Trending This Week")
   

   st.caption("Explore the most popular luxury outfits loved by fashion enthusiasts.")
   with st.container(border=True):

    st.image(
    "c:/Users/simar/Desktop/fashion/photos/black lookbook.jpg",
     use_container_width=True
   )

   st.markdown("## 🖤 Black Royal Look")

   st.caption("Elegant Evening Collection")

   left, right = st.columns(2)

   with left:
     st.metric("👁 Views", "15.8M")

   with right:
      st.metric("❤️ Likes", "2.4M")

   st.success("🔥 Trending This Week")
   st.button("🛍 Shop Now", key="shop_black")
  # ===========================
  # QUANTIQUE PURCHASE
  # ===========================

   st.divider()
  
   st.subheader("🛒 Purchase Your Outfit")
   if "payment_done" not in st.session_state:
    st.session_state.payment_done = False

   if "gift" not in st.session_state:
    st.session_state.gift = ""

   dress = st.selectbox(
    "Choose Your Dress",
    [
        "🖤 Black Royal Look",
        "🌸 Floral Summer Dress",
        "💜 Lavender Mood",
        "🤍 Casual Chic"
    ]
   )

   price = st.selectbox(
    "Select Price",
    [
        "₹8,999",
        "₹12,999",
        "₹18,999",
        "₹25,999"
    ]
   )

   if st.button("💳 Buy Now"):
      st.session_state.payment_done = True
   if st.session_state.payment_done:



     st.success("✅ 💰 Payment Successful!")
     st.write(f"**Dress Purchased:** {dress}")

     st.write(f"**Amount Paid:** {price}")
     st.snow()


     st.info("🎁 Congratulations! You unlocked the QUANTIQUE Luxury Wheel!")

     if st.button("🎡 Spin the Wheel"):

        gifts = [
            "💎 Diamond Earrings",
            "👠 Luxury Heels",
            "👜 Designer Handbag",
            "🌸 Luxury Perfume",
            "💄 Premium Makeup Kit",
            "🧣 Silk Scarf",
            "⌚ Luxury Watch",
            "🎟 VIP Fashion Show Pass",
            "🎁 Mystery Fashion Box",
            "💸 20% Discount Coupon"
        ]
        
        st.session_state.gift = random.choice(gifts)

        st.balloons()

    # --------------------------
    # Show Gift
    # --------------------------

     if st.session_state.gift != "":

        st.markdown("---")

        st.subheader("🎉 Congratulations!")

        st.warning(f"You Won: {st.session_state.gift}")

        st.write("✨ Your surprise gift has been added to your order.")

        st.write("💜 Thank you for shopping with **QUANTIQUE**.")

        # --------------------------
        # Shop Again
        # --------------------------

        if st.button("🛍 Shop Again"):

            st.session_state.payment_done = False

            st.session_state.gift = ""

            st.rerun()

       