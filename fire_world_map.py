import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/fire_data_7.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Collect coordinate and brightness data.
    lons, lats, brights = [], [], []
    for row in reader:
        lons.append(row[2])
        lats.append(row[1])
        brights.append(row[3])

# Map the data.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5 * bright for bright in brights],
        'color': brights,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'},
    },
}]

title = 'Observed fires for the last seven days.'
my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
