import pandas as pd
from clean_data import clean_text

# Load dataset
df = pd.read_csv("../dataset/spam.csv")

# Apply text cleaning
df['cleaned_text'] = df['text'].apply(clean_text)

# Remove duplicate messages
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("../dataset/cleaned_data.csv", index=False)

print("Preprocessing completed!")
