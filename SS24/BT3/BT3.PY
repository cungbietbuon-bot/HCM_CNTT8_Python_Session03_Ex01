class MemberCard:

    point_value_vnd = 1000
    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name.title()

        self.__points = 0
        self.__tier = "Standard"

    @property
    def points(self):
        return self.__points

    @property
    def tier(self):
        return self.__tier

    def earn_points(self, bill_amount):

        earned = bill_amount // 10000

        self.__points += earned

        old_tier = self.__tier

        if self.__points >= 100:
            self.__tier = "VIP"

        return earned, old_tier != self.__tier

    def redeem_points(self, points_to_use):

        if points_to_use <= 0:
            return False, 0

        if points_to_use > self.__points:
            return False, 0

        self.__points -= points_to_use

        discount = (
            points_to_use *
            MemberCard.point_value_vnd
        )

        return True, discount

    @classmethod
    def update_point_value(cls, new_value):

        if new_value > 0:
            cls.point_value_vnd = new_value

    @staticmethod
    def is_valid_card_id(card_id):

        if len(card_id) != 4:
            return False

        if not card_id.startswith("RC"):
            return False

        return card_id[2:].isdigit()


cards_database = []

card1 = MemberCard("RC01", "Nguyen Van A")
card2 = MemberCard("RC02", "Tran Thi B")
card1.earn_points(1500000)
card2.earn_points(200000)
cards_database.append(card1)
cards_database.append(card2)

def find_card(card_id):

    for card in cards_database:
        if card.card_id == card_id:
            return card

    return None

while True:

    print("===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm")
    print("6. Thoát chương trình")
    print("================================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":
        if len(cards_database) == 0:
            print("Chưa có dữ liệu.")
            continue

        stt = 1

        for card in cards_database:

            print(
                f"{stt}. Mã: {card.card_id} | "
                f"Tên: {card.name:<20} | "
                f"Điểm: {card.points} | "
                f"Hạng: {card.tier}"
            )

            stt += 1

    elif choice == "2":
        print("=== ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ===")

        card_id = input(
            "Nhập mã thẻ: "
        ).strip()

        existed = False

        for card in cards_database:
            if card.card_id == card_id:
                existed = True
                break

        if existed:

            print("\nMã thẻ đã tồn tại trong hệ thống!")
            print("Vui lòng kiểm tra lại.")
            continue

        if not MemberCard.is_valid_card_id(card_id):

            print("\nMã thẻ không hợp lệ!")
            continue

        name = input(
            "Nhập tên khách hàng: "
        )

        new_card = MemberCard(
            card_id,
            name
        )

        cards_database.append(new_card)

        print("Đăng ký thẻ thành viên thành công!")
        print(f"Mã thẻ: {new_card.card_id}")
        print(f"Tên khách hàng: {new_card.name}")
        print(f"Điểm ban đầu: {new_card.points}")
        print(f"Hạng thẻ: {new_card.tier}")

    elif choice == "3":
        print("=== KHÁCH MUA HÀNG - TÍCH ĐIỂM ===")

        card_id = input(
            "Nhập mã thẻ: "
        ).strip()

        card = find_card(card_id)

        if card is None:
            print("Không tìm thấy thẻ.")
            continue

        bill_amount = int(
            input("Nhập tổng tiền hóa đơn: ")
        )

        earned, upgraded = card.earn_points(
            bill_amount
        )

        print(f"Khách hàng: {card.name}")
        print(
            f"Hóa đơn: {bill_amount:,} VNĐ"
        )
        print(
            f"Số điểm được tích: {earned}"
        )
        print(
            f"Tổng điểm hiện tại: {card.points}"
        )

        if upgraded:
            print(
                "Chúc mừng! Khách hàng đã được nâng hạng lên VIP."
            )

        print(
            f"Hạng thẻ hiện tại: {card.tier}"
        )

    elif choice == "4":
        print("=== KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ===")

        card_id = input(
            "Nhập mã thẻ: "
        ).strip()

        card = find_card(card_id)

        if card is None:
            print("Không tìm thấy thẻ.")
            continue

        points_to_use = int(
            input(
                "Nhập số điểm muốn sử dụng: "
            )
        )

        success, discount = card.redeem_points(
            points_to_use
        )

        if success:
            print(
                f"Đã trừ {points_to_use} điểm."
            )

            print(
                f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!"
            )

            print(
                f"Số điểm còn lại: {card.points}"
            )

            print(
                f"Hạng thẻ hiện tại: {card.tier}"
            )

        else:
            print("Không thể đổi điểm!")
            print(
                "Số điểm muốn sử dụng vượt quá số điểm hiện có."
            )
            print(
                f"Điểm hiện tại của khách: {card.points}"
            )
            print(
                f"Số điểm sau giao dịch: {card.points}"
            )

    elif choice == "5":
        print(
            "=== CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ==="
        )

        print(
            f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

        new_value = int(
            input(
                "Nhập tỷ giá mới cho 1 điểm: "
            )
        )

        MemberCard.update_point_value(
            new_value
        )

        print("Cập nhật tỷ giá thành công!")

        print(
            f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ"
        )

    elif choice == "6":
        print(
            "Cảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!"
        )
        break

    else:
        print(
            "Vui lòng chọn từ 1 đến 6!"
        )