

from connection import connect_to_db

def insert_Staff_information(Staff):
    try:
        conn = connect_to_db()
        with conn.cursor() as cursor:
            select_query = "SELECT id FROM shedule WHERE name = %s"
            cursor.execute(select_query, (Staff[0],))
            inserted_data = cursor.fetchone()

            print("Вставленные данные:", inserted_data)

    except Exception as e:
        print(f"Ошибка при вставке данных: {e}")

    finally:
        conn.close()



def update_login_password(user_id, new_login, new_password):
    try:
        conn = connect_to_db()
        with conn.cursor() as cursor:
            update_query = "UPDATE doctors SET login = %s, password = %s WHERE id = %s"
            cursor.execute(update_query, (new_login, new_password, user_id))
            conn.commit()

            print("Данные обновлены успешно!")

    except Exception as e:
        print(f"Ошибка при обновлении данных: {e}")

    finally:
        conn.close()


