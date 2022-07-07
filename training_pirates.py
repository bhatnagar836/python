def cannons_ready(gunners):
    print("Shiver me timbers!") if "nay" in gunners.values() else print("Fire!")
    return "Shiver me timbers!" if "nay" in gunners.values() else "Fire!"


cannons_ready({'Mike':'aye', 'Joe':'aye', 'Johnson':'aye', 'Peter':'aye'})