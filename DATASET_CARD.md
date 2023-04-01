# Dataset: NYSE Financial Data

## Motivation
The primary motivation behind creating the NYSE Financial Data dataset card is 
to enhance my personal investment workflow. By having a well-structured and 
comprehensive dataset at hand, I can analyze the financial performance of 
companies listed on the New York Stock Exchange and make more informed investment 
decisions. Additionally, this dataset card serves as a means to compare the predictions 
made by AI models with my own findings, which will help me to assess the effectiveness 
of these models in predicting financial trends and identifying potential investment 
opportunities. Ultimately, the dataset card aims to improve my investment 
decision-making process and assist me in achieving better returns on my investments.

### Overview
This dataset contains financial metrics and stock prices for companies listed 
on the New York Stock Exchange (NYSE). The data keys cover a wide range of 
financial indicators, allowing for in-depth financial analysis of the listed companies.

### Dataset Builder
The dataset was built using DatasetBuilder, a powerful tool for collecting and organizing data.

### Composition
- 66627 instances
- Each instance is a historical financial quarter for a company listed on the NYSE.
- Each instance is indexed by a unique identifier of the format "TICKER-Qx-YYYY", 
    where 'TICKER' is the company's ticker symbol, 'YYYY' is the financial year and Q'x' 
    is the quarter number (1, 2, 3 or 4). e.g. 'AAPL-2018-Q1' is the first quarter of 2018 for Apple Inc.
- 66 features
    - 'date', 'start_date' and 'period' are the only non-numeric features and are present for identification.
    - 'start_date' is actually repeated over a total of three columns.
    - 'priceRatioRelativeToS&P_1Q', 'priceRatioRelativeToS&P_2Q', 'priceRatioRelativeToS&P_3Q' 
        and 'priceRatioRelativeToS&P_4Q' are the columns that can be considred as labels. 
        These detail the future relative price increase of the stock versus the S&P500. '1Q' 
        is looking at the next quarter, '2Q' is looking at the quarter after that, and so on.

- The dataset was built in a greedy manner by keeping as many features as possible. This means 
    that there are many features that may be highly correlated with each other and 
    care should be taken in the preprocessing steps.

### Dataset Information

#### General insights
1. Dataset shifts: This dataset holds data dating from the 1980s all the way to the present day. Keep in mind that the market dynamics might have changed over time, leading to possible dataset shifts. To account for these shifts, consider dividing the dataset into a training set and a test set using a time-based split. This will ensure that the model is trained on data that is representative of the time period it will be predicting on. One could also consider performing stationarity tests on the time series data. If requred, consider making use of techniques to make the time series data stationary.

2. Leakage: The columns 'priceRatioRelativeToS&P_1Q', 'priceRatioRelativeToS&P_2Q', 'priceRatioRelativeToS&P_3Q', and 'priceRatioRelativeToS&P_4Q' can be considered as labels, indicating future relative price increases of the stock versus the S&P500. To prevent leakage, ensure that these columns are not used to calculate any other features and that they are not present as input features.

3. Correlated features: The dataset was built in a greedy manner by keeping as many features as possible, meaning that there may be many features that are highly correlated with each other. To prevent overfitting and reduced model performance, perform feature selection or dimensionality reduction techniques to reduce the number of features in the dataset.

4. Missing values: The dataset is completely raw and has not been processed. As such, there will certainly be NaN values that must be handled. 

5. Data types: The only columns in the dataset that are not numeric are "date", "start_date" and "period". All others are either float64 or int64.

6. Outliers: The dataset is completely raw and has not been processed. As such, there are likely to be outliers.

7. Scaling: The dataset is completely raw and has not been processed. As such ll data is unscaled.

#### Features
# TODO: Add dtypes
The dataset includes the following data features:
- PE_avg
- PE_high
- PE_low
- S&P500PriceAverage
- S&P500PriceHigh
- S&P500PriceLow
- assetTurnover
- averageInventory
- averagePayables
- averageReceivables
- bookValuePerShare
- capexPerShare
- capexToDepreciation
- capexToOperatingCashFlow
- capexToRevenue
- capitalExpenditureCoverageRatio
- cashConversionCycle
- cashFlowCoverageRatios
- cashFlowToDebtRatio
- cashPerShare
- cashRatio
- companyEquityMultiplier
- currentRatio
- date
- daysOfInventoryOutstanding
- daysOfPayablesOutstanding
- daysOfSalesOutstanding
- daysSalesOutstanding
- debtToAssets
- debtToEquity
- dividendPaidAndCapexCoverageRatio
- dividendYield
- earningsYield
- ebitdaratio
- ebtPerEbit
- effectiveTaxRate
- enterpriseValue
- enterpriseValueMultiple
- enterpriseValueOverEBITDA
- eps
- evToFreeCashFlow
- evToOperatingCashFlow
- evToSales
- fixedAssetTurnover
- freeCashFlowOperatingCashFlowRatio
- freeCashFlowPerShare
- freeCashFlowYield
- grahamNetNet
- grahamNumber
- grossProfitMargin
- incomeQuality
- intangiblesToTotalAssets
- interestCoverage
- interestDebtPerShare
- inventoryTurnover
- investedCapital
- longTermDebtToCapitalization
- netCurrentAssetValue
- netDebtToEBITDA
- netIncomePerEBT
- netIncomePerShare
- netProfitMargin
- operatingCashFlowPerShare
- operatingCashFlowSalesRatio
- operatingCycle
- operatingProfitMargin
- payablesTurnover
- payoutRatio
- period
- pretaxProfitMargin
- priceEarningsRatio
- priceEarningsToGrowthRatio
- priceRatioRelativeToS&P_1Q
- priceRatioRelativeToS&P_2Q
- priceRatioRelativeToS&P_3Q
- priceRatioRelativeToS&P_4Q
- priceToBookRatio
- priceToFreeCashFlowsRatio
- priceToOperatingCashFlowsRatio
- priceToSalesRatio
- quickRatio
- receivablesTurnover
- researchAndDdevelopementToRevenue
- returnOnAssets
- returnOnCapitalEmployed
- returnOnEquity
- returnOnTangibleAssets
