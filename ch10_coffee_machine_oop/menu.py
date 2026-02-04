class MenuItem:
    """각 메뉴 아이템들을 모델링합니다."""
    def __init__(self, 이름, 물, 우유, 커피, 가격):
        self.이름 = 이름
        self.가격 = 가격
        self.ingredients = {
            "물": 물,
            "우유": 우유,
            "커피": 커피,
        }


class Menu:
    """음료 메뉴를 모델링합니다."""
    def __init__(self):
        self.menu = [
            MenuItem(이름="라떼", 물=200, 우유=150, 커피=24, 가격=2.5),
            MenuItem(이름="에스프레소", 물=50, 우유=0, 커피=18, 가격=1.5),
            MenuItem(이름="카푸치노", 물=250, 우유=50, 커피=24, 가격=3),
            MenuItem(이름="캬라멜 마키아또", 물=200, 우유=60, 커피=26, 가격=4),
        ]

    def get_items(self):
        """이용 가능한 모든 메뉴 아이템의 이름을 반환합니다."""
        options = ""
        for item in self.menu:
            options += f" {item.이름} /"
        return options

    def find_drink(self, order_이름):
        """특정 음료를 이름으로 메뉴에서 검색합니다. 해당 아이템이 존재하면 반환하고, 그렇지 않으면 None을 반환합니다."""
        for item in self.menu:
            if item.이름 == order_이름:
                return item
        print("죄송합니다. 해당 아이템은 이용할 수 없습니다.")