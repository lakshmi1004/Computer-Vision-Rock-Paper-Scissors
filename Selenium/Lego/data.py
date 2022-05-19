from dataclasses import dataclass
from typing import Optional

@dataclass
class Lego_Theme:
    uuid_list: list
    id_list: list
    link_list: Optional[list]
    img_list: Optional[list]

@dataclass
class Lego_Data_info(Data):
    Product_name: list
    Rating: list
    Prices: list
    link: list
    Flag: list
    Pieces:list
    Availability:list
    Item_num:list
    UUID:list