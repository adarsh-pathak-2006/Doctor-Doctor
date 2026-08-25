from .prompt import prompt
from .ai import generate_response

def final_response(age, condition, prior_conditions):
    final_prompt=prompt(age=age, condition=condition, prior_medical_history=prior_conditions)
    response=generate_response(defined_prompt=final_prompt)
    return response