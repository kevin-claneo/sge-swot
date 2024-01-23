import streamlit as st

def setup_streamlit():
    st.set_page_config(
    page_title="SEO Strategy and SWOT Analysis - Kevin (Claneo)",
    page_icon=":rotating_light:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/kirchhoff-kevin/',
        'About': "This is an app for checking your topical authority! Adapted from Lee Foot's GSC-connector check out his apps: https://leefoot.co.uk"
    }
    )
    st.image("https://www.claneo.com/wp-content/uploads/Element-4.svg", width=600, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption(":point_right: Join Claneo and support exciting clients as part of the Consulting team") 
    st.caption(':bulb: Make sure to mention that *Kevin* brought this job posting to your attention')
    st.link_button("Learn More", "https://www.claneo.com/en/career/#:~:text=Consulting")
    st.title("Check the topical authority of a GSC property")
    st.divider()



    # List of common industries
    industries = [
        "Advertising & Marketing", "Aerospace & Defense", "Agriculture", 
        "Automotive", "Banking & Finance", "Biotechnology", "Chemicals", 
        "Construction", "Consumer Goods & Services", "Education", "Energy", 
        "Entertainment & Leisure", "Food & Beverages", "Healthcare", "Hospitality", 
        "Information Technology", "Insurance", "Manufacturing", "Media", 
        "Pharmaceuticals", "Real Estate", "Retail", "Telecommunications", 
        "Transportation & Logistics", "Utilities"
    ]
    
    # Customer acquisition channels
    acquisition_channels = [
        "Online Advertising", "Social Media", "Email Marketing", 
        "Content Marketing", "SEO", "Affiliate Marketing", 
        "Direct Sales", "Public Relations", "Trade Shows", 
        "Word of Mouth", "Partnerships"
    ]


with st.form("seo_strategy_form"):
    setup_streamlit()
    # Select box for industry
    industry = st.selectbox("Select Your Industry", industries)
    # Sliders for various attributes
    company_size = st.slider("Company Size", 1, 10, 5)
    competitiveness = st.slider("Competitiveness", 1, 10, 5)
    resources_availability = st.slider("Resources Availability", 1, 10, 5)
    size_of_seo_team = st.slider("Size of SEO Team", 1, 10, 5)
    brand_strength = st.slider("Brand Strength", 1, 10, 5)

    # Multi-select box for customer acquisition channels
    selected_acquisition_channels = st.multiselect("Customer Acquisition Channels", acquisition_channels)

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Submitted data: ")
        st.write(f"Industry: {industry}")
        st.write(f"Company Size: {company_size}, Competitiveness: {competitiveness}, Resources: {resources_availability}, SEO Team Size: {size_of_seo_team}, Brand Strength: {brand_strength}")
        st.write(f"Acquisition Channels: {', '.join(selected_acquisition_channels)}")

        # Here you can add the logic to process the input data and integrate with ChatGPT for analysis

# Additional logic for processing and ChatGPT integration goes here
