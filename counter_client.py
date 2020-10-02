from __future__ import print_function
import logging

import grpc

import counter_pb2
import counter_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = counter_pb2_grpc.CounterStub(channel)
        response = stub.Increment(counter_pb2.IncrementRequest(value=100))
    print("Added 100 to counter: " + str(response.value))


if __name__ == '__main__':
    logging.basicConfig()
    run()
