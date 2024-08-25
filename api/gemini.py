import google.generativeai as genai
import typing_extensions as typing
import json

class GoatQuiz(typing.TypedDict):
    Question: str
    Answer: bool

def AIMatchmake():
    genai.configure(api_key='AIzaSyB7y9Bji5w_rlYPkn6bdwbt83kKMjK7yvw')

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        generation_config={
            "response_mime_type": "application/json",
            "response_schema": GoatQuiz 
        }
    )

    prompt = """
        Write a short quiz related to the 17 Sustainable Development Goals of the United Nations in Korean.
        The answer should be true or false.
    """

    response = genai.generate_text(prompt=prompt)
    print(response)
    if not response or not hasattr(response, 'result') or response.result is None:
            raise ValueError("The AI model did not return any output.")
    
    generated_text = response.result
    
    # Assuming the response is directly JSON serializable as per the prompt request
    try:
        quiz_data = json.loads(generated_text)
    except json.JSONDecodeError:
        raise ValueError("The AI model did not return a valid JSON response.")
    
    # Validate against the GoatQuiz structure
    for item in quiz_data:
        if not isinstance(item, dict) or 'Question' not in item or 'Answer' not in item:
            raise ValueError("The AI model returned data that doesn't match the GoatQuiz schema.")

    return quiz_data