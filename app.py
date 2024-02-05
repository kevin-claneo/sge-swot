import streamlit as st

def setup_streamlit():
    st.set_page_config(
        page_title="SGE SWOT Analysis - Kevin (Claneo)",
        page_icon=":rotating_light:",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.linkedin.com/in/kirchhoff-kevin/',
            'About': "This is an app, that provides you an analysis basis for SGE"
        }
    )
    st.image("https://www.claneo.com/wp-content/uploads/Element-4.svg", width=600, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.caption(":point_right: Join Claneo and support exciting clients as part of the Consulting team")
    st.caption(':bulb: Make sure to mention that *Kevin* brought this job posting to your attention')
    st.link_button("Learn More", "https://www.claneo.com/en/career/#:~:text=Consulting")
    st.title("SGE SWOT Analysis")
    st.divider()

    
def setup_user_input_forms():
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
    st.header("SWOT Analysis Input")
    st.subheader("Please answer the following questions based on your company's current situation:")

    # Additional inputs for business model, SEO model, etc.
    business_model = st.selectbox("What is your business model?", ["E-commerce", "Local business", "SaaS", "Affiliate", "Publisher", "Consumer", "B2B-Services"])
    
    seo_model = st.selectbox("What is your SEO model?", ["Aggregator", "Integrator"])
    with st.expander("🛈 Learn more about SEO models"):
        st.markdown("""
        **Aggregators** and **Integrators** have fundamentally different approaches to growth:

        - **Aggregators** channel demand through superior user experience and free distribution. They leverage network effects by consolidating demand (e.g., Google, Amazon).
        
        - **Integrators** own the entire value chain (suppliers, production, distribution) and focus on maximizing margins by providing unique value and controlling distribution (e.g., Apple, Peloton).
        
        Choose the model that best describes your company's approach.
        """)
    
    industry = st.selectbox("What industry does your company belong to?", industries)
    competitive_landscape = st.selectbox("What best describes your competitive landscape?", ["Dog fight", "Monopoly", "Emerging", "Stable"])
    with st.expander("🛈 Learn more about competitive landscapes"):
        st.markdown("""
        **Understanding your competitive landscape:**
    
        - **Dog fight**: Highly competitive market with numerous players fighting for market share.
        - **Monopoly**: Dominated by a single player, with little to no competition.
        - **Emerging**: A new, growing market with relatively few competitors.
        - **Stable**: A mature market with established players and steady growth rates.
        
        Select the option that best describes the current state of your market.
        """)
    company_size = st.selectbox("What is your company size?", ["Micro (1-10 employees)", "Small (11-50 employees)", "Medium (51-250 employees)", "Large (251-500 employees)", "Enterprise (500+ employees)"])
    resources_adaptable_to_SGE = st.select_slider("How adaptable are your resources to changes brought by SGE?", options=['Very Inflexible', 'Somewhat Inflexible', 'Neutral', 'Somewhat Adaptable', 'Very Adaptable'])
    revenue_streams_resilient_to_SGE = st.radio("Are your revenue streams resilient to potential changes in organic search due to SGE?", ('Yes', 'Somewhat', 'No'))
    employees_ready_for_AI = st.radio("Is your workforce ready for AI advancements and integration?", ('Yes', 'No'))
    brand_recognized_in_SGE = st.radio("Do you believe your brand is strong enough to be recognized in SGE-driven search results?", ('Yes', 'No'))
    customer_acquisition_channels_diversified = st.radio("Are your customer acquisition channels diversified beyond organic search?", ('Yes', 'No'))
    content_uniquely_valuable = st.radio("Is your content uniquely valuable and difficult to replicate by AI?", ('Yes', 'No'))
    market_growing_with_SGE = st.radio("Do you see the market growing with the advent of SGE?", ('Yes', 'No'))
    competition_lagging_in_AI_adaptation = st.radio("Is your competition lagging in adapting to AI?", ('Yes', 'No'))
    socio_political_trends_supportive_of_AI = st.radio("Are socio-political trends supportive of AI integration in your industry?", ('Yes', 'No'))

    return {
        "business_model": business_model,
        "seo_model": seo_model,
        "industry": industry,
        "competitive_landscape": competitive_landscape,
        "company_size": company_size,
        "resources_adaptable_to_SGE": resources_adaptable_to_SGE,
        "revenue_streams_resilient_to_SGE": revenue_streams_resilient_to_SGE,
        "employees_ready_for_AI": employees_ready_for_AI,
        "brand_recognized_in_SGE": brand_recognized_in_SGE,
        "customer_acquisition_channels_diversified": customer_acquisition_channels_diversified,
        "content_uniquely_valuable": content_uniquely_valuable,
        "market_growing_with_SGE": market_growing_with_SGE,
        "competition_lagging_in_AI_adaptation": competition_lagging_in_AI_adaptation,
        "socio_political_trends_supportive_of_AI": socio_political_trends_supportive_of_AI
    }
def perform_detailed_swot_analysis(user_inputs):
    # Mapping user inputs to conditions
    conditions = {
        "resources_adaptable_to_SGE": "Very Adaptable" in user_inputs["resources_adaptable_to_SGE"],
        "revenue_streams_resilient_to_SGE": user_inputs["revenue_streams_resilient_to_SGE"] == "Yes",
        "employees_ready_for_AI": user_inputs["employees_ready_for_AI"] == "Yes",
        "brand_recognized_in_SGE": user_inputs["brand_recognized_in_SGE"] == "Yes",
        "customer_acquisition_channels_diversified": user_inputs["customer_acquisition_channels_diversified"] == "Yes",
        "content_uniquely_valuable": user_inputs["content_uniquely_valuable"] == "Yes",
        "market_growing_with_SGE": user_inputs["market_growing_with_SGE"] == "Yes",
        "competition_lagging_in_AI_adaptation": user_inputs["competition_lagging_in_AI_adaptation"] == "Yes",
        "socio_political_trends_supportive_of_AI": user_inputs["socio_political_trends_supportive_of_AI"] == "Yes"
    }

    # Assuming the advanced_swot_analysis function is adjusted to use these conditions
    # Here you would call the advanced_swot_analysis function and pass the conditions
    swot_analysis = advanced_swot_analysis(**conditions)
    
    return swot_analysis
    
def main():
    setup_streamlit()  # Your initial setup function

    user_inputs = setup_user_input_forms()

    if st.button("Perform SWOT Analysis"):
        swot_results = perform_detailed_swot_analysis(user_inputs)
        st.subheader("SWOT Analysis Results")
        for category, factors in swot_results.items():
            st.markdown(f"**{category}:**")
            for factor in factors:
                st.write(f"- {factor}")

if __name__ == "__main__":
    main()
    
