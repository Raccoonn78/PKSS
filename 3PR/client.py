import socket 
import pickle


  


class MainClient(socket.socket):

  def __init__(self):
    super().__init__()
    self.start_client()
      

  def start_client(self):

    try:
      self.message = ''
      self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.s.connect(('localhost', 3030))# Подключаемся к нашему серверу.
      while self.message.lower().strip() != 'stopp':
          
          self.true=int(input('введите номер задания (1-5) либо 0-> '))



          if self.true==0:
            self.message = [0]
            self.connectServer()
            print("Client stop")
            break

          if self.true==1: # первое хадание №16
              self.message = self.one16()
              self.connectServer()  # вызов функции для отправки сообщения 
             
          if self.true==2: #второе задание №19
            self.message = self.one19()
            self.connectServer()

          if self.true==3: # треть задание №22
            self.message = self.one22()
            self.connectServer()

          if self.true==4: # четвертое задание № 25
            self.message = self.one25()
            self.connectServer()

          if self.true==5: #пятое задание № 28
            self.message = self.one28()
            self.connectServer()

          



    except KeyboardInterrupt:
      self.s.close()
      print('shutdown this shit...')




  def connectServer(self):# функция для отправки запросов , в нем мы передаем наше ссобщение с данными серверу  , это для упрощения кода 
    self.message=pickle.dumps(self.message)
    print('')
    print("Отправил...")

    self.s.sendall(self.message)  # send message
    print("Ждем...")
    print('')
    
    self.data = self.s.recv(1024).decode('utf-8')  # receive response
    print('Answer :  ' + self.data)  # show in terminal
    print('')
    print('')
    print('')


  def one16(self):
    list=[1]
    print('Вывести на печать отpицательные значения функции')
    
    print(list)
    return list


  def one19(self):
    list=[2]
    print('Hайти пеpвый отpицательный член последовательности')

    

    print(list)
    return list

  def one22(self):
    list=[3]
    
    print('Получить наибольшее число вида 3k, меньшее N')

    num=int(input('введите число N -> '))
    list.append(num)    

    return list

  def one25(self):
    list=[4]
    print(' y=(4x-3x+tg(x))/А')
    
    num=int(input('введите число A  -> '))
    list.append(num)    
    return list
    pass

  def one28(self):
    list=[5]
    print('вычисления функции z=sin(x)-5cos(x-2)')
    
    

    return list
    pass



if __name__ == '__main__':
	ex = MainClient()
