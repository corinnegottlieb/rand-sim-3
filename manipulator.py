class Manipulator:
    def __init__(self, data):
        self.data = data

    def filter_by(self, value, key = None):
        if key == None:
            return list(
                self.data["obj"][value]
            )
        else:
            return list(
                filter(lambda d: d[key] == value, self.data["arr"])
        )
    
    def filter_by(self, date):
        filtered = []
        for data in self.data["arr"]:
            if data["date"][0] == date:
            filtered.append()