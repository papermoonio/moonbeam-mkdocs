class NavLink:
    def __init__(self, url: str, *, title: str):
        self.url = url
        self.title = title

    def to_mkdocs_config(self):
        return {self.title: self.url}
