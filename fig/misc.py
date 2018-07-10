import pandas as pd
import glob
import seaborn as sns
from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np

# LOAD MEAN GENOTYPE, PHENOTYPE, POPULATION DATA
# and filter to most recent update in each dataframe

dfp = pd.concat([pd.read_csv(f) for f in glob.glob("Phenotypes_*.csv")], ignore_index=True)

fil_dfp = dfp[dfp['update'] == dfp['update'].max()].reset_index(drop=True)

dfg = pd.concat([pd.read_csv(f) for f in glob.glob("../collected/Genotypes_*.csv")], ignore_index=True)

fil_dfg = dfg[dfg['update'] == dfg['update'].max()].reset_index(drop=True)

dfo = pd.concat([pd.read_csv(f) for f in glob.glob("Population_*.csv")], ignore_index=True)

fil_dfo = dfo[dfo['update'] == dfo['update'].max()].reset_index(drop=True)

# stitch together dataframes using 'seed'

dfc = fil_dfp.join(
        fil_dfg.set_index('seed').drop(columns=['update']), on='seed'
        ).reset_index(drop=True
        ).join(fil_dfo.set_index('seed').drop(columns=['update']), on='seed'
        ).reset_index(drop=True)

print(np.sort(dfc['mean_avoid_over1']))
