"""
Download a rendered png from a panel in grafana into a subdirectory.
"""

subdir_name = 'grafana_graphs'

# Wattage
data = {
    'url': 'http://127.0.0.1:3000/render/dashboard-solo/db/zonnepanelen?orgId=1&panelId=1&theme=light&width=500&height=250',
    'subdir': subdir_name,
    'filename': 'zonnepanelen_1_1.png',
    'overwrite': True
}

# call  downloader component to save the file
hass.services.call('downloader', 'download_file', data)

# Opwekking Dag
data = {
    'url': 'http://127.0.0.1:3000/render/dashboard-solo/db/opwekking-dag-kwh?orgId=1&panelId=1&theme=light&width=500&height=250',
    'subdir': subdir_name,
    'filename': 'zonnepanelen_1_2.png',
    'overwrite': True
}

# call  downloader component to save the file
hass.services.call('downloader', 'download_file', data)

# Opwekking Week
data = {
    'url': 'http://127.0.0.1:3000/render/dashboard-solo/db/opwekking-week-kwh?orgId=1&panelId=1&theme=light&width=500&height=250',
    'subdir': subdir_name,
    'filename': 'zonnepanelen_1_3.png',
    'overwrite': True
}

# call  downloader component to save the file
hass.services.call('downloader', 'download_file', data)

# Opwekking Maand
data = {
    'url': 'http://127.0.0.1:3000/render/dashboard-solo/db/opwekking-maand-kwh?orgId=1&panelId=1&theme=light&width=500&height=250',
    'subdir': subdir_name,
    'filename': 'zonnepanelen_1_4.png',
    'overwrite': True
}

# call  downloader component to save the file
hass.services.call('downloader', 'download_file', data)
