import json
import pandas as pd


# Load JSON file
with open("C:\\ai_ml_project\\train.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract useful fields
rows = []

for article in data['data']:
    for paragraph in article['paragraphs']:
        context = paragraph['context']
        for qa in paragraph['qas']:
            question = qa['question']
            answers = qa['answers']
            
            # Take first answer
            answer_text = answers[0]['text'] if answers else ""

            rows.append({
                "context": context,
                "question": question,
                "answer": answer_text
            })

# Convert to DataFrame
df = pd.DataFrame(rows)

# Save as Excel
df.to_excel("C:\\ai_ml_project\\squad_dataset.xlsx", index=False)

print("✅ Conversion completed! File saved as squad_dataset.xlsx")