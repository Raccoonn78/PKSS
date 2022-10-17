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
            for i in range(3):

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
    print("Отправил...")

    self.s.sendall(self.message)  # send message
    print("Ждем...")
    
    self.data = self.s.recv(1024).decode('utf-8')  # receive response
    print('Answer :  ' + self.data)  # show in terminal



  def one16(self):
    list=[1]
    print('pассчитать и вывести на печать максимальные значения втpех паpах чисел, вводимых с клавиатуpы')
    for i in range(2):
      num=int(input('введите число -> '))
      list.append(num)
    print(list)
    return list


  def one19(self):
    list=[2]
    print(' Получить с использованием функции пользователя наименьшее значение.')
    
    num=int(input('введите число A -> '))
    list.append(num)

    num=int(input('введите число B -> '))
    list.append(num)

    num=int(input('введите число C -> '))
    list.append(num)

    print(list)
    return list

  def one22(self):
    list=[3]
    print(' Пpовеpить с использованием функции пользователя их четность')
    
    num=int(input('введите число a -> '))
    list.append(num)    

    num=int(input('введите число b -> '))
    list.append(num)    

    num=int(input('введите число c -> '))
    list.append(num)    

    num=int(input('введите число d -> '))
    list.append(num)    

    return list

  def one25(self):
    list=[4]
    print(' Проверить степень двойки')
    
    num=int(input('введите число  -> '))
    list.append(num)    
    return list
    pass

  def one28(self):
    list=[5]
    print('вычисления функции F(X,Y)')
    
    num=int(input('введите X -'))
    list.append(num)   

    num=int(input('введите Y -'))
    list.append(num)   

    return list
    pass



if __name__ == '__main__':
	ex = MainClient()
