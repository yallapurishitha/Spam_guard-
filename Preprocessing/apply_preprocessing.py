import pandas as pd
from clean_data import clean_text

# Load SMS dataset
df = pd.read_csv(
    "../dataset/sms/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Remove missing values and duplicates
df = df.dropna()
df = df.drop_duplicates()

# Clean messages
df["cleaned_text"] = df["message"].apply(clean_text)

# Save cleaned dataset
df.to_csv("../dataset/sms/cleaned_sms.csv", index=False)

print("SMS preprocessing completed!")
