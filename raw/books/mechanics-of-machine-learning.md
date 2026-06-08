# The Mechanics of Machine Learning

- **Authors:** Terence Parr and Jeremy Howard
- **URL:** https://mlbook.explained.ai/
- **Status at capture:** Work in progress, version 0.4
- **Captured:** 2026-06-04 by Claude Code (web fetch)

> **Provenance note.** This file is an *agent-fetched extract* of the online book, not a
> verbatim mirror. Each chapter section below was produced by fetching the corresponding
> `*.html` page and extracting key claims, techniques, code, and quotes. Quoted sentences
> are reproduced as faithfully as the fetch allowed; numbers and code are transcribed from
> the rendered pages. For the authoritative text, see the live URLs.

The book is a practical primer for programmers who want to learn machine learning fast. Rather
than surveying many algorithms, it concentrates on "a few powerful models (algorithms) that are
extremely effective on real problems" — primarily **Random Forests** — and teaches the
end-to-end applied workflow through two running datasets: NYC apartment rent (regression) and
heavy-equipment auction prices (the Kaggle "Blue Book for Bulldozers" time-series regression).

## Table of Contents (captured)

1. Welcome! — `preface.html`
2. How Machine Learning Works — `intro.html`
3. A First Taste of Applied Machine Learning — `first-taste.html`
4. Development Tools — `tools.html`
5. Exploring and Denoising Your Data Set — `prep.html`
6. Categorically Speaking — `catvars.html`
7. Exploring and Cleaning the Bulldozer Dataset — `bulldozer-intro.html`
8. Bulldozer Feature Engineering — `bulldozer-feateng.html`
9. Train, Validate, Test — `bulldozer-testing.html`

---

## 1. Welcome! (preface.html)

**Audience.** Programmers with at least ~1 year of experience, preferably Python. "Computer
programming is required to do machine learning and programmers are the primary target audience
of this book." Math required is only "high school level algebra and geometry," not advanced math.

**Philosophy.** Intuition over formalism: "the math notation is really just a precise and
concise way to express the results of someone's intuitive leap." The authors spend "most of our
time with the ideas and mechanisms behind machine learning" rather than proofs. The approach is
deliberately narrow and opinionated — focus on "just a few powerful models (algorithms) that are
extremely effective on real problems" and champion Random Forests as "a single powerful model"
that covers most cases.

**Tools of the trade.** Anaconda, Jupyter notebooks/Lab, pandas, NumPy, scikit-learn, matplotlib.

**What you'll learn.** How "machine learning works and how to apply it in practice," with a
"broadly-applicable recipe" for the workflow; "the overall process of applying machine learning
is pretty straightforward."

---

## 2. How Machine Learning Works (intro.html)

**Definition.** Machine learning "turns experience into expertise, generalizing from training
data to make accurate predictions or classifications in new situations." "To generalize means
that we get accurate predictions for feature vectors not found in the training set." Central
tension: accuracy without overfitting.

**Apartment-rent motivating problem.** Predict NYC rent from 4 features (bedrooms, bathrooms,
latitude, longitude). Progressive sophistication of approaches:
- Memorization (dictionary of exact feature→price) — perfect on training data, fails on new data, can't handle identical features mapping to different prices.
- Averaging prices for identical feature combinations.
- k-nearest neighbors (average prices of similar apartments).
- Linear regression (weighted formula).
- Decision trees (partition feature space into ranges).

**Random Forest regressors.** RF solves single-tree overfitting by:
1. Building many trees, each on a random bootstrap sample (sampling with replacement).
2. Randomly excluding features at splits (decorrelating trees).
3. Averaging predictions across trees.

Analogy: "An RF behaves very much like a group of real estate agents looking for comparable
apartments and cooperating to estimate an apartment's price ('crowdsourcing')." The authors call
RFs "the Swiss Army Knife™ of the machine learning world" and recommend them as the default model
for most practical problems.

**Random Forest classifiers.** Same machinery for discrete targets. Regressor leaves predict the
average target; classifier leaves predict the most common category; the forest aggregates votes
(a "meta-voting scheme"). Illustrated with apartment interest level (low/medium/high). "Most
models have both predictor and classifier variants." Both regressor and classifier "carve up
feature space into groups of similar observations."

**Big Picture vocabulary.**
- Feature vectors (X), targets (y: scalar or category), training data = (X, y) pairs.
- Model = "a combination of data structure, algorithm, and mathematics that captures the
  relationship described by a collection of (feature vector, target) pairs."
- Supervised (labeled, the book's focus) vs unsupervised (unlabeled; clustering).
- Underfitting (can't capture the relationship) vs overfitting (too specific to training data).
- Parameters (learned from data, e.g., tree structure) vs hyperparameters (set by the
  programmer, e.g., k in kNN, number of trees).
- Validation: reserve a validation set to measure generalization; keep a final test set
  completely untouched until the end.

Epigraph: "Without data you're just another person with an opinion" — W. Edwards Deming.
"Without understanding the underlying algorithms, we can't successfully apply machine learning."

---

## 3. A First Taste of Applied Machine Learning (first-taste.html)

Three worked examples, all Random Forest:

1. **NYC apartment rent (regression).** Kaggle Two Sigma rental data (`rent-ideal.csv`).
   `RandomForestRegressor(n_estimators=10)`. Training MAE $189 (5.51%); validation MAE $303 (8.80%).
   Location (lat/long) alone gives 15.10% error — location matters most.
2. **Breast cancer (binary classification).** Wisconsin Breast Cancer (569 patients, 30 features).
   `RandomForestClassifier(n_estimators=300)` on 7 selected features → 91.86% validation accuracy.
   Radius error was the most predictive feature.
3. **Handwritten digits (MNIST, multiclass).** 10,000-image sample, 28×28 → 784 features.
   `RandomForestClassifier(n_estimators=900)` → 94.45% accuracy vs `LogisticRegression` 90.20%.
   A "4" misclassified as "7" because training data lacked similar fours — "Models can only make
   predictions based upon the training data provided to them."

**Universal recipe:**
```python
df = pd.read_csv(datafile)
X = df[[feature_columns]]
y = df[target_column]
m = ChooseYourModel(hyper_parameters)
m.fit(X, y)
y_pred = m.predict(test_record)
```

---

## 5. Exploring and Denoising Your Data Set (prep.html)

**Quick sniff.** Load with pandas, `df.shape` → (49352, 15), `df.info()`. Practitioners spend
"roughly 75% of their time acquiring, cleaning, and otherwise preparing data."

**Denoising = removing out-of-scope/bad records.** Decide bounds *before* looking at data:
price floor $1,000, ceiling $10,000; NYC bounding box (lat 40.55–40.94, long −74.1 to −73.67).
"It's critical that we decide what these bounds are before looking at the data." Anomalies found:
max $4,490,000/mo, min $43/mo, 12 records at coords (0,0), apartments in Boston. Delete 11
zero-coordinate records, filter to NYC box.

**Noisy vs denoised model (RandomForestRegressor, n_estimators=100, oob_score=True):**
- Raw data: OOB R² = **−0.0076** (terrible), avg validation MAE **$622** (unstable).
- Cleaned data: OOB R² = **0.8677**, avg validation MAE **$294**.
- Competing models on clean data: Lasso 0.5764 (train R²), Gradient Boosting 0.8046 (val R²) — RF wins.

**Log in, exp out.** Apartment prices are right-skewed; `log(price)` ≈ normal, making
average-based predictions robust to outliers without manual denoising.
```python
y_log = np.log(y)
rf.fit(X, y_log)        # OOB R² = 0.8767 on UNFILTERED noisy data — matches denoised 0.8677
...
y_predicted = np.exp(rf.predict(X_test))   # invert to dollars
```
Trade-off: log-transform matches R² without domain knowledge, but its MAE is worse than the
denoised model's. "If we care more about MAE than R², then cleaning the data gets us a better
model than simply taking the log of the prices."

---

## 6. Categorically Speaking (catvars.html)

Categorical-encoding techniques (for Random Forests):

1. **Label encoding** — map categories to integer codes. Works for high-cardinality nominal
   variables but treats unordered categories as ordered, so trees need to be larger. Minimal
   impact on the apartment model.
   ```python
   df['col_cat'] = df['col'].astype('category').cat.as_ordered()
   df['col_cat'] = df['col_cat'].cat.codes + 1
   ```
2. **Frequency encoding** — replace category with its count in training data. "There might be
   predictive power in the number of apartments managed by a particular manager." Didn't help here.
   ```python
   counts = df['col'].value_counts(); df['enc'] = df['col'].map(counts)
   ```
3. **One-hot encoding** — mentioned but not used here (too many columns).
4. **Target (mean) encoding** — replace category with the average target for that category, via
   the `category_encoders` library. Popular with competition winners but risks overfitting;
   validation transforms must fit only on training data.
   ```python
   from category_encoders.target_encoder import TargetEncoder
   encoder = TargetEncoder(cols=['col']); encoder.fit(df_train, df_train['target'])
   df_encoded = encoder.transform(df_test)
   ```
5. **Extracting features from strings** — booleans (`str.contains`), word/element counts. "has
   doorman" / "num_photos" gave marketing insight but didn't move price much.
6. **Synthesizing numeric features** — combine existing columns. **Warning on target-derived
   features:** "This is a form of data leakage, which is a general term for the use of features
   that directly or indirectly hint at the target variable." Such features must be computed from
   training data only and applied to validation via stored mappings.
7. **Injecting external neighborhood info** — Manhattan distance from each apartment to desirable
   neighborhood centers. "Definitely worth trying as a general rule," especially for
   location-based prediction. OOB 0.868 → **0.872**.
   ```python
   for hood, loc in neighborhoods.items():
       df[hood] = np.abs(df.latitude - loc[0]) + np.abs(df.longitude - loc[1])
   ```

**RFs are forgiving:** "RFs simply ignore features without much predictive power," so you can pile
on engineered features without confusing the model (though pruning unimportant ones aids interpretability).

---

## 9. Train, Validate, Test (bulldozer-testing.html)

**The testing trilogy.** Training set (learn) → validation set (tune hyperparameters during
development) → test set (final, untouched). "The only true measure of model generality comes from
computing metrics on a test set that has never previously been run through the model." "Every
change made to a model after testing it on a dataset, tailors the model to that dataset; that
dataset is no longer an objective measure of generality."

**Splitting.**
- Time-insensitive data → random holdout, ~70/15/15 train/val/test.
- Time-sensitive data (bulldozers) → sort chronologically, take last 15% as test, prior 15% as
  validation, first 70% as train. "Randomly splitting a dataset would yield training and
  validation sets that overlap in time ... it allows the model to train on data from the future."
  Actual splits: train 1989–2011 (389,126), val 2011 (12,000), test 2012 (11,574).

**OOB scoring caveat.** RF out-of-bag samples act as automatic validation, but for time-series
data "OOB samples are within the same date range as the training samples," so "metrics derived
from OOB samples are ... overly optimistic about the generality of a model."

**Consistency between sets** — "Transformations of validation and test sets can only use data
derived from the training set": same category→integer codes; fill missing numerics with training
medians; treat unseen validation/test categories as missing (encode 0); align one-hot columns.

**Hyperparameter tuning** (sequential, not full grid): `n_estimators` up until plateau;
`max_features` ~0.1–0.6; `min_samples_leaf` ~1–15. Bulldozer: `max_features` auto→0.3,
`min_samples_leaf` 1→2, RMSLE 0.2469 → 0.2327. Then iteratively drop the least-important ~10% of
features, recomputing importances (handles collinearity).

**Inflation adjustment.** Detected systematic bias: "Model underpredicts by $2352" over 20 years
of price inflation; added the average adjustment to predictions (segment-specific would be better).

**True generality.** Final model: test RMSLE 0.2396 (val 0.2275), test MAE $6,018; ~top 5% of
Kaggle competitors. Close val/test scores ⇒ "The model isn't overfit to the training data and,
therefore, doesn't fall apart when we move from the validation to the test set." Cautionary:
108 of 475 Kaggle competitors hit perfect validation scores via extreme overfitting but did
poorly on the hidden test set — held-out test sets are irreplaceable.
