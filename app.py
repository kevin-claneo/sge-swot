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
    customer_acquisition_channel = st.multiselect("What are your customer acquisition channels?", acquisition_channels)
    resources_adaptable_to_SGE = st.select_slider("How adaptable are your resources to changes brought by SGE?", options=['Very Inflexible', 'Somewhat Inflexible', 'Neutral', 'Somewhat Adaptable', 'Very Adaptable'])
    revenue_streams_resilient_to_SGE = st.radio("Are your revenue streams resilient to potential changes in organic search due to SGE?", ('Yes', 'Somewhat', 'No'))
    employees_ready_for_AI = st.radio("Is your workforce ready for AI advancements and integration?", ('Yes', 'No'))
    brand_recognized_in_SGE = st.radio("Do you believe your brand is strong enough to be recognized in SGE-driven search results?", ('Yes', 'No'))
    customer_acquisition_channels_diversified = st.radio("Are your customer acquisition channels diversified beyond organic search?", ('Yes', 'No'))
    content_uniquely_valuable = st.radio("Is your content uniquely valuable and difficult to replicate by AI?", ('Yes', 'No'))
    market_growing_with_SGE = st.radio("Do you see the market growing with the advent of SGE?", ('Yes', 'No'))
    competition_lagging_in_AI_adaptation = st.radio("Is your competition lagging in adapting to AI?", ('Yes', 'No'))
    socio_political_trends_supportive_of_AI = st.radio("Are socio-political trends supportive of AI integration in your industry?", ('Yes', 'No'))
    technological_infrastructure = st.radio("Is your technological infrastructure advanced enough to integrate and leverage AI technologies efficiently?",('Yes', 'No'))
    innovation_capability = st.select_slider("How would you rate your company's capability for innovation and adopting new technologies?", options=['Very Low', 'Low', 'Moderate', 'High', 'Very High'])  
    market_trends_awareness = st.radio("Is your company aware of and actively monitoring market trends related to SGE and AI?", ('Yes', 'No'))
    customer_behavior_changes = st.radio("Are you observing significant changes in customer behavior due to advancements in AI and search technologies?", ('Yes', 'No'))
    external_economic_factors = st.radio("Do external economic factors (e.g., recession, rapid growth) currently pose a risk or opportunity for your business?", options=['Risk', 'Opportunity', 'Neither'])

    return {
        "business_model": business_model,
        "seo_model": seo_model,
        "industry": industry,
        "competitive_landscape": competitive_landscape,
        "company_size": company_size,
        "customer_acquisition_channel": customer_acquisition_channel,
        "resources_adaptable_to_SGE": resources_adaptable_to_SGE,
        "revenue_streams_resilient_to_SGE": revenue_streams_resilient_to_SGE,
        "employees_ready_for_AI": employees_ready_for_AI,
        "brand_recognized_in_SGE": brand_recognized_in_SGE,
        "content_uniquely_valuable": content_uniquely_valuable,
        "market_growing_with_SGE": market_growing_with_SGE,
        "competition_lagging_in_AI_adaptation": competition_lagging_in_AI_adaptation,
        "socio_political_trends_supportive_of_AI": socio_political_trends_supportive_of_AI,
        "technological_infrastructure": technological_infrastructure,
        "innovation_capability": innovation_capability,
        "market_trends_awareness": market_trends_awareness,
        "customer_behavior_changes": customer_behavior_changes,
        "external_economic_factors": external_economic_factors,
    }
def analyze_seo_channel_impact(customer_acquisition_channel):
    if "SEO" in customer_acquisition_channel:
        # Strength: Proven expertise in leveraging organic search, which is critical in an SGE-impacted landscape.
        return ("Strengths", "Expertise in SEO optimizing for SGE changes")
    else:
        # Weakness: Missing out on organic search opportunities, particularly critical as search engines evolve with SGE.
        return ("Weaknesses", "Lack of presence in organic search, a missed opportunity with SGE advancements")

def analyze_digital_advertising_impact(customer_acquisition_channel):
    if "Online Advertising" in customer_acquisition_channel:
        # Opportunity: Utilizing AI-driven advertising platforms to dynamically adapt to changing consumer behaviors.
        return ("Opportunities", "Leveraging AI-driven advertising for dynamic market responsiveness")
    else:
        # Threat: Falling behind competitors who are capitalizing on the precision and adaptability of AI-driven ads.
        return ("Threats", "Risk of being outmaneuvered by competitors using AI-driven advertising strategies")

def evaluate_channel_diversification(customer_acquisition_channel):
    digital_channels = {"Online Advertising", "Social Media", "Email Marketing", "Content Marketing", "SEO"}
    selected_digital_channels = set(customer_acquisition_channel) & digital_channels

    if len(selected_digital_channels) >= 3:
        # Strength: Robust digital presence across multiple platforms, enhancing market reach and resilience.
        return ("Strengths", f"Diversified digital presence across {len(selected_digital_channels)} platforms")
    elif len(selected_digital_channels) > 0:
        # Weakness: Limited diversification may not fully capitalize on digital's potential.
        return ("Weaknesses", "Limited diversification within digital channels")      
        
def perform_detailed_swot_analysis(user_inputs):
    swot_categories = {
        "Strengths": [],
        "Weaknesses": [],
        "Opportunities": [],
        "Threats": []
    }

    # List of functions to call for analysis - ensure each returns a valid tuple
    analysis_functions = [
        analyze_seo_channel_impact,
        analyze_digital_advertising_impact,
        evaluate_channel_diversification
    ]
    
    for func in analysis_functions:
        category, message = func(user_inputs["customer_acquisition_channel"])
        if category and message:  # Simple check to ensure non-empty values
            swot_categories[category].append(message)
        
    adaptability = user_inputs["resources_adaptable_to_SGE"]
    if adaptability in ["Very Adaptable", "Somewhat Adaptable"]:
        swot_categories["Strengths"].append("Adaptable resources to SGE changes")
    elif adaptability in ["Very Inflexible", "Somewhat Inflexible"]:
        swot_categories["Weaknesses"].append("Resources poorly adaptable to SGE changes")

    # Employees readiness for AI
    if user_inputs["employees_ready_for_AI"] == "Yes":
        swot_categories["Strengths"].append("Workforce ready for AI advancements")
    else:
        swot_categories["Weaknesses"].append("Workforce unprepared for AI advancements")

    # Brand recognition in SGE
    if user_inputs["brand_recognized_in_SGE"] == "Yes":
        swot_categories["Strengths"].append("Strong brand recognition in SGE")
    else:
        swot_categories["Weaknesses"].append("Lack of brand recognition in SGE")

    # Revenue streams resilience
    if user_inputs["revenue_streams_resilient_to_SGE"] == "Yes":
        swot_categories["Strengths"].append("Resilient revenue streams to SGE changes")
    elif user_inputs["revenue_streams_resilient_to_SGE"] == "No":
        swot_categories["Weaknesses"].append("Vulnerable revenue streams to SGE changes")

    # Market growth with SGE
    if user_inputs["market_growing_with_SGE"] == "Yes":
        swot_categories["Opportunities"].append("Growing market with SGE advancements")
    else:
        swot_categories["Threats"].append("Stagnating or declining market with SGE advancements")

    # Competition lagging in AI adaptation
    if user_inputs["competition_lagging_in_AI_adaptation"] == "Yes":
        swot_categories["Opportunities"].append("Competitive advantage with faster AI adaptation")
    else:
        swot_categories["Threats"].append("Competitors may overtake with faster AI adaptation")

    # Socio-political trends supportive of AI
    if user_inputs["socio_political_trends_supportive_of_AI"] == "Yes":
        swot_categories["Opportunities"].append("Favorable socio-political environment for AI integration")
    else:
        swot_categories["Threats"].append("Regulatory and socio-political challenges to AI integration")
    if user_inputs["technological_infrastructure"] == "Yes":
        swot_categories["Strengths"].append("Advanced technological infrastructure for AI integration")
    else:
        swot_categories["Weaknesses"].append("Technological infrastructure not ready for efficient AI integration")
    
    if user_inputs["innovation_capability"] in ["High", "Very High"]:
        swot_categories["Strengths"].append("High capability for innovation and adopting new technologies")
    elif user_inputs["innovation_capability"] in ["Very Low", "Low"]:
        swot_categories["Weaknesses"].append("Limited capability for innovation and slow adoption of new technologies")
    
    if user_inputs["market_trends_awareness"] == "Yes":
        swot_categories["Opportunities"].append("Awareness and active monitoring of market trends related to SGE and AI")
    else:
        swot_categories["Threats"].append("Lack of awareness or monitoring of significant market trends")
    
    if user_inputs["customer_behavior_changes"] == "Yes":
        swot_categories["Opportunities"].append("Significant changes in customer behavior favoring AI-driven solutions")
    elif user_inputs["customer_behavior_changes"] == "No":
        swot_categories["Threats"].append("Potential oversight of evolving customer expectations and behaviors")
    if user_inputs["external_economic_factors"] == "Opportunity":
        swot_categories["Opportunities"].append("Favorable external economic conditions")
    elif user_inputs["external_economic_factors"] == "Risk":
        swot_categories["Threats"].append("Adverse external economic conditions")

    return swot_categories

def display_swot_matrix(swot_categories):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Strengths")
        for strength in swot_categories["Strengths"]:
            st.write(f"- {strength}")
        
        st.subheader("Weaknesses")
        for weakness in swot_categories["Weaknesses"]:
            st.write(f"- {weakness}")

    with col2:
        st.subheader("Opportunities")
        for opportunity in swot_categories["Opportunities"]:
            st.write(f"- {opportunity}")
        
        st.subheader("Threats")
        for threat in swot_categories["Threats"]:
            st.write(f"- {threat}")

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
    
