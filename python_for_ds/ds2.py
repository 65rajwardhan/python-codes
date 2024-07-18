#pandas groupby()
import pandas as pd
technologies={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'fee':[2000,23000,23400,40000,50000,456600,90000],
    'duration':['30d','40d','35d','50d','69d','3d','5d'],
    'discount':[11.4,23.7,13.5,66.7,None,12.8,6.7]
    }
df=pd.DataFrame(technologies)
print(df)

#using groupby() to compute the sum
df2=df.groupby(['courses']).sum()
print(df2)

######################
#group by multiple columns
df2=df.groupby(['courses','duration']).sum()
print(df2)

####################
#add index to grouped data
#add row index to the group by result
df2=df.groupby(['courses','duration']).sum().reset_index()
print(df2)

###############################
import pandas as pd
technologies={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'fee':[2000,23000,23400,40000,50000,456600,90000],
    'duration':['30d','40d','35d','50d','69d','3d','5d'],
    'discount':[11.4,23.7,13.5,66.7,None,12.8,6.7]
    }
df=pd.DataFrame(technologies)
print(df)
df.columns


#get list of all column names from header
column_header=list(df.columns.values)
print("the column Header",column_header)

#using list(df) to get column header as list
column_header=list(df.column)
column_header

#####################
###########
########
####
#pandas shuffle dataframe rows
import pandas as pd
technologies={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'fee':[2000,23000,23400,40000,50000,456600,90000],
    'duration':['30d','40d','35d','50d','69d','3d','5d'],
    'discount':[11.4,23.7,13.5,66.7,None,12.8,6.7]
    }
df=pd.DataFrame(technologies)
print(df)

#shuffle rows and return all rows
df1=df.sample(frac=0.5)
print(df1)

##################
#create a new index starting from zero
df1=df.sample(frac=1).reset_index()
print(df1)

###################################
#drop shuffle index
df1=df.sample(frac=1).reset_index(drop=True)
print(df1)

#######################################
#pandas joins
import pandas as pd
technologies1={
    'courses':["spark","pyspark","python","pandas"],
    'Fee':[2000,23000,456600,90000],
    'Duration':['30d','40d','35d','5d']
    }
index_lebel=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=index_lebel)
df1

technologies2={
    'courses':["spark","java","python","go"],
    'Fee':[200,2300,4600,900]
    }
index_lebel2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_lebel2)
df2
#pandas join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

#inner join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

#right join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

#left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)

#########################
###################
###########
import pandas as pd
technologies1={
    'courses':["spark","pyspark","python","pandas"],
    'Fee':[2000,23000,456600,90000],
    'Duration':['30d','40d','35d','5d']
    }
df1=pd.DataFrame(technologies1)
df1

technologies2={
    'courses':["spark","java","python","go"],
    'Fee':[200,2300,4600,900]
    }
df2=pd.DataFrame(technologies2)
df2
#pandas join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right")
print(df3)

#inner join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='inner')
print(df3)

#right join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='right')
print(df3)

#left join
df3=df1.join(df2,lsuffix="_left",rsuffix="_right",how='left')
print(df3)

##############################
#merge
import pandas as pd
technologies1={
    'courses':["spark","pyspark","python","pandas"],
    'Fee':[2000,23000,456600,90000],
    'Duration':['30d','40d','35d','5d']
    }
index_lebel=['r1','r2','r3','r4']
df1=pd.DataFrame(technologies1,index=index_lebel)


technologies2={
    'courses':["spark","java","python","go"],
    'Fee':[200,2300,4600,900]
    }
index_lebel2=['r1','r6','r3','r5']
df2=pd.DataFrame(technologies2,index=index_lebel2)

#merge
df3=df1.merge(df2)
df3

################
import pandas as pd
df=pd.DataFrame({
    'courses':["spark","pyspark","python","pandas"],
    'Fee':[2000,23000,456600,90000]
    })
df1=pd.DataFrame({
    'courses':["pandas","java","hadoop","hypperion"],
    'Fee':[200,2300,4600,900]})
#using pandas concat
data=[df,df1]
df2=pd.concat(data)
df2

#concatenate multiple dataframes
import pandas as pd
df=pd.DataFrame({
    'courses':["spark","pyspark","python","pandas"],
    'Fee':[2000,23000,456600,90000]
    })
df1=pd.DataFrame({
    'courses':["pandas","java","hadoop","hypperion"],
    'Fee':[200,2300,4600,900]})
df3=pd.DataFrame({
    'Duration':["30days","40days","50days","60days"],
    'Discount':[20000,23090,45600,9900]})

#appending multiple dataframes
df3=pd.concat([df,df1,df2])
print(df3)

##################################
##############
######
##
#read excel file
import pandas as pd
df=pd.read_excel('c:/1-python/AWS Cloud and DevOps Training (Responses).xlsx')
print(df)

#using series.values.tolist()
col_list=df.courses.values
print(col_list)
col_list=df.courses.values.tolist()
print(col_list)

#using series.values.tolist
col_list=df["courses"].values.tolist()
print(col_list)

#using lis function
col_list=list(df["courses"])
print(col_list)

###############################
#convert to numpy array
col_list=df['courses'].to_numpy()
print(col_list)

##############################
