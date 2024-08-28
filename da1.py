import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = {
    "Tehran": {"lat": 35.6892, "lon": 51.3890, "population": 8694000},
    "Mashhad": {"lat": 36.2605, "lon": 59.6168, "population": 3074000},
    "Isfahan": {"lat": 32.6539, "lon": 51.6660, "population": 1960000},
    "Karaj": {"lat": 35.8400, "lon": 50.9391, "population": 1937000},
    "Shiraz": {"lat": 29.5918, "lon": 52.5837, "population": 1566000},
    "Tabriz": {"lat": 38.0831, "lon": 46.2919, "population": 1558000},
    "Qom": {"lat": 34.6399, "lon": 50.8759, "population": 1283000},
    "Ahvaz": {"lat": 31.3203, "lon": 48.6692, "population": 1185000},
    "Kermanshah": {"lat": 34.3142, "lon": 47.0650, "population": 946000},
    "Urmia": {"lat": 37.5553, "lon": 45.0728, "population": 736224}
}
plt.figure(figsize=(8, 6))

m = Basemap(lat_0=32, lon_0=54, width=2E6, height=2E6, llcrnrlon=44, llcrnrlat=25, urcrnrlon=63, urcrnrlat=40,
            resolution='i', projection='lcc')
m.drawcoastlines()
m.shadedrelief()
m.drawcountries()

for city, data in cities.items():
    x, y = m(data["lon"], data["lat"])
    m.plot(x, y, "ok", markersize=max(data["population"] / 1000000, 5))
    plt.text(x, y, city, fontsize=10, ha='right', color="white")
plt.title("Major Cities of Iran with Population")
plt.show()
