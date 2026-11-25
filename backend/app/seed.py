from sqlalchemy import select
from app.db.session import SessionLocal
from app.db.models import Ticket

SEED=[
("Aarav Sharma","aarav@example.com","Refund not received for cancelled order","I cancelled my order last week and still haven't received the refund. Please check the status.","high","billing"),
("Meera Iyer","meera@example.com","Unable to sign in after password reset","The password reset link worked but I still cannot sign in. I get an error after entering my new password.","urgent","account"),
("Kabir Singh","kabir@example.com","Product feature request","It would be helpful to export reports as CSV. Is this on your roadmap?","normal","product"),
("Sara Khan","sara@example.com","Charged twice for monthly subscription","I see two charges on my card for the same subscription this month.","high","billing"),
("Rohan Verma","rohan@example.com","Mobile app crashes on startup","The Android app crashes immediately after opening since yesterday's update.","urgent","technical"),
("Ananya Das","ananya@example.com","Update email address on my account","I need to change my account email address. Can you help me do this safely?","normal","account"),
]

def seed():
    with SessionLocal() as db:
        if db.scalar(select(Ticket).limit(1)): return
        for i,(name,email,subject,desc,priority,category) in enumerate(SEED,1):
            db.add(Ticket(ticket_number=f"SP-{1000+i}",customer_name=name,customer_email=email,subject=subject,description=desc,priority=priority,category=category,status="open" if i%3 else "in_progress"))
        db.commit()
