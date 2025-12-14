from my_project import db
from my_project.auth.domain.staff import Staff

class StaffDAO:
    @staticmethod
    def get_all():
        return Staff.query.all()

    @staticmethod
    def get_by_id(staff_id):
        return Staff.query.get(staff_id)

    @staticmethod
    def create(data):
        new_staff = Staff(
            name=data.get('name'),
            shop_idshop=data.get('shop_idshop'),
            position=data.get('position')
        )
        db.session.add(new_staff)
        db.session.commit()
        return new_staff

    @staticmethod
    def update(staff_id, data):
        staff = Staff.query.get(staff_id)
        if not staff:
            return None

        staff.name = data.get('name', staff.name)
        staff.shop_idshop = data.get('shop_idshop', staff.shop_idshop)
        staff.position = data.get('position', staff.position)

        db.session.commit()
        return staff

    @staticmethod
    def delete(staff_id):
        staff = Staff.query.get(staff_id)
        if not staff:
            return None

        db.session.delete(staff)
        db.session.commit()
        return staff
