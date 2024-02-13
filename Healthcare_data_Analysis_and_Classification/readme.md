<h1>Stroke Patients Analysis And Classification</h1>

<p> The project includes analysis of stroke patients dataset and creating classification models for categorizing patients into stroke patients and no-stroke patients.</p>
<p> The project is divided into three stages EDA, Visualization and Modeling ,while in last part I share my thoughts. The data for the project was taken from Kaagle.</p>

<h3><strong>1. EDA</strong></h3>
<ol>
    <li>In this stage, data was analysed to see if there are any null values, data inconsistencies etc. and get rid of it.</li>
    <li>Only 'BMI' column contained null values which were replaced with mean BMI to maintain the distribution.</li>
    <li>Column 'gender' had only one value Other, which was replaced with Male value based on values of other features.</li>
    <li>Also, distribution of data and some basic relationships were visualized to understand the data better.</li>
</ol>

<h3><strong>2. Visualization</strong></h3>
<ol>
    <li>The new data created from the visualization was used to create a responsive dashboard to compare or analyse patients with respect to lifestyle health features provided in data.</li>
    <li>Some numerical variables were converted in categorical groups for better categorising.</li>
    <li>Some new measures were created using DAX to help with visualization and understanding of patients stats better.</li>
</ol>

<h3><strong>3. Modeling<strong></h3>
<ol>
    <li>The data was preprocessed in the stage with handling categorical variables, Scaling the data etc.</li>
    <li> The target varaible 'stroke' conatained heavy imbalance between the categories. The imbalanced was removed using SMOTE.</li>
    <li>6 classification models using Decision Tree, KNN, Logistic Regression, Random Forest, SVC, XGBoost were created.</li>
    <li>The performance was analysed for individual classifier and the best model was selected using hyperparameter tuning.</li>
    <li>The best model of each classifier was trained and tested on the data and metrics scores were recorded and stored for final comparison and conclusion.</li>
    <li>The model should be selected based on domain knowledge as the evaluation criteria might change.</li>
</ol>

<h3><strong>4. Conclusion</strong></h3>
<ol>
    <li>The original data was healvily imbalanced, which affected the result significantly. Using SMOTE improved results slightly which os still good.</li>
    <li>Regarding Evaluation criteria, In healthcare domain, recall is as important as accuracy, because we want more patients to get treated while avoiding unnecessary treatment for healthy people.
    </li>
    <li>The situation demands balanced evaluation between accuracy and recall, which makes 'f1-score with recall score' most valuable metric.</li>
    <li>Based on above metric, I recommend Logistic Regression. Even though it lacks a little in terms Accuracy. The recall score, f1 score and ROC-AUC score makes it suitable candidate for me.But, it just my opinion.  
    </li>
    <li> As I mentioned earlier, domain experts can have different opinion depending how they want to handle the problem.</li>
</ol>