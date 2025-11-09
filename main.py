from api import Project



x = Project(folder = "proj")
y = x.newCollection(name = "main")
z = y.addGameObject(id = "go" , position = dict(x = 1.0))
o = z.addGameObject(id = "go-1")
f = z.addCollectionFactory(id = "factory")
f.id = "hhhhh"
p = o.addCollectionProxy(id = "proxy")
o.addCamera(id = "cam")


print(x.model_dump_json(indent=4))