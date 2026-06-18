class SustainabilityRecommender:
    """
    Combines user consumption data with RAG knowledge to provide
    hyper-personalized sustainability advice.
    """
    
    @staticmethod
    def generate_personalized_prompt(data, context=""):
        """
        Creates a detailed prompt for the AI based on user footprint.
        """
        breakdown = data['footprint']['breakdown']
        total = data['footprint']['total']
        score = data['score']['score']
        grade = data['score']['grade']
        
        prompt = f"""
        User Sustainability Profile:
        - Total Monthly Carbon Footprint: {total} kg CO2e
        - Sustainability Score: {score}/100 (Grade: {grade})
        - Breakdown:
            * Electricity: {breakdown['Electricity']} kg CO2e
            * Water: {breakdown['Water']} kg CO2e
            * Travel: {breakdown['Travel']} kg CO2e ({data['inputs']['travel_km']} km via {data['inputs']['transport_mode']})
        
        Retrieved Knowledge:
        {context}
        
        Task:
        1. Identify the biggest area for improvement for this user.
        2. Provide 3 specific, actionable recommendations to reduce their footprint.
        3. Estimate the potential monthly CO2 savings and monetary savings if they follow these.
        4. Align your advice with SDG 7 (Energy), 12 (Consumption), and 13 (Climate Action).
        
        Format your response with clear headings and bullet points.
        """
        return prompt

    @staticmethod
    def get_advice(data, ai_client, rag_pipeline):
        # 1. Determine the primary area of concern
        breakdown = data['footprint']['breakdown']
        max_source = max(breakdown, key=breakdown.get)
        
        # 2. Retrieve specific knowledge for that source
        query = f"How to reduce {max_source} consumption and carbon footprint?"
        retriever = rag_pipeline.get_retriever()
        context = ""
        if retriever:
            docs = retriever.get_relevant_documents(query)
            context = "\n\n".join([doc.page_content for doc in docs])
            
        # 3. Generate response
        prompt = SustainabilityRecommender.generate_personalized_prompt(data, context)
        response = ai_client.get_response(prompt, system_prompt="You are a Senior Sustainability Architect.")
        
        return response
