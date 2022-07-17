class Student:
	def __init__(self, id, gakunen, first, family):
		self.student_id = id  # 学籍番号
		self.first_name = first  # 名
		self.family_name = family  # 姓
		self._gakunen = gakunen # 学年

	def full_name(self):
		return self.first_name+ " " + self.family_name

taro = Student(1234,3,'Taro','Yamada')
hanako = (1301,2,'Hanako','Sato')

print(taro.full_name)