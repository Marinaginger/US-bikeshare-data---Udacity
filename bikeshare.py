import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("Please pick a city to explore from these 3( chicago, new york city or washington)\n please write the city name exactly as it is written \n").lower()
    while city not in ( 'chicago', 'new york city', 'washington'):
         print ("please try again!")
         city = input("Please pick a city to explore from these 3( chicago, new york city or washington)\n please write the city name exactly as it is written \n").lower()
       
    # get user input for month (all, january, february, ... , june)
    month = input("Please pick a month(all, january, february, march, april, may, june)\n please write the month name exactly as it is written \n").lower()
    while month not in ( 'all', 'january', 'february', 'march', 'april', 'may', 'june'):
         print ("please try again!")
         month = input("Please pick a month(all, january, february, march, april, may, june)\n please write the month name exactly as it is written \n").lower()
    # get user input for day of week (all, monday, tuesday, ... sunday)
  # get user input for month (all, january, february, ... , june)
    day = input("Please pick a day(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n please write the day name exactly as it is written \n").lower()
    while day not in ( 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
         print ("please try again!")
         day= input("Please pick a day(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)\n please write the day name exactly as it is written \n").lower()
    
    print('-'*40)
    return city, month, day
         
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_name'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\nMost Common Month is ', popular_month)

    # display the most common day of week
    popular_day = df['day_name'].mode()[0]
    print('\nMost Common day is ', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Common start Hour is ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station = df['Start Station'].mode()[0]
    print('\nMost Common start station is ', Start_Station)
    # display most commonly used end station
    End_Station = df['End Station'].mode()[0]
    print('\nMost Common end station is ', End_Station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df ['End Station'] 
    Trip = df['Trip'].mode()[0]
    print('\nMost common trip is ', Trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Total_Time = df['Trip Duration'].sum()
    print('Total travel time in seconds is', Total_Time)
    print('Total travel time in hours is', Total_Time/60/60)
    print('Total travel time in days is', Total_Time/60/60/24)
    # display mean travel time
    Mean_Time = df['Trip Duration'].mean()
    print('Mean travel time in seconds is', Mean_Time)
    print('Mean travel time in minutes is', Mean_Time/60)
    Standard_Deviation = df['Trip Duration'].std()
    print('The standard deviation in seconds is', Standard_Deviation)
    print('The standard deviation in minutes is', Standard_Deviation/60)
    Median_Time = df['Trip Duration'].median()
    print('Median travel time in seconds is', Median_Time)
    print('Median travel time in minutes is', Median_Time/60)
    Min_Time = df['Trip Duration'].min()
    print('The shortest travel time in seconds is', Min_Time)
    Max_Time = df['Trip Duration'].max()
    print('The longest travel time in seconds is', Max_Time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users = df['User Type'].value_counts()
    print('\nUser Types are \n', users)
    # Display counts of gender
    try:
       print('\nGender Types are\n', df['Gender'].value_counts())
    except KeyError:
       print ("\nFor Gender Types in this city there are No Available data!")
    # Display earliest, most recent, and most common year of birth
    try:
      print('\nEarliest Year of birth is', df['Birth Year'].min())
    except KeyError:
      print("\nFor Earliest Year of birth in this city there are No Available data!")
    try:
      print('\nMost Recent Year of birth is', df['Birth Year'].max())
    except KeyError:
      print("\nFor Most Recent Year of birth in this city there are No Available data!")
    try:
      print('\nMost common Year of birth is', df['Birth Year'].mode()[0])
    except KeyError:
      print("\nFor Most common Year of birth in this city there are No Available data!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """Displays raw data for user in sets of 5 rows."""
    #Ask the user whether they would like to display 5 rows of data.
    index = 0
    user_decision = input("\n Would you like to display 5 rows of data?\n please answer with yes or no.\n").lower()
    if user_decision.lower() != 'yes':
         print("This is the end of US bike share data journey!")
    else:
            while index + 5 < df.shape[0]:
                print(df.iloc[index:index+5])
                index+=5
    #Ask the user whether they would like to display 5 more rows of data.
                user_decision = input("\n Would you like to display 5 more rows of data?\n please answer with yes or no.\n").lower()
                if user_decision.lower() != 'yes':
                    print("This is the end of US bike share data journey!")
                    break
                else:
                    print(df.iloc[index:index+5])
                    
                    
              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
           print("Thank you, your journey is completed!")
           break
            
if __name__ == "__main__":
    main()
    