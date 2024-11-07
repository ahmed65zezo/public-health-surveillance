import pandas as pd
import matplotlib.pyplot as plt

# read file using pandas library
df = pd.read_excel(r"D:\trainning\trainning.xlsx")

# Checking if the data include null values or not
md = df.isnull().sum()
print(md)

# Checking if the data include dublicated values or not
dub = df.drop_duplicates(inplace=True)
print(dub)

# # Quick Overview of the Data
# loc = df['Location'].value_counts()
# print(loc)

# sex = df['Gender'].value_counts()
# print(sex)

# chronic = df['Chronic_Conditions'].value_counts()
# print(chronic)

# travel = df['Travel_History'].value_counts()
# print(travel)

# stay = df['Hospitalization_Requirement'].value_counts()
# print(stay)

# disease = df['Disease_Severity'].value_counts()
# print(disease)


# # Visualization
# fig, axis = plt.subplots(2,2)
# color = ['#16423C','#6A9C89','#C4DAD2']

# #pie
# sex = df['Gender'].value_counts()

# axis[0,1].pie(sex,autopct='%1.1f%%', textprops={'fontsize': 8,'color' :'w'}, startangle=90, colors=color)
# axis[0,1].set_title('Patient Gender',fontsize='12',color='black',fontweight='bold')
# axis[0,1].tick_params(axis='x',labelsize=3)
# axis[0,1].legend(labels=sex.index,prop={'size': 5},loc='lower left')
# axis[0,1].tick_params(axis='y',labelsize=5)


# # bar
# loc = df['Location'].value_counts()

# labels = ['Urban', 'Rural', 'Suburban']
# axis[0,0].bar(loc.index[-5:], loc.values[-5:], label=labels, color=color)
# axis[0,0].set_title('Patients Locaten', fontsize='12', color='black', fontweight='bold')
# axis[0,0].set_ylabel('Number of Patients', fontsize='7', color='black', fontweight='bold')
# axis[0,0].tick_params(axis='y', labelsize=8)
# axis[0,0].grid(axis='y', color='r', alpha=0.35, linestyle=':')


# #pie
# chronic = df['Chronic_Conditions'].value_counts()

# axis[1,0].pie(chronic,autopct='%1.1f%%', textprops={'fontsize': 8,'color' :'w'}, startangle=90, colors=color)
# axis[1,0].set_title('Chronic Conditions',fontsize='12',color='black',fontweight='bold')
# axis[1,0].legend(labels=chronic.index,prop={'size': 5},loc='lower left')


# #bar
# disease = df['Disease_Severity'].value_counts()

# labels = ['Mild', 'Moderate', 'Severe']
# axis[1,1].bar(disease.index[-5:], disease.values[-5:],label=labels, color=color)
# axis[1,1].set_title('Disease Severity', fontsize='12', color='black', fontweight='bold')
# axis[1,1].set_ylabel('Number of Patients', fontsize='7', color='black', fontweight='bold')
# axis[1,1].tick_params(axis='y', labelsize=8)
# axis[1,1].grid(axis='y', color='r', alpha=0.35, linestyle=':')


# # Display the plots
# plt.tight_layout()
# plt.show()