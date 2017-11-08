from dao import create_booking

def new_booking(booking):
    booking1 = create_booking(booking['customer_id'], booking['screening_id'])
    return booking1, 201