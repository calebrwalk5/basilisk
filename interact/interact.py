import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from transformers import AutoTokenizer
from transformers import TFGPT2LMHeadModel

# Load the model and tokenizer
model = tf.compat.v1.train.import_meta_graph('models/124M/model.ckpt.meta')
model.restore(tf.compat.v1.train.latest_checkpoint('models/124M/'))
tokenizer = AutoTokenizer.from_pretrained("gpt2")

def generate_text(prompt):
    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="tf")
    
    # Generate text
    generated_text = model.predict(input_ids)
    
    # Decode the generated text
    generated_text = tokenizer.decode(generated_text.numpy()[0], skip_special_tokens=True)
    
    return generated_text

prompt = input("Enter a prompt to generate text: ")
generated_text = generate_text(prompt)
print(generated_text)