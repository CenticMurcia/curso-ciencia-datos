false_positive_rate, recall, thresholds = roc_curve(y_true, y_probs)
roc_auc = auc(false_positive_rate, recall)

print(u'AUC:', roc_auc)

plt.plot(false_positive_rate, recall, 'b')
plt.plot([0, 1], [0, 1], 'r--')
plt.title(u'AUC = %0.2f' % roc_auc)