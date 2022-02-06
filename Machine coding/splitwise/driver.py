import sys
sys.path.append("/Users/arujmahajan/Python/Machine coding")
from splitwise.controllers.user_controller import UserController
from splitwise.controllers.group_controller import GroupController
from splitwise.controllers.bill_controller import BillController
from splitwise.services.bill_service import BillService
from splitwise.services.group_service import GroupService
from splitwise.services.user_service import UserService

user_controller = UserController(UserService())
bill_controller = BillController(BillService())
group_controller = GroupController(GroupService())

user1 = user_controller.add_user('user1','Aruj')
user2 = user_controller.add_user('user2','Rahul')
user3 = user_controller.add_user('user3','Pawan')
user4 = user_controller.add_user('user4','Ashray')
user5 = user_controller.add_user('user5','Shaun')

members = [user1,user2,user3,user4,user5]
group1 = group_controller.add_group('group1','avengers',members)

paid_by = {'user1':200,'user2':100,'user3':50,'user4':50,'user5':100}
contribution = {'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}

bill1 = bill_controller.add_bill('bill1','group1',500,contribution,paid_by)
balance = bill_controller.get_user_balance('user1')
print(balance)