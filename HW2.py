# Rows = predicted classes
# Columns = actual classes

confusion_matrix = [
    [5, 10, 5],   # Predicted Cat
    [15, 20, 10], # Predicted Dog
    [0, 15, 10]   # Predicted Rabbit
]

class_names = ["Cat", "Dog", "Rabbit"]

precision_values = []
recall_values = []

for index, class_name in enumerate(class_names):
    true_positive = confusion_matrix[index][index]

    total_predicted = sum(confusion_matrix[index])
    total_actual = sum(row[index] for row in confusion_matrix)

    precision = true_positive / total_predicted
    recall = true_positive / total_actual

    precision_values.append(precision)
    recall_values.append(recall)

    print(f"{class_name}:")
    print(f"  Precision = {precision:.4f}")
    print(f"  Recall    = {recall:.4f}")

# Macro averages: average of the individual class results
macro_precision = sum(precision_values) / len(class_names)
macro_recall = sum(recall_values) / len(class_names)

# Micro averages: total correct predictions divided by all predictions
correct_predictions = sum(
    confusion_matrix[i][i] for i in range(len(class_names))
)
total_predictions = sum(sum(row) for row in confusion_matrix)

micro_precision = correct_predictions / total_predictions
micro_recall = correct_predictions / total_predictions

print("\nOverall Results:")
print(f"Macro Precision = {macro_precision:.4f}")
print(f"Macro Recall    = {macro_recall:.4f}")
print(f"Micro Precision = {micro_precision:.4f}")
print(f"Micro Recall    = {micro_recall:.4f}")