
from pycardano import PaymentSigningKey, StakeSigningKey, PaymentVerificationKey, StakeVerificationKey, Address, Network

from blockfrost import BlockFrostApi, ApiError, ApiUrls


#payment_signing_key = PaymentSigningKey.generate()
#payment_verification_key = PaymentVerificationKey.from_signing_key(payment_signing_key)
#payment_signing_key.save("payment.skey")
#payment_verification_key.save("payment.vkey")




payment_verification_key = PaymentVerificationKey.load("payment1.vkey")
enterprise_address = Address(payment_part=payment_verification_key.hash(),
                             network=Network.TESTNET)
print(enterprise_address)

