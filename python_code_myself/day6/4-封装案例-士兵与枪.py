class Gun:
    def __init__(self,model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self,count):
        self.bullet_count += count

    def shoot(self):
        if(self.bullet_count > 1):
            print(f'{self.model}开枪')
            self.bullet_count -= 1
            print(f'剩余子弹数量{self.bullet_count}')
        else:
            print(f'{self.model}没有子弹了,无法开枪')

class Soldier:
    def __init__(self,name,gun:Gun = None):
        self.name = name
        self.gun = gun

    def fire(self):
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
            return

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)
        self.gun.shoot()

if __name__ == '__main__':
    ak47 = Gun("ak47")
    # ak47.add_bullet(50)
    # ak47.shoot()
    xusanduo = Soldier('许三多')
    xusanduo.fire()
    xusanduo.gun = ak47
    xusanduo.fire()