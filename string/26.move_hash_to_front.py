s = "Move#Hash#to#Front"

hashes = s.count('#')

result = '#' * hashes + s.replace('#','')

print(result)