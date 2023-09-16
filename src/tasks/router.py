from fastapi import APIRouter, Depends
from starlette.background import BackgroundTasks

from auth.base_config import current_user
from tasks.tasks import send_email_report_dashboard

router = APIRouter(prefix="/reports")


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {"status": 200, "data": "The letter was sent", "details": None}
