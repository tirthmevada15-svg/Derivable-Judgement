# Health Inferential Statistics Analysis using Python

## Project Overview
This project applies **inferential statistical techniques** to a real-world health dataset to identify relationships between **demographic, lifestyle, and medical factors** such as age, BMI, smoking habits, exercise frequency, and diabetes status.

The goal is to move beyond descriptive statistics and use **data-driven statistical testing** to support healthcare-related insights and decision-making.

---

## Dataset Description
The dataset contains **500 health records** with the following key attributes:

- Age & Age Group  
- Gender & Region  
- BMI (Body Mass Index)  
- Smoking Status  
- Exercise Frequency  
- Blood Pressure  
- Cholesterol Level  
- Glucose Level  
- Diabetes Status  
- Hypertension  

## Technologies Used
- **Python**
- **Pandas** – data handling & cleaning  
- **NumPy** – numerical computation  
- **Matplotlib & Seaborn** – data visualization  
- **SciPy** – statistical testing  
- **StatsModels** – inferential analysis  

---

## Methodology & Statistical Techniques

### Data Cleaning
- Checked for missing values
- Removed null records
- Converted categorical health indicators (diabetes, hypertension) into numerical format

### Descriptive Statistics
- Mean, median, standard deviation
- Distribution understanding of all numerical variables

### Inferential Statistics Applied
| Technique | Purpose |
|--------|--------|
| Confidence Interval | Estimate population mean age |
| Chi-Square Test | Relationship between smoking & diabetes |
| Independent T-Test | BMI comparison between diabetic & non-diabetic groups |
| ANOVA | BMI differences across exercise frequency levels |
| Covariance & Correlation | Relationship between age and BMI |

## Visualizations

### BMI vs Diabetes (Boxplot)
- Compares BMI distribution for diabetic and non-diabetic individuals
- Helps visually identify differences in central tendency and spread

### Correlation Heatmap
- Shows correlation between:
  - Age
  - BMI
  - Blood Pressure
  - Cholesterol Level
  - Glucose Level
- Uses color intensity to represent strength and direction of relationships

## Key Findings & Insights
- **BMI differs between diabetic and non-diabetic individuals**
- **Lifestyle factors** such as smoking and exercise influence health outcomes
- **Exercise frequency** impacts BMI levels
- **Age and BMI** show measurable correlation
- Statistical decisions were made using **p-values (α = 0.05)** ensuring scientific validity

## Learning Outcomes
- Practical application of inferential statistics using Python
- Understanding hypothesis testing and confidence intervals
- Interpreting statistical outputs and visualizations
- Translating data analysis into real-world healthcare insights

## Real-World Applications
This project reflects real public health analysis workflows and can be used for:
- Healthcare risk assessment
- Preventive health policy planning
- Epidemiological research
- Academic & student learning projects
