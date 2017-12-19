"""
Download a rendered png from a panel in grafana into a subdirectory.
"""

subdir_name = 'grafana_graphs'

# example parameters for downloader component
data = {
    'url': 'http://grafanaviewer:GrafanaC00l@homeassistant.vd-meer.com:3000/render/dashboard-solo/db/zonnepanelen?orgId=1&panelId=2&theme=light&width=500&height=250',
    'subdir': subdir_name,
    'filename': 'zonnepanelen_1_2',
    'overwrite': True
}

# call  downloader component to save the file
hass.services.call('downloader', 'download_file', data)

# example parameters for downloader component
data = {
    'url': 'http://grafanaviewer:GrafanaC00l@homeassistant.vd-meer.com:3000/render/dashboard-solo/db/zonnepanelen?orgId=1&panelId=1&theme=light&width=500&height=250',
    'subdir': subdir_name,
    'filename': 'zonnepanelen_1_1',
    'overwrite': True
}

# call  downloader component to save the file
hass.services.call('downloader', 'download_file', data)
