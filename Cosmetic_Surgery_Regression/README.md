# Cosmetic Surgery Interest: Regression Analysis

An analysis of how self-esteem, body satisfaction, and an additional survey measure (`IMPREAL`) are associated with reported desire for cosmetic surgery.

## Overview

This academic project applies multiple linear regression to a dataset of **170 respondents**. It covers model estimation, hypothesis testing, confidence and prediction intervals, residual diagnostics, and model refinement.

The baseline model explains approximately **46.6% of the variation** in the desire score. Body satisfaction has a significant negative association with desire, holding the other predictors constant. An extension including a categorical gender variable improves the in-sample fit and roughly halves the body satisfaction coefficient (from −0.69 to −0.32), so part of the baseline association is shared with the gender difference.

## Data and variables

The notebook reads `Surgery-data.xlsx`, containing 170 rows and six columns. Its saved inspection output reports no missing values.

| Variable | Role | Description |
| --- | --- | --- |
| `DESIRE` | Response | Reported desire for cosmetic surgery |
| `SELFESTM` | Predictor | Self-esteem score |
| `BODYSAT` | Predictor | Body satisfaction score |
| `IMPREAL` | Predictor | Additional survey score; its exact definition requires the dataset codebook |
| `GENDER` | Categorical extension | Binary category coded 0 or 1; category labels require confirmation |
| `STUDENT` | Identifier | Record identifier, excluded from the regression models |

The dataset codebook was not supplied. The notebook and this README both refer to `IMPREAL` by its column name only. The Excel dataset is required to rerun the analysis and is not included in this folder.

## Tools and methods

**Python · pandas · NumPy · statsmodels · SciPy · Matplotlib · Seaborn · openpyxl**

- Ordinary least squares (OLS) regression.
- Coefficient t-tests, the overall F-test, and 95% confidence intervals.
- ANOVA tables and explained versus unexplained variation.
- Residual-versus-fitted plots and variance inflation factors (VIF).
- Interaction, quadratic, categorical, and log-response extensions.
- Model comparison using adjusted R-squared and AIC for models sharing the same response scale.

## Baseline model

```text
DESIRE = 13.7842 − 0.0110 × SELFESTM − 0.6873 × BODYSAT + 0.5228 × IMPREAL
```

| Measure | Saved result |
| --- | ---: |
| R-squared | 0.4658 |
| Adjusted R-squared | 0.4561 |
| Overall F-statistic | 48.2410 |
| Overall model p-value | 1.7905 × 10⁻²² |
| AIC | 771.6430 |

Holding the other predictors constant, a one-point increase in body satisfaction is associated with a **0.6873-point lower desire score** (p ≈ 2.70 × 10⁻¹²). Its 95% coefficient confidence interval is **[−0.8669, −0.5076]**. Self-esteem is not statistically significant in this specification (p = 0.758), while `IMPREAL` has a significant positive coefficient.

These are associations in the observed sample and do not establish causation.

## Model comparison

| Specification | Adjusted R-squared | AIC | Finding |
| --- | ---: | ---: | --- |
| Baseline linear | 0.4561 | 771.6430 | Preferred among the baseline, interaction, and quadratic models |
| Add `SELFESTM × BODYSAT` | 0.4528 | 773.6403 | Interaction not significant (p = 0.959) |
| Add `BODYSAT²` | 0.4530 | 773.5841 | Quadratic term not significant (p = 0.811) |
| Add `C(GENDER)` | Approximately 0.485 | Approximately 763.2 | Stronger in-sample fit than the baseline |

In the categorical extension, category 1 has an estimated desire score **2.1865 points lower** than category 0, controlling for the three quantitative predictors (p ≈ 0.001). The demographic labels cannot be assigned without confirming the coding. Body satisfaction remains significant in this model (coefficient −0.3223, p ≈ 0.026), but its estimated association is about half the baseline value.

A log-response model is also explored. Its unadjusted AIC cannot be directly compared with the raw-response models because the response scale changes. A lower displayed AIC alone does not demonstrate that this model is better.

## Prediction and uncertainty

For `SELFESTM = 20`, `BODYSAT = 5`, and `IMPREAL = 5`, the baseline model produces:

| Output | Value |
| --- | ---: |
| Predicted mean desire score | 12.7409 |
| 95% confidence interval for the mean | [12.1130, 13.3688] |
| 95% prediction interval for one new respondent | [8.1293, 17.3525] |

The prediction interval is wider because it includes individual variation as well as uncertainty in the estimated mean.

## Project files

| File | Contents |
| --- | --- |
| [Cosmetic_Surgery_Regression.ipynb](Cosmetic_Surgery_Regression.ipynb) | Analysis, regression output, diagnostics, and interpretations |
| `README.md` | Project overview, findings, and reproduction instructions |

## How to run

1. Open `Cosmetic_Surgery_Regression.ipynb` in Jupyter Notebook, JupyterLab, or Google Colab.
2. Obtain `Surgery-data.xlsx` and place it in the notebook's working directory. In Colab, upload the Excel file into the session.
3. Install dependencies in the notebook environment:

   ```python
   %pip install pandas numpy statsmodels matplotlib seaborn openpyxl scipy
   ```

4. Restart the kernel and run the cells in order.

Results above are taken from the notebook's saved outputs. Package versions are not pinned.

## Limitations and technical notes

- **Validation:** Reported fit measures are in-sample; the notebook does not evaluate predictive performance on a held-out dataset.
- **Data context:** The original source, sampling method, scale definitions, and gender coding require documentation. Findings should not be generalized beyond the sample without further evidence.
- **Diagnostics:** Baseline predictor VIF values range from approximately 1.03 to 2.36. These do not suggest severe predictor multicollinearity, but they do not validate every regression assumption.
- **ANOVA:** The notebook reports the full-model decomposition using `model.ess`, `model.ssr`, and `model.centered_tss`. The sequential (Type I) ANOVA row F-tests depend on predictor order and differ from the overall regression F-test. The corrected ANOVA cells have not been rerun; the Excel dataset is required to generate their outputs.
- **Interpretation:** The categorical extension improves in-sample fit, while the interaction and quadratic additions do not. Further validation is needed before selecting a model for prediction.

## Author and context

**Nisha Mahambre**  
MGMT 650 regression analysis project

This folder is part of an analytics portfolio. It demonstrates statistical modeling and interpretation and is not a clinical decision tool.
