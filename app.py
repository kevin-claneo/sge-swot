import streamlit as st

def setup_streamlit():
    st.set_page_config(
        page_title="SGE SWOT Analysis - Kevin (Claneo)",
        page_icon=":rotating_light:",
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
    st.header("SWOT Analysis Input")
    st.subheader("Please answer the following questions based on your company's current situation:")

    business_model = st.selectbox(
        "What is your business model?", 
        ["E-commerce", "Local business", "SaaS", "Affiliate", "Publisher", "Consumer", "B2B-Services"]
    )
    
    seo_model = st.selectbox(
        "What is your SEO model?", 
        ["Aggregator", "Integrator"], help="""
        **Aggregators** and **Integrators** have fundamentally different approaches to growth:

        - **Aggregators** channel demand through superior user experience and free distribution. They leverage network effects by consolidating demand (e.g., Google, Amazon).
        
        - **Integrators** own the entire value chain (suppliers, production, distribution) and focus on maximizing margins by providing unique value and controlling distribution (e.g., Apple, Peloton).
        
        Choose the model that best describes your company's approach.
        """
    )
    
    industry = st.selectbox(
        "What industry does your company belong to?", 
        [
            "Advertising & Marketing", "Aerospace & Defense", "Agriculture", 
            "Automotive", "Banking & Finance", "Biotechnology", "Chemicals", 
            "Construction", "Consumer Goods & Services", "Education", "Energy", 
            "Entertainment & Leisure", "Food & Beverages", "Healthcare", "Hospitality", 
            "Information Technology", "Insurance", "Manufacturing", "Media", 
            "Pharmaceuticals", "Real Estate", "Retail", "Telecommunications", 
            "Transportation & Logistics", "Utilities"
        ]
    )
    
    competitive_landscape = st.selectbox(
        "What best describes your competitive landscape?", 
        ["Dog fight", "Monopoly", "Emerging", "Stable"], help="""
        **Understanding your competitive landscape:**
    
        - **Dog fight**: Highly competitive market with numerous players fighting for market share.
        - **Monopoly**: Dominated by a single player, with little to no competition.
        - **Emerging**: A new, growing market with relatively few competitors.
        - **Stable**: A mature market with established players and steady growth rates.
        
        Select the option that best describes the current state of your market.
        """
    )
    
    company_size = st.selectbox(
        "What is your company size?", 
        ["Micro (1-10 employees)", "Small (11-50 employees)", "Medium (51-250 employees)", "Large (251-500 employees)", "Enterprise (500+ employees)"]
    )
    
    customer_acquisition_channel = st.multiselect(
        "What are your customer acquisition channels?", 
        [
            "Online Advertising", "Social Media", "Email Marketing", 
            "Content Marketing", "SEO", "Affiliate Marketing", 
            "Direct Sales", "Public Relations", "Trade Shows", 
            "Word of Mouth", "Partnerships"
        ]
    )
    
    resources_adaptable_to_SGE = st.slider(
        "Rate the adaptability of your resources to changes brought by SGE", 
        0, 100, 50, help="0% being not adaptable at all, 100% being fully adaptable"
    )
    
    revenue_streams_resilient_to_SGE = st.slider(
        "Rate the resilience of your revenue streams to potential changes in organic search due to SGE", 
        0, 100, 50, help="0% being not resilient at all, 100% being fully resilient"
    )
    
    employees_ready_for_AI = st.slider(
        "Rate how prepared your workforce is for AI advancements and integration", 
        0, 100, 50, help="0% being not prepared at all, 100% being fully prepared"
    )
    
    brand_recognized_in_SGE = st.slider(
        "Rate the recognition of your brand in SGE-driven search results", 
        0, 100, 50, help="0% being not recognized at all, 100% being highly recognized"
    )
    
    customer_acquisition_channels_diversified = st.slider(
        "Rate the diversification of your customer acquisition channels beyond organic search", 
        0, 100, 50, help="0% being not diversified at all, 100% being fully diversified"
    )
    
    content_uniquely_valuable = st.slider(
        "Rate the uniqueness and value of your content in being difficult to replicate by AI", 
        0, 100, 50, help="0% being easily replicable, 100% being highly unique and valuable"
    )
    
    market_growing_with_SGE = st.slider(
        "Rate your perception of the market growth with the advent of SGE", 
        0, 100, 50, help="0% being shrinking market, 100% being rapidly growing market"
    )
    
    competition_lagging_in_AI_adaptation = st.slider(
        "Rate how much your competition is lagging in adapting to AI", 
        0, 100, 50, help="0% being at the same pace or ahead, 100% being significantly behind"
    )
    
    socio_political_trends_supportive_of_AI = st.slider(
        "Rate the supportiveness of socio-political trends for AI integration in your industry", 
        0, 100, 50, help="0% being not supportive, 100% being highly supportive"
    )
    
    technological_infrastructure = st.slider(
        "Rate the advancement of your technological infrastructure for integrating and leveraging AI technologies", 
        0, 100, 50, help="0% being outdated, 100% being state-of-the-art"
    )
    
    innovation_capability = st.slider(
        "Rate your company's capability for innovation and adopting new technologies", 
        0, 100, 50, help="0% being very low capability, 100% being very high capability"
    )
    
    market_trends_awareness = st.slider(
        "Rate your company's awareness of and active monitoring of market trends related to SGE and AI", 
        0, 100, 50, help="0% being unaware, 100% being highly aware and actively monitoring"
    )
    
    customer_behavior_changes = st.slider(
        "Rate the significance of changes in customer behavior due to advancements in AI and search technologies", 
        0, 100, 50, help="0% being no change, 100% being significant changes observed"
    )
    
    external_economic_factors = st.slider(
        "Rate the impact of external economic factors on your business (e.g., recession, rapid growth)", 
        -100, 100, 0, help="-100% being high risk, 100% being high opportunity, 0% being neutral"
    )

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
        "customer_acquisition_channels_diversified": customer_acquisition_channels_diversified,
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
    swot_categories = {"Strengths": [], "Weaknesses": [], "Opportunities": [], "Threats": []}
    
    analysis_functions = [analyze_seo_channel_impact, analyze_digital_advertising_impact, evaluate_channel_diversification]
    for func in analysis_functions:
        result = func(user_inputs["customer_acquisition_channel"])
        if result:  # Check if result is not None
            category, message = result
            swot_categories[category].append(message)

    if user_inputs["resources_adaptable_to_SGE"] > 75:
        swot_categories["Strengths"].append("High adaptability of resources to SGE changes")
    elif user_inputs["resources_adaptable_to_SGE"] < 25:
        swot_categories["Weaknesses"].append("Low adaptability of resources to SGE changes")

    # Revenue streams resilient to SGE
    if user_inputs["revenue_streams_resilient_to_SGE"] > 75:
        swot_categories["Strengths"].append("Resilient revenue streams to SGE changes")
    elif user_inputs["revenue_streams_resilient_to_SGE"] < 25:
        swot_categories["Weaknesses"].append("Vulnerable revenue streams to SGE changes")

    # Employees ready for AI
    if user_inputs["employees_ready_for_AI"] > 75:
        swot_categories["Strengths"].append("Workforce well-prepared for AI advancements")
    elif user_inputs["employees_ready_for_AI"] < 25:
        swot_categories["Weaknesses"].append("Workforce poorly prepared for AI advancements")

    # Brand recognized in SGE
    if user_inputs["brand_recognized_in_SGE"] > 75:
        swot_categories["Strengths"].append("Strong brand recognition in SGE-driven search results")
    elif user_inputs["brand_recognized_in_SGE"] < 25:
        swot_categories["Weaknesses"].append("Low brand recognition in SGE-driven search results")

    # Customer acquisition channels diversified
    if user_inputs["customer_acquisition_channels_diversified"] > 75:
        swot_categories["Strengths"].append("Well-diversified customer acquisition channels")
    elif user_inputs["customer_acquisition_channels_diversified"] < 25:
        swot_categories["Weaknesses"].append("Poorly diversified customer acquisition channels")

    # Content uniquely valuable
    if user_inputs["content_uniquely_valuable"] > 75:
        swot_categories["Strengths"].append("Highly unique and valuable content difficult to replicate by AI")
    elif user_inputs["content_uniquely_valuable"] < 25:
        swot_categories["Weaknesses"].append("Content easily replicable by AI, lacking uniqueness")

    # Additional factors integration
    # Technological infrastructure, innovation capability, market trends awareness, etc.
    # Similar logic applies to these as shown above

    # Market growing with SGE
    if user_inputs["market_growing_with_SGE"] > 75:
        swot_categories["Opportunities"].append("Growing market with the advent of SGE")
    elif user_inputs["market_growing_with_SGE"] < 25:
        swot_categories["Threats"].append("Market challenges with the advent of SGE")

    # Competition lagging in AI adaptation
    if user_inputs["competition_lagging_in_AI_adaptation"] > 75:
        swot_categories["Opportunities"].append("Competitive advantage with faster AI adaptation")
    elif user_inputs["competition_lagging_in_AI_adaptation"] < 25:
        swot_categories["Threats"].append("Risk of falling behind in AI adaptation")

    # Socio-political trends supportive of AI
    if user_inputs["socio_political_trends_supportive_of_AI"] > 75:
        swot_categories["Opportunities"].append("Favorable socio-political environment for AI integration")
    elif user_inputs["socio_political_trends_supportive_of_AI"] < 25:
        swot_categories["Threats"].append("Challenges from socio-political environment for AI integration")

    # External economic factors
    if user_inputs["external_economic_factors"] > 0:
        swot_categories["Opportunities"].append("Positive impact from external economic conditions")
    elif user_inputs["external_economic_factors"] < 0:
        swot_categories["Threats"].append("Negative impact from external economic conditions")

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
    setup_streamlit()
    user_inputs = setup_user_input_forms()
    if st.button("Perform SWOT Analysis"):
        swot_results = perform_detailed_swot_analysis(user_inputs)
        display_swot_matrix(swot_results)

if __name__ == "__main__":
    main()
    
