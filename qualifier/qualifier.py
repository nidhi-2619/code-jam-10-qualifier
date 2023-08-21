from PIL import Image

def valid_input(image_size: tuple[int, int], tile_size: tuple[int, int], ordering: list[int]) -> bool:
    """
    Return True if the given input allows the rearrangement of the image, False otherwise.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once.
    """
    if image_size[0]%tile_size[0]!=0 or image_size[1]%tile_size[1]!=0:
        return False 
    if not len(set(ordering))==len(ordering):
        return False
    no_of_tiles = (image_size[0]*image_size[1])/(tile_size[0]*tile_size[1])
    # total area of all tiles 
    tot_area = (no_of_tiles*(tile_size[0]*tile_size[1]))
    image_area = image_size[0]*image_size[1]
    # check if there isn't a blank space 
    if tot_area!=image_area:
        return False
    if not no_of_tiles.is_integer():
        return False 
    if len(ordering)!=no_of_tiles:
        return False
    return True
        


def rearrange_tiles(image_path: str, tile_size: tuple[int, int], ordering: list[int], out_path: str) -> None:
    """
    Rearrange the image.

    The image is given in `image_path`. Split it into tiles of size `tile_size`, and rearrange them by `ordering`.
    The new image needs to be saved under `out_path`.

    The tile size must divide each image dimension without remainders, and `ordering` must use each input tile exactly
    once. If these conditions do not hold, raise a ValueError with the message:
    "The tile size or ordering are not valid for the given image".
    """
    
    image = Image.open(image_path)
    if not valid_input(image.size,tile_size,ordering):
            raise ValueError("The tile size or ordering are not valid for the given image")
    
    newImg = Image.new(image.mode, image.size)
    cols = image.size[0]//tile_size[0]
    rows = image.size[1]//tile_size[1]
    for index,tile_index in enumerate(ordering):
        x = (index%cols)*tile_size[0]
        y = (index//cols)*tile_size[1]
        
        tx_pos = (tile_index%cols)*tile_size[0]
        ty_pos = (tile_index//cols)*tile_size[1]
        
        tile = image.crop((tx_pos, ty_pos, tx_pos + tile_size[0], ty_pos + tile_size[1]))
        newImg.paste(tile, (x, y))

                   
             
    newImg.save(out_path)
    
    