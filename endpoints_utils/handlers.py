from db_operations.actions import write_message_to_db, get_all_messages_by_user, get_specific_message_by_id, \
    delete_message_by_id


def write(data):
    message, subject, writer, receiver = data.get("message", ""), data.get("subject", ""), \
                                data.get("from", ""), data.get("to", "")
    try:
        if not writer:
            raise Exception("No write specified")
        if not receiver:
            raise Exception("No receiver specified")
        if not message:
            raise Exception("No message to send")
        if not subject:
            raise Exception("Subject not specified")
        write_message_to_db(writer, receiver, subject, message)
        bundle = {
            "status" : 200,
            "response": "Message sent successfully"
        }
    except Exception as error:
        bundle = {
            "status" : 400,
            "response": error.message
        }
    return bundle

def delete(data):
    id = data.get("message_id", "")
    try:
        if not id:
            raise Exception("No id specified")

        response = delete_message_by_id(id)

        bundle = {
            "status" : response.get("status", ""),
            "response": response.get("response", "")
        }
    except Exception as error:
        bundle = {
            "status" : 400,
            "response": error.message
        }
    return bundle

def get_messages(data, only_unread= False):
    user = data.get("user", "")
    try:
        if not user:
            raise Exception("No user specified")

        messages = get_all_messages_by_user(user, only_unread=only_unread)

        bundle = {
            "status" : 200,
            "response": messages
        }
    except Exception as error:
        bundle = {
            "status" : 400,
            "response": error.message
        }
    return bundle

def get_message_by_id(data):
    id = data.get("message_id", "")
    try:
        if not id:
            raise Exception("No id specified")

        message = get_specific_message_by_id(id)

        bundle = {
            "status" : 200,
            "response": message
        }
    except Exception as error:
        bundle = {
            "status" : 400,
            "response": error.message
        }

    return bundle






