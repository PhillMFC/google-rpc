
import grpc
import rpcProto_pb2_grpc as pb2_grpc
import rpcProto_pb2 as pb2

class UnaryClient(object):

    def get_operator():
        operators: tuple[str] = ('+','-','/','*')
        input_line: str = input('Escolha uma das operações abaixo:\n-> + Soma\n-> - Subtração\n-> / Divisão\n-> * Multiplicação\n').strip()
        
        while not input_line in operators:
            print('\nOperador inválido.\n\n')
            input_line = UnaryClient.get_operator()
            
        return input_line 

    def get_operands():
        input_line: str = input('Digite 2 números para efetuar a operação:\n').strip()
        operands: list[str] = input_line.strip().split()
        
        while len(operands)>2:
            print('\nMais de 2 números enviados.\n\n')
            operands = UnaryClient.get_operands()
            
        while len(operands)<2:
            print('\nMenos de 2 números enviados.\n\n')
            operands = UnaryClient.get_operands()
            
        try:
            first = float(operands[0])
            second = float(operands[1])          
        except:
            print('\nNúmeros inválidos.\n\n')
            return UnaryClient.get_operands()
            
        return [first, second]  

    def send_message( operands, operator):
        
        with grpc.insecure_channel('ec2-18-223-212-98.us-east-2.compute.amazonaws.com:50051') as channel:
            stub = pb2_grpc.calculatorStub(channel)
            request = pb2.operands(first_operand = operands[0], second_operand = operands[1])
            
            if(operator == '+'):
                return stub.sum(request)
                
            elif(operator == '-'):
                return stub.sub(request)
                
            elif(operator == '*'):
                return stub.mul(request)
                
            elif(operator == '/'):
                return stub.div(request)
               
if __name__ == '__main__':
    operator = UnaryClient.get_operator()
    operands = UnaryClient.get_operands()
    result = UnaryClient.send_message(operands, operator)
    print(f'{result}')