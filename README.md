# Fraud Detection on Classified Ads

_Methodology_
-----

There are several Data Analytics methodologies. Three popular methodologies are "Cross-industry standard process for data mining (CRISP-DM)", "The knowledge discovery in databases (KDD) process", and Microsoft's "Team Data Science Process (TDSP)".

1. CRISP-DM

![CRISP-DM](https://barnraisersllc.com/wp-content/uploads/2018/09/CRISP_en.png)![CRISP-DM2](https://www.actuaries.digital/wp-content/uploads/2016/07/datapic2.png)*CRIPS-DM*

2. KDD

![KDD](https://www.actuaries.digital/wp-content/uploads/2016/07/datapic1.png)*KDD* 

3. TDSP

![TDSP](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/media/overview/tdsp-lifecycle2.png)![TDSP2](https://docs.microsoft.com/en-us/azure/machine-learning/team-data-science-process/media/overview/tdsp-tasks-by-roles.png)*TDSP*

4. Extra: Methadology mentioned in the "R for Data Science" book
![R](https://d33wubrfki0l68.cloudfront.net/795c039ba2520455d833b4034befc8cf360a70ba/558a5/diagrams/data-science-explore.png)*Graph in the book R for Data Science*

5. Extra: A standard machine learning pipeline (source: Practical Machine Learning with Python, Apress/Springer)
![Machine Learning Workflow](https://cdn-images-1.medium.com/max/1600/1*2T5rbjOBGVFdSvtlhCqlNg.png)


I have summarized the tasks within each step of CRISP-DM  below. It is worth noting that this is an **iterative** (not a linear) process. Thus, we may call this process a "Data Science Lifecyle".

_**Not:** Asagida belirtilen ana basliklar, en cok kullanilan metodoloji olan CRISM-DM'ye istinaden secilmis olup alt basliklar okuduklarima istinaden benim kendi degerlendirmemdir. Bircok kaynakta asamalar/alt basliklar farkli sekilde ele alinabilmektedir._

* Business Understanding
    - Defining Objectives - Problem Definition
    - Identifying Data Sources
* Data Understanding
    - Data collection/acquisition
    - Exploring Raw Data (Initial EDA)
        + Describing Data
        + Viewing Structure/Data Types
        + Verifying Data Quality
* Data Preparation 
    - Tidying Data (Data Wrangling)
        + Reshaping Data (melting, pivoting vs.)
        + Splitting Cells
    - Data Preprocessing (Data Wrangling?)
        + Data Cleansing
            - Missing, Outlier, Inconsistent and Noisy Data Analysis
            - Converting Data Types
        + Data Transformation (Manipulation)
            - Feature Engineering
            - Feature Scaling (Standardization, Normalization)
            - Feature Selection (Data Reduction)
    - Data Exploration (EDA)
        + Summary
        + Visual
    - Sampling (Data cok buyukse)?
    - Data Splitting
    - Setting up a Pipeline (Asagidaki asamada olabilir)?
* Modelling
    - Selecting Modeling Techniques
    - Building Model
    - Assessing Model
* Evaluation
    - Evaluating Results
    - Reviewing Process
* Deployment


