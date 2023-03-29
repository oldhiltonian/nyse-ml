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

### Data Features

The dataset includes the following data keys:
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
