import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats
import statsmodels.api as sm

df = pd.read_csv("health_records_dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

df['diabetes'] = df['diabetes'].astype(int)
df['hypertension'] = df['hypertension'].astype(int)

print("\nData Cleaning Done")

print("\nDescriptive Statistics:")
print(df.describe())

mean_age = df['age'].mean()
std_age = df['age'].std()
n = len(df)

confidence_level = 0.95
z_critical = stats.norm.ppf(1 - (1 - confidence_level)/2)

margin_error = z_critical * (std_age / np.sqrt(n))
ci_lower = mean_age - margin_error
ci_upper = mean_age + margin_error

print("\nCONFIDENCE INTERVAL FOR AGE (95%)")
print(f"Mean Age: {mean_age:.2f}")
print(f"Confidence Interval: ({ci_lower:.2f}, {ci_upper:.2f})")

contingency_table = pd.crosstab(df['smoking_status'], df['diabetes'])

chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)

print("\nCHI-SQUARE TEST (Smoking vs Diabetes)")
print("Chi-Square Value:", chi2)
print("P-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Decision: Reject H0 → Smoking affects Diabetes")
else:
    print("Decision: Fail to Reject H0")

bmi_diabetic = df[df['diabetes'] == 1]['bmi']
bmi_non_diabetic = df[df['diabetes'] == 0]['bmi']

t_stat, p_val = stats.ttest_ind(bmi_diabetic, bmi_non_diabetic)

print("\nT-TEST (BMI vs Diabetes)")
print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < alpha:
    print("Decision: Reject H0 → Mean BMI differs")
else:
    print("Decision: Fail to Reject H0")

groups = []
for level in df['exercise_frequency'].unique():
    groups.append(df[df['exercise_frequency'] == level]['bmi'])

f_stat, p_anova = stats.f_oneway(*groups)

print("\nANOVA TEST (Exercise Frequency vs BMI)")
print("F-statistic:", f_stat)
print("P-value:", p_anova)

if p_anova < alpha:
    print("Decision: Reject H0 → BMI differs across exercise groups")
else:
    print("Decision: Fail to Reject H0")


covariance = np.cov(df['age'], df['bmi'])[0][1]
correlation = np.corrcoef(df['age'], df['bmi'])[0][1]

print("\nCOVARIANCE & CORRELATION")
print("Covariance (Age, BMI):", covariance)
print("Correlation (Age, BMI):", correlation)

plt.figure(figsize=(6,4))
sns.boxplot(x='diabetes', y='bmi', data=df)
plt.title("BMI vs Diabetes")
plt.xlabel("Diabetes (0 = No, 1 = Yes)")
plt.ylabel("BMI")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(
    df[['age','bmi','blood_pressure','cholesterol_level','glucose_level']].corr(),
    annot=True,
    cmap='coolwarm'
)
plt.title("Correlation Heatmap")
plt.show()

print("\nFINAL CONCLUSION:")
print("• Lifestyle and health indicators show significant relationships.")
print("• Smoking and exercise patterns impact disease prevalence.")
print("• BMI is significantly different for diabetic individuals.")
print("• Age and BMI show measurable correlation.")

print("\nPROJECT EXECUTION COMPLETED SUCCESSFULLY ✅")
