<h1> Predicting Sales of Different Products of Different Outlets of Big Mart using Regression </h1>

<p>
    The project is about predicting Sales of different products from different Big Mart Outlets. 
</p>
<p>
    The project was divided into two parts understanding the dataset [EDA] and analysing performance of different Regression models on the data.
</p>

<h3><strong>1. EDA</strong></h3>
<ol>
    <li>
        This stage involved understanding the data and gettting rid of the unwanted things.
    </li>
    <li>
        Columns 'Item_weight' and 'Outlet_Type' had missing values. For Column 'Item_weight' the missing values were replaced with weight of same products from different outlets if it was available. For column 'Outlet_Type' the null values were replaced with mode of data.The null values still remained were dropped. 
    </li>
    <li>
        The data was incosistent in column 'Item_Fat_Content' i.e. same values were present in different format which were reaplce with one consistent value
    </li>
    <li>
        The data in columns 'Item_Visisbility' and 'Item_Outlet_Sales' were skewed which were converted to normal distribution using log-transformation and cuberoot-transformation resp.
    </li>
    <li>
        Columns 'Item_Visibility' and 'Item_Outlet_Sales' had OUtliers which were handled using IQR method.
    </li>
    <li>
        The data was visualised using different graphs using matplotlib and seaborn.
    </li>
</ol>

<h3><strong>2. Model Builing</strong></h3>
<ol>
    <li>
        For first step, the unwanted columns like index and identifiers were dropped.
    </li>
    <li>
        The categorical columns were encoded using pandas get_dummies and Label Encoder.
    </li>
    <li>
        The numerical columns were scaled down using StandardScaler as Regression models are sensitive to range of data.
    </li>
    <li>
        Different regression models like Linear Regression, Random Forest Regression, Support Vector Regression and XGBoost Regression etc. were evaluated with cross_validation and hyperparameters against the data. 
    </li>
    <li>
        R2_score and Mean_Absolute_Error was used for individual evaluation while R2_score and Root_Mean_Squared_Error were metrics for final evaluation.
    </li>
</ol>

<h3><strong>3. Conclusion</strong></strong></h3>
<ol>
    <li>
        Based on evaluation, SVM seems to performed well while XGBoost can also be a choice as it is close to SVM. Overall performance of models is above average but not good.
    </li>
    <li>
        With more in-depth modeling like feature selection, more hyperparameter tuning, improved performance can be achieved.
    </li>
</ol>
