# Vehicle Insurance Fraud Detection

Comparing machine learning models to identify potentially fraudulent vehicle insurance claims and support investigation decisions.

## Overview

Insurance fraud detection involves a practical tradeoff: catching more fraudulent claims can also increase the number of legitimate claims sent for investigation. This project explores that tradeoff using claim, policy, vehicle, and policyholder information.

The analysis compares six classification approaches, addresses a strongly imbalanced target, and evaluates performance primarily through **fraud recall**, alongside precision, F1-score, and confusion matrices.

**Key result:** Tuned XGBoost achieved **95.5% fraud recall**, identifying **170 of 178 fraudulent claims** in the test set, as documented in the notebook analysis. The accompanying tradeoff was **1,181 false positives**, giving approximately **12.6% precision**.

## Dataset

| Attribute | Description |
| --- | --- |
| Input file | `fraud_oracle.csv` |
| Original size | 15,420 records and 33 columns, including the target |
| Target | `FraudFound_P`: `1` = fraud; `0` = non-fraud |
| Class distribution | Approximately 6% fraud and 94% non-fraud |
| After age filtering | 15,100 records, including 892 fraud cases |
| Training / test split | 12,080 / 3,020 records; stratified 80/20 split |

Predictors include policy type, fault attribution, deductible, vehicle age, prior claims, accident area, and police-report information. The dataset contains records from 1994–1996, which limits conclusions about current claims patterns.

The notebook loads the CSV from a Google Drive link and provides a local-file alternative. The CSV is not included in this project folder; running the notebook requires access to the linked dataset or a local copy.

## Tools

Python, Jupyter Notebook, pandas, NumPy, Matplotlib, Seaborn, scikit-learn, imbalanced-learn, XGBoost, and Requests.

## Analysis workflow

1. **Inspect and explore:** Review data types, category frequencies, distributions, and relationships with fraud.
2. **Clean:** Remove `PolicyNumber` and `RepNumber`; exclude records with `Age < 16`.
3. **Encode and engineer features:** Apply binary, ordinal, and one-hot encoding; create indicators combining vehicle age with supplements and young policyholders with missing police reports. Create and subsequently remove a quick-claim indicator and remove the age-band proxy.
4. **Split and scale:** Use a stratified split with `random_state=42`; fit `StandardScaler` on training data for age and deductible, then transform the test set.
5. **Address imbalance:** Compare class weighting and SMOTE applied to training data while preserving the test distribution.
6. **Train and evaluate:** Compare Logistic Regression, Decision Tree, K-Nearest Neighbors, Random Forest, XGBoost, and a soft Voting Classifier. Use grid search, stratified cross-validation, and probability-threshold adjustment in selected experiments.
7. **Assess business implications:** Examine feature importance, investigation workload, and an illustrative financial-value scenario.

## Results

An always-non-fraud classifier would achieve roughly 94% accuracy while detecting no fraud. Recall therefore provides a more useful measure of fraud coverage, but must be considered with precision and investigation capacity.

| Model / approach | Fraud recall |
| --- | ---: |
| Tuned XGBoost with class weighting | **95.5%** |
| Decision Tree with balanced class weights | 86% |
| Logistic Regression with balanced class weights | 85% |
| Random Forest with SMOTE | 85% |
| Logistic Regression with SMOTE and adjusted threshold | 81% |
| Logistic Regression with SMOTE | 27% |
| Tuned KNN with SMOTE | 25% |

Results summarize the notebook's saved evaluations and written analysis. XGBoost recall is calculated as `170 / 178`; other values follow the rounded classification reports. Some later evaluation outputs are not saved in the notebook, including the tuned XGBoost report.

For tuned XGBoost, the notebook documents the following test-set counts:

| Actual class | Predicted non-fraud | Predicted fraud |
| --- | ---: | ---: |
| Non-fraud | 1,661 | 1,181 |
| Fraud | 8 | 170 |

The project selects tuned XGBoost for its fraud coverage. Its precision is `170 / (170 + 1,181)`, approximately **12.6%**. Investigators would review about seven legitimate claims for every fraudulent claim detected. Threshold selection should therefore reflect investigation capacity and the relative costs of missed fraud and false alarms. A model flag supports investigation rather than establishing fraud.

## Business-value analysis

The notebook explores an illustrative value calculation:

```text
Illustrative value = (TP × 5,215) − (FP × 107) − (FN × 5,215)
```

The assumptions represent avoided losses for detected fraud, investigation costs for false alarms, and losses from missed fraud. This section uses an XGBoost probability threshold of `0.30`, separate from the default classification rule used in the model-comparison code.

Dollar totals are not reported here because the notebook conclusion contains inconsistent financial estimates, and the financial evaluation output is not saved. The calculation is a simplified scenario, excludes investigation costs for true positives and other operating costs, and does not establish realized savings or incremental return against a baseline.

## Project files

| File | Contents |
| --- | --- |
| `Vehicle_Insurance_Fraud_Detection_Project.ipynb` | Data exploration, preprocessing, model training, evaluation, and business-value analysis |
| `README.md` | Project overview and instructions |

## How to run

1. Download `Vehicle_Insurance_Fraud_Detection_Project.ipynb` and open it in Jupyter Notebook, JupyterLab, or Google Colab.
2. Install the required packages in the notebook environment:

   ```python
   %pip install numpy pandas matplotlib seaborn scikit-learn imbalanced-learn xgboost requests
   ```

3. Run the data-loading cell. If the Google Drive download is unavailable, obtain `fraud_oracle.csv`, place it alongside the notebook, and replace the remote-loading code with:

   ```python
   df = pd.read_csv("fraud_oracle.csv")
   ```

4. Restart the kernel and run all cells in order. Grid searches, especially Random Forest tuning, may take substantial time.

Package versions are not pinned, and the supplied notebook has not been rerun for this README. Results may differ across environments.

## Limitations and next steps

- **Reproducibility:** Rerun the full notebook, retain all evaluation outputs, reconcile the written conclusions with those outputs, and record package versions.
- **Validation:** Move scaling into cross-validation pipelines. Random Forest tuning currently uses data resampled before cross-validation; move SMOTE inside each fold to avoid contamination between folds. Consider SMOTENC or class weighting for mixed categorical features.
- **Model selection:** Confirm performance on a separate final holdout or temporal split after model and threshold selection.
- **Operational use:** Evaluate precision-recall curves, calibration, investigation volume, fairness across demographic groups, and realistic costs before deployment.
- **Interpretation:** Feature importance describes model behavior, not causation. Assess current, representative data before applying historical patterns to new claims.

## Contributors

**Anand Arya · Nisha Mahambre · Olga Nureeva · Ava Sirois**  
Group 7, **SCH-MGMT 657: Data Science for Business**  
Isenberg School of Management

This folder is part of an analytics portfolio and presents a collaborative academic project.
