import os

def rename_folders(base_path):
    items = os.listdir(base_path)

    for item in items:
        item_path = os.path.join(base_path, item)

    
        if os.path.isdir(item_path) and "PBS" in item: #se pone entre comillas el texto a buscar
            new_name = item.replace("PBS", "DEVOLUCION") #se pone entre comillas el texto a buscar y a reemplazar
            new_path = os.path.join(base_path, new_name)
            
            os.rename(item_path, new_path)
            print(f'Renamed: {item} -> {new_name}')

if __name__ == "__main__":
    base_path = os.path.join(os.getcwd(), "INFORMACION")
    
    if os.path.exists(base_path) and os.path.isdir(base_path):
        rename_folders(base_path)
    else:
        print(f'EL DIRECTORIO NO INFORMACION NO EXISTE {base_path}')