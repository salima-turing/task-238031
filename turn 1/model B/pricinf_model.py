# Assuming you have the following pricing model function defined in a separate module (e.g., `pricing_model.py`)

def calculate_listing_price(property_size, location):
    # Simple pricing model for demonstration purposes
    base_price = property_size * 100
    location_factor = 1.0

    if location == 'Urban':
        location_factor = 1.5
    elif location == 'Suburban':
        location_factor = 1.2

    return base_price * location_factor
