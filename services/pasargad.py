"""
سرویس اتصال به درگاه پرداخت پاسارگاد
بر اساس مستندات رسمی REST API پاسارگاد
"""

import os
import json
import hmac
import hashlib
import base64
from datetime import datetime
from typing import Optional
import httpx
from dotenv import load_dotenv

load_dotenv()

class PasargadPayment:
    def __init__(self):
        self.merchant_code = os.getenv("PASARGAD_MERCHANT_CODE")
        self.terminal_id = os.getenv("PASARGAD_TERMINAL_ID")
        self.certificate_path = os.getenv("PASARGAD_CERTIFICATE_PATH")
        self.callback_url = os.getenv("PASARGAD_CALLBACK_URL")
        
        self.base_url = "https://pep.shaparak.ir"
        self.redirect_url = f"{self.base_url}/payment.aspx"

    def _generate_signature(self, data: str) -> str:
        """تولید امضا با استفاده از کلید خصوصی"""
        # TODO: پیاده‌سازی کامل با certificate
        # فعلاً placeholder
        return base64.b64encode(data.encode()).decode()

    async def create_payment(
        self,
        amount: int,
        invoice_number: str,
        invoice_date: str,
        mobile: Optional[str] = None,
        email: Optional[str] = None
    ) -> dict:
        """
        ایجاد درخواست پرداخت
        """
        payload = {
            "MerchantCode": self.merchant_code,
            "TerminalCode": self.terminal_id,
            "Amount": amount,
            "InvoiceNumber": invoice_number,
            "InvoiceDate": invoice_date,
            "CallbackUrl": self.callback_url,
            "Timestamp": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        }
        
        if mobile:
            payload["Mobile"] = mobile
        if email:
            payload["Email"] = email

        # در نسخه واقعی باید signature بسازیم
        signature = self._generate_signature(json.dumps(payload))
        payload["Sign"] = signature

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/Api/v1/Payment/Get/RedirectLink",
                    json=payload,
                    timeout=30.0
                )
                return response.json()
            except Exception as e:
                return {"error": str(e), "success": False}

    async def verify_payment(
        self,
        invoice_number: str,
        invoice_date: str,
        amount: int,
        reference_id: str
    ) -> dict:
        """
        تأیید پرداخت (Verify)
        """
        payload = {
            "MerchantCode": self.merchant_code,
            "TerminalCode": self.terminal_id,
            "InvoiceNumber": invoice_number,
            "InvoiceDate": invoice_date,
            "Amount": amount,
            "ReferenceNumber": reference_id
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/Api/v1/Payment/Verify",
                    json=payload,
                    timeout=30.0
                )
                return response.json()
            except Exception as e:
                return {"error": str(e), "success": False}

    async def check_transaction(self, reference_id: str) -> dict:
        """بررسی وضعیت تراکنش"""
        # پیاده‌سازی کامل در آینده
        pass


# نمونه استفاده
async def test_payment():
    pasargad = PasargadPayment()
    result = await pasargad.create_payment(
        amount=150000,
        invoice_number="INV-20250728001",
        invoice_date="2025/07/28 14:30:00",
        mobile="09121234567"
    )
    print(result)


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_payment())
