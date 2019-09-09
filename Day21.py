set1 = {'Toyota','Lexus','BMW','GMC',"Sonata"}
set1.discard('Sonata')
y = set1.pop()

print('{},\n{},\n{}'.format(len(set1),y,set1))