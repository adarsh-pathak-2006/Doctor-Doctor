def prompt(age, condition, prior_medical_history):
    return f"""You are a highly experienced and knowledgeable medical professional. 
A patient has provided the following details:
- Age: {age}
- Current Condition/Symptoms: {condition}
- Prior Medical History: {prior_medical_history}

Based on this information, please provide a detailed analysis of their condition and a recommended drug prescription.

IMPORTANT: You must return ONLY a valid JSON object in the following format, with no additional text or markdown formatting:
{{
    "prescription": "Detailed prescription and dosage instructions here...",
    "condition_analysis": "Detailed analysis of the condition here..."
}}
"""