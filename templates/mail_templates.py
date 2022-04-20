def prepare_notification_email_message(data):
    message_type = data.get("message_type")
    name = data.get("name")
    address = data.get("address")
    phone_no = data.get("phone_no")
    email = data.get("email")
    subject = data.get("subject")
    message = data.get("message")
    return {
        "subject": f"""{message_type} message from User.""",
        "message": f"""<div><p>{message_type} mail from User</p>
                            <p>{subject}</p>
                            <p>{message}</p>
                            User Details<br/>
                            Name: {name}<br/>
                            Address: {address}<br/>
                            M(b): {phone_no}<br/>
                            Email: {email}
                            <br/><br/>
                            <p><em>****Autogenerated email.****</em></p>
                        </div>"""
    }