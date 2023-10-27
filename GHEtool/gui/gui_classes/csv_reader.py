"""
This files contains the code related to interpreting the csv files within the GHEtool GUI.
"""

from GHEtool import FOLDER

import pandas as pd


def find_dec_and_sep(loc: str) -> tuple:
    """
    This function finds the decimal point and separator of the csv file.
    Options for the decimal point are: '.' or ','.
    Options for the separator are: ' ', '   ', ',', ';'.

    Parameters
    ----------
    loc : str
        Location of the file which should be loaded

    Returns
    -------
    tuple : str, str, tuple
        decimal point, separator, column names

    Raises
    ------
    ValueError
        When no solution can be found
    FileNotFoundError
        When the file does not exist
    """

    list_of_sep = [',', ';', ' ', '   ']
    list_of_dec = ['.', ',']

    df = None

    for sep in list_of_sep:
        for dec in list_of_dec:
            if sep == dec:
                continue
            try:
                df = pd.read_csv(loc, sep=sep, decimal=dec)
                float(df.iloc[0, 0])
                return dec, sep, tuple(df.columns)
            except FileNotFoundError:
                raise FileNotFoundError('The file for the hourly load cannot be found.')
            except ValueError:
                continue

    if df is None:
        # no solution has been found
        raise ValueError('The csv-file is not readable.')


if __name__ == '__main__':
    print(find_dec_and_sep(f'{FOLDER}/Examples/hourly_profile.csv'))
    # what if there is no dec sep?