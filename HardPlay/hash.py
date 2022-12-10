def hash_object(temp_str):
    from hashlib import sha256

    hashed_temp_str = sha256(temp_str.encode('utf-8')).hexdigest()

    return hashed_temp_str
