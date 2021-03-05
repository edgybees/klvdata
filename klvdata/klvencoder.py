import io


class KLVEncoder:
    def __init__(self, dst_stream : io.BytesIO):
        self.stream = dst_stream

    def write(self, value : bytes):
        # self.stream.write(key)
        # value_len = len(value)
        #
        # if value_len > 128:
        #     # BER Long form
        #     len_bytes = value_len.to_bytes(4, byteorder='big')
        #     self.stream.write(128 + 4)
        #     self.stream.write(len_bytes)
        # else:
        #     # BER Short form
        #     self.stream.write(value_len.to_bytes(1, byteorder='big'))

        self.stream.write(value)


# JSON  ->  Tags  ->  LocalSet / 101  ->  Bytes
