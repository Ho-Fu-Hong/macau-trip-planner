import os

STOPS = ["Venetian Macao", "Londoner Macao", "Parisian Macao"]
print("syncing", len(STOPS), "stops to", os.environ.get("NAS_URL"))
