from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header"""
    result: list[str] = []
    # step through table
    for row in table:
        # Save every value under the key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str, list[str]]:
    """Reformats data so that it's a dictionary with column headers as keys"""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry will all column values
        result[key] = column_values(table, key)
    return result


def tabulate(data: dict[str,list[str]]) -> dict[str, list[str]]:
    """Reformats data as a string that can be used as input to tabulate"""
    universities: dict[str, list[str]] = {}
    # loop through keys of university
    for key in universities:
        # for each key, make a dictionary entry will all column values
        universities.append(key)
    return universities



def head(columns: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """
    Extracts the first 'rows' rows from the given table and returns the data as a dictionary
    with column names as keys and a list of corresponding values as values.
    """
    result: dict[str, list[str]] = {}
    for column in columns:
        values: list[str] = []
        i: int = 0
        if len(columns[column]) <= number_rows:
            result[column] = columns[column]
        else:
            while i < number_rows:
                values.append(columns[column][i])
                i += 1
            result[column] = values
    return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    # loop through column in columns
    for column in columns:
        result[column] = table[column]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenates two column-based tables into a new table
    
    Args:
    - a: A column-based table of data that will not be mutated
    - b: A column-based table of data that will not be mutated
    
    Returns:
    A new column-based table that contains all columns from table1 and table2
    """
    result: dict[str, list[str]] = {}
    
    for col in a:
        result[col] = a[col]
    
    for col in b:
        if col in result:
            result[col] += b[col]
        else:
            result[col] = b[col]
    
    return result


def count(items: list[str]) -> dict[str, int]:
    """Given a list of items, produce a dictionary of counts for each unique item
    
    Args:
    - items: A list of strings to count the frequencies of
    
    Returns:
    A dictionary of the counts of each of the items in the input list
    """
    result: dict[str, int] = {}
    
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    
    return result

