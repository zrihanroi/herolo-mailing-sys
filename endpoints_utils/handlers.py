from db_operations.actions import write_message_to_db

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
        # update db here..
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

def get_all(data):
    return "test"
















