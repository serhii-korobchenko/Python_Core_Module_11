class Session:
    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port
        

    def __enter__(self):   # called when interpretor go in context and return what will be written in ver after 'as'
        print(f"connected to {self.addr}:{self.port}")
        return self

    def __exit__(self, exception_type, exception_value, traceback): # called when interpretor go out from context 
        self.connected = False
        if exception_type is not None:
            print("Some error!")
        else:
            print("No problem")

#                                                            Result:
localhost_session = Session("localhost")#                    connected to localhost:8080

with localhost_session as session:#
    print(session is localhost_session)                    # True
    print(localhost_session.connected)                     # True
#                                                            connected to localhost:8080
print(localhost_session.connected)                         # False