# Proxy Detection

"Proxy Detection" as the name suggests, projects aim is to detect/classify network traffic into VPN and NON-VPN class. For the the data-set that is used is “VPN-nonVPN dataset (ISCXVPN2016)” by Canadian Institute for Cybersecurity.

### Data-set citation:
Gerard Drapper Gil, Arash Habibi Lashkari, Mohammad Mamun, Ali A. Ghorbani, "Characterization of Encrypted and VPN Traffic Using Time-Related Features", In Proceedings of the 2nd International Conference on Information Systems Security and Privacy(ICISSP 2016) , pages 407-414, Rome, Italy.

## Methodology

The data us tested on 3 algorithms:

### i. Gaussian Naive Bayes:
    Using Gaussian Naive Bayes algorithm with the above-mentioned training and testing set of data, the accuracy was 53.51%.
    This gives the worst accuracy among the ones that we tried, since Naive Bayes considers that all the features involved are independent, that rarely occurs in real scenarios.

### ii. Decision Tree Classifier:
    Using Decision Tree Classifier with dataset, the accuracy for testing data was 88.99%. 
    Although results are better than the previous algorithm, it can be improved.

### iii. Random Forest Classifier.

    Using Random Forest Classifier with dataset, the accuracy was 91.41%, best among the algorithms that we tried.
    Although these provide a sufficient assurance that using ML algorithms is better, there’s scope to use more refined algorithms and better the accuracy than presented here.

## Summary:

| Algorithm | Accuracy |
| ----------- | ----------- |
|Gaussian Naive Bayes | 53.51% |
| Decision Tree Classifier | 88.99% |
| Random Forest Classifier | 91.41% |

Although, the results are satisfactory there's scope for plenty of improvement. 


