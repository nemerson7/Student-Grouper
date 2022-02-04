import pandas as pd
from src.get_data import get_data
from src.process_data import process_data, output_to_tex
from src.utilities import texdoc


if __name__ == "__main__":
    df = get_data()
    grouplist = process_data(df)
    output_to_tex(grouplist = grouplist, starterdoc = texdoc)
    
