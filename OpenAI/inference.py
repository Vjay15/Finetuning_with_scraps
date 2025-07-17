import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv("../apikey.env")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
st.set_page_config(
    page_title="Fine Tuned Model Inference",
    layout="wide",  
    initial_sidebar_state="expanded"
)

st.title("Inferencing Fine Tuned Model")

# Create two columns
col1, col2 = st.columns([5,5])

# Left side - Input Form
with col1:
    st.header("Input Form")
    question = st.text_input("Enter the question")
    marks = st.number_input("Enter the marks", min_value=0, max_value=10, value=2)
    
    rubrics = False
    if st.checkbox("Provide rubrics:"):
        rubric = st.text_area("Enter the rubric", height=100)
        rubrics = True
    
    answer = st.text_area("Enter the answer", height=200)
    difficulty = st.selectbox("Select the difficulty level", ["easy", "medium", "hard"])

# Right side - Results
with col2:
    st.header("Evaluation Results")
    
    def validate_fields():
        errors = []
        if not question.strip():
            errors.append("Question is required")
        if not answer.strip():
            errors.append("Answer is required")
        if not difficulty:
            errors.append("Difficulty level is required")
        if rubrics and not rubric.strip():
            errors.append("Rubric is required when the checkbox is selected")
        return errors

    message_content = {
        "question": question,
        "marks": marks,
        "rubric": rubric if 'rubric' in locals() else "No rubric provided",
        "answer": answer,
        "difficulty": difficulty
    }

    message_data = json.dumps(message_content)

    if st.button("Evaluate Answer", type="primary"):
        validation_errors = validate_fields()
        if validation_errors:
            for error in validation_errors:
                st.error(f"❌ {error}")
        else:
            with st.spinner("Evaluating..."):
                try:
                    response = client.chat.completions.create(
                        model="ft:gpt-4.1-mini-2025-04-14:greatify::BrMVNxDG",
                        messages=[
                            {
                                "role": "system", 
                                "content": "You are an expert answer evaluator. Your job is to evaluate student answers fairly based on a flexible rubric and the specified difficulty level, dont mention the difficulty level in your explanation.\n\nInstructions:\n1. Return the score out of the total marks.\n2. Give a brief explanation justifying the score, referencing key points from the rubric.\n3. Suggest at least one specific way the student can improve their answer quality or overall academic performance as feedback.\n4. Use the rubric as a guideline, not a rigid checklist and if Rubric is not provided, then create your very own rubric.\n5. Adjust the strictness of grading based on difficulty:\n   - 'easy' → lenient evaluation; minor issues can be overlooked.\n   - 'medium' → balanced and reasonable evaluation.\n   - 'hard' → stricter evaluation; all points must be well explained and accurate."
                            },
                            {
                                "role": "user", 
                                "content": message_data
                            }
                        ]
                    )
                    
                    st.success("✅ Evaluation Complete!")
                    st.markdown("### Results:")
                    result = json.loads(response.choices[0].message.content)
                    st.text("Score: " + result["Score"])
                    st.text("Explanation: " + result["Explanation"])
                    st.text("Feedback: " + result["Feedback"])
                    
                    
                except Exception as e:
                    st.error(f"❌ Error during evaluation: {str(e)}")
    
    # Show input preview
    if st.checkbox("Show Input Preview"):
        st.json(message_content)