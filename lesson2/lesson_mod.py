import ephem

mars = ephem.Moon('2000/01/01')
const = ephem.constellation(mars)

print(const)