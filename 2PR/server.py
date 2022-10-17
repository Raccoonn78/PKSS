from copyreg import pickle
from re import L
import socket
import pickle

from matplotlib.pyplot import cla


class MainServer(socket.socket):

	def __init__(self):
		super().__init__()

		

		self.start_my_server()

	

	def start_my_server(self):

		try:
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
			self.s.listen() # Начинаем прослушивать входящие соединения.
			print('Workiing...')
			
			self.conn, self.addr = self.s.accept()# Метод который принимает входящее соединение.

			while True:
				print('Workiing...while...True...')
				 
				print('...')
				self.data = self.conn.recv(1024) # Получаем данные из сокета.

				input_data = bytearray()
				
				input_data=pickle.loads(self.data) ##конвертируем из байтового типа в обычный 
				


				if input_data[0] ==0: # проверка если первый элемент переданного массива явл stop то сервер выкл
					print('Server stop')
					break


				if input_data[0]==1:

					print("выполняем первую функцию one16()...")
					print(" ")
					answer=self.one16()  ### вызываем первую функцию для первого задания
					
					self.conn.sendall(str(answer[1]).encode('utf-8'))# Отправляем данные в сокет.


				if input_data[0]==2:
					print("выполняем первую функцию two19()...")
					print(" ")
					answer=self.two19()  ### вызываем первую функцию для первого задания
					
					self.conn.sendall(str(answer[0]).encode('utf-8'))# Отправляем данные в сокет.

					
				if input_data[0]==3:
					print("выполняем первую функцию three22()...")
					print(" ")
					answer=self.three22()  ### вызываем первую функцию для первого задания
					
					self.conn.sendall(str(answer).encode('utf-8'))# Отправляем данные в сокет.

					
				if input_data[0]==4:
					print("выполняем первую функцию four25()...")
					print(" ")
					answer=self.four25()  ### вызываем первую функцию для первого задания
					
					self.conn.sendall(str(answer).encode('utf-8'))# Отправляем данные в сокет.


				if input_data[0]==5:
					print("выполняем первую функцию five28()...")
					print(" ")
					answer=self.five28()  ### вызываем первую функцию для первого задания
					
					self.conn.sendall(str(answer).encode('utf-8'))# Отправляем данные в сокет.

					
					
					
				
				

		except KeyboardInterrupt:
			self.s.close()
			print('shutdown this shit...')
	
	def one16(self):
		input_d=bytearray()

		input_d = pickle.loads(self.data)
		input_d.remove(1) # удаляем первый элемент чтобы сделать массив только из чисел

		input_d.sort() # сортируем массив по возврастанию 
		return input_d
	
	def two19(self):
		input_d=bytearray()

		input_d = pickle.loads(self.data)
		input_d.remove(2) # удаляем первый элемент чтобы сделать массив только из чисел

		input_d.sort() # сортируем массив по возврастанию 
		return input_d
	
	def three22(self):
		input_d=bytearray()
		input_d = pickle.loads(self.data)

		input_d.remove(3)

		for i in range(4):

			if input_d[i]%2==0:

				input_d[i]=str(input_d[i])+' четное'
			else:

				input_d[i]=str(input_d[i])+ ' не четное'

		return input_d

	def four25(self):
		input_d=bytearray()
		input_d = pickle.loads(self.data)

		input_d.remove(4)

		summ=0

		while input_d[0]>1:

			if input_d[0]%2==0:

				summ+=1
				input_d[0]=input_d[0]/2

			else:

				input_d[0]="число не является степенью двойки"
				return input_d
				
		input_d[0]='число является 2 в '+str(summ)+ ' степени'

		return input_d
		
	def five28(self):

		input_d=bytearray()
		input_d = pickle.loads(self.data)

		input_d.remove(5)

		x=input_d[0]
		y = input_d[1]

		ans = ( 2*(x**3) - 4*(x**2) + x + 1 ) / ( 9*(y**3) + y + 4 ) +( 3*(y**2) +5*(y) )
		
		return ans
		



	




if __name__ == '__main__':
	ex = MainServer()























































# def start_my_server():

# 	try:
# 		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 		s.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
# 		s.listen(5) # Начинаем прослушивать входящие соединения.
# 		print('Workiing...')
		

# 		while True:
# 			conn, addr = s.accept() # Метод который принимает входящее соединение.
# 			data = conn.recv(1024) # Получаем данные из сокета.
# 			if data ==b'stop':
# 				data = 'stop'
# 				conn.sendall(data)
# 				break
# 			if data==b'one':
# 				tab_1(data)
# 			if data==b'two':
# 				tab_2()
# 			if data==b'three':
# 				tab_3()
# 			if data==b'four':
# 				tab_4()
# 			if data==b'five':
# 				tab_5()
			
# 			conn.sendall(data) # Отправляем данные в сокет.
# 			print(data.decode('utf-8'))

# 	except KeyboardInterrupt:
# 		s.close()
# 		print('shutdown this shit...')



# def tab_1(data):
# 	print('one well done')

# def tab_2():
# 	print('two well done')

# def tab_3():
# 	print('three well done')

# def tab_4():
# 	print('four well done')

# def tab_5():
# 	print('five well done')