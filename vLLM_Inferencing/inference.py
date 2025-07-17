from openai import OpenAI
model_id = "meta-llama/Meta-Llama-3-8B"  # Modify OpenAI's API key and API base to use vLLM's API server.
openai_api_key = "EMPTY"
openai_api_base = "https://treatments-frost-minor-creation.trycloudflare.com/v1" #Using Cloudflare Tunneling
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

prompts = alpaca_prompt.format("You are an expert answer evaluator. Your job is to evaluate student answers fairly based on a flexible rubric and the specified difficulty level.\n\nInstructions:\n1. Return the score out of the total marks.\n2. Give a detailed explanation justifying the score, referencing key points from the rubric.\n3. Suggest at least one specific way the student can improve their answer quality or overall academic performance.\n4. Use the rubric as a guideline, not a rigid checklist.\n5. Adjust the strictness of grading based on difficulty:\n   - 'easy' → lenient evaluation; minor issues can be overlooked.\n   - 'medium' → balanced and reasonable evaluation.\n   - 'hard' → stricter evaluation; all points must be well explained and accurate.",
        "{\"question\": \"Trace the sequence of events which occur when a bright light is focused on your eyes.\", \"answer\": \"The pupil gets small due to light. This protects the eyes from damage caused by too much light.\", \"rubrics\": \"1 mark for pupil detecting and reacting to bright light, 1 mark for iris contraction, 1 mark for pupil becoming smaller to reduce light entry.\", \"score\": 3, \"difficulty\": \"easy\"}",
        "",
     )
completion = client.completions.create(model="sci",
                                      prompt=prompts, temperature=0.7, top_p=0.9, max_tokens=500)
print("LoRA_1 result:", completion.choices[0].text)
prompts = alpaca_prompt.format("You are an expert answer evaluator. Your job is to evaluate student answers fairly based on a flexible rubric and the specified difficulty level.\n\nInstructions:\n1. Return the score out of the total marks.\n2. Give a detailed explanation justifying the score, referencing key points from the rubric.\n3. Suggest at least one specific way the student can improve their answer quality or overall academic performance.\n4. Use the rubric as a guideline, not a rigid checklist.\n5. Adjust the strictness of grading based on difficulty:\n   - 'easy' → lenient evaluation; minor issues can be overlooked.\n   - 'medium' → balanced and reasonable evaluation.\n   - 'hard' → stricter evaluation; all points must be well explained and accurate.",
        "{\"question\": \"Examine the interdependent relationship among nature, technology and institutions in the economic development.\", \"marks\": 3, \"rubric\": \"1 mark for explaining the role of nature (providing resources). 1 mark for explaining the role of technology (means of utilization). 1 mark for explaining the role of institutions (framework for development).\", \"answer\": \"Nature gives us things. Technology is there. Institutions are also part of it.\", \"difficulty\": \"hard\"}",
        "",
     )
completion = client.completions.create(model="soc",
                                      prompt=prompts, temperature=0.0, max_tokens=500)
print("LoRA_2 result:", completion.choices[0].text)