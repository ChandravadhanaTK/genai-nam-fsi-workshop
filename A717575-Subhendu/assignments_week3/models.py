from pydantic import BaseModel
from typing import Optional
from database import insert_rows, get_row_by_id, update_row, delete_row, patch_row


class Items(BaseModel):
    name: Optional[str] = ""
    price: Optional[float] = 0.0
    is_offer: Optional[bool] = False


class ItemsRequest(Items):
    
    item_id: int
    last_update: Optional[str] = ""
    
    def insert(self):
        insert_rows("items", "item_id", [self.model_dump()]) 
    
    def delete(self):
        delete_row("items", "item_id", self.item_id)
    
    def update(self):
        update_row("items", "item_id", self.item_id, self.model_dump())
    
    def patch(self):
        patch_row("items", "item_id", self.item_id, self.model_dump(exclude_unset=True))

    def get(self):
        data = get_row_by_id("items", "item_id", self.item_id)
        if data:
            for field_name, value in data.items():
                if hasattr(self, field_name):  # Check if field exists in the model
                    setattr(self, field_name, value)
