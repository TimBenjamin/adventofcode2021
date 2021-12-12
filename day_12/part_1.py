
connections = [] # list of 2-element sets
routes = [] # all the routes

with open("input.txt") as file:
    while line := file.readline().strip():
        connections.append(set(line.split("-")))

# find starting points
for conn in connections:
    if "start" in conn:
        dest = "".join(conn.difference({"start"}))
        routes.append(["start", dest])

def getVisited(route):
    visited = set()
    for r in route:
        if r.lower() == r:
            visited.add(r)
    return visited

def updateRoutes(routes):
    newRoutes = []
    for route in routes:
        visited = getVisited(route)
        source = route[len(route)-1]
        if source == "end":
            newRoutes.append(route)
            continue
        for conn in connections:
            if source in conn:
                dest = "".join(conn.difference({source}))
                if dest == "start":
                    continue
                else:
                    if dest == "end":
                        newRoute = route.copy()
                        newRoute.append(dest)
                        newRoutes.append(newRoute)
                    elif (dest.lower() == dest and dest not in visited) or dest.lower() != dest:
                        newRoute = route.copy()
                        newRoute.append(dest)
                        newRoutes.append(newRoute)
                        if dest.lower() == dest:
                            visited.add(dest)
                    else:
                        pass
                    
    return newRoutes

while True:
    newRoutes = updateRoutes(routes)
    if len(newRoutes) == len(routes):
        break
    routes = newRoutes
    
print("num routes:", len(routes))
