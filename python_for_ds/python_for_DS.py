#series
#similar to list in python

import pandas as pd
songs=pd.Series([145,142,38,14],name='count')
songs.index

songs1=pd.Series([145,142,38,14],name='count',
    index=['paul','john','george','ringo'])
songs1.index
songs1

###############################

import pandas as pd
f1=pd.read_csv('age.csv')
f1

###############################3
import pandas as np
numpy_ser=np.array([145,142,38,13])
songs1=pd.Series([145,142,38,13],name='count',
    index=['paul','john','george','ringo'])
songs1[1]
#o/p=142
numpy_ser[1]

songs1.mean()
numpy_ser.mean()
###################################
#operations performed create ,read,update and delete
#creation
george=pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],
name='george_Songs')
george
#########################
george['1968']
george['1970']

#####################################
#we can iterate over data in series
#as well. when iterating aver series
for item in george:
    print(item)
    
###########################
#updating values in series
george['1969']=68
george['1969']
george

################################
#deletion
s= pd.Series([2,3,4],index=[1,2,3])
del s[1]
s
##############################
#convert types
songs_66=pd.Series([3,9,11,7],
                   index=['paul','john','george','ringo'],
                   name='counts')
songs_66.dtypes
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
#erroe
pd.to_numeric(songs_66.apply(str),errors='coerce')
#if we pass errors='coerce'we can see it supports many formats
songs_66.dtypes
#dealing with None
#the .fillna will replace them with given value
songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes
#########################
#drop nan value
songs_66=pd.Series([3,None,11,7],
index=['paul','john','george','ringo'],
name='counts')
songs_66=songs_66.dropna()
songs_66
#################################
#append,combining,and joining two series
songs_69=pd.Series([7,4,6,9],
index=['paul','john','george','ringo'],
name='counts')
songs=pd.concat([songs_66,songs_69])
songs
###############################
#plotting series
import matplotlib.pyplot as plt
fig=plt.figure()
songs_69.plot()
plt.legend()
###########
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend
#################
#histogram
import numpy as np
data=pd.Series(np.random.randn(500),name="500_random")
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
#########################################
#DATA FRAMES
#it is 2-D data structure
#T check current version of pandas
import pandas as pd
pd.__version__
####################
#using constructor
#create pandas dataframe from list
import pandas as pd
technologies=[["spark",20000,"30days"],
             ["pandas",20000,"40days"]]
df=pd.DataFrame(technologies)
print(df)
#############################

column_name=["courses","fee","duration"]
row_lebel=["a","b"]
df=pd.DataFrame(technologies,columns=column_name,index=row_lebel)
print(df)
###########################
df.dtypes
######################
import pandas as pd
technologies={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'Fee':[2000,23000,23400,40000,50000,456600,90000],
    'Duration':['30d','40d','35d','50d','69d','3d','5d'],
    'Discount':[11.4,23.7,13.5,66.7,13.6,12.8,6.7]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)
#############################
#all columns to best possible type
df2=df.convert_dtypes()
print(df2.dtypes)
#############
##all columns to same type
df=df.astype(str)
print(df.dtypes)
##########
#change type from one or multiple columns
df=df.astype({"Fee":int,"Discount":float})
print(df.dtypes)
#######################
#conver data type for all columns in list
df=pd.DataFrame(technologies)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes
#########################
#ignores error
df=df.astype({"courses":int},errors='ignore')
df.dtypes
####################
#generate errors
df=df.astype({"courses":int},errors='raise')
############
#conver feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df['Discount']=pd.to_numeric(df['Discount'])
df.dtypes
##########################
technologies2={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'Fee':[2000,23000,23400,40000,50000,456600,90000],
    'Duration':['30d','40d','35d','50d','69d','3d','5d'],
    'Discount':[11.4,23.7,13.5,66.7,13.6,12.8,6.7]
    }
df=pd.DataFrame(technologies2)
df
#convert data frame into csv file
df.to_csv('data_file.csv')
##############################
#pandas data frame basic operation
import pandas as pd
import numpy as np
technologies={
    'courses':["aa","bb","cc","dd","ee",None,"ff","gg"],
    'Fee':[2000,23000,23400,40000,np.nan,50000,456600,90000],
    'Duration':['30d','40d','35d','','50d','69d','3d','5d'],
    'Discount':[11.4,23.7,13.5,66.7,13.6,12.8,6.7,9.0]
    }
row_lebel=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_lebel)
print(df)

#data frame properties
df.shape
df.size
df.columns
df.columns.values
df.index
df.dtypes
df.info

############################
#accessing one column  content
df['Fee']

#accessing two columns content
cols=['Fee','Duration']
df[cols]
df[['Fee','Duration']]

#select certain rows and assign it to another dataframe
df2=df[6:]
df2=df[:6]
df2

########################
#accessing certain cells 'Duration'
df['Duration'][3]

#subtracting specific value from a column
df['Fee']=df['Fee']-5000
df["Fee"]

#######################
df['Fee']=df['Fee']+5000
df["Fee"]

######################
#describe dataframe of all numeric columns
df.describe()
#it will show 5 num summery

#################################
#rename()-renames pandas dataframe column
df=pd.DataFrame(technologies,index=row_lebel)
df
#assign new header by settin new column names
df.columns=['A','B','C','D']
df

####################################3
#rename column name using rename() method
df=pd.DataFrame(technologies,index=row_lebel)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2','C':'c3','D':'c4'})
df2

###########################
#drop dataframes Rows and columns
df=pd.DataFrame(technologies,index=row_lebel)

#drop rows by lebels
df1=df.drop(['r1','r2'])
df1

#delete rows by position /index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1

#delete rows by index range
df1=df.drop(df.index[2:])
df1

#when tou have default index for  row
df=pd.DataFrame(technologies)
df1=df.drop(0)
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0)#it will delete row 0 and row3
df1
df1=df.drop(range(0,2))#it will delete 0 and 1
df1

######################################
import pandas as pd
import numpy as np
technologies={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'Fee':[2000,23000,23400,40000,50000,456600,90000],
    'Duration':['30d','40d','35d','50d','69d','3d','5d'],
    'Discount':[11.4,23.7,13.5,66.7,13.6,12.8,6.7]
    }
row_lebel=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies)
print(df)
#drop column by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)
#using inplace =true
df.drop(df.columns[2],axis=1,inplace=True)
print(df)
##################################
df.DataFrame(technologies)

#drop two or more columns by lebel name
df2=df.drop(["courses","Fee"],axis=1)
print(df2)

##################################
#drop two or more columns by index
df=df.DataFrame(technologies)

df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
#################################
#drop columns form list of columns
df=pd.DataFrame(technologies)
df.columns
lisCol=["courses","Fee"]
df2=df.drop(lisCol,axis=1)
print(df2)
################
#remove coiumns from dataframe inplace
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df

###################################
############
import pandas as pd
import numpy as np
technologies={
    'courses':["aa","bb","cc","dd","ee",None,"ff","gg"],
    'Fee':[2000,23000,23400,40000,np.nan,50000,456600,90000],
    'Duration':['30d','40d','35d','','50d','69d','3d','5d'],
    'Discount':[11.4,23.7,13.5,66.7,13.6,12.8,6.7,9.0]
    }
row_lebel=['r0','r1','r2','r3','r4','r5','r6','r7']
df=pd.DataFrame(technologies,index=row_lebel)
print(df)

#df.iloc[startrow:endrow,startcolumn:endcolumn]

df=pd.DataFrame(technologies,index=row_lebel)
#below are quick examples
df2=df.iloc[:,0:2]
df2

df2=df.iloc[1:4,0:3]
df2

##################
df2=df.iloc[0:2,:]
df2

#slicing specific rows and columns using iloc attribute
df3=df.iloc[1:2,1:3]
df3

df2=df.iloc[2]#select row by index
df2
#select row by integer index

df2=df.iloc[2,3,6]#select rows by index list
df2=df.iloc[1:5]#select rows by integer index
df2=df.iloc[:1]#select first row
df2=df.iloc[:3]#select first three rows
df2=df.iloc[-1:]#select last row
df2=df.iloc[::2]#select alternate row
df2

##########################
#select rows by index labels
df2=df.loc['r2'] #select row by lebal
df2
df2=df.loc[['r2','r3','r6']] #select row by index lebel
df2=df.loc['r1':'r5'] #SELECT INDEX BY LEBel index row
df2
df2=df.loc['r1':'r5':2] #select alternate row
df2

##############################################
#pandas select columns by name or index
#by using df[] notation
df2=df['courses']
df2
#select ultiple columns
df2=df[["courses","Fee","Duration"]]

#using loc[] to take column slices
df2=df.loc[:,["courses","Fee","Discount"]]
#select random column
df2=df.loc[:,["courses","Fee","Discount"]]
#select columns between two columns
df2=df.loc[:,'Fee':'Discount']
#select column by range
df2=df.loc[:,'Duration':]
#select columns by range
#all columns up to "duration"
df2=df.loc[:,:'Duration']
#select every alternate column
df2=df.loc[:,::2]

############################################
##############################
#pandas.dataframe.query() for examples
#query all rows with courses=cc
df2=df.query("courses=='cc'")
print(df2)

#####################################
#not equals condition
df2=df.query("courses !='cc'")
df2

#################################
#pandas add new column to DataFrame
import pandas as pd
import numpy as np
technologies={
    'courses':["aa","bb","cc","dd","ee"],
    'Fee':[2000,23000,23400,40000,50000],
    'Duration':['30d','40d','35d','3d','5d'],
    'Discount':[11.4,13.6,12.8,6.7,9.0]
    }
row_lebel=['r0','r1','r2','r3','r4']
df=pd.DataFrame(technologies,index=row_lebel)
print(df)

######################################
#pandas add new column to DataFrame
tutors=['ram','sham','akash','abhi','raj']
df2=df.assign(TutorsAssigned=tutors)
print(df2)
##############################
#add multiple columns to dataframe
MNCCompanies=['TATA','HCL','Infosys','google','amazon']
df2=df.assign(MNC=MNCCompanies,tutors=tutors)
df2

####################################
#derive new column from existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_Percent=lambda x: x.Fee * x.Discount/100)
print(df2)

#######################################
#append column to existing pandas DataFrame
df.pd.DataFrame(technologies)
df["MNCCompanies"]=MNCCompanies
print(df)

##########################
#add column at specific postion
df=pd.DataFrame(technologies)
df.insert(0,'tutors',tutors)
print(df)

#############################
#pandas rename column
df2=df.rename(columns={'courses':'courses_list'})
print(df2.columns)

##############################
#rename multiple columns
df.rename(columns={'courses':'courses_list','Fee':'Feelist','Duration':'Duration_list'},inplace=True)
print(df2.columns)
df.columns
###########################
#quick example to get number of rowa in dataFrames
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count
column_count=len(df.axes[1])
column_count

###################################

df.pd.DataFrame(technologies)
rows_count=df.shape[0]
rows_count
column_count=df.shape[1]
print(rows_count)
print(column_count)

#####################################
#using DataFrame.apply() to apply function add column
import pandas as pd
import numpy as np

data={"A":[1,2,3],
      "B":[4,5,6],
      "C":[7,8,9]}

df=pd.DataFrame(data)
print(df)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

################################
#using appiy function single column
def add_4(x):
    return x+4
df["B"]=df["B"].apply(add_4)
df["B"]

######################
#apply to multiple columns
df[["A","B"]]=df[["A","B"]].apply(add_4)
df

###########################
#apply lambda function to each column
df2=df.apply(lambda x : x+20)
df2

#apply lambda functiom to single column
df["A"]=df["A"].apply(lambda x : x-20)
df

################################
#using dataframe transform
def add_4(x):
    return x+4
df=df.transform(add_4)
print(df)

####################################
#using pandas dataframe.map
df["A"]=df["A"].map(lambda A : A/2.)
df

###############################
#using numpy function of single column
#using dataframe.apply() & [] operator
import numpy as np
df['A']=df['A'].apply(np.square)
print(df)

########################
df['A']=np.square(df['A'])
print(df)

###############################
#pandas groupby()
import pandas as pd
technologies={
    'courses':["aa","bb","cc","dd","ee","ff","gg"],
    'Fee':[2000,23000,23400,40000,50000,456600,90000],
    'Duration':['30d','40d','35d','50d','69d','3d','5d'],
    'Discount':[11.4,23.7,13.5,66.7,None,12.8,6.7]
    }
df=pd.DataFrame(technologies)
print(df.dtypes)

