import gmaps
key = 'yourkey'
gmaps.configure(api_key=key)

marker_locations = [
    (35.040617, 135.729071),
    (35.027294, 135.798195),
    (35.002098, 135.759172),
    (34.986095, 135.758799),
    (35.014323, 135.677888),
    (34.967386, 135.772682),
    (35.026626, 135.762361),
    (35.015056, 135.748239),
    (34.992253, 135.758629),
    (35.016527, 135.782448),
    (35.026429, 135.780822),
]

fig = gmaps.figure()
label = ['금각사', '은각사', '호텔', '교토역', '도월교', '후시미', '교토황궁', '니조성', '히가시 혼간지', '헤이안 신궁', '교토대학']
markers = gmaps.marker_layer(marker_locations,  label=label)
fig.add_layer(markers)
fig
