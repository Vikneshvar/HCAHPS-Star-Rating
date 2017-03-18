import sys
import pandas as pd
import xlsxwriter

reload(sys)
sys.setdefaultencoding('utf8')


df_infection=pd.read_csv('Infection.csv',skipinitialspace=True)
df_survey=pd.read_csv('Survey.csv',skipinitialspace=True)

print(df_infection.columns)
print(df_survey.columns)



# Convert to excel using xlsxwriter object
writer_infection = pd.ExcelWriter('Infection.xlsx', engine='xlsxwriter')
writer_survey = pd.ExcelWriter('Survey.xlsx', engine='xlsxwriter')

df_infection.to_excel(writer_infection,sheet_name='Infection')
df_survey.to_excel(writer_survey,sheet_name='Survey')

writer_infection.save()
writer_survey.save()



