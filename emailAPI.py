#!/usr/bin/env python
import imaplib, email, sys, json,email.parser


user = 'EmailAddress'
password = 'Password'
imap_url = 'smtpURL/IMAPURL'


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


# Final Working
def search(code):
    result, data = con.search(None, 'SUBJECT', '"{}"'.format(code))
    msgs = get_emails(data)
    searchCount=[]
    searchResult = []
    countMail = 0
    for msg in reversed(msgs):
        countMail = countMail + 1
        data = get_body(email.message_from_bytes(msg[0][1]))
        # dataString = data.decode('Windows-1252').encode('UTF8').decode()
        dataString = email.parser.BytesParser().parsebytes(data).as_string()
        dataString = dataString.replace('\n', '').replace('\r', '')
        searchResult.append('<div id=section'+str(countMail)+' ><hr><br>Email Thread : ' + str(countMail) + ' of ' + str(len(msgs)) + '&nbsp;&nbsp;&nbsp; <a href=#section'+str(countMail-1)+'>Previous</a> &nbsp;&nbsp;&nbsp;<a href=#section'+str(countMail+1)+'>Next</a> <hr><br></div>' +dataString )
    print(json.dumps(searchResult))
    exit


def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split():
        typ, data = con.fetch(num,'(RFC822)')
        msgs.append(data)
    return msgs


if __name__ == '__main__':
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    con.utf8_enabled = True
    con.select('INBOX')
    code = sys.argv[1]
    search(code)



