# 📧 Spam Email Classifier (Python + C + scikit-learn)

## Overview
This project demonstrates a **Naive Bayes classifier** for detecting spam messages using Python & scikit-learn, and integrates a C program to read the Python output.  

## Tech Used
- Python (basic syntax, text processing)
- scikit-learn (ML)
- C (basic file handling & display)

## Workflow
1. Load SMS Spam Collection dataset
2. Preprocess text (CountVectorizer)
3. Train a Naive Bayes classifier
4. Evaluate model accuracy
5. Test custom messages
6. Save results to a text file
7. Use C program to read & display results

## How to Run
### Python

python spam_classifier.py

### C

gcc spam_display.c -o spam_display
./spam_display


## Sample Output

=== Spam Email Classification Result ===
Model Accuracy: 0.9850
Sample Message Prediction: spam

