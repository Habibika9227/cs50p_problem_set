# class Hat:
#     def __init__(self,name,house):
#         self.name=name
#         self.house=house
        
#     def __str__(self):
#         return (f'{self.name} is from {self.house}')
    

# s1=Hat('abdullahi','mandera')
# s2=Hat('ahmed','khalalio')
# s3=Hat('feisal','berdale')
# print(s1)
# print(s2)
# print(s3)
class Hat:
    def __init__(self,name,house):
        self.name=name
        self.house=house
        
    def __str__(self):
        return f'{self.name} is from {self.house}'
    
s1=Hat('abdullahi','mandera')
s2=Hat('ahmed','khalalio')
s3=Hat('feisal','berdale')

print(s1)
print(s2)
print(s3)