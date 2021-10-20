import pandas as pd
data=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/netflix_titles_5085.csv')
import warnings
warnings.filterwarnings("ignore")
tvshow_df= data[data['type'] =='TV Show']
tvshow_df['tv_duration'] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)
movies_df= data[data['type'] =='Movie']
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)
import matplotlib.pyplot as plt
#import seaborn 
import seaborn as sns

#check null and replace with nan
print(movies_df.isnull().sum())
movies_df.cast.fillna("nan", inplace=True)
print(movies_df.isnull().sum())
print(movies_df.cast)

new_movies_df = movies_df[movies_df.cast!= 'nan'].set_index('title').cast.str.split(',', expand=True).stack().reset_index(level=1, drop=True)
plt.title('Top 10 Actor Movies Based on The Number of Titles')
sns.countplot(y = new_movies_df, order=new_movies_df.value_counts().index[:10])
plt.show()

###########################################################################################

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
