from sentence_transformers import SentenceTransformer, util
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

model = SentenceTransformer('all-mpnet-base-v2')

df = pd.read_csv("harry_potter_spells.csv")

spell_embeddings = model.encode(df["description"].tolist(), convert_to_tensor=True)

@app.route('/suggest', methods = ["POST"])

def suggest_spell():
    data = request.json
    user_input = data.get("problem","")
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(user_embedding, spell_embeddings)
    best_match_idx = similarities.argmax().item()
    
    result ={
        "spell": df.iloc[best_match_idx]["name"],
        "description": df.iloc[best_match_idx]["description"]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)