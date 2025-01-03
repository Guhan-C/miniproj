import pandas as pd
import language_tool_python

# Load the TSV file
file_path = r"D:\INTEGRATED MSC DATA SCIENCE\8th SEMESTER\MiniProject\Dataset\archive\cola_public\raw\in_domain_train.tsv"
  # Replace with the path to your TSV file
data = pd.read_csv(file_path, sep='\t', header=None, names=["Source","Label","Wrong","Sentence"])

ungrammatical_sentences = data[data["Label"] == 0]

# Initialize LanguageTool
tool = language_tool_python.LanguageTool('en-US')

# Analyze grammatical errors
errors_data = []
for sentence in ungrammatical_sentences["Sentence"]:
    matches = tool.check(sentence)
    errors = [{"ruleId": match.ruleId, "message": match.message, "suggestions": match.replacements} for match in matches]
    errors_data.append({"Sentence": sentence, "Errors": errors})

# Convert errors to DataFrame
errors_df = pd.DataFrame(errors_data)

# Save to a CSV file for analysis
errors_df.to_csv("grammar_errors_label_0.csv", index=False)

print("Analysis complete. Saved to 'grammar_errors_label_0.csv'")


# Filter sentences with label 0



