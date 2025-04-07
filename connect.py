
from graph import graph, packages
from algo import dijkstra

source = 'A'

shortest_paths = dijkstra(graph, source)

sorted_packages = sorted(
    packages.items(),
    key=lambda item: shortest_paths[item[1]]  
)

print("🚚 Delivery Plan (Sorted by Priority):")
for pkg, location in sorted_packages:
    distance = shortest_paths[location]
    print(f"📦 {pkg} → {location} (Distance: {distance})")
