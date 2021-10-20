#Import pandas library
import  pandas as pd


#Read csv file imdb movies and print the shape of imdb_movies.

imdb_movies=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/imdb_movies_3070.csv')
#print(imdb_movies.shape)

#Read csv file imdb ratings and print the shape of imdb_ratings.
imdb_ratings=pd.read_csv('https://cleveredailabs.s3.ap-south-1.amazonaws.com/imdb_ratings_8874.csv')
#print(imdb_ratings.shape)

#Create a new dataframe ratings & print its shape
ratings = pd.DataFrame({'Title':imdb_movies.title,'Rating': imdb_ratings.weighted_average_vote})
#print(ratings.shape)

#Drop all duplicates values  
ratings.drop_duplicates(subset=['Title','Rating'], inplace=True)
ratings.dropna()
print(ratings.shape)

#Read csv file netflix_titles & print shape of data
data=pd.read_csv("https://cleveredailabs.s3.ap-south-1.amazonaws.com/netflix_titles_5085.csv")
print(data.shape)

#Merge the two dataframe ratings and data and print the merged_df
merged_df=ratings.merge(data,left_on='Title',right_on='title',how='inner')
print(merged_df.shape)

#Sort the dataframe merged_df and print the top 5 rows of merged_df.
merged_df=merged_df.sort_values(by='Rating', ascending= True)
#print(merged_df.head(5))


#sort values in ascending order 
old_movie = merged_df.sort_values("release_year", ascending = True)

#check for ("") in duartion column
old_movie = old_movie[old_movie['duration'] != ""]

#print old_movie
print(old_movie[['title','release_year']][:20])



import seaborn as sns
import matplotlib.pyplot as plt

#Find correlation matrix and print it.
corr_data=data.corr()
print(corr_data)
plt.figure(figsize=(30,10))
#Plot the correlation matrix
sns.heatmap(corr_data,annot=True)
plt.show()
