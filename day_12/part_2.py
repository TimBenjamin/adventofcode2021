
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

def visitCheckOK(dest, route):
    if dest.lower() != dest:
        return True 
    visited = set()
    seen = ""
    for r in route:
        if r.lower() == r:
            if r in visited:
                seen = r
            visited.add(r)
    if dest not in visited:
        return True
    if dest in visited and seen == "":
        return True
    return False

def updateRoutes(routes):
    newRoutes = []
    for route in routes:
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
                    elif visitCheckOK(dest, route):
                        newRoute = route.copy()
                        newRoute.append(dest)
                        newRoutes.append(newRoute)
                    else:
                        pass
                    
    return newRoutes

while True:
    newRoutes = updateRoutes(routes)
    if len(newRoutes) == len(routes):
        break
    routes = newRoutes
    
print("num routes:", len(routes))
