import cse163_utils  # noqa: F401
# This is a hacky workaround to an unfortunate bug on macs that causes an
# issue with seaborn, the graphing library we want you to use on this
# assignment.  You can just ignore the above line or delete it if you are
# not using a mac!
# Add your imports and code here!
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Homework 3: Part 0
# Problem 0) Parse data


def parse(file_name):
    return pd.read_csv(file_name, na_values=['---'])

# Problem 1) completions_between_years


def completions_between_years(dt, year_1, year_2, sex):
    """
    Return a dataframe inlcluding the data which have data between
    the given years and with the given sex.

    Take a dataframe, earlier year, later year, and one type of sex.
    """
    btw_years = (dt['Year'] >= year_1) & (dt['Year'] < year_2)
    given_sex = dt['Sex'] == sex
    return dt[btw_years & given_sex]


# Problem 2) compare_bachelors_1980


def compare_bachelors_1980(dt):
    """
    Return a tuple inlcluding the percentanges of men and women
    with a minimum education of bachelor's degrees in 1980.

    Take a dataframe
    """
    year = dt['Year'] == 1980
    m_bachelors = (dt['Sex'] == 'M') & (dt['Min degree'] == "bachelor's")
    w_bachelors = (dt['Sex'] == 'F') & (dt['Min degree'] == "bachelor's")
    return (dt[year & m_bachelors]['Total'].iat[0]),\
        (dt[year & w_bachelors]['Total'].iat[0])


# Problem 3) top_2_2000s


def top_2_2000s(dt):
    """
    Return a list of tuples inlcluding the minimum educations
    and mean percentages of the first and second top level from 2000 to 2010.

    Take a dataframe
    """
    btw_years = (dt['Year'] >= 2000) & (dt['Year'] <= 2010)
    given_sex = dt['Sex'] == 'A'
    sorted_data = dt[btw_years & given_sex].groupby('Min degree').\
        mean().sort_values('Total', ascending=False).head(2)
    return [(sorted_data.index[0], sorted_data.Total[0]),
            (sorted_data.index[1], sorted_data.Total[1])]


# Problem 4) percent_change_bachelors_2000s


def percent_change_bachelors_2000s(dt, sex='A'):
    """
    Return percent differences as a float between the
    total percents of bachelor's degrees as the minimal
    educational degrees in 2000 and in 2010.

    Take a dataframe and a type of sex.
    If a type of sex is not included as a parameter,
    it will be considered as all individuals.
    """
    year_1 = dt['Year'] == 2000
    year_2 = dt['Year'] == 2010
    M_degree = dt['Min degree'] == "bachelor's"

    if sex == 'A':
        percent_change \
            = dt[M_degree & year_2 & (dt['Sex'] == 'A')]['Total'].item()\
            - dt[M_degree & year_1 & (dt['Sex'] == 'A')]['Total'].item()
    elif sex == 'M':
        percent_change \
            = dt[M_degree & year_2 & (dt['Sex'] == 'M')]['Total'].item()\
            - dt[M_degree & year_1 & (dt['Sex'] == 'M')]['Total'].item()
    elif sex == 'F':
        percent_change \
            = dt[M_degree & year_2 & (dt['Sex'] == 'F')]['Total'].item()\
            - dt[M_degree & year_1 & (dt['Sex'] == 'F')]['Total'].item()
    return percent_change


# Homework 3: Part 1
# Problem 0) Line Chart


def line_plot_bachelors(dt):
    """
    Take a dataframe and produce a line graph on the total percentages
    of all people with a minimum education of
    bachelor's degrees over years.
    """
    min_degree = (dt['Min degree'] == "bachelor's")
    given_sex = dt['Sex'] == 'A'
    filtered_data = dt[min_degree & given_sex]
    sns.relplot(x='Year', y='Total', data=filtered_data, kind='line')
    plt.savefig('line_plot_bachelors.png')


# Problem 1) bar Chart


def bar_chart_high_school(dt):
    """
    Take a dataframe and produce a bar graph on the total percentages of
    the types of sex with a minimum education of high school degrees in 2009.
    """
    year = dt['Year'] == 2009
    min_degree = dt['Min degree'] == "high school"
    filtered_data = dt[min_degree & year]
    sns.catplot(x='Sex', y='Total', data=filtered_data, kind='bar')
    plt.savefig('bar_chart_high_school.png')


# Problem 2) Custom Plot


def plot_hispanic_min_degree(dt):
    """
    Take a dataframe and produce line graphs on the total percentages
    of Hispanic individuals with a minimum education of high school
    and bachelor degrees from 1900 to 2010.
    """
    btw_years = (dt['Year'] >= 1990) & (dt['Year'] <= 2010)
    min_degrees = (dt['Min degree'] == "bachelor's")\
        | (dt['Min degree'] == "high school")
    given_sex = dt['Sex'] == 'A'
    filtered_data = dt[min_degrees & btw_years & given_sex]
    sns.lineplot(x='Year', y='Hispanic', data=filtered_data, hue='Min degree')
    plt.savefig('plot_hispanic_min_degree.png')


# Homework 3: Part 2


def fit_and_predict_degrees(dataframe):
    filtered_data = dataframe[['Year', 'Min degree', 'Sex', 'Total']].dropna()
    X = filtered_data.loc[:, filtered_data.columns != 'Total']
    X = pd.get_dummies(X)
    y = filtered_data['Total']
    (X_train, X_test, y_train, y_test) = \
        train_test_split(X, y, test_size=0.20)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    mse_trained = mean_squared_error(y_train, y_train_pred)
    mse_tested = mean_squared_error(y_test, y_test_pred)
    return ('Train MSE:', mse_trained), ('Test MSE:', mse_tested)


def main():
    data = pd.read_csv('hw3-nces-ed-attainment.csv', na_values=['---'])

    completions_between_years(data, 2007, 2008, 'F')
    compare_bachelors_1980(data)
    top_2_2000s(data)
    percent_change_bachelors_2000s(data)
    line_plot_bachelors(data)
    bar_chart_high_school(data)
    plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == '__main__':
    main()
