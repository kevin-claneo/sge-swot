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
     
    reliance_on_SEO = st.slider(
        "What percentage of your customer acquisition relies on SEO?",
        0, 100, 25, help="0% being no reliance at all, 100% being fully reliant on SEO"
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
        "reliance_on_SEO": reliance_on_SEO,
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



        
def perform_detailed_swot_analysis(user_inputs):
    swot_categories = {"Strengths": [], "Weaknesses": [], "Opportunities": [], "Threats": []}
    
    if user_inputs["business_model"] in ["E-commerce", "SaaS"]:
        swot_categories["Opportunities"].append("Digital-first business model well-positioned for online growth")
    else:
        swot_categories["Strengths"].append("Diverse business model reduces reliance on single market trends")

    # Evaluate SEO model impact
    if user_inputs["seo_model"] == "Aggregator":
        swot_categories["Weaknesses"].append("Aggregator model may face challenges with content uniqueness in SGE")
    elif user_inputs["seo_model"] == "Integrator":
        swot_categories["Strengths"].append("Integrator model's control over value chain could offer competitive edge")

    # Industry-specific SWOT adjustments
        industry_impacts = {
        "Advertising & Marketing": {
            "Opportunities": ["Leveraging SGE for targeted advertising and personalized marketing campaigns"],
            "Threats": ["Increased ad complexity and competition"]
        },
        "Aerospace & Defense": {
            "Strengths": ["Advanced technological infrastructure can leverage AI for innovation"],
            "Threats": ["Security risks associated with AI-driven systems"]
        },
        "Agriculture": {
            "Opportunities": ["Use of AI for predictive analytics in crop management"],
            "Threats": ["Dependence on AI for critical decisions without understanding AI limitations"]
        },
        "Automotive": {
            "Strengths": ["Integration of AI in vehicles for enhanced user experience"],
            "Weaknesses": ["Challenges in adopting AI at scale due to regulatory and safety concerns"]
        },
        "Banking & Finance": {
            "Strengths": ["High-value proprietary financial data"],
            "Threats": ["Risk of financial misinformation through AI hallucinations"]
        },
        "Biotechnology": {
            "Opportunities": ["AI-driven research and development"],
            "Threats": ["Ethical and safety concerns with AI in biotech"]
        },
        "Chemicals": {
            "Opportunities": ["AI for optimizing chemical manufacturing processes"],
            "Threats": ["Intellectual property risks with AI-driven discoveries"]
        },
        "Construction": {
            "Strengths": ["AI for project management and efficiency"],
            "Weaknesses": ["Adaptability to AI-driven design and planning tools"]
        },
        "Consumer Goods & Services": {
            "Opportunities": ["Enhanced customer service through AI"],
            "Threats": ["Commoditization of consumer goods through AI-driven marketplaces"]
        },
        "Education": {
            "Opportunities": ["Personalized learning experiences through AI"],
            "Threats": ["AI content generation overshadowing critical thinking and learning processes"]
        },
        "Energy": {
            "Opportunities": ["AI for efficient energy management and distribution"],
            "Threats": ["Cybersecurity risks in critical energy infrastructure"]
        },
        "Entertainment & Leisure": {
            "Strengths": ["Engaging content creation using AI"],
            "Weaknesses": ["Loss of creative jobs to AI"]
        },
        "Food & Beverages": {
            "Opportunities": ["AI in supply chain optimization"],
            "Threats": ["Challenges in maintaining food safety standards with AI-driven processes"]
        },
        "Healthcare": {
            "Strengths": ["Proprietary data as a competitive advantage"],
            "Threats": ["Misrepresentation of health information through AI hallucinations"]
        },
        "Hospitality": {
            "Opportunities": ["AI-driven customer service enhancements"],
            "Threats": ["Depersonalization of guest experiences"]
        },
        "Information Technology": {
            "Strengths": ["Frontier of AI advancements"],
            "Weaknesses": ["Rapid pace of technological change requires continuous adaptation"]
        },
        "Insurance": {
            "Opportunities": ["AI for personalized insurance products"],
            "Threats": ["Data privacy concerns with AI-driven risk assessments"]
        },
        "Manufacturing": {
            "Strengths": ["Efficiency gains through AI in manufacturing processes"],
            "Weaknesses": ["High costs of integrating AI into existing systems"]
        },
        "Media": {
            "Opportunities": ["Content customization and recommendation through AI"],
            "Threats": ["AI-driven content creation challenging traditional media's value"]
        },
        "Pharmaceuticals": {
            "Opportunities": ["Accelerated drug discovery through AI"],
            "Threats": ["Regulatory challenges in validating AI-driven research"]
        },
        "Real Estate": {
            "Opportunities": ["AI for market analysis and investment insights"],
            "Threats": ["Dependence on AI algorithms for pricing and valuation"]
        },
        "Retail": {
            "Opportunities": ["Enhanced online shopping experiences", "Integration with voice search and AI-driven assistants"],
            "Threats": ["Increased competition from better-optimized SGE content"]
        },
        "Telecommunications": {
            "Strengths": ["Use of AI for network optimization and customer service"],
            "Weaknesses": ["Adapting to AI-driven changes in consumer communication habits"]
        },
        "Transportation & Logistics": {
            "Opportunities": ["AI for route optimization and logistics management"],
            "Threats": ["Automation displacing jobs in transportation"]
        },
        "Utilities": {
            "Strengths": ["AI for grid management and predictive maintenance"],
            "Weaknesses": ["Investment and adaptation to AI technologies"]
        }
    }
    
    # Incorporate industry-specific impacts into SWOT
    industry_specifics = industry_impacts.get(user_inputs["industry"], {})
    for category, impacts in industry_specifics.items():
        swot_categories[category].extend(impacts)
        
    if user_inputs["business_model"] in ["E-commerce", "SaaS"]:
        swot_categories["Opportunities"].append("Digital-first business model well-positioned for online growth")
    else:
        swot_categories["Strengths"].append("Diverse business model reduces reliance on single market trends")

    if user_inputs["resources_adaptable_to_SGE"] > 75:
        swot_categories["Strengths"].append("High adaptability of resources to SGE changes")
    elif user_inputs["resources_adaptable_to_SGE"] < 25:
        swot_categories["Weaknesses"].append("Low adaptability of resources to SGE changes")
        
    if user_inputs["reliance_on_SEO"] > 50:
        swot_categories["Weaknesses"].append("High reliance on SEO poses risk with algorithm changes")
    else:
        swot_categories["Strengths"].append("Balanced customer acquisition strategy beyond SEO")
        
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
    
