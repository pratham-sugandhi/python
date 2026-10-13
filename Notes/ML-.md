### **ML-**

### 



inp / out	->

&#x20;			logic (hypothesis)



&#x09;					-> new inp

&#x09;							-> predicted out









\# Supervised learning- labeled data --> inp/out available







1 classification					2 regression



classify/ categories					range



dogs/cats						marks

spams							aqi / stocks





\# unsupervised learning- unlabeled data --> only inp





1 clustering -

iPhone + charger





\# Reinforcement learning- goal oriented -->

&#x09;supervised + unsupervised





rewards/ penalties











\# SK LEARN -

well documented

easy to learn

works well with np \& pd

professional / begs





\# Algo -



Linear Regression - regression

Logistic Reg - classification

KNN - K nearest neighbor

Decision Tree - R/C

Naive Bayes - C

SVM - R/C





#### **# Linear Regression : -**





&#x09;		**Train**

&#x09;		  **|**

&#x09;		  **|**

&#x09;		**Model**

&#x09;		  **|**

&#x09;		  **|**

**--new i/p		Regressor	--- new o/p**











###### **# OVERFITTING -**

**Model is too complex**



&#x09;**X, Y ka relation kitna fit karega**



**Agar model training data ko yaad kar ke testing data par analysis kare toh performance low hojata hai**



**training accuracy - 95%  Low Bias (error on cost function)**

**test accuracy - 65%  High Variance (sensitive to changes in dataset)**





**cost function may reduced to zero;**





###### \# UNDERFITTING -

**Model is too simple**



**Training - 75% High Bias**

**Test - 65%   Low Variance**





**optimal model for us :- low bias \& low variance**





**# Bias Variance Tradeoff -**

&#x09;			**Underfit    overfit** 



**num of parameter -		Inc**

**num of neurons -**		**Inc**

**num of layers -** 		**Inc**







**# REGULARIZATION -**



&#x09;**cost fun zero na ho min rahe**



1. Lasso Regression  - 

&#x20;   penalty add krte hai :

&#x09;

&#x09;jitney jyada features utni high penalty, so model will work to find out unimportant feature and make them 0





2\. Ridge Regression -



&#x09;similar to Lasso but we take square





##### **# LOGISTIC REGRESSION FOR CLASSIFICATION -**

&#x09;

**WHY ? -**

**val on BFL are not prob**

**h(x) < 0 \& >1**

**outliers - shift BFL**





**we use sigmoid activation fun to get prob** 



