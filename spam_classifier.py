# spam_classifier.py
# Naive Bayes ML model for Spam Email Classification
# Author: VarshithaMandapati

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load dataset (make sure you have 'spam.csv' in the same folder)
data = pd.read_csv("spam.csv", encoding="latin-1")
data = data[['v1', 'v2']]
data.columns = ['label', 'message']
data['label_num'] = data.label.map({'ham':0, 'spam':1})

X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label_num'], test_size=0.2, random_state=42)
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", round(accuracy,4))

sample_msg = ["Congratulations! You've won a free ticket. Reply now!"]
sample_vec = vectorizer.transform(sample_msg)
prediction = model.predict(sample_vec)[0]
pred_label = "spam" if prediction==1 else "ham"
print("Sample Message Prediction:", pred_label)

with open("spam_output.txt", "w") as f:
    f.write(f"Model Accuracy: {accuracy:.4f}\n")
    f.write(f"Sample Message Prediction: {pred_label}\n")
