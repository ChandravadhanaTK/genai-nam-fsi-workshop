# router for items end points
from fastapi import APIRouter, HTTPException, status
from models import Items, ItemsRequest

router = APIRouter(prefix="/items",
    tags=['items'],)


@router.post("/{item_id}", response_model=Items)
async def create_item(item_id: int, item_req: Items):
    """Insert an item to items table

    Args:
        item_id (int): the item id
        item_req (Items): the item details

    Raises:
        HTTPException: 404 - not found

    Returns:
        Items: items response
    """
    item = ItemsRequest(**{"item_id":item_id})
    item.get()
    if item.name != "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item already exists")
    if item_req.name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item name is required")
    for k, v in item_req.model_dump().items():
        setattr(item, k, v)
    item.insert()
    return item


@router.get("/{item_id}", response_model=Items)
async def read_item(item_id: int, is_offer: bool = None):
    """get an item from database by item_id and option is_offer

    Args:
        item_id (int): item id
        is_offer (bool, optional): get items in offer. Defaults to None.

    Raises:
        HTTPException: 404 - if item not found

    Returns:
        Items: item details
    """
    item = ItemsRequest(**{"item_id":item_id})
    item.get()
    if item.name == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    if is_offer is None:
        return item
    if item.is_offer == is_offer:
        return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@router.put("/{item_id}", response_model=Items)
async def put_item(item_id: int, item_req: Items):
    """update an existing item by item_id
    NOTE: this will replace the existing item with the new item

    Args:
        item_id (int): item id
        item_req (Items): request body

    Raises:
        HTTPException: 404 - if item not found

    Returns:
        Items: item details
    """
    item = ItemsRequest(**{"item_id":item_id})
    item.get()
    if item.name == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    for k, v in item_req.model_dump().items():
        setattr(item, k, v)
    item.update()
    return item


@router.patch("/{item_id}", response_model=Items)
async def patch_item(item_id: int, item_req: Items):
    """update an existing item by item_id., use this api to make specific changes to the item

    Args:
        item_id (int): item id
        item_req (Items): request body

    Raises:
        HTTPException: 404 - if item not found

    Returns:
        Items: item details
    """
    item = ItemsRequest(**{"item_id":item_id})
    item.get()
    if item.name == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    for k, v in item_req.model_dump(exclude_defaults=True).items():
        setattr(item, k, v)
    item.patch()
    return item


@router.delete("/{item_id}", response_model=Items)
async def delete_item(item_id: int):
    """delete an item by item_id

    Args:
        item_id (int): item id

    Raises:
        HTTPException: 404 - if item not found

    Returns:
        Items: item details
    """
    item = ItemsRequest(**{"item_id":item_id})
    item.get()
    if item.name == "":
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    item.delete()
    return item
