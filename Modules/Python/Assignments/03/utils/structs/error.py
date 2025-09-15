




from dataclasses import dataclass


@dataclass
class Error:
    id:int=None
    name:str=None
    details:str=None



    # def __str__(self):
    #     return "Error({})".format(
    #         ', '.join(
    #             [
    #                 f"{f'id={self.id}' if id != None else ''}",
    #                 f"{f'name={self.name}' if self.name != None else ''}",
    #                 f"{f'details={self.details}' if self.details != None else ''}"
    #             ]
                
    #         )
    #     )
    

    def test(self):
        [].sort()