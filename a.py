def __new__(self, socket_buffer=None):
  return self.from_buffer_copy(socket_buffer)

def __init__(self, socket_buffer=None):
  # map protocol constants to their names
  self.protocol_map = {1:"ICMP", 6:"TCP", 17:"UDP"}
  v
  # human readable IP addresses
  self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
  self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))
  # human readable protocol
  try:
  self.protocol = self.protocol_map[self.protocol_num]
  except:
  self.protocol = str(self.protocol_num)
