Resources 
https://scikit-learn.org/stable/modules/sgd.html
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html#sklearn.linear_model.SGDClassifier

SGD(Stochastic Gradient Descent) is an approach to fitting linear classifiers and regressors under convex loss functions.

The advantages of Stochastic Gradient Descent are:
1. Efficiency.
2. Ease of implementation (lots of opportunities for code tuning).

The disadvantages of Stochastic Gradient Descent include:
1. SGD requires a number of hyperparameters such as the regularization parameter and the number of iterations.
2. SGD is sensitive to feature scaling.

SGD Classifier: It implements a plain stochastic gradient descent learning routine which supports different loss functions and penalties for classification. Below is the decision boundary of a SGDClassifier trained with the hinge loss, equivalent to a linear SVM.

![image](https://user-images.githubusercontent.com/66998557/120855903-b2c8b480-c59c-11eb-92cc-55745a1680f8.png)
