Resources:
https://scikit-learn.org/stable/modules/svm.html


SVM 

A support vector machine (SVM) is a supervised machine learning model that uses classification algorithms for two-group classification problems. After giving an SVM model sets of labeled training data for each category, they’re able to categorize new text.

How it works!

Let's assume there are two tags - red and blue, and two data features x and y in the plane. We have to find that given a pair (x, y), classify it as red or blue!

![image](https://user-images.githubusercontent.com/66998557/119236606-f4e20700-bb55-11eb-9dfb-ff7c3e142983.png)


A support vector machine takes these data points and outputs the hyperplane (which in two dimensions it’s simply a line) that best separates the tags. This line is the decision boundary: anything that falls to one side of it we will classify as blue, and anything that falls to the other as red.

![image](https://user-images.githubusercontent.com/66998557/119236651-48545500-bb56-11eb-9e89-dabd555c419b.png)

For SVM, the best hyperplane is the one which maximises the margins for both tags

![image](https://user-images.githubusercontent.com/66998557/119236685-70dc4f00-bb56-11eb-82e0-61c2d68e9f62.png)

SVC:
1. https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC 
2. https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
3. https://stackoverflow.com/questions/35572000/how-can-i-plot-a-confusion-matrix
4. https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.make_pipeline.html

Linear SVC
1. https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html#sklearn.svm.LinearSVC

NuSVC
1. https://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html#sklearn.svm.NuSVC
