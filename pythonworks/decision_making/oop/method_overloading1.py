class parent:
    vechicles=["passion pro","swift"]
    def properties(self):
        return self.vechicles
class child(parent):
    def properties(self):
        self.veh=super().properties()
        self.veh.append("hunder")
        return self.veh
ch=child()
print(ch.properties())