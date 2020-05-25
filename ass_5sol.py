class Item:
     def __init__(self,name,price,category):
         if price<=0:
             raise ValueError("Invalid value for price, got {}".format(price))
         self.name=name
         self.price=price
         self.category=category
     def __str__(self):
         return "{0}{1}{2}{3}{4}".format(self.name,'@',self.price,'-',self.category)
class Query:
     def __init__(self,field,operation,value):
         op_list=['IN','GT','EQ','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
         self.field=field
         self.value=value
         if operation not in op_list:
             raise ValueError("Invalid value for operation, got {}".format(operation))
         else:
             self.operation=operation
     def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
class Store:
     def __init__(self):
         self.list_items=[]
     def add_item(self,item):
         self.list_items.append(item)
     def __str__(self):
         if len(self.list_items)==0:
             return("No items")
         else:
             return '\n'.join(map(str,self.list_items))
     def filter(self,query):
         #print(query.field,query.operation,query.value)
         #self.list2=[]
         filter_obj=Store()
         if query.operation=='EQ':
             for i in self.list_items:
                 #print(i.name,i.price,i.category)
                 if query.field=="name" and query.value==i.name:
                     filter_obj.add_item(i)
                 elif query.field=="price" and query.value==i.price:
                     filter_obj.add_item(i)
                 elif query.field=="category" and query.value==i.category:
                     filter_obj.add_item(i)

         elif query.operation=='GT':
             for i in self.list_items:
                 if query.field=="price" and i.price>query.value:
                     filter_obj.add_item(i)

         elif query.operation=='GTE':
             for i in self.list_items:
                 if query.field=="price" and i.price>=query.value:
                     filter_obj.add_item(i)

         elif query.operation=='LT':
             for i in self.list_items:
                 if query.field=="price" and i.price<query.value:
                     filter_obj.add_item(i)

         elif query.operation=='LTE':
             for i in self.list_items:
                 if query.field=="price" and i.price<=query.value:
                     filter_obj.add_item(i)
         elif query.operation=='IN':
             for i in self.list_items:
                 if query.field=="name" and i.name in query.value:
                     filter_obj.add_item(i)
                 if query.field=="price" and i.price in query.value:
                     filter_obj.add_item(i)

                 if query.field=="category" and i.category in query.value:
                     filter_obj.add_item(i)

         elif query.operation=="STARTS_WITH":
             for i in self.list_items:
                 if query.field=="name" and i.name.startswith(query.value):
                     filter_obj.add_item(i)
                 if query.field=="category" and i.category.startswith(query.value):
                     filter_obj.add_item(i)

         elif query.operation=="ENDS_WITH":
             for i in self.list_items:
                 if query.field=="name" and i.name.endswith(query.value):
                     filter_obj.add_item(i)
                 if query.field=="category" and i.category.endswith(query.value):
                     filter_obj.add_item(i)

         elif query.operation=="CONTAINS":
             for i in self.list_items:
                 if query.field=="name" and query.value in i.name:
                     filter_obj.add_item(i)
                 if query.field=="category" and query.value in i.category:
                     filter_obj.add_item(i)

         return filter_obj

     def exclude(self,query):
         exclude_list=Store()
         include_list=self.filter(query)
         print(include_list)
         for item in self.list_items:
             if item not in include_list.list_items:
                 exclude_list.add_item(item)
         return exclude_list
     def count(self):
         return len(self.list_items)







