
from django.core.paginator import Paginator

names = ["Ravi","kumar","mohan","krishna","murali","prasad","Naveen"]

p = Paginator(names,3)

ref = p.page(1)

print(ref.object_list)
print(ref.has_next())
print(ref.has_previous())
print(ref.next_page_number())
#print(ref.previous_page_number())
print("-----------------------------")
print(ref.start_index())
print(ref.end_index())
