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
    st.subheader("Inspired by Growth Memo #235 - SWOTing SGE")
    st.link_button("Read it here", "https://www.growth-memo.com/p/sge-swot-analysis?utm_source=kevinkirchhoff&utm_medium=referral")
    
    st.divider()
def setup_user_input_forms():
    st.subheader("Please answer the following questions based on your company's current situation:")
    # User inputs
    business_model = st.selectbox("What is your business model?", ["E-commerce", "Local business", "SaaS", "Affiliate", "Publisher", "Consumer", "Retail", "B2B-Services"])
    seo_model = st.selectbox(
        "What is your SEO model?", 
        ["Aggregator", "Integrator"], help="""
        **Aggregators** and **Integrators** have fundamentally different approaches to growth:

        - **Aggregators** channel demand through superior user experience and free distribution. They leverage network effects by consolidating demand (e.g., Google, Amazon).
        
        - **Integrators** own the entire value chain (suppliers, production, distribution) and focus on maximizing margins by providing unique value and controlling distribution (e.g., Apple, Peloton).
        
        Choose the model that best describes your company's approach.
        """
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
    company_size = st.selectbox("What is your company size?", ["Micro (1-10 employees)", "Small (11-50 employees)", "Medium (51-250 employees)", "Large (251-500 employees)", "Enterprise (500+ employees)"])
    reliance_on_SEO = st.slider("What percentage of your customer acquisition relies on SEO?", 0, 100, 50, help="0% being no reliance at all, 100% being fully reliant on SEO")
    resources_adaptable_to_SGE = st.slider("Rate the adaptability of your resources to changes brought by generative AI technologies", 0, 100, 50, help="0% being not adaptable at all, 100% being fully adaptable")
    employees_ready_for_AI = st.slider("Rate how prepared your workforce is for AI advancements and integration", 0, 100, 50, help="0% being not prepared at all, 100% being fully prepared")
    brand_recognition = st.slider("Rate your brand recognition in search engines", 0, 100, 50, help="0% being not recognized at all, 100% being highly recognized")
    content_uniquely_valuable = st.slider("Rate the uniqueness and value of your content in being difficult to replicate by AI", 0, 100, 50, help="0% being easily replicable, 100% being highly unique and valuable")
    market_trends_awareness = st.slider("Rate your company's awareness of and active monitoring of market trends related to generative AI and search technologies", 0, 100, 50, help="0% being unaware, 100% being highly aware and actively monitoring")
    external_economic_factors = st.slider("Rate the impact of external economic factors on your business", -100, 100, 0, help="-100% being high risk, 100% being high opportunity, 0% being neutral")

    return {
        "business_model": business_model,
        "seo_model": seo_model,
        "competitive_landscape": competitive_landscape,
        "company_size": company_size,
        "reliance_on_SEO": reliance_on_SEO,
        "resources_adaptable_to_SGE": resources_adaptable_to_SGE,
        "employees_ready_for_AI": employees_ready_for_AI,
        "brand_recognition": brand_recognition,
        "content_uniquely_valuable": content_uniquely_valuable,
        "market_trends_awareness": market_trends_awareness,
        "external_economic_factors": external_economic_factors,
    }
    
def perform_detailed_swot_analysis(user_inputs):       
    swot_categories = {"Strengths": [], "Weaknesses": [], "Opportunities": [], "Threats": []}

    # Business Model Evaluation with focus on SGE
    if user_inputs["business_model"] == "E-commerce":
        if user_inputs["seo_model"] == "Integrator":
            swot_categories["Opportunities"].append(
                "SGE enhances product discoverability and detailed comparisons, favoring e-commerce sites with rich, structured data."
            )
        elif user_inputs["seo_model"] == "Aggregator":
            swot_categories["Threats"].append(
                "Aggregators may face competition from direct brands in SGE, which could prioritize original content and direct data sources."
            )

    elif user_inputs["business_model"] == "SaaS":
        swot_categories["Opportunities"].append(
            "SGE offers a platform for SaaS companies to highlight unique software solutions through conversational search queries."
        )

    elif user_inputs["business_model"] == "Local business":
        if user_inputs["company_size"] in ["Large", "Enterprise"]:
            swot_categories["Opportunities"].append(
                "Large local businesses or chains might leverage SGE for better visibility in local and conversational search results."
            )
        else:
            swot_categories["Weaknesses"].append(
                "Smaller local businesses need to ensure high-quality, unique content to compete in SGE-driven local searches."
            )

    elif user_inputs["business_model"] == "Publisher":
        if user_inputs["content_uniquely_valuable"] > 90:
            swot_categories["Opportunities"].append(
                "Publishers with high-quality, unique content can leverage SGE for authoritative answers, driving user engagement."
            )
        else:
            swot_categories["Threats"].append(
                "SGE poses a risk of reducing traffic to publishers if their content does not stand out or directly answer user queries."
            )

    elif user_inputs["business_model"] == "Affiliate":
        if user_inputs["content_uniquely_valuable"] > 90:
            swot_categories["Opportunities"].append(
                "Unique and authoritative content may capture SGE attention, maintaining affiliate traffic."
            )
        else:
            swot_categories["Threats"].append(
                "Affiliates face significant threats from SGE if it directly answers queries, potentially bypassing referral links."
            )
    elif user_inputs["business_model"] == "B2B-Services":
        if user_inputs["content_uniquely_valuable"] > 75:
            swot_categories["Opportunities"].append(
                "Unique B2B content can leverage SGE to highlight niche expertise and drive targeted leads."
            )
        else:
            swot_categories["Threats"].append(
                "Lack of distinctive content may limit visibility in SGE, impacting lead generation."
            )

    elif user_inputs["business_model"] == "Consumer":
        swot_categories["Opportunities"].append(
            "Consumer brands can utilize SGE to enhance user engagement and personalize experiences."
        )
    
    # General evaluations
    general_evaluations(user_inputs, swot_categories)

    return swot_categories

def general_evaluations(user_inputs, swot_categories):
    # Evaluates SEO reliance, content value, competitive landscape, and other general factors

    # Reliance on SEO evaluation
    if user_inputs["reliance_on_SEO"] > 50:
        swot_categories["Threats"].append(
            "High reliance on SEO may lead to vulnerabilities as SGE changes search dynamics."
        )
    else:
        swot_categories["Strengths"].append(
            "Low reliance on SEO indicates diversified acquisition channels, offering resilience against SGE changes."
        )

    # Content uniqueness evaluation
    if user_inputs["content_uniquely_valuable"] > 75:
        swot_categories["Strengths"].append(
            "High-quality, unique content positions the company well for visibility in SGE's nuanced search results."
        )
    else:
        swot_categories["Weaknesses"].append(
            "Generic content risks being overshadowed in SGE, emphasizing the need for distinctiveness."
        )

    # Competitive landscape evaluation
    competitive_landscape = user_inputs["competitive_landscape"]
    if competitive_landscape == "Monopoly" or competitive_landscape == "Stable":
        swot_categories["Strengths"].append(
            f"A {competitive_landscape.lower()} market position offers a strong foundation for leveraging SGE to solidify market dominance."
        )
    elif competitive_landscape == "Dog fight" or competitive_landscape == "Emerging":
        swot_categories["Opportunities"].append(
            f"In a {competitive_landscape.lower()} market, SGE presents opportunities for market differentiation and capturing new segments."
        )
        swot_categories["Threats"].append(
            f"A {competitive_landscape.lower()} competitive landscape increases the urgency for innovation and adaptability in response to SGE advancements."
        )
    # Adaptability of resources to SGE and AI technologies
    if user_inputs["resources_adaptable_to_SGE"] > 75:
        swot_categories["Strengths"].append("High adaptability of resources to generative AI changes positions the company favorably for future technological shifts.")
    elif user_inputs["resources_adaptable_to_SGE"] < 25:
        swot_categories["Weaknesses"].append("Low adaptability of resources to generative AI changes may hinder the company's ability to respond to technological advancements.")

    # Workforce preparedness for AI
    if user_inputs["employees_ready_for_AI"] > 75:
        swot_categories["Strengths"].append("A workforce well-prepared for AI advancements enhances the company's innovative capacity and readiness for future challenges.")
    elif user_inputs["employees_ready_for_AI"] < 25:
        swot_categories["Weaknesses"].append("A workforce poorly prepared for AI advancements may slow down the company's adaptation to technological changes.")

    # Brand recognition evaluation
    if user_inputs["brand_recognition"] > 75:
        swot_categories["Strengths"].append("Strong brand recognition in search engines could lead to better visibility and authority in generative AI-driven search results.")
    elif user_inputs["brand_recognition"] < 25:
        swot_categories["Weaknesses"].append("Low brand recognition in search engines may limit visibility in generative AI-driven search enhancements.")

    # Market trends awareness
    if user_inputs["market_trends_awareness"] > 75:
        swot_categories["Strengths"].append("High awareness of market trends related to generative AI and search technologies enables proactive strategic planning.")
    else:
        swot_categories["Threats"].append("Lack of awareness or active monitoring of generative AI and search technology trends could lead to missed opportunities and strategic misalignments.")

    # External economic factors
    if user_inputs["external_economic_factors"] > 0:
        swot_categories["Opportunities"].append("Positive external economic conditions could provide growth opportunities and financial stability.")
    elif user_inputs["external_economic_factors"] < 0:
        swot_categories["Threats"].append("Adverse external economic conditions may pose financial and operational risks.")

def display_swot_matrix(swot_categories):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Strengths")
        for strength in swot_categories["Strengths"]:
            st.write(f"- {strength}")
        
        st.subheader("Opportunities")
        for opportunity in swot_categories["Opportunities"]:
            st.write(f"- {opportunity}")
        
    with col2:
        st.subheader("Weaknesses")
        for weakness in swot_categories["Weaknesses"]:
            st.write(f"- {weakness}")

        
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
    
