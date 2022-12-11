def request_signature(user_request_dumps, api_key, time_request, api_secret):
    from hash import hash_object

    hashed_user_request_dumps = hash_object(user_request_dumps)
    request_signature = f'{api_key}/{time_request}/{hashed_user_request_dumps}/{api_secret}'
    hashed_request_signature = hash_object(request_signature)

    return hashed_request_signature
