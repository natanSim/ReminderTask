from flask import Flask, request

app = Flask(__name__)


@app.route('/reminder', methods=['GET'])
def get_user_by_information():
    print(f"data from client : {dict(request.args)}")
    reminder_list = list(dict(request.args).values())
    add_reminder_to_text_file(reminder_list)

    return "OK"

# def show_reminder_file(user_reminder):
#     reminder_text = 'reminder.txt'
#     copy_reminder_list = user_reminder.copy()
#
#     with open(reminder_text, 'r') as read_text:
#         check = read_text.read()
#         for i in range(len(user_reminder)):
#             if copy_reminder_list[i] in check:
#                 copy_reminder_list.remove(user_reminder[i])
#


def add_reminder_to_text_file(reminder_list):
    reminder_text = "reminder.txt"
    with open(reminder_text, 'a') as add_reminder:
        add_reminder.write(f'data from client: {reminder_list}\n')


if __name__ == '__main__':
    app.run()
