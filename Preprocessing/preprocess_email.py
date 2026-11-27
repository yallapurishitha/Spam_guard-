import pandas as pd
from clean_data import clean_text

# Load email dataset directly from ZIP
df = pd.read_csv(
    "../dataset/email/enron_spam_data (2).zip",
    compression="zip"
)

# Remove missing values
df = df.dropna(subset=["Message", "Spam/Ham"])

# Combine subject and message
df["text"] = (
    df["Subject"].fillna("").astype(str)
    + " "
    + df["Message"].fillna("").astype(str)
)

# Clean email text
df["cleaned_text"] = df["text"].apply(clean_text)

# Remove duplicates
df = df.drop_duplicates(subset=["cleaned_text", "Spam/Ham"])

# Save cleaned dataset
df.to_csv("../dataset/email/cleaned_email.csv", index=False)

print("Email preprocessing completed!")
