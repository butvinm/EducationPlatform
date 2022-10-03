from dataclasses import dataclass


@dataclass(init=False)
class ImageBlock:
    url: str
    size: int

    def __init__(self, entity: str) -> None:
        """Parse size and url from entity string

        Args:
            entity (str): raw string block entity from parsed text 
        """
        
        splitted = entity.split(', ')
        if len(splitted) == 1:
            self.size = None
            self.url = splitted[0]
        elif len(splitted) == 2:
            self.size = int(splitted[0])
            self.url = splitted[1]
        else:
            raise ValueError