import pandas as pd
data=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/netflix_titles_5085.csv')
import warnings
warnings.filterwarnings("ignore")
tvshow_df= data[data['type'] =='TV Show']
tvshow_df['tv_duration'] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)
movies_df= data[data['type'] =='Movie']
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)
import matplotlib.pyplot as plt

#plot first plot for movies_df
x=movies_df['movies_duration']
x.plot(kind ='hist')
plt.xlabel('movies_duration')
plt.show()

#plot second plot for tvshow_df
x=tvshow_df['tv_duration']
x.plot(kind='hist')
plt.xlabel('tv_duration')
plt.show()

####################################################################

import pandas as pd
data=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/netflix_titles_5085.csv')
import warnings
warnings.filterwarnings("ignore")
tvshow_df= data[data['type'] =='TV Show']
tvshow_df['tv_duration'] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)
movies_df= data[data['type'] =='Movie']
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)
import matplotlib.pyplot as plt

#plot boxplot for movies_df
x=movies_df['movies_duration']
x.plot(kind= 'box')
plt.xlabel('movies_duration')
plt.show()

#########################################################################

import pandas as pd
data=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/netflix_titles_5085.csv')
import warnings
warnings.filterwarnings("ignore")
tvshow_df= data[data['type'] =='TV Show']
tvshow_df['tv_duration'] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)
movies_df= data[data['type'] =='Movie']
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)
import matplotlib.pyplot as plt

#plot the density graph for movies_df
x=movies_df['movies_duration']
x.plot.kde()
plt.show()

#############################################################################3

#write your code here
#write your code here
import pandas as pd
data= pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/Pokemon_4685.csv')
data2= data[['HP', 'Attack','Defense','Sp. Atk','Sp. Def','Speed' ,'Generation']]
import seaborn as sns

corr_data= data2.corr

newdata=data[(data['Type 1']=='Fire') |(data['Type 2']=='Fire')]
newdata2=data[(data['Type 1']=='Water') |(data['Type 2']=='Water')]

#plot the scatter graph1
import matplotlib.pyplot as plt
plt.scatter(x=newdata['Attack'],y=newdata['Defense'], color= 'Red' )
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.show()
