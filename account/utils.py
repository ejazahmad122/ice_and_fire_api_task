from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        """send password reset email

        Args:
            data (dict): data abot email
        """
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email='faltomail60@gmail.com',
            to=[data['to_email']]
        )
        email.send()
