#Import pandas library
import  pandas as pd
#import matplotlib library
import matplotlib.pyplot as plt


#reading the given dataset
df= pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/top50_3285.csv')

#Top five rows using head()
#print(df.head(5))

#Print all column names in data dataframe.
#print(df.columns)

# print the Null values 
#print(df.isnull().sum())

#print the info of data set
#print(df.info())

#print The dimension of the data frame
#print(df.shape)

#Recommend the Artist Name which has highest poularity.
#print(df['Artist.Name'].value_counts())


#Recommend which Artist Name is Most Popular.
#df.set_index('Artist.Name', inplace=True)             
#print(df['Popularity'].idxmax())

#Recommend which Artist Name has highest Danceability

#print(df['Danceability'].idxmax())


#Recommend which Artist Name has highest duration of Song.
#print(df['Length.'].idxmax())


#Recommend the Artist Name which has highest Energy
#print(df['Energy'].idxmax())

#Recommend the Artist Name which has highest Beats.Per.Minute
#print(df['Beats.Per.Minute'].idxmax())

#Recommend the Artist Name which has highest Liveness.
#print(df['Liveness'].idxmax())

#Recommend which Genre has highest count in Spotify dataset.
#print(df['Genre'].value_counts().idxmax())

#Recommend top 10 artist with top genres
'''top10 = pd.DataFrame(df.groupby('Artist.Name')[['Genre']].count().sort_values(by= 'Genre', ascending= False))

print(list(top10.index))'''

'''for i in range(0,10):
  print(top10.index[i])
#print(top10.index[0:10]) '''                                         #print as a list/one below the other?

#Recommend which genre has highest popularity.
'''genre= df.groupby('Genre')[['Popularity']].mean().sort_values(by= 'Popularity', ascending= False)
print(genre.index[0])'''

#Recommend and visualise Beats.Per.Minute for different Genres.?
y= df['Beats.Per.Minute']
x= df['Genre']
plt.figure(figsize= (30,8))
plt.scatter(x,y,color= 'Red')
plt.show()



#Recommend which genre has highest Energy.
'''df.set_index('Genre', inplace=True)             
print(df['Energy'].idxmax())'''

#Recommend which genre has highest Liveness.
'''print(df['Liveness'].idxmax())'''

#Recommend which genre has most suitable for dancing
'''dance = df.groupby('Genre')[['Danceability']].mean().sort_values(by= 'Danceability', ascending= False)
print(dance.index[0])  ''' 
