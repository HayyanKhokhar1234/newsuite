class DH_Endpoint(object):
    def __init__(self,public_key1,public_key2,private_key):
        self.public_key1=public_key1
        self.public_key2=public_key2
        self.private_key=private_key

        self.full_key=None

        def generate_partial_key(self):
            partial_key=self.public_key1**self.private_key
            return partial_key

