import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
   
def generate_car_matrix():

    df = pd.read_csv('dataset-1.csv')
    
    matrix = df.pivot(index='id_1', columns='id_2', values='car')
    
  """
  This function uses the pivot method in pandas to rearrange the DataFrame accordingly.
  The pivot function will place 'id_1' values as index, 'id_2' values as columns, and 'car' values as the matrix elements.
  Then, it sets the diagonal values to 0.
  """

    matrix.values[[range(len(matrix))]*2] = 0

    return matrix

# Result
result = generate_car_matrix()
print(result)


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
           
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

# Result
df = pd.read_csv('dataset-1.csv')
result = get_type_count(df)
print(result)

    return dict()
"""
This function uses the cut function from pandas to categorize the 'car' column into 'low', 'medium', and 'high' Then,
it calculates the count of occurrences for each category and returns the result as a dictionary, 
sorted alphabetically based on keys.
"""

def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """

    mean_bus_value = df['bus'].mean()

    
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

   
    bus_indexes.sort()

    return bus_indexes

# Result
df = pd.read_csv('dataset-1.csv')
result = get_bus_indexes(df)
print(result)
    return list()
"""
This function calculates the mean value of the 'bus' column,
then identifies the indices where the 'bus' values are greater than twice the mean.
The resulting indices are sorted in ascending order and returned as a list.
"""
def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
def filter_routes(df):
   
    route_avg_truck = df.groupby('route')['truck'].mean()

    
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

   
    selected_routes.sort()

    return selected_routes

#Result
df = pd.read_csv('dataset-1.csv')
result = filter_routes(df)
print(result)
    return list()
"""
This function uses the groupby method to group the DataFrame by the 'route' column 
and then calculates the mean value of the 'truck' column for each route.
It filters the routes where the average of the 'truck' column is greater than 7,
converts the selected routes to a sorted list, and returns the result.
"""

def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
   def multiply_matrix(input_matrix):
    
    modified_matrix = input_matrix.copy()

    
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    
    modified_matrix = modified_matrix.round(1)

    return modified_matrix

# Result
result_from_question1 = generate_car_matrix()
modified_result = multiply_matrix(result_from_question1)
print(modified_result)

    return matrix
"""
This function first creates a copy of the input matrix to avoid modifying the original DataFrame. 
then applies the specified logic:like values greater than 20 are multiplied by 0.75, and values 20 or less are multiplied by 1.25. 
as a result, the values are rounded to 1 decimal place, and the modified DataFrame is returned.
"""
def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
