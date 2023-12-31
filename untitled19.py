# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CeSPI7bxvV4t2-GuZ2CehNSJT-Qv_517
"""

import csv
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy as nltk_accuracy

# Extract features from the input list of words
def extract_features(words):
    return dict([(word, True) for word in words])

if __name__ == '__main__':
    # Read employee reviews from CSV file
    employee_reviews = []
    with open('/content/drive/MyDrive/new_dataset_for_project.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            review = row[0]
            sentiment = row[1]
            employee_reviews.append((review, sentiment))

    # Extract features from employee reviews
    features = [(extract_features(review.split()), sentiment) for (review, sentiment) in employee_reviews]

    # Define the train and test split (80% and 20%)
    threshold = 0.8
    num_train = int(threshold * len(features))

    # Create training and test datasets
    features_train = features[:num_train]
    features_test = features[num_train:]

    # Print the number of datapoints used
    #print('Number of training datapoints:', len(features_train))
    print('Number of test datapoints:', len(features_test))

    # Train a Naive Bayes classifier
    classifier = NaiveBayesClassifier.train(features_train)
    print('\nAccuracy of the classifier:', nltk_accuracy(classifier, features_test))

    N = 10
    print('\nTop', N, 'most informative words:')
    for i, item in enumerate(classifier.most_informative_features()):
        print(str(i+1) + '.', item[0])
        if i == N - 1:
            break

    # Test input employee reviews
    input_reviews = [
        'I enjoy working with my team.',
        'The workload is overwhelming and unrealistic.',
        'The company values its employees and their well-being.',
        'There is a lack of communication and transparency.',
        'Employees not find environment of company good for their growth'
    ]
    print('\nEmployee review predictions:')
    for review in input_reviews:
        print('\nReview:', review)

        # Compute the probabilities
        probabilities = classifier.prob_classify(extract_features(review.split()))

        # Pick the maximum value
        predicted_sentiment = probabilities.max()
        print('Predicted sentiment:', predicted_sentiment)

import matplotlib.pyplot as plt

# Test input employee reviews
input_reviews = [
    'I enjoy working with my team.',
    'The workload is overwhelming and unrealistic.',
    'The company values its employees and their well-being.',
    'There is a lack of communication and transparency.',
]

# Create empty lists to store sentiments and their counts
sentiments = []
sentiment_counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}

# Predict sentiments for input reviews
for review in input_reviews:
    probabilities = classifier.prob_classify(extract_features(review.split()))
    predicted_sentiment = probabilities.max()
    sentiments.append(predicted_sentiment)
    sentiment_counts[predicted_sentiment] += 1

# Extract sentiment categories and their respective counts
categories = sentiment_counts.keys()
counts = sentiment_counts.values()

# Create a bar chart
plt.bar(categories, counts)

# Add labels and title to the chart
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.title('Employee Sentiment Analysis')

# Display the chart
plt.show()