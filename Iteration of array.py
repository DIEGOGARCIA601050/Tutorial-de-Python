planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
i=-1
noi=len(planets)
while noi>0:
    print(planets[noi-1])
    print(planets[noi:], ':', noi)
    noi=noi-1
print(planets[0:], ': ')
while abs(i) <= len(planets):
    print(planets[i])
    print(planets[0:i], ':', i)
    i=i-1
print(planets[0:0], ':', 0)
