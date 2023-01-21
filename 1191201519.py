import pandas as pd
import streamlit as st
import time
import webbrowser
from PIL import Image

st.title ("Predicting Mental Health Risk Factors Among College Students: A Comparative Analysis of Different Classification Algorithms ")

df = pd.read_csv("Student Mental health.csv")

#Select Location
Select = st.radio("Please select", ("Introduction", "Problem Statement", "Data Cleaning", "Exploratory Data Analysis", "Feature Selection" ,"Model Selection and Comparison", "Model Evaluation"))

if Select == "Introduction":
    # set header
    st.header('Introduction')
    st.write("Mental health is a critical issue that affects individuals of all ages, and it has become increasingly important in recent years to understand the factors that contribute to mental health among young adults. University students, in particular, are at a high risk for mental health issues such as depression, anxiety, and panic attacks. Many university students experience mental health concerns at various stages of their education. This becomes even more important when they near the end of their studies and consider their future options.With the increasing pressure to succeed academically and socially, university students are more susceptible to mental health problems than ever before. Understanding the risk factors that contribute to mental health issues among university students is crucial to helping them get the support they need. In this study, we aim to use machine learning techniques to predict mental health risk factors among university students by analysing their demographic, academic and self-reported mental health symptoms data. We will compare the performance of different classification algorithms and identify the most important predictors of mental health risk among university students. The fundamental goal of this research is to investigate the state of mental well-being in university students by utilising numerous personality factors and fields of specialty")
    MH = df
    
elif Select == "Problem Statement":
    # set header
    st.header('Problem Statement')
    st.markdown("The problem statement that I am going to study is the effects of student's gender, age, course, course year, CGPA and marital status on their mental health and to use machine learning techniques to predict mental health risk factors.")
    MH = df
    
elif Select == "Data Cleaning":
    # set header
    st.header('Pre-processing data')
    
    # set subheader
    st.subheader('Detecting rows with null values in the dataset')
    st.markdown('First, locate the null value in the dataset')
    image = Image.open('DataCleaning(1).png')
    st.image(image, caption='Null value in the dataset')
    st.markdown("Since the null value was only affecting one row which is row 43, I decided to remove it due to having no method to validated the student's age.")
    
    st.subheader('Drop column "Timestamp"')
    st.markdown('Next, to drop unused column in this experiment.')
    image = Image.open('DataCleaning(2).png')
    st.image(image, caption='Column Timestamp dropped.')
    
    st.subheader('Shorten column properties')
    image = Image.open('DataCleaning(4).png')
    st.image(image, caption='Column names shortened.')
    st.markdown("This step makes them easier to comprehend and to refer to when performing data analysis.")
    
    st.subheader('Standardise "Course Year" column')
    st.markdown('Values in "Course Year" column were found not consistently formated as some entries being written as "year 1" and others as "Year 1"')
    image = Image.open('DataCleaning(3).png')
    st.image(image, caption='Column Timestamp dropped.')
    st.markdown("To standardise the format, a custom function was created to extract the last character of each string, which corresponds to the year number. The function also converted the values into integers. This cleaning process ensured that the 'Course Year' column was consistent and in a format suitable for analysis. Furthermore, it also allowed for accurate calculations and comparisons to be made based on the course year of the students.")
    
    st.subheader('Cleaning values in "Course" column and "CGPA" column')
    st.markdown("Cleaning the values in the 'Course' column would consume the majority of my work, given the dataset was received from a Google form and student responses are short form. I conducted research on each course in this column to harmonise the data and identify similar courses.")
    st.markdown("Furthermore, I removed unnecessary space in ‘CGPA’ values and replaced the CGPA scores ranging from 1 to 5")
    image = Image.open('DataCleaning(5).png')
    st.image(image, caption='Courses are grouped up into one if they are the same course and CGPA of students are range from 1 being the lowest and 5 being the highest.')
    
    
    
elif Select == "Exploratory Data Analysis":
    # set header
    st.header('Exploratory Data Analysis')
    
    # set subheader
    st.subheader('Descriptive Question')
    st.markdown('"How many instances are there in the dataset?"')
    image = Image.open('EDA(1).png')
    st.image(image, caption='Student Mental health dataset by www.kaggle.com')
    st.markdown('There are 101 instances in the dataset.')
    
    # set subheader
    st.subheader('Descriptive Question')
    st.markdown('"What is the mean age among the participants in the study?"')
    image = Image.open('EDA(2).png')
    st.image(image, caption='Descriptive statistics of age')
    st.markdown('From the descriptive statistics above, we can clearly observe the count, mean, standard deviation, min, interquartile range and the max value of the student’s age. We are able to see that the count is 100 as we have 100 rows of data after performing data preprocessing. The minimum age from our dataset is 18 years old which suggests the youngest of respondents to the survey was a first year student while the max is 24 years old which I would assume is a year 4 student. The answer is the meanos students age is 20.53.')
    image = Image.open('EDA(3).png')
    st.image(image, caption='Age distributions of students in the dataset.')
    st.markdown('By looking at the bar chart, we can tell that the respondents are students between the ages of 18 and 24. In comparison to others, responses from students aged 20-23 are minimal.')
    
    # set subheader
    st.subheader('Exploratory Question')
    st.markdown('"What is the gender distribution of students in the dataset?"')
    image = Image.open('EDA(4).png')
    st.image(image, caption='Gender distribution of students in the dataset')
    st.markdown('Majority of the students who took the survey were females which stands at 75% of the dataset while only 25% of male students took the survey.')
    
    # set subheader
    st.subheader('Exploratory Question')
    st.markdown('“What is the distribution of students with positive mental health issues and negative mental issues?”')
    image = Image.open('EDA(5).png')
    st.image(image, caption='Mental health distribution of students in the dataset')
    st.markdown('By observing the pie chart above, we can see that 64% of students from the dataset is facing mental health issues and 36% of students does not face either depression, anxiety or panic attack.')
    
    # set subheader
    st.subheader('Exploratory Question')
    st.markdown('“What is the most common course of the participants in the dataset?”')
    image = Image.open('EDA(6).png')
    st.image(image, caption='Course count of students in the dataset')
    st.markdown('In the bar plot of the dataset, it was observed that IT is the most common course among the student respondents, with the second highest being engineering. Biotechnology, pharmacy, finance, research, business administration, marine science, accounting and radiography were the least common courses among the student respondents. This information provides valuable insight into the composition of the student population in the dataset and may be useful in further analysis and understanding the study population.')
    
    # set subheader
    st.subheader('Exploratory Question')
    st.markdown('"What is the proportion of participants who seek treatment while having mental health conditions in the dataset?"')
    image = Image.open('EDA(7).png')
    st.image(image, caption='Students facing mental health that seeks treatment and dont.')
    st.markdown('Based on the pie chart, it can be observed that a vast majority (90.6%) of the student respondents in the dataset do not seek treatment for their mental health conditions. This indicates that a significant portion of students may not be receiving the support they need to manage their mental health. The proportion of students who do seek treatment for their mental health issues (9.4%) is relatively small, highlighting the need for more effective outreach and support for students struggling with mental health issues. ')
    
    # set subheader
    st.subheader('Exploratory Question')
    st.markdown('"What is the relationship between the course and the prevalence of mental health issues among students?"')
    image = Image.open('EDA(8).png')
    st.markdown('The bar plot of count of students with mental health issues reveals some interesting insights. IT, Engineering, Human Science, Islamic Education, are the top four courses where students report experiencing mental health issues. IT has the highest number of students reporting mental health concerns with 21 out of 27 students. Engineering comes in second with 17 out of 26 students. Human Science and Islamic Education have a similar number of students with 4 out of 8 students each. It is worth noting that these courses tend to be demanding, which could explain why students in these fields are more likely to report mental health issues. This highlights the importance of providing support and resources for students in these fields.')
    
    # set subheader
    st.subheader('Exploratory Question')
    st.markdown('"Is there a significant difference in the CGPA of students with mental health issues compared to students without mental health issues?"')
    image = Image.open('EDA(9).png')
    st.image(image, caption='CGPA of students with mental health vs dont')
    st.markdown('Upon examination of the comparative bar plot of CGPA for students with and without mental health issues, we find that the majority of students have reported a CGPA of 3.0 and above. However, what is intriguing is that despite experiencing mental health issues, the distribution of CGPA for these students is not vastly different from that of their peers who do not report such issues. This suggests that, on average, students with mental health issues are still performing academically at a similar level to their peers.')
    
    # set subheader
    st.subheader('Predictive Question')
    st.markdown('“Will a student in their 3rd year of study have a higher likelihood of experiencing a panic attack compared to a student in their 1st year of study?”')
    image = Image.open('EDA(10).png')
    st.image(image, caption='Proportions of students in Year 1 and Year 3 with and without panic attack.')
    st.markdown('Based on the data analysed, it appears that there is not a significant difference in the likelihood of experiencing a panic attack between students in their 1st year of study and students in their 3rd year of study. However, it is worth noting that while a higher proportion of 1st year students (around 70%) did not report experiencing a panic attack, the sample size of 3rd year students is smaller, which means 3rd year students have a higher likelihood of experiencing a panic attack. This may be due to 3rd year students being close to graduating and stressing on harder subjects. ')
    
    # set subheader
    st.subheader('Heatmap Analysis')
    image = Image.open('EDA(11).png')
    st.image(image, caption='Heatmap on correlation analysis of the dataset')
    st.markdown('The heatmap of correlation analysis between variables in our dataset reveals some intriguing insights. Perhaps the most striking discovery is the strong association between Marital Status and Depression. This suggests that marital status may play a significant role in the development of depression symptoms among university students. Furthermore, the heatmap also highlights a strong correlation between Anxiety, Panic Attack, and Depression. This highlights the interconnected nature of these mental health issues and the importance of addressing them together. Additionally, the heatmap also indicates a slight correlation between Marital Status and seeking medical assistance (treatment) which implies that marital status may also be a factor in the decision to seek help for mental health issues among university students. Overall, these findings provide valuable insights into the underlying factors that contribute to mental health issues among university students.')
    
elif Select == "Feature Selection":
    # set header
    st.header('“What is the suitable feature selection technique to use for predicting the cause of mental health?”')
    st.markdown('The suitable feature selection technique to use for predicting the cause of mental health is the chi-squared test in combination with the SelectKBest function and k-means clustering. The chi-squared test is a statistical test that calculates the relationship between each feature and the target variable, and scores them based on how informative they are in predicting the target variable. This allows us to determine which factors are most relevant in predicting mental health outcomes.')
    st.markdown('Additionally, the SelectKBest function allows us to select the top k features with the highest scores from the chi-squared test, which helps in reducing the dimensionality of the data, and improves the accuracy and efficiency of the final classifier.')
    st.markdown('Furthermore, the k-means clustering algorithm is particularly useful in identifying patterns and structures in the data, which can be helpful in understanding the causes of mental health issues.')
    
    # set header
    st.header('“How should I obtain the optimal feature set?”')
    st.markdown('The optimal feature set can be obtained by using feature selection techniques. In this topic’s case, chi-squared test and the feature selection algorithm used is SelectKBest. The feature selection selects the top 5 features that have highest correlation with the response variable. The descriptor variable would be the student’s gender, age, course, course year, CGPA and marital status. The response variable is Depression, Anxiety, Panic Attack and Mental Health Issue.')
    image = Image.open('FS.png')
    st.image(image, caption='Features selected using SelectKBest function and K-Means Clustering')
    
elif Select == "Model Selection and Comparison":
    # set header
    st.header('Model Selection and Comparison')
    st.markdown('In order to choose the best classifier among the chosen four which includes, Random Forest, Logistic Regression, Decision Tree and SVC, I used pipeline function to choose the best classifier and output the accuracy.')
    image = Image.open('MS(1).png')
    st.image(image, caption='Accuracy scores for model selection')
    st.markdown('Logistic Regression Classifier appears to be the most accurate among 4 classifiers in our case where the features used are Gender, Age, Course, CGPA and Marital Status selected from feature selection, which are all factors that have been shown to be related to mental health issues.')
    
elif Select == "Model Evaluation":
    st.header('Model Evaluation')
    st.markdown('To evaluate the performance of Linear Regression, hyperparameter tuning is applied to compare the performance of Linear Regression with and without hyperparameter tuning.')
    image = Image.open('MS(2).png')
    st.image(image, caption='Comparison between both model')
    st.markdown("Hyperparameter tuning was performed using GridSearchCV from sklearn.model_selection library. The range of values for the 'C' and 'penalty' hyperparameters were [0.1, 1, 10, 100, 1000] and ['l1', 'l2'] respectively. The evaluation metric used to select the best set of hyperparameters was accuracy. The best set of hyperparameters found were C = 0.1 and penalty = 'l2' by using a 5-fold cross validation technique.")
    st.markdown("The model with hyperparameter tuning had higher accuracy, recall, precision, and F1 scores, but a lower AUC score than the model without tuning. It's crucial to balance recall and AUC when identifying students with mental health issues. Overall, the model with tuning performed better, but the trade-off between AUC and other metrics should be considered.")
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
with open("1191201519_IrfanDaniel_Report.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Report",
                    data=PDFbyte,
                    file_name="1191201519_IrfanDaniel_Report.pdf",
                    mime='application/octet-stream')
