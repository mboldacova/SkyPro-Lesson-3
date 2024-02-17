from address import Address
from mailing import Mailing

letter = Mailing(Address("123", "Green St", "12", "San Diego", "CA", "92108"), 
                 Address("57",  "1st St", "1", "New York", "NY", "11000"), 
                 "$25.78", "1234567890")

print(f"Letter with the tracking number {letter.track} mailed from address: {letter.from_address} to: {letter.to_address}. Cost of mailing: {letter.cost}")