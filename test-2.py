import os
from tcia_utils import nbia

# Define the output directory (change this to your desired path)
output_dir = '/run/user/1000/gvfs/google-drive:host=iitj.ac.in,user=inside/0AHQz8868jekVUk9PVA/1YqcMDQfacnQj45n8Z32AVSY-yljbGeYI/1UZOpbp785fqfxKiqBFB9UQiC6M-nY5IC'

# Change the current working directory to the output directory
os.chdir(output_dir)

# Retrieve the list of series
df = nbia.getSeries(collection="CPTAC-UCEC", modality="RTSTRUCT", format="df")
series_ids = list(df["SeriesInstanceUID"])

# Download the series
nbia.downloadSeries(series_ids[:1], input_type="list", format="df")

