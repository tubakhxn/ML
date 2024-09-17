from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
#0 for Setosa 1 for Versicolor

# Step 2: Split the dataset into training and testing sets
#feature matrix= x containing the 4 measurements (sepal length, sepal width, petal length, petal width) for each iris flower
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#y labels (targets), which are the species of each iris flower
# Step 3: Initialize the Gaussian Naïve Bayes classifier
gnb = GaussianNB()

# Step 4: Train the model on the training data
gnb.fit(X_train, y_train)

# Step 5: Make predictions on the test set
y_pred = gnb.predict(X_test)

# Step 6: Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=iris.target_names)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
#Gaussian Naive Bayes (GNB) Trains on the training data (X_train and y_train) using gnb.fit(X_train, y_train).
# Additional Step: Allow user input for prediction
while True:
    try:
        print("\nEnter the features of a new Iris flower for prediction.")
        sepal_length = float(input("Sepal Length (cm): "))
        sepal_width = float(input("Sepal Width (cm): "))
        petal_length = float(input("Petal Length (cm): "))
        petal_width = float(input("Petal Width (cm): "))
        
        user_input = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = gnb.predict(user_input)
        
        print(f"The predicted class is: {iris.target_names[prediction[0]]}")
        
    except ValueError:
        print("Please enter valid numeric values.")
    except KeyboardInterrupt:
        print("\nExiting.")
        break
