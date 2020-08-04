from sys import maxsize


class MantisProject:
    def __init__(self, projectname=None, description=None, id=None):
        self.projectname = projectname
        self.description = description
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.projectname, self.description)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.projectname == other.projectname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize