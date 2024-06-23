from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Specify the local path where your model is saved
def Load_model():
    local_model_path = "./model"
    # Load the tokenizer and model from the local directory
    tokenizer = AutoTokenizer.from_pretrained(local_model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(local_model_path)

    return model, tokenizer

# Function to generate a summary
def generate_summary(model, tokenizer, text, max_input_length=512, max_output_length=150, num_beams=4):
    # Tokenize the input text
    inputs = tokenizer(
        text, 
        return_tensors="pt", 
        max_length=max_input_length, 
        truncation=True
    )
    
    # Generate summary tokens
    summary_ids = model.generate(
        inputs["input_ids"], 
        max_length=max_output_length,       # Adjust max length of the summary
        num_beams=num_beams,                # Adjust the number of beams for beam search
        early_stopping=True                 # Stop early if all beam searches finish early
    )
    
    # Decode the summary tokens
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary