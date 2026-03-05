class HouseItem:
    def __init__(self,name,area):
        """
        初始化方法
        :param name: 家具名字
        :param area: 家具的占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return f'家具名字是{self.name},占地面积为{self.area}平米'

class House:
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area # 剩余可用面积
        self.items_list=[]  #家具列表

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area,
                   self.free_area, self.items_list))

    def add_item(self,item:HouseItem):  #:+对象类型可以进行注解，可以使得pycharm进行联想
        if self.free_area >= item.area:
            self.free_area -= item.area
            self.items_list.append(item.name)
            print(f'家具{item.name}放置成功')
        else:
            print(f"剩余空间不够，无法放入{item.name}")



if __name__ == '__main__':
    bed = HouseItem("席梦思",4)
    chest = HouseItem('衣柜',2)
    table = HouseItem('餐桌',1.5)
    print(bed)
    print(chest)
    print(table)
    house = House("两室一厅",6)
    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
    print(house)