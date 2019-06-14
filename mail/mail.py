# Import module or library
import imaplib
import email

def fetch_mail():

    # Setting of account
    UserName = "s161075.sample@gmail.com"
    PassName = "570161ss"

    # Initialization
    mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)

    # Login
    mail.login(UserName, PassName)

    # Select label
    mail.select()

    # Fetch e-mails
    type, data = mail.search(None, 'All')
    for i in data[0].split():
        gmail = dict()

        ok, x = mail.fetch(i,'RFC822')
        ms = email.message_from_string(x[0][1].decode('iso-2022-jp'))

        # Get and decode address
        ad = email.header.decode_header(ms.get('From'))
        ms_code = ad[0][1]
        if ms_code != None:
            address = ad[0][0].decode(ms_code)
            address += ad[1][0].decode(ms_code)
        else:
            address = ad[0][0]

        gmail['address'] = address

        # Get and decode subject
        sb = email.header.decode_header(ms.get('Subject'))
        ms_code = sb[0][1]
        if ms_code != None:
            subject = sb[0][0].decode(ms_code)
        else:
            subject = sb[0][0]

        gmail['subject'] = subject

        # Get and decode body
        if ms.is_multipart():
            for payload in ms.get_payload():
                if payload.get_content_type() == "text/plain":
                    body = payload.get_payload(decode="True").decode('utf-8')
        else:
            if ms.get_content_type() == "text/plain":
                body = ms.get_payload()

        gmail['body'] = body


        gmails.append(gmail)

    # Logout
    mail.close()
    mail.logout()
