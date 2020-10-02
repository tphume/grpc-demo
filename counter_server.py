from concurrent import futures
import logging

import grpc
import counter_pb2
import counter_pb2_grpc


class Counter(counter_pb2_grpc.CounterServicer):
    # Our global counter
    counter = 0

    def Increment(self, request, context):
        self.counter += request.value
        return counter_pb2.IncrementReply(value=self.counter)

    def GetCounter(self, request, context):
        return counter_pb2.GetCounterReply(value=self.counter)


def serve():
    # I have made this work only on one thread because i have not added locking for counter
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    counter_pb2_grpc.add_CounterServicer_to_server(Counter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
