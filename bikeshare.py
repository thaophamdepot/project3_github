import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#COMMENT FOR BRANCH 'refactoring'
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # FIRST COMMENT
    # get user input for city (chicago, new york city, washington).    
    city = ("Would you like to see data for Chicago, New York, or Washington? ").lower()
    while city.lower() not in ['chicago', 'new york city', 'washington']:
        city = input ("Please choose: Chicago, New York, or Washington? ").lower()

    # get user input for month (all, january, february, ... , june)
    month = "Which month (january, february, march, april, may, june or all) would you like to filter the data? "
    while month.lower() not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Please choose: january, february, march, april, may, june or all) would you like to filter the data? ").lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = "Which day? (all, monday, tuesday, ... sunday): "
    while (day.lower() not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]):
        day = input("Please choose: all, monday, tuesday, ... sunday: ").lower()

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
    #load intended file into data frame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month from Start Time into new column called month
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month if applicable

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("What is the most popular month for traveling?\n", popular_month) 
    print("\nThat tooks %s seconds." % (time.time() - start_time))
    
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day
    popular_day = df['day_of_week'].mode()[0]
    print("What is the most popular day for traveling?\n", popular_day)
    print("\nThat tooks %s seconds." % (time.time() - start_time))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("What is the most popular hour for traveling?\n", popular_hour)
    print("\nThat tooks %s seconds." % (time.time() - start_time))
    
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("What is the most popular start station: ", common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("What is the most popular end station: ", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print("Most frequent combination of start station and end station trip: ", frequent_combination)

    print("\nThat tooks %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel)


    print("\nThat tooks %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types: ", user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
      gender = df['Gender'].value_counts()
      print("Counts of gender: ", gender)
    else:
      print("No gender data.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("\nEarliest year of birth:", df['Birth Year'].min())
        print("\nMost recent year of birth:", df['Birth Year'].max())
        print("\nMost common year of birth:", df['Birth Year'].mode()[0])
    else:
        print("\nNo birth year data.")

    print("\nThat tooks %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data (df):
    """Asking 5 lines of the raw data and more, if they want"""
    raw_data = 0
    while True:
        answer = input("\nWould you like to see the raw data? Enter yes or no.\n").lower()
        if answer not in ['yes', 'no']:
            answer = input("Please enter yes or no.\n").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("\nWould you like to see more? Enter yes or no.\n").lower()
            if again == 'no':
                break
            elif again == 'yes':
                raw_data += 5
                print(df.iloc[raw_data : raw_data + 5])
        elif answer == 'no':
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#SECOND COMMENT
if __name__ == "__main__":
	main()
