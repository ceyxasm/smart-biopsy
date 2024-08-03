from tcia_utils import nbia

df = nbia.getSeries(collection = "CPTAC-UCEC", modality =   "RTSTRUCT", format = "df")
df = list( df["SeriesInstanceUID"])
nbia.downloadSeries( df[:10], input_type="list", format="df")
