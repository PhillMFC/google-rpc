import grpc
from concurrent import futures
import time
import rpcProto_pb2_grpc as pb2_grpc
import rpcProto_pb2 as pb2


class UnaryService(pb2_grpc.calculatorServicer):

    def __init__(self, *args, **kwargs):
        pass

    def sum(self, request, context):

        # get the string from the incoming request
        operands = [request.first_operand, request.second_operand]
        print('operadores: ', operands)
        result = eval(f'{operands[0]} + {operands[1]}')
        print('resultado: ', result)
        
        return pb2.result(result=result)
    
    def sub(self, request, context):

        # get the string from the incoming request
        operands = [request.first_operand, request.second_operand]
        print('operadores: ', operands)
        result = eval(f'{operands[0]} - {operands[1]}')
        print('resultado: ', result)
        
        return pb2.result(result=result)

    
    def mul(self, request, context):

        # get the string from the incoming request
        operands = [request.first_operand, request.second_operand]
        print('operadores: ', operands)
        result = eval(f'{operands[0]} * {operands[1]}')
        print('resultado: ', result)
        
        return pb2.result(result=result)
    
    def div(self, request, context):

        # get the string from the incoming request
        operands = [request.first_operand, request.second_operand]
        print('operadores: ', operands)
        result = eval(f'{operands[0]} / {operands[1]}')
        print('resultado: ', result)
        
        return pb2.result(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    pb2_grpc.add_calculatorServicer_to_server(UnaryService(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print("Servidor ovindo em: localhost:50051")
    serve()