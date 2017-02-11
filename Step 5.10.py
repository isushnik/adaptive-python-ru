units = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1.0, 'cm': 0.01, 'mm': 0.001}
value, unit_from, tr, unit_to = input().split()
res = float(value) * units[unit_from] / units[unit_to]
print("%.2e" % res)
