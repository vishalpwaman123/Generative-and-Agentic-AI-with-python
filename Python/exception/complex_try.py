def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} chai")
        if flavour == "unknown":
            raise ValueError("We dont know that flavour")
    except ValueError as error:
        print(f"Error : {error}")
    else:
        print(f"Chai is ready {flavour}")
    finally:
        print("-----------------please Next Customer---------------")

serve_chai("Masala")
serve_chai("unknown")