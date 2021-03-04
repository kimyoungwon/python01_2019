# uwnetid: 1724787

import geopandas
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(shp_file, csv_file):
    '''
    Combines two dataset into one dataframe.
    Merges 'CTIDFP00' columns in the SHP file
    with 'CensusTract' in the CSV file.
    If the SHP file does not have corresponding for food access,
    the vaules will be missing value (NaN).

    Takes SHP and CSV files as arguments.
    '''
    shp_dt = geopandas.read_file(shp_file)
    csv_dt = pd.read_csv(csv_file)
    return shp_dt.merge(csv_dt, left_on='CTIDFP00',
                        right_on='CensusTract', how='left')


def percentage_food_data(df):
    '''
    Returns the percentage of valid census tracts in Washington
    among all census tracts.
    The value of the percentage is a float between 0 and 100.

    Takes a merged dataframe as an argument.
    '''
    return (len(df.dropna())/len(df))*100


def plot_map(df):
    '''
    Plots a default map of Washington which does not inlcude any customization.
    Saves the map in a file called 'washington_population_map.png'.

    Takes a merged dataframe as an argument.
    '''
    df.plot()
    plt.title('Map of Washington')
    plt.savefig('washington_map.png')


def plot_population_map(df):
    '''
    Plots a map of Washington colored by the population in a certain region.
    Saves the map in a file called 'washington_population_map.png'.

    Takes a merged dataframe as an argument.
    '''
    df.dropna().plot(column='POP2010', figsize=(15, 7), legend=True)
    plt.title('Population in Census Track')
    plt.savefig('washington_population_map.png')


def plot_population_county_map(df):
    '''
    Plots a map of Washington colored by the population in each county.
    Saves the map in a file called 'washington_county_population_map.png'.

    Takes a merged dataframe as an argument.
    '''
    population_by_county = df.dropna().dissolve(by='County', aggfunc='sum')
    population_by_county.plot(column='POP2010', figsize=(15, 7), legend=True)
    plt.title('Population in Each County')
    plt.savefig('washington_county_population_map.png')


def plot_food_access_by_county(df):
    '''
    Plots four maps of Washington colored by the ratio of population
    in each county that relates to low access from a food source or low income.
    Four maps are about 1) the ratio of people with "low access"
    at the half mile level among the population in the 2010 census,
    2) the ratio of people with "low access" and "low income"
    at the half mile level among the population in the 2010 census,
    3) the ratio of people with "low access"
    at the 10 mile level among the population in the 2010 census,
    4) the ratio of people with "low access" and "low income"
    at the 10 mile level among the population in the 2010 census
    Saves the maps in a file called 'washington_county_food_access.png'.

    Takes a merged dataframe as an argument.
    '''
    wa_population = df[['County', 'geometry', 'POP2010', 'lapophalf',
                        'lapop10', 'lalowihalf', 'lalowi10']]
    population_by_county = wa_population.dropna().dissolve(by='County',
                                                           aggfunc='sum')
    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, figsize=(20, 10), ncols=2)
    for col_name in list(population_by_county.columns.values)[2:7]:
        population_by_county[col_name+'_share'] =\
            population_by_county[col_name]/population_by_county.POP2010
    ax1.set_title('Low Access: Half')
    population_by_county.plot(ax=ax1, column='lapophalf_share',
                              legend=True, vmin=0, vmax=1)
    ax2.set_title('Low Access + Low Income: Half')
    population_by_county.plot(ax=ax2, column='lalowihalf_share',
                              legend=True, vmin=0, vmax=1)
    ax3.set_title('Low Access: 10')
    population_by_county.plot(ax=ax3, column='lapop10_share',
                              legend=True, vmin=0, vmax=1)
    ax4.set_title('Low Access + Low Income: 10')
    population_by_county.plot(ax=ax4, column='lalowi10_share',
                              legend=True, vmin=0, vmax=1)
    fig.savefig('washington_county_food_access.png')


def plot_low_access_tracts(df):
    '''
    Plots a map of Washington colored by the population having "low access."
    The population includes
    1) at 500 people or at least 33% of the people in the census tract
    at the half mile level from a food source (Urban) and
    2) at 500 people or at least 33% of the people in the census tract
    at the 10 mile level from a food source (Ruran).
    Saves the map in a file called 'plot_low_access_tracts'.

    Takes a merged dataframe as an argument.
    '''
    low_access_pop = df[['Urban', 'Rural', 'geometry', 'POP2010', 'lapophalf',
                        'lapop10']].dropna()
    urban_low_access = (low_access_pop['Urban'] == 1) &\
        ((low_access_pop['lapophalf'] >= 500) |
         ((low_access_pop['lapophalf']/low_access_pop['POP2010']) > 0.33))
    rural_low_access = (low_access_pop['Rural'] == 1) &\
        ((low_access_pop['lapop10'] >= 500) |
         ((low_access_pop['lapop10']/low_access_pop['POP2010']) > 0.33))
    low_access = low_access_pop[urban_low_access | rural_low_access]
    fig, ax = plt.subplots(1, figsize=(10, 10))
    ax.set_title('Low Access from a Food Resource')
    df.plot(ax=ax, color='#EEEEEE', vmin=0, vmax=1)
    low_access_pop.plot(ax=ax, color='#AAAAAA', vmin=0, vmax=1)
    low_access.plot(ax=ax, vmin=0, vmax=1)
    fig.savefig('washington_low_access.png')


def main():
    wa = load_in_data('tl_2010_53_tract00/tl_2010_53_tract00.shp',
                      'food_access.csv')
    percentage_food_data(wa)
    plot_map(wa)
    plot_population_map(wa)
    plot_population_county_map(wa)
    plot_food_access_by_county(wa)
    plot_low_access_tracts(wa)


if __name__ == '__main__':
    main()
