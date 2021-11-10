
import base64
from .credentials import bs_shortcode,consumer_key,consumer_secrete,lnm_passkey
from .timestamp import format_time


def decode_password():
    pass_to_be_encoded = bs_shortcode + lnm_passkey + format_time() # The password exected is a combination of shortcode, the passkey, and the formated time
    #Encoding the password
    pass_encoded = base64.b64encode(pass_to_be_encoded.encode()) 
    #Decoding the password
    pass_decoded = pass_encoded.decode('utf_8') 
    return pass_decoded
