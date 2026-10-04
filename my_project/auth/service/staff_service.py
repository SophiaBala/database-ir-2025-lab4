from my_project.auth.dao.staff_dao import StaffDAO

class StaffService:

    @staticmethod
    def get_all_staff():
        return StaffDAO.get_all()


    @staticmethod
    def create_staff(data):
        return StaffDAO.create(data)

    @staticmethod
    def update_staff(staff_id, data):
        return StaffDAO.update(staff_id, data)

    @staticmethod
    def delete_staff(staff_id):
        return StaffDAO.delete(staff_id)
